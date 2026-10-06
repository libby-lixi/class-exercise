import logging
from venv import logger

def require_columns(df, required_cols):
    """Check that all required columns exist."""
    missing_columns = [col for col in required_cols if col not in df.columns]
    if missing_columns:
        logger.error(f"Missing columns: {','.join(missing_columns)}")
        raise ValueError(f"Missing columns: {','.join(missing_columns)}")
    logger.info("All required columns are present")
    return df

