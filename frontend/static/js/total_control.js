// 全局变量（与index.html中定义的变量一致）
// month_index：当前显示月份（初始为1）
// time_interval：切换间隔（5000ms=5秒）

// 1. 月份切换函数：1→12循环
function month_index_charge() {
    if (month_index === 12) {
        month_index = 1;  // 12月后重置为1月
    } else {
        month_index++;    // 每月递增1
    }
    // 月份切换后重新绘制地图和时间线
    map_chart();
    timeline();
}

// 2. 初始化绘制地图和时间线（页面加载时执行）
map_chart();
timeline();

// 3. 定时切换月份（每5秒执行一次）
setInterval(month_index_charge, time_interval);