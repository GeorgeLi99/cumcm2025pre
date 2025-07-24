import pandas as pd


def extract_sites_data(file_name, start_site='1141A', end_site='1269A'):
    """
    提取csv文件中从start_site到end_site的所有站点数据。
    假设文件无表头，第一列为日期，后面依次为1141A、1142A、...、1269A等站点数据。
    :param file_name: csv文件路径
    :param start_site: 起始站点编号（字符串）
    :param end_site: 结束站点编号（字符串）
    :return: 只包含所需站点数据的DataFrame，列名为站点编号
    """
    # 读取csv文件，无表头
    df = pd.read_csv(file_name, header=None)

    # 生成站点编号列表
    start_num = int(start_site[:-1])
    end_num = int(end_site[:-1])
    suffix = start_site[-1]
    site_ids = [f"{i}{suffix}" for i in range(start_num, end_num + 1)]

    # 计算这些站点在csv中的列索引（假设第2列开始为1141A）
    start_col = 1 + (start_num - int(start_site[:-1]))  # 其实就是1
    end_col = start_col + (end_num - start_num)

    # 提取对应列
    sites_data = df.iloc[:, start_col:end_col+1]
    sites_data.columns = site_ids  # 设置列名为站点编号

    return sites_data


if __name__ == "__main__":
    sites_df = extract_sites_data(
        'data/站点_20250101-20250215/站点_20250101-20250215/china_sites_20250215.csv')
    print(sites_df)
