package com;

/*
 * -----神兽护体，代码无Bug------
 *  ┏┓   ┏┓
 * ┏┛┻━━━┛┻┓
 * ┃       ┃
 * ┃   ━   ┃  围观是一种态度
 * ┃ ┳┛ ┗┳ ┃
 * ┃       ┃  围观是为了提高知名度
 * ┃   ┻   ┃
 * ┃       ┃
 * ┗━┓   ┏━┛
 *   ┃ 围┃
 *   ┃ 观┃
 *   ┃ 专┗━━━┓
 *  ┃  用　 　 ┣┓
 *  ┃         ┏┛
 *   ┗┓┓┏━┳┓┏┛
 *    ┃┫┫ ┃┫┫
 *    ┗┻┛ ┗┻┛
 * @Title: MinTemperatureMapper
 * @Package: com
 * @Description:
 * @Author: Yang（杨）
 * @Date: 2023/3/15 - 10:53
 */

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class MinTemperatureMapper extends Mapper<LongWritable, Text,Text, FloatWritable> {
    private static final int MISSING = -9999;
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, FloatWritable>.Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] values = line.split(",");
//      获取年份
        String year = values[1];
//      获取月份
        String month = values[2];
//      拼接年份和月份，作为输出key
        String textKey = year+"-"+month;
//      获取气温数据
        float temp = Float.parseFloat(values[5]);
        float air;
        if (temp != MISSING){
// 气温数据的膨胀因子为10，需要将获取的气温数据除以10
            air = temp/10;
            context.write(new Text(textKey),new FloatWritable(air));
        }


    }
}
