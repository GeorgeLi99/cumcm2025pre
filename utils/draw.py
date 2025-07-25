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
