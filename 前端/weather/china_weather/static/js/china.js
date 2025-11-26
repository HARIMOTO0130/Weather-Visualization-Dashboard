// 简化版中国地图数据
(function () {
    // 基本地图数据结构
    var geoJSON = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "北京"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [116.38, 40.25], [116.58, 40.25], [116.58, 40.45], [116.38, 40.45], [116.38, 40.25]
                    ]]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "上海"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [121.47, 31.23], [121.67, 31.23], [121.67, 31.43], [121.47, 31.43], [121.47, 31.23]
                    ]]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "广东"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [113.27, 23.13], [113.47, 23.13], [113.47, 23.33], [113.27, 23.33], [113.27, 23.13]
                    ]]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "四川"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [104.07, 30.63], [104.27, 30.63], [104.27, 30.83], [104.07, 30.83], [104.07, 30.63]
                    ]]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "黑龙江"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [[
                        [126.67, 45.83], [126.87, 45.83], [126.87, 46.03], [126.67, 46.03], [126.67, 45.83]
                    ]]
                }
            }
        ]
    };
    
    // 全局变量定义
    if (typeof window !== 'undefined') {
        window.chinaMapData = geoJSON;
        // 注册到ECharts（如果已加载）
        if (typeof echarts !== 'undefined') {
            echarts.registerMap('china', geoJSON);
        }
    }
    
    // 导出数据（Node.js环境）
    if (typeof module !== 'undefined' && typeof module.exports !== 'undefined') {
        module.exports = geoJSON;
    }
})();