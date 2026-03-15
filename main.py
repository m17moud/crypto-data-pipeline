from scripts.extract_crypto import extract_data
from scripts.load_to_db import load_data


def run_pipeline():

    data = extract_data()

    load_data(data)

    print("Pipeline executed successfully")


if __name__ == "__main__":
    run_pipeline()