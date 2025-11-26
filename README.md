# 气象数据分析项目运行指南

## 项目概述
本项目是一个基于时间序列模型的NCDC气象数据分析系统，包含前端Django可视化界面和后端MapReduce数据处理功能。

![a7474b6312d8bcf5f6e78cf20ddc1241](https://github.com/user-attachments/assets/c9779668-0222-4b33-a08b-0c53c1dbb8d0)


## 运行步骤

### 1. 准备工作

#### 1.1 环境准备
- 确保已安装Python 3.8+、JDK 1.8、Maven 3.6+
- 确保Hadoop 2.9.2集群已正常运行
- 确保MySQL数据库（192.168.56.101:3306）已启动且创建了china_all数据库

#### 1.2 数据准备
- 将气象数据文件上传至HDFS：
  ```bash
  hadoop fs -mkdir -p /china_all/
  hadoop fs -put <气象数据文件> /china_all/
  ```

### 2. 后端MapReduce任务运行

#### 2.1 编译后端项目

```bash
# 编译TemperatureDemo项目
cd 后端/TemperatureDemo/TemperatureDemo
mvn clean package

# 编译china_etl项目
cd ../../china_etl/china_etl
mvn clean package
```

#### 2.2 运行ETL任务

```bash
# 运行数据清洗任务
hadoop jar target/china_etl-1.0-SNAPSHOT.jar com.ChinaDriver
```

#### 2.3 运行温度计算任务

```bash
# 运行最高温度计算任务
hadoop jar ../TemperatureDemo/target/TemperatureDemo-1.0-SNAPSHOT.jar com.MaxTemperature

# 运行最低温度计算任务
hadoop jar ../TemperatureDemo/target/TemperatureDemo-1.0-SNAPSHOT.jar com.MinTemperature
```

### 3. 前端Django项目运行

#### 3.1 安装依赖

```bash
cd 前端
pip install -r requirements.txt
```

#### 3.2 数据库初始化（首次运行）

```bash
cd weather
python manage.py migrate
```

#### 3.3 启动Django服务器

```bash
# 开发模式启动
python manage.py runserver 0.0.0.0:8000

# 生产环境建议使用uWSGI或Gunicorn
```

## 注意事项

### 1. 数据库配置
- 确保MySQL服务在192.168.56.101:3306上正常运行
- 确保用户名root和密码1234正确
- 确保china_all数据库已创建
- 确保数据库字符集为utf8mb4

### 2. Hadoop配置
- 确保HDFS服务正常运行
- 确保mapred-site.xml中配置了正确的资源限制
- 确保core-site.xml中配置了正确的文件系统URI
- 运行任务前确保输出目录不存在，或添加`-Dmapreduce.output.fileoutputformat.outputdir=新路径`参数

### 3. 数据处理
- 气象数据格式必须符合NCDC标准
- 处理缺失值(-9999)已在代码中处理，但其他异常值需预处理
- 大数据量处理时注意调整JVM内存参数

### 4. Django运行
- 生产环境必须修改SECRET_KEY
- 生产环境建议配置HTTPS
- 建议配置静态文件服务（如Nginx）
- 注意数据库连接池配置以优化性能

### 5. 性能优化
- 对于大规模数据，考虑增加Reducer数量
- 前端图表可考虑分页加载或数据抽样
- 定期清理HDFS中不必要的中间结果

## 常见问题排查

1. **Django连接MySQL失败**
   - 检查数据库服务是否运行
   - 检查防火墙设置是否允许访问3306端口
   - 检查用户名密码是否正确

2. **Hadoop任务失败**
   - 检查HDFS路径是否正确
   - 检查YARN资源是否充足
   - 查看任务日志定位具体错误

3. **前端页面无数据**
   - 检查后端MapReduce任务是否成功完成
   - 检查数据是否已导入MySQL数据库
   - 检查数据库查询语句是否正确

## 联系与支持
如有任何问题，请联系项目维护人员。
