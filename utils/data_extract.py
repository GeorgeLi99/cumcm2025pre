import pandas as pd
import numpy as np


def remove_invalid_rows(df, invalid_rows=None):
    """
    丢弃原始csv数据中为无效值的所有行。
    :param df: 原始DataFrame
    :param invalid_rows: 无效值的行索引列表
    :return: 只包含有效行的DataFrame
    """
    if invalid_rows is not None:
        df = df.drop(invalid_rows)
    else:
        df = df.dropna(axis=0, how='any')
    return df


def remove_invalid_city_columns(df, invalid_columns=None):
    """
    删除含有无效值（NaN或指定无效值）的城市列，只保留所有数据都有效的城市。
    :param data: DataFrame，城市数据
    :param invalid_columns: 无效值的列索引列表
    :return: 只包含无无效值列的DataFrame
    """
    if invalid_columns is not None:
        df = df.drop(invalid_columns, axis=1)
    else:
        df = df.dropna(axis=1, how='any')
    return df


def extract_sites_data(file_name, start_site='1141A', end_site='1269A', invalid_type_values=None, invalid_values=None):
    """
    先丢弃原始csv数据中为无效值的所有行，再丢弃有无效值的所有城市列。
    :param file_name: csv文件路径
    :param start_site: 起始站点编号（字符串）
    :param end_site: 结束站点编号（字符串）
    :param invalid_type_values: 某一列（如type）为这些值的行会被丢弃
    :param invalid_values: 其他无效值（如-9999、空字符串等）会被替换为np.nan
    :return: 只包含所需站点数据且无无效值城市的DataFrame，列名为站点编号
    """
    df = pd.read_csv(file_name, header=None)

    # 先丢弃无效行
    # df = remove_invalid_rows(df)

    start_num = int(start_site[:-1])
    end_num = int(end_site[:-1])
    suffix = start_site[-1]
    site_ids = [f"{i}{suffix}" for i in range(start_num, end_num + 1)]

    base_num = 1001
    base_col = 3

    start_col = base_col + (start_num - base_num)
    end_col = base_col + (end_num - base_num)

    sites_data = df.iloc[:, start_col:end_col+1]
    sites_data.columns = site_ids

    # 再丢弃有无效值的城市列
    # sites_data = remove_invalid_city_columns(sites_data)

    return sites_data


def save_data_as_csv(data, file_name, original_file=None):
    """
    保存数据到csv文件，并在前面加上原始csv的第1/2/3列。
    不写入header（列名），不写入索引。
    :param data: 需要保存的DataFrame（只包含站点数据）
    :param file_name: 保存的文件名
    :param original_file: 原始csv文件路径（用于提取前3列）
    """
    if original_file is not None:
        # 读取原始csv的前3列
        original_df = pd.read_csv(
            original_file, header=None, usecols=[0, 1, 2])
        # 拼接前3列和站点数据
        result = pd.concat([original_df, data], axis=1)
    else:
        result = data
    result.to_csv(file_name, index=False, header=False)


def extract_current_hour_data(file_name):
    df = pd.read_csv(file_name)
    df = df.iloc[[0, 1, 3, 5, 7, 10, 12], :]
    df.to_csv(file_name+"_current_hour.csv", header=True, index=False)
    return df


def extract_some_city_data(file_name, city_cols: list):
    df = pd.read_csv(file_name)
    df = df.iloc[:, city_cols]
    df.to_csv(file_name+"_some_city_data.csv",
              header=True, index=False)
    return df


if __name__ == "__main__":
    sites_df = extract_sites_data(
        'data/站点_20250101-20250215/站点_20250101-20250215/china_sites_20250215.csv')
    print(sites_df)
