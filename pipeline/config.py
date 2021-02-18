from pathlib import Path


class Config:
    DATASET_URL = "https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/yshdbyj6zy-1.zip"
    ARTIFACTS_PATH = Path("./artifacts")
    RAW_DATA = str(ARTIFACTS_PATH / "data_raw.csv")
    PROCESSED_DATA = str(ARTIFACTS_PATH / "data_processed.csv")
    METRICS = str(ARTIFACTS_PATH / "metrics.json")
    PLOT_BY_REGION = str(ARTIFACTS_PATH / "by_region.png")
