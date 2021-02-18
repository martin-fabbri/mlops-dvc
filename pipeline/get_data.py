import os
import zipfile

import wget

from config import Config

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
url = Config.DATASET_URL
zip_name = "data.zip"
wget.download(url, zip_name)

with zipfile.ZipFile(zip_name, "r") as zip_ref:
    zip_ref.filelist[0].filename = Config.RAW_DATA
    zip_ref.extract(zip_ref.filelist[0])

os.remove(zip_name)
