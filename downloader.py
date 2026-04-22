import logging
import os
import re
import asyncio
import zipfile
import shutil
from typing import List
from xml.etree import ElementTree
import httpx
from tqdm import tqdm


logger = logging.getLogger(__name__)

class Downloader:
    def __init__(self):
        self.BASE_URL = "https://arquivos.receitafederal.gov.br/public.php/webdav"
        self.SHARE_TOKEN = "YggdBLfdninEJX9"
        self.DAV_NS = {"d": "DAV:"}
        self.DOWNLOAD_DIR = "data/temp"
        self.CSV_DIR = "data"
        self.DOWNLOAD_CHUNK_SIZE = 4 * 1024
        self.MAX_CONCURRENT_TASKS = 4

    async def _propfind(self, path: str = "") -> ElementTree.Element:
        """Execute a WebDAV PROPFIND request and return parsed XML."""
        url = f"{self.BASE_URL}/{path}".rstrip("/") + "/"
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method="PROPFIND",
                url=url,
                auth=httpx.BasicAuth(username=self.SHARE_TOKEN, password=""),
                headers={"Depth": "1"},
                timeout=10.0,
            )
            response.raise_for_status()
            return ElementTree.fromstring(response.content)
        
    async def _get_available_directories(self) -> List[str]:
        """Get all available data directories from Receita Federal."""
        root = await self._propfind()
        directories = []
        for response in root.findall("d:response", self.DAV_NS):
            href = response.find("d:href", self.DAV_NS).text
            # Match YYYY-MM directory pattern from href path
            match = re.search(r"(\d{4}-\d{2})/?$", href)
            if match:
                directories.append(match.group(1))
        if not directories:
            raise ValueError("No data directories found")
        return sorted(directories)
    
    async def _get_latest_directory(self) -> str:
        """Get the latest data directory from Receita Federal."""
        return (await self._get_available_directories())[-1]
    
    async def _get_directory_files(self, directory: str) -> List[str]:
        """Get list of ZIP files in a directory."""
        root = await self._propfind(directory)
        files = []
        for response in root.findall("d:response", self.DAV_NS):
            href = response.find("d:href", self.DAV_NS).text
            # Extract .zip filenames from href
            match = re.search(r"/([^/]+\.zip)$", href, re.IGNORECASE)
            if match:
                files.append(match.group(1))
        return files
    
    async def _download_file(self, directory: str, filename: str, semaphore: asyncio.Semaphore):
        os.makedirs(self.DOWNLOAD_DIR, exist_ok=True)
        async with semaphore:
            async with httpx.AsyncClient() as client:
                url = f"{self.BASE_URL}/{directory}/{filename}"
                async with client.stream(
                    method="GET",
                    url=url,
                    auth=httpx.BasicAuth(username=self.SHARE_TOKEN, password=""),
                    timeout=20.0,
                ) as response:
                    response.raise_for_status()
                    total = int(response.headers["Content-Length"])
                    with tqdm(total=total, desc=filename, unit_scale=True, unit="B") as progress:
                        filepath = os.path.join(self.DOWNLOAD_DIR, filename)
                        with open(filepath, "wb") as f:
                            async for chunk in response.aiter_bytes(chunk_size=self.DOWNLOAD_CHUNK_SIZE):
                                f.write(chunk)
                                progress.update(len(chunk))
    
    def _extract_files(self):
        for filename in os.listdir(self.DOWNLOAD_DIR):
            if filename.endswith(".zip"):
                filepath = os.path.join(self.DOWNLOAD_DIR, filename)
                logger.info(f"Extracting {filename}...")
                try:
                    with zipfile.ZipFile(filepath, "r") as zip_ref:
                        zip_ref.extractall(path=self.CSV_DIR)
                except Exception as e:
                    logger.info(f"Error extracting {filename}: {e}")

    def _clear_temp_files(self):
        if not os.path.exists(self.DOWNLOAD_DIR):
            return None
        shutil.rmtree(self.DOWNLOAD_DIR)

    async def execute(self):
        semaphore = asyncio.Semaphore(self.MAX_CONCURRENT_TASKS)
        latest_directory = await self._get_latest_directory()
        files = await self._get_directory_files(latest_directory)
        await asyncio.gather(*[
            self._download_file(latest_directory, filename, semaphore) for filename in files
        ])
        self._extract_files()
        self._clear_temp_files()