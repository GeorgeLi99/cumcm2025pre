
import pandas as pd

# 导入extract_sites_data函数，从utils.data_extract模块中
from utils import extract_sites_data, save_data_as_csv, remove_invalid_rows, remove_invalid_city_columns


def extract_last_hour_data(file_name):
    data = pd.read_csv(file_name)
    data = data.iloc[-15:, :]
    print(f"\n")
    print("提取最后15行数据")
    print(data)
    data = remove_invalid_rows(data, invalid_rows=[355])
    data = remove_invalid_city_columns(data)
    data.to_csv("res/china_sites_20250215_1141A_1269A_last_hour.csv",
                header=True, index=False)
    return data

def transpose_data(data):
    pass
    


if __name__ == "__main__":
    # 调用extract_sites_data函数，提取指定csv文件中1141A到1269A的数据
    data = extract_sites_data(
        "data/站点_20250101-20250215/站点_20250101-20250215/china_sites_20250215.csv")
    save_data_as_csv(data, "res/china_sites_20250215_1141A_1269A.csv",
                     "data/站点_20250101-20250215/站点_20250101-20250215/china_sites_20250215.csv")
    print(f"\n")
    print("提取1141A到1269A的数据")
    print(data)
    extract_last_hour_data(
        "res/china_sites_20250215_1141A_1269A.csv")
