// 绘制省份气温&风速地图（ECharts）
function map_chart() {
    // 1. 获取主区域DOM元素（需与index.html中主区域ID一致）
    var chartDom = document.getElementById('id3');
    var myChart = echarts.init(chartDom);
    
    // 2. 数据转换函数（适配ECharts散点格式）
    function convertData(data) {
        var res = [];
        for (var i = 0; i < data.length; i++) {
            var geoCoord = echarts.util.mapData.params.geoJson.features;
            for (var j = 0; j < geoCoord.length; j++) {
                if (geoCoord[j].properties.name === data[i].name) {
                    res.push([
                        geoCoord[j].properties.cp[0],  // 省份经度
                        geoCoord[j].properties.cp[1],  // 省份纬度
                        data[i].value                  // 风速值（用于散点大小）
                    ]);
                    break;
                }
            }
        }
        return res;
    }
    
    // 3. ECharts配置项
    var option = {
        // 标题（显示当前月份）
        title: {
            text: "2022年各省份" + month_index + "月份平均温度和风速情况",
            textStyle: text_style,  // 全局文字样式（index.html中定义）
            top: '5%',
            left: 'center'
        },
        // 提示框（鼠标悬浮显示）
        tooltip: {
            show: true,
            trigger: 'item',
            formatter: function (params) {
                // 自定义提示内容：省份+气温+风速
                return params.name + '<br/>' + 
                       '平均气温：' + params.value[2] + '°C<br/>' + 
                       '平均风速：' + params.value[0] + ' m/s';
            }
        },
        // 视觉映射器（气温颜色分级）
        visualMap: {
            show: true,
            left: '8%',
            top: 'bottom',
            seriesIndex: [1],  // 只作用于第2个系列（地图）
            pieces: [          // 气温区间颜色配置
                {gt: 25, label: '25°C以上', color: '#FF3300'},
                {gt: 20, lte: 25, label: '20°C-25°C', color: '#FF9966'},
                {gt: 10, lte: 20, label: '10°C-20°C', color: '#66FF33'},
                {gt: 0, lte: 10, label: '0°C-10°C', color: '#33CCFF'},
                {gt: -10, lte: 0, label: '-10°C-0°C', color: '#3333FF'},
                {lte: -10, label: '-10°C以下', color: '#6600CC'}
            ]
        },
        // 地图系列
        series: [
            // 散点图系列（显示风速）
            {
                name: '风速',
                type: 'scatter',
                coordinateSystem: 'geo',
                symbolSize: function (val) {
                    // 根据风速值动态调整散点大小
                    return Math.max(val[2] * 3, 10);
                },
                label: {
                    show: false
                },
                emphasis: {
                    label: {
                        show: true,
                        formatter: '{b}'
                    }
                },
                data: convertData(window.map_data2[month_index])
            },
            // 地图系列（显示气温）
            {
                name: '气温',
                type: 'map',
                map: 'china',
                roam: true,
                emphasis: {
                    label: {
                        show: true
                    }
                },
                data: window.map_data1[month_index]
            }
        ],
        // 地理坐标系
        geo: {
            map: 'china',
            roam: true,
            zoom: 1.2,
            label: {
                emphasis: {
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    areaColor: '#323c48',
                    borderColor: '#000'
                },
                emphasis: {
                    areaColor: '#2a333d'
                }
            }
        }
    };
    
    // 使用配置项
    myChart.setOption(option);
    
    // 响应式调整
    window.addEventListener('resize', function() {
        myChart.resize();
    });
}