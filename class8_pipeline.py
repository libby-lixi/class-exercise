import logging
from pathlib import Path
import sys
# from class8_src.class8_data_loader import load_netflix
# from class8_src.class8_data_validator import require_columns
from class8_src import load_netflix, require_columns

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

def main():
    input_path = Path("data/netflix_titles.csv")

    try:
        df = load_netflix(input_path)
        df = require_columns(df,["title", "type", "release_year"])
    except ValueError:
        sys.exit(1)
        logger.error("Pipeline Completion")
        

if __name__ == "__main__":
    main()

