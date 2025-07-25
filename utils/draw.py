import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


def draw_line_chart_of_iaqi(iaqis, aqis, pollutant_labels=['pm2.5', 'pm10', 'so2', 'no2', 'o3', 'co']):
    num_cities = len(aqis)
    num_iaqi = len(iaqis[0]) if iaqis else 0
    base_colors = ['#FF0000', '#00FF00',
                   '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']

    fig, axes = plt.subplots(num_cities, 1, figsize=(
        8, 3*num_cities), constrained_layout=True)
    if num_cities == 1:
        axes = [axes]
    for i in range(num_cities):
        ax = axes[i]
        x_labels = ['AQI'] + pollutant_labels
        x = np.arange(len(x_labels))
        y = [aqis[i]] + list(iaqis[i])
        colors = ['#FF0000'] + base_colors[:len(iaqis[i])]
        ax.bar(x, y, color=colors)
        ax.set_xticks(x)
        ax.set_xticklabels(x_labels)
        ax.set_ylabel('iaqi and aqi of city '+str(i+1))
        ax.set_title(f'city{i+1} AQI and IAQI comparison')
    plt.show()


def draw_line_chart_every_day(iaqis, aqis, pollutant_labels=['pm2.5', 'pm10', 'so2', 'no2', 'o3', 'co']):
    """
    绘制每个城市的AQI和IAQI随时间变化的折线图，所有城市在同一画布上。
    :param iaqis: IAQI数据，格式为 [天][城市][分项]
    :param aqis: AQI数据，格式为 [天][城市]
    """
    num_days = len(iaqis)
    num_cities = len(iaqis[0])  # 城市数量
    num_pollutants = len(iaqis[0][0])  # 分项数量
    days = np.arange(1, num_days + 1)  # 天数
    colors = ['#FF0000', '#FFA500', '#90EE90', '#ADD8E6', '#DDA0DD', '#D3D3D3']
    # 创建子图
    fig, axes = plt.subplots((num_cities + 1) // 2, 2, figsize=(10, 5
                                                                * ((num_cities + 1) // 2)), constrained_layout=True)

    for city in range(num_cities):
        ax = axes[city // 2, city % 2]  # 计算当前城市对应的子图位置
        # AQI数据
        city_aqi = [aqis[day][city] for day in range(num_days)]

        # 绘制AQI
        ax.plot(days, city_aqi, label='AQI',
                marker='o', mfc="white", ms=3, color='blue', linestyle='-')

        # 绘制每个IAQI分项
        for pollutant_index in range(num_pollutants):
            city_iaqi = [iaqis[day][city][pollutant_index]
                         for day in range(num_days)]
            ax.plot(
                days, city_iaqi, label=f'IAQI {pollutant_labels[pollutant_index]}',
                marker='o', mfc="white", ms=4, color=colors[pollutant_index], linestyle='--')

        # 设置标题和标签
        ax.set_title(f'city{city + 1} AQI and IAQI comparison')
        ax.set_xlabel('day')
        ax.set_ylabel('value')
        ax.grid(True, linestyle='--', alpha=0.5)

    handles, labels = ax.get_legend_handles_labels()  # 获取最后一个子图的图例
    # 在全局位置添加图例
    fig.legend(handles, labels, loc='upper left',
               bbox_to_anchor=(0.248, 0.978), ncol=2)
    # 将图片以高分辨率保存到 picture 文件夹
    # plt.savefig('picture/Figure_five_day_comparison.png',
    #             dpi=1000, bbox_inches='tight', pad_inches=0.1)
    plt.show()
