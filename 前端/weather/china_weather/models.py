from django.db import models

# 中国地图数据模型
class ChinaMap(models.Model):
    month = models.IntegerField()
    province = models.CharField(max_length=50)
    temp = models.IntegerField()
    wind_speed = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'china_map'

# 省份温度数据模型
class ProvinceTemp(models.Model):
    province = models.CharField(max_length=50)
    month = models.IntegerField()
    temp = models.IntegerField()
    temp_forecast = models.FloatField()
    
    class Meta:
        managed = False
        db_table = 'province_temp'

# 省份气压数据模型
class ProvincePressure(models.Model):
    month = models.IntegerField()
    province = models.CharField(max_length=50)
    pressure = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'province_pressure'

# 城市温度数据模型
class CityTemp(models.Model):
    city = models.CharField(max_length=50)
    month = models.IntegerField()
    temp = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'city_temp'

# 城市降水量Top10数据模型
class CityPrecipitationTop10(models.Model):
    month = models.IntegerField()
    city = models.CharField(max_length=50)
    precipitation_6 = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'city_precipitation_top10'
