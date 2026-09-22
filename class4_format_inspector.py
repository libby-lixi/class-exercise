import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    df = pd.read_csv(filepath)
    logger.info(f"Inspecting CSV file at: {filepath}")
    print(df.head(3))


def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    logger.info(f"Inspecting JSON file at: {filepath}")
    print(data)


def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    logger.info(f"Inspecting YAML file at: {filepath}")
    print(data)


def inspect_env():
    """Read a .env file and display basic information."""

    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    api_key = os.getenv("API_KEY")

    logger.info(".env file loaded successfully.")

    print(username)
    print(password)
    print(api_key)

    # TODO:
    # 1. Log at INFO that .env was loaded.
    # 2. Print keys.
    # Do not print passwords, API keys, or other secret values.
    pass



def main():
    # TODO:
    # 1. Create a Path object for the data directory.
    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    # 3. Call each inspection function using the matching path.
    # 4. Call inspect_env() without an argument.
    data_directory = Path("data")

    csv_path = data_directory / "sample.csv"
    json_path = data_directory / "sample.json"
    yaml_path = data_directory / "sample.yaml"


    inspect_csv(csv_path)
    inspect_json(json_path)
    inspect_yaml(yaml_path)

    inspect_env()


    pass


if __name__ == "__main__":
    main()