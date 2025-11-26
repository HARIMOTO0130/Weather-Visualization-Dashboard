// 绘制全局时间线（1-12月自动切换）
function timeline() {
    // 1. 获取时间线DOM容器（需与index.html中容器ID一致）
    var chartDom = document.getElementById('time_line');
    var myChart = echarts.init(chartDom);
    
    // 2. 定义时间线节点：1-12月
    var months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
    
    // 3. ECharts配置项（参考官网示例修改）
    var option = {
        // 时间线核心配置
        timeline: {
            data: months,  // 时间节点：1-12月
            autoPlay: true,  // 自动播放
            loop: true,  // 循环播放（12月后回到1月）
            playInterval: time_interval,  // 切换间隔（复用全局变量，5000ms=5秒）
            left: '5%',  // 距离左侧5%（控制宽度）
            right: '5%',  // 距离右侧5%（控制宽度）
            controlStyle: {
                show: false  // 隐藏控制按钮（暂停/播放）
            },
            itemStyle: {
                color: '#00C6FB',  // 时间节点颜色（与大屏风格统一）
                borderColor: '#fff',
                borderWidth: 2
            },
            lineStyle: {
                color: '#195BB9',  // 时间线颜色
                width: 3
            },
            label: {
                normal: {
                    color: '#fff',  // 未选中节点文字颜色
                    fontSize: 12
                },
                emphasis: {
                    color: '#00C6FB',  // 选中节点文字颜色
                    fontSize: 14,
                    fontWeight: 'bold'
                }
            },
            checkpointStyle: {
                color: '#FFD700',  // 选中节点高亮颜色（金色）
                borderColor: '#fff',
                borderWidth: 3,
                radius: 8
            }
        },
        // 时间线对应的内容（此处无需显示内容，仅保留空series）
        series: []
    };
    
    // 4. 渲染时间线
    myChart.setOption(option);
    
    // 5. 窗口大小自适应
    window.addEventListener('resize', function () {
        myChart.resize();
    });
}