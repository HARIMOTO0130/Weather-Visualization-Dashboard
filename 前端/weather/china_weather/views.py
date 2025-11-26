from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import pandas as pd
import numpy as np
from django.utils.safestring import mark_safe
from sqlalchemy import create_engine, text
import json

# 递归转换numpy类型为Python原生类型
def convert_numpy_types(obj):
    """将numpy类型转换为Python原生类型，确保可以正确JSON序列化"""
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        # 特别处理字典键，确保键不是numpy类型
        new_dict = {}
        for key, value in obj.items():
            # 转换键中的numpy类型
            new_key = convert_numpy_types(key) if isinstance(key, (np.integer, np.floating)) else key
            new_dict[new_key] = convert_numpy_types(value)
        return new_dict
    elif isinstance(obj, (list, tuple)):
        return [convert_numpy_types(item) for item in obj]
    return obj

#创建mysql的连接 - 严格使用指定的连接字符串
engine = create_engine('mysql+pymysql://root:1234@192.168.56.101:3306/china_all')
table_name=['china_map','province_temp','province_pressure','city_temp','city_precipitation_top10']
sql_base='select * from '

# 初始化数据结构，避免连接失败时应用崩溃
map_data1 = {}
map_data2 = {}
months = []
provinces = []
line_data = {}
tree_data = {}
word_data = {}
bar_data = {}

# 尝试从数据库加载数据
try:
    # 读取地图数据
    sql = text(sql_base + table_name[0])
    with engine.connect() as connect:
        map_data = pd.read_sql(sql, connect)
    
    map_data['temp'] = np.round(map_data['temp']/10, 0)
    map_data['wind_speed'] = np.round(map_data['wind_speed']/10, 0)
    months = map_data['month'].unique()
    
    # 各省份气温数据
    for item in months:
        mydata = map_data[map_data['month'] == item]
        data_temp = []
        data_wind = []
        for i in mydata.index:
            dict_temp = {'name': mydata.loc[i, 'province'], 'value': mydata.loc[i, 'temp']}
            data_temp.append(dict_temp)
            dict_wind = {'name': mydata.loc[i, 'province'], 'value': mydata.loc[i, 'wind_speed']}
            data_wind.append(dict_wind)
        map_data1[item] = data_temp
        map_data2[item] = data_wind
    
    # 读取折线图数据
    sql = text(sql_base + table_name[1])
    with engine.connect() as connect:
        temp_province_data = pd.read_sql(sql, connect)
    
    temp_province_data['temp'] = np.round(temp_province_data['temp']/10, 0)
    temp_province_data['temp_forecast'] = np.round(temp_province_data['temp_forecast'], 0)
    provinces = list(temp_province_data['province'].unique())
    
    line_data = {}
    for item in provinces:
        temp_dict = {}
        temp_province = temp_province_data[temp_province_data['province'] == item]
        temp_dict['month'] = list(temp_province['month'].values)
        temp_dict['temp'] = list(temp_province['temp'].values)
        temp_dict['temp_forecast'] = list(temp_province['temp_forecast'].values)
        line_data[item] = temp_dict
    
    # 读取树图数据
    sql = text(sql_base + table_name[2])
    with engine.connect() as connect:
        pressure_data = pd.read_sql(sql, connect)
    
    pressure_data['pressure'] = pressure_data['pressure']/10
    tree_data = {}
    for item in months:
        mydata = pressure_data[pressure_data['month'] == item]
        pressure_month = []
        for i in mydata.index:
            pressure = {'name': mydata.loc[i, 'province'], 'value': mydata.loc[i, 'pressure']}
            pressure_month.append(pressure)
        tree_data[item] = pressure_month
    
    # 读取词云数据
    sql = text(sql_base + table_name[3])
    with engine.connect() as connect:
        city_temp_data = pd.read_sql(sql, connect)
    
    city_temp_data['temp'] = city_temp_data['temp']/10
    city_temp_data = city_temp_data.dropna()
    
    word_data = {}
    for item in months:
        mydata = city_temp_data[city_temp_data['month'] == item]
        temp_month = []
        for i in mydata.index:
            temperature = {'name': mydata.loc[i, 'city'], 'value': mydata.loc[i, 'temp']}
            temp_month.append(temperature)
        word_data[item] = temp_month
    
    # 读取条形图数据
    sql = text(sql_base + table_name[4])
    with engine.connect() as connect:
        precipitation_data = pd.read_sql(sql, connect)
    
    precipitation_data['precipitation_6'] = precipitation_data['precipitation_6']/10
    bar_data = {}
    for item in months:
        mydata = precipitation_data[precipitation_data['month'] == item]
        precipitation_month = {}
        precipitation_month['city'] = list(mydata['city'].values)
        precipitation_month['precipitation'] = list(mydata['precipitation_6'].values)
        bar_data[item] = precipitation_month
        
    print("数据库连接成功，数据加载完成")
    
except Exception as e:
    # 数据库连接失败时，使用默认数据
    print(f"数据库连接失败: {str(e)}")
    # 创建默认数据结构
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    provinces = ['北京', '上海', '广东', '四川', '黑龙江']
    
    # 生成默认气温数据
    for month in months:
        # 根据月份生成合理的温度值范围
        base_temp = 15 - (6 - month) * 2  # 1月冷，7月热
        temp_data = []
        wind_data = []
        
        for province in provinces:
            # 为不同省份设置不同的温度基数
            province_temp_offset = {
                '北京': -2,
                '上海': 0,
                '广东': 8,
                '四川': 2,
                '黑龙江': -15
            }
            
            temp = base_temp + province_temp_offset.get(province, 0) + np.random.randint(-3, 4)
            wind = 2 + np.random.random() * 3
            
            temp_data.append({'name': province, 'value': round(temp, 0)})
            wind_data.append({'name': province, 'value': round(wind, 1)})
        
        map_data1[month] = temp_data
        map_data2[month] = wind_data
        
        # 设置默认树图数据
        tree_data[month] = [{'name': p, 'value': 1013 + np.random.randint(-20, 20)} for p in provinces]
        
        # 设置默认条形图数据
        bar_data[month] = {
            'city': ['广州', '深圳', '杭州', '南京', '武汉'],
            'precipitation': [np.random.randint(50, 200) for _ in range(5)]
        }
    
    # 设置默认词云数据
    cities = ['广州', '深圳', '北京', '上海', '成都']
    for month in months:
        word_data[month] = [{'name': city, 'value': 15 + np.random.randint(-10, 15)} for city in cities]
    
    # 设置默认折线图数据
    for province in provinces:
        line_data[province] = {
            'month': list(range(1, 13)),
            'temp': [15 - (6 - m) * 2 + np.random.randint(-2, 3) for m in range(1, 13)],
            'temp_forecast': [15 - (6 - m) * 2 + np.random.randint(-2, 3) for m in range(1, 13)]
        }

def get_weather_data(request):
    # 从数据库获取气象数据
    try:
        month = request.GET.get('month', '1')
        
        # 如果已经加载了数据，直接返回
        if month in map_data1:
            response_data = {'data': map_data1[month], 'month': month}
            safe_response_data = convert_numpy_types(response_data)
            return JsonResponse(safe_response_data)
        else:
            # 从数据库动态获取该月份的数据
            sql = text(f"SELECT province, temp FROM china_map WHERE month = {month}")
            with engine.connect() as connect:
                mydata = pd.read_sql(sql, connect)
            
            # 处理数据格式
            temp_data = []
            for i in mydata.index:
                dict_temp = {
                    'name': mydata.loc[i, 'province'],
                    'value': np.round(mydata.loc[i, 'temp'] / 10, 0)
                }
                temp_data.append(dict_temp)
            
            response_data = {'data': temp_data, 'month': month}
            safe_response_data = convert_numpy_types(response_data)
            return JsonResponse(safe_response_data)
    except Exception as e:
        # 出错时返回默认数据
        default_data = [
            {'name': '北京', 'value': 15},
            {'name': '上海', 'value': 20},
            {'name': '广东', 'value': 25},
            {'name': '四川', 'value': 18},
            {'name': '黑龙江', 'value': 0}
        ]
        response_data = {'data': default_data, 'month': month, 'error': str(e)}
        safe_response_data = convert_numpy_types(response_data)
        return JsonResponse(safe_response_data)

def index(request):
    """主页面视图，渲染气象数据分析系统首页"""
    print("渲染主页面，开始转换numpy类型")
    # 转换所有数据中的numpy类型为Python原生类型
    safe_map_data1 = convert_numpy_types(map_data1)
    safe_map_data2 = convert_numpy_types(map_data2)
    safe_provinces = convert_numpy_types(provinces)
    safe_line_data = convert_numpy_types(line_data)
    safe_tree_data = convert_numpy_types(tree_data)
    safe_word_data = convert_numpy_types(word_data)
    safe_bar_data = convert_numpy_types(bar_data)
    
    print("numpy类型转换完成，准备渲染页面")
    return render(request, 'index.html', {
        'map_data1': mark_safe(json.dumps(safe_map_data1)),
        'map_data2': mark_safe(json.dumps(safe_map_data2)),
        'provinces': mark_safe(json.dumps(safe_provinces)),
        'line_data': mark_safe(json.dumps(safe_line_data)),
        'tree_data': mark_safe(json.dumps(safe_tree_data)),
        'word_data': mark_safe(json.dumps(safe_word_data)),
        'bar_data': mark_safe(json.dumps(safe_bar_data))
    })

def login(request):
    """保持兼容性的登录视图，重定向到主页面"""
    print("登录视图被调用，重定向到主页面")
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/')

