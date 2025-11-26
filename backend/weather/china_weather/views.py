from django.shortcuts import render
import pandas as pd
import numpy as np
from django.utils.safestring import mark_safe
from sqlalchemy import create_engine, text
from django.http import JsonResponse

# 1. 建立MySQL数据库连接（需替换为实际IP）
engine = create_engine('mysql+pymysql://root:root@192.168.4.190:3306/china_all')

# 2. 读取china_map表数据（含省份、月份、气温、风速）
sql = text('SELECT * FROM china_map')
with engine.connect() as conn:
    map_data = pd.read_sql(sql, conn)

# 3. 数据预处理：还原真实值（原始数据×10膨胀）
map_data['temp'] = np.round(map_data['temp'] / 10, 0)  # 气温÷10，保留0位小数
map_data['wind_speed'] = np.round(map_data['wind_speed'] / 10, 0)  # 风速÷10，保留0位小数

# 4. 获取所有月份（1-12）
months = sorted(map_data['month'].unique())  # 确保月份按1-12排序

# 5. 构建ECharts地图所需数据格式（key=月份，value=省份数据列表）
# map_data1：气温数据（地图颜色映射）
# map_data2：风速数据（地图散点大小映射）
map_data1 = {}
map_data2 = {}

for month in months:
    # 筛选当前月份数据
    month_data = map_data[map_data['month'] == month]
    temp_list = []  # 气温数据列表：[{name: 省份, value: 气温}, ...]
    wind_list = []  # 风速数据列表：[{name: 省份, value: 风速}, ...]
    
    for idx in month_data.index:
        # 构建气温数据字典
        temp_dict = {
            'name': month_data.loc[idx, 'province'],
            'value': month_data.loc[idx, 'temp']
        }
        # 构建风速数据字典
        wind_dict = {
            'name': month_data.loc[idx, 'province'],
            'value': month_data.loc[idx, 'wind_speed']
        }
        temp_list.append(temp_dict)
        wind_list.append(wind_dict)
    
    map_data1[month] = temp_list
    map_data2[month] = wind_list

# 主页视图函数：传递地图数据到模板
def login(request):
    return render(request, 'index.html', {
        'map_data1': mark_safe(map_data1),  # mark_safe：防止Django转义JSON格式
        'map_data2': mark_safe(map_data2)
    })

# 地图参考模板视图（修改为显示2022年1月份温度和风速数据）
def map_sample(request):
    """渲染地图参考模板，显示2022年1月份中国各省份平均温度和风速概况"""
    return render(request, '地图对照模板.html', {
        'map_data1': mark_safe(map_data1),  # 传递气温数据
        'map_data2': mark_safe(map_data2)   # 传递风速数据
    })
