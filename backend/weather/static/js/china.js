// 中国地图数据占位符
console.log('China map data placeholder loaded');

// 注册中国地图（简化版）
if (window.echarts) {
    // 注册中国地图
    echarts.registerMap('china', {
        type: 'FeatureCollection',
        features: [
            // 这里可以添加简化的中国省份GeoJSON数据
            // 为了演示，我们提供一些主要省份的中心点坐标
        ]
    });
    
    // 补充省份中心点坐标数据
    echarts.util.mapData.params.geoJson.features = [
        {properties: {name: '北京', cp: [116.4074, 39.9042]}},
        {properties: {name: '上海', cp: [121.4737, 31.2304]}},
        {properties: {name: '广东', cp: [113.2644, 23.1291]}},
        {properties: {name: '江苏', cp: [118.7674, 32.0415]}},
        {properties: {name: '浙江', cp: [120.1536, 30.2875]}},
        {properties: {name: '山东', cp: [117.0009, 36.6758]}},
        {properties: {name: '河南', cp: [113.6253, 34.7466]}},
        {properties: {name: '河北', cp: [114.5149, 38.0423]}},
        {properties: {name: '湖南', cp: [112.9822, 28.1941]}},
        {properties: {name: '湖北', cp: [114.3055, 30.5928]}},
        {properties: {name: '四川', cp: [104.0665, 30.6598]}},
        {properties: {name: '福建', cp: [119.3062, 26.0745]}},
        {properties: {name: '安徽', cp: [117.2830, 31.8612]}},
        {properties: {name: '黑龙江', cp: [126.6425, 45.7560]}},
        {properties: {name: '辽宁', cp: [123.4315, 41.8057]}},
        {properties: {name: '吉林', cp: [125.3245, 43.8172]}},
        {properties: {name: '陕西', cp: [108.9480, 34.3416]}},
        {properties: {name: '山西', cp: [112.5492, 37.8767]}},
        {properties: {name: '江西', cp: [115.8922, 28.6764]}},
        {properties: {name: '云南', cp: [102.7100, 25.0454]}},
        {properties: {name: '广西', cp: [108.3200, 22.8170]}},
        {properties: {name: '贵州', cp: [106.7135, 26.5784]}},
        {properties: {name: '重庆', cp: [106.5516, 29.5633]}},
        {properties: {name: '天津', cp: [117.1902, 39.3434]}},
        {properties: {name: '新疆', cp: [87.6168, 43.7934]}},
        {properties: {name: '甘肃', cp: [103.8343, 36.0611]}},
        {properties: {name: '青海', cp: [101.7789, 36.6172]}},
        {properties: {name: '宁夏', cp: [106.2329, 38.4860]}},
        {properties: {name: '内蒙古', cp: [111.7519, 40.8174]}},
        {properties: {name: '西藏', cp: [91.1142, 29.6466]}},
        {properties: {name: '海南', cp: [109.8908, 19.0399]}},
        {properties: {name: '香港', cp: [114.1733, 22.3200]}},
        {properties: {name: '澳门', cp: [113.5493, 22.1987]}},
        {properties: {name: '台湾', cp: [121.5654, 25.0330]}}
    ];
}