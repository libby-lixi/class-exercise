import logging
from venv import logger

def require_columns(df, required_columns):
    """Check that all required columns exist."""
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        logger.error(f"Missing columns: {missing_columns}")
        return False
    logger.info("All required columns are present.")
    return True