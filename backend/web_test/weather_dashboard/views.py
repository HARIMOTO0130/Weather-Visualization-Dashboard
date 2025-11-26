from django.shortcuts import render

# 天气仪表盘首页视图
def dashboard_view(request):
    """显示天气信息大屏的主视图"""
    # 这里可以添加数据查询逻辑，从数据库获取真实的天气数据
    # 目前使用的是模板中的模拟数据
    
    context = {
        'title': '天气信息大屏展示',
        'description': '实时天气数据可视化展示'
    }
    
    return render(request, 'dashboard.html', context)