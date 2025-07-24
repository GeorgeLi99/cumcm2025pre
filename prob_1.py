
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


def transpose_data_and_mean(data):
    # 将1142A到1150A、1151A到1222A、1223A到1269A的数据按列求平均值，然后重新整合数据，再转置
    data_1142A_1150A = data.iloc[:, 3:8]
    data_1151A_1222A = data.iloc[:, 9:56]
    data_1223A_1269A = data.iloc[:, 57:]
    data_1142A_1150A_mean = data_1142A_1150A.mean(axis=1)
    data_1151A_1222A_mean = data_1151A_1222A.mean(axis=1)
    data_1223A_1269A_mean = data_1223A_1269A.mean(axis=1)
    data_mean = pd.concat(
        [data_1142A_1150A_mean, data_1151A_1222A_mean, data_1223A_1269A_mean], axis=1)
    data_mean.columns = [
        '1142A_1150A(ShangHai)', '1151A_1222A(JiangSu)', '1223A_1269A(ZheJiang)']
    # 提取第2/4/6/8/10/13/15行
    data_mean = data_mean.iloc[[0, 2, 4, 6, 8, 11, 13], :]
    data_mean.index = ['aqi', 'pm2.5', 'pm10', 'so2', 'no2', 'co', 'o3']
    data_mean = data_mean.T
    print(f"\n")
    print("转置并求平均值")
    print(data_mean)
    return data_mean


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
    df = pd.read_csv("res/china_sites_20250215_1141A_1269A_last_hour.csv")
    df = transpose_data_and_mean(df)
    df.to_csv("res/china_sites_20250215_1141A_1269A_last_hour_mean_and_transpose.csv",
              header=True, index=True)
