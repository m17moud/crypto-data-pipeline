import logging
from scripts.extract_crypto import extract_data
from scripts.load_to_db import load_data

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    
    logging.info("Pipeline started")

    data = extract_data()

    load_data(data)

    logging.info("Pipeline finished successfully")


if __name__ == "__main__":
    run_pipeline()
