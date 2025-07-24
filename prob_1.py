
import pandas as pd

# 导入extract_sites_data函数，从utils.data_extract模块中
from utils import extract_sites_data

if __name__ == "__main__":
    # 调用extract_sites_data函数，提取指定csv文件中1141A到1269A的数据
    data = extract_sites_data(
        "data/站点_20250101-20250215/站点_20250101-20250215/china_sites_20250215.csv")
    print(data)
