
import pandas as pd
import numpy as np
import os


# 导入extract_sites_data函数，从utils.data_extract模块中
from utils import extract_sites_data, save_data_as_csv, \
    draw_line_chart_of_iaqi, draw_line_chart_every_day, remove_invalid_rows, remove_invalid_city_columns, extract_current_hour_data, extract_some_city_data, calculate_iaqi


def extract_last_hour_data(file_name):
    data = pd.read_csv(file_name)
    data = data.iloc[-15:, :]
    print(f"\n")
    print("提取最后15行数据")
    print(data)
    data = remove_invalid_rows(data, invalid_rows=[355])
    data = remove_invalid_city_columns(data)
    data.to_csv(file_name.replace(".csv", "_last_hour.csv"),
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
    data_mean = data_mean.iloc[[0, 1, 3, 5, 7, 10, 12], :]
    data_mean.index = ['aqi', 'pm2.5', 'pm10', 'so2', 'no2', 'co', 'o3']
    data_mean = data_mean.T
    print(f"\n")
    print("转置并求平均值")
    print(data_mean)
    return data_mean


def extract_all_data():
    pass


def to_py(obj):
    if isinstance(obj, np.generic):
        return obj.item()
    elif isinstance(obj, (list, tuple)):
        return type(obj)(to_py(x) for x in obj)
    else:
        return obj


def round_nested(obj, ndigits=0):
    if isinstance(obj, (list, tuple)):
        return type(obj)(round_nested(x, ndigits) for x in obj)
    elif isinstance(obj, float):
        return round(obj, ndigits)
    else:
        return obj


if __name__ == "__main__":
    all_iaqis = []
    all_aqis = []
    for i in range(1, 6):
        # 构建文件名和子文件夹
        day_str = f"{i:d}"  # 不补零
        subdir = f"res/2025021{day_str}"
        os.makedirs(subdir, exist_ok=True)
        src_file = f"data/站点_20250101-20250215/站点_20250101-20250215/china_sites_2025021{day_str}.csv"
        res_file = f"{subdir}/china_sites_2025021{day_str}_1141A_1269A.csv"

        # 1. 提取1141A到1269A的数据并保存
        data = extract_sites_data(src_file)
        save_data_as_csv(data, res_file, src_file)
        print(f"已提取 {src_file} 的1141A到1269A数据")

        # 2. 提取最后一小时数据
        extract_last_hour_data(res_file)
        last_hour_file = res_file.replace('.csv', '_last_hour.csv')
        print(f"已提取 {res_file} 的最后一小时数据")

        # 3. 转置并求均值
        df = pd.read_csv(last_hour_file)
        df = transpose_data_and_mean(df)
        mean_transpose_file = res_file.replace(
            '.csv', '_last_hour_mean_and_transpose.csv')
        df.to_csv(mean_transpose_file, header=True, index=True)
        print(f"已转置并求均值，保存为 {mean_transpose_file}")

        # 4. 提取当前小时的数据
        extract_current_hour_data(last_hour_file)
        current_hour_file = last_hour_file + "_current_hour.csv"
        print(f"已提取24小时数据，保存为 {current_hour_file}")

        # 5. 提取部分城市数据（举例：第6~10列）
        extract_some_city_data(current_hour_file, [6, 7, 8, 9, 10,11])
        some_city_file = current_hour_file + "_some_city_data.csv"
        print(f"已提取部分城市数据，保存为 {some_city_file}")

        # 6. 读取最终数据，准备后续计算
        print("开始计算IAQI")
        df = pd.read_csv(some_city_file)
        aqis, iaqis = calculate_iaqi(df)
        all_iaqis.append(iaqis)
        all_aqis.append(aqis)
        print(f"{some_city_file} 处理完成\n")
    # 在输出前调用
    all_iaqis = to_py(all_iaqis)
    all_aqis = to_py(all_aqis)
    all_iaqis = round_nested(all_iaqis, 0)
    all_aqis = round_nested(all_aqis, 0)
    for i in range(len(all_iaqis)):
        print(f"day {i+1} AQI of five cities:")
        print(all_aqis[i])
        print(f"day {i+1} IAQI of five cities:")
        print(all_iaqis[i])
        print(f"\n")
    draw_line_chart_every_day(all_iaqis, all_aqis)

    # print("\n")
    # print("IAQI:")
    # print(iaqis)
    # print("\n")
    # print("AQI:")
    # print(aqis)
