import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_netflix(filepath):
    try:
        df = pd.read_csv(filepath)
        logger.info("Netflix data loaded successfully.")
        return df
    except Exception as e:
        logger.error(f"Error loading Netflix data: {e}")
        return pd.DataFrame()

