"""
Extract a dataset from a URL like Kaggle or data.gov.
JSON or CSV formats tend to work well
"""
import os
import requests

def extract(
    url1="https://raw.githubusercontent.com/nogibjj/Xianjing_Huang_Mini_Proj_test/main/customers.csv",
    url2="https://raw.githubusercontent.com/nogibjj/Xianjing_Huang_Mini_Proj_test/main/orders.csv",
    file_path1="data/customers.csv",
    file_path2="data/orders.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url1) as r:
        with open(file_path1, "wb") as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, "wb") as f:
            f.write(r.content)
    return file_path1, file_path2

