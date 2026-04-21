from datetime import datetime
import logging
from feed_database import FeedDatabase


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger(__name__)

feed_database = FeedDatabase()
logger.info(f"starting to feed the database...")
start = datetime.now()
feed_database.execute()
end = datetime.now()
logger.info(f"finished in {((end - start).total_seconds() / 60):.2f}min")