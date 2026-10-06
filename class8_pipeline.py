import logging
from pathlib import Path
from class8_data_loader import load_netflix
from class8_data_validator import require_columns

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

def main():
    input_path = Path("data/netflix_titles.csv")
    df = load_netflix(input_path)
    require_columns(df, ["title", "date_added", "rating"])
    pass

if __name__ == "__main__":
    main()

