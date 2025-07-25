import pandas as pd
import numpy as np


def calculate_iaqi(df):
    all_iaqis = []
    iaqis = []
    aqis= []
    for col in df.columns:
        for row in range(len(df[col])):
            if row == 0:
                aqis.append(df[col][row])
            elif row == 1:
                # 计算pm2.5的IAQI
                if df[col][row] <= 35:
                    iaqis.append(df[col][row]/35*50)
                elif df[col][row] <= 75:
                    iaqis.append((df[col][row]-35)/40*50+50)
                elif df[col][row] <= 115:
                    iaqis.append((df[col][row]-75)/40*50+100)
                elif df[col][row] <= 150:
                    iaqis.append((df[col][row]-115)/35*50+150)
                elif df[col][row] <= 250:
                    iaqis.append((df[col][row]-150)/100*100+200)
                elif df[col][row] <= 350:
                    iaqis.append((df[col][row]-250)/100*100+300)
                elif df[col][row] <= 500:
                    iaqis.append((df[col][row]-350)/150*100+400)
                else:
                    iaqis.append(500)
                    print("发现pm2.5大于500的值")
            elif row == 2:
                # 计算pm10的IAQI
                if df[col][row] <= 50:
                    iaqis.append(df[col][row]/50*50)
                elif df[col][row] <= 150:
                    iaqis.append((df[col][row]-50)/100*50+50)
                elif df[col][row] <= 250:
                    iaqis.append((df[col][row]-150)/100*50+100)
                elif df[col][row] <= 350:
                    iaqis.append((df[col][row]-250)/100*50+150)
                elif df[col][row] <= 420:
                    iaqis.append((df[col][row]-350)/70*100+200)
                elif df[col][row] <= 500:
                    iaqis.append((df[col][row]-420)/80*100+300)
                elif df[col][row] <= 600:
                    iaqis.append((df[col][row]-500)/100*100+400)
                else:
                    iaqis.append(500)
                    print("发现pm10大于600的值")
            elif row == 3:
                # 计算so2的IAQI
                if df[col][row] <= 150:
                    iaqis.append(df[col][row]/30*50)
                elif df[col][row] <= 500:
                    iaqis.append((df[col][row]-150)/350*50+50)
                elif df[col][row] <= 650:
                    iaqis.append((df[col][row]-500)/150*50+100)
                elif df[col][row] <= 800:
                    iaqis.append((df[col][row]-650)/150*50+150)
                else:
                    iaqis.append(200)
                    print("发现so2大于800的值")
            elif row == 4:
                # 计算no2的IAQI
                if df[col][row] <= 100:
                    iaqis.append(df[col][row]/40*50)
                elif df[col][row] <= 200:
                    iaqis.append((df[col][row]-100)/100*50+50)
                elif df[col][row] <= 700:
                    iaqis.append((df[col][row]-200)/500*50+100)
                elif df[col][row] <= 1200:
                    iaqis.append((df[col][row]-700)/500*50+150)
                elif df[col][row] <= 2340:
                    iaqis.append((df[col][row]-1200)/1140*100+200)
                elif df[col][row] <= 3090:
                    iaqis.append((df[col][row]-2340)/750*100+300)
                elif df[col][row] <= 3840:
                    iaqis.append((df[col][row]-3090)/750*100+400)
                else:
                    iaqis.append(500)
                    print("发现no2大于3840的值")
            elif row == 5:
                # 计算o3的IAQI
                if df[col][row] <= 100:
                    iaqis.append(df[col][row]/100*50)
                elif df[col][row] <= 160:
                    iaqis.append((df[col][row]-100)/60*50+50)
                elif df[col][row] <= 215:
                    iaqis.append((df[col][row]-160)/55*50+100)
                elif df[col][row] <= 265:
                    iaqis.append((df[col][row]-215)/50*50+150)
                elif df[col][row] <= 800:
                    iaqis.append((df[col][row]-265)/535*100+200)
                else:
                    iaqis.append(400)
                    print("发现o3大于800的值")
            elif row == 6:
                # 计算co的IAQI
                if df[col][row] <= 5:
                    iaqis.append(df[col][row]/5*50)
                elif df[col][row] <= 10:
                    iaqis.append((df[col][row]-5)/5*50+50)
                elif df[col][row] <= 35:
                    iaqis.append((df[col][row]-10)/25*100+100)
                elif df[col][row] <= 60:
                    iaqis.append((df[col][row]-35)/25*100+150)
                elif df[col][row] <= 90:
                    iaqis.append((df[col][row]-60)/30*100+200)
                elif df[col][row] <= 120:
                    iaqis.append((df[col][row]-90)/30*100+300)
                elif df[col][row] <= 150:
                    iaqis.append((df[col][row]-120)/30*100+400)
                else:
                    iaqis.append(500)
                    print("发现co大于150的值")
        all_iaqis.append(iaqis)
        iaqis = []
    return aqis, all_iaqis
