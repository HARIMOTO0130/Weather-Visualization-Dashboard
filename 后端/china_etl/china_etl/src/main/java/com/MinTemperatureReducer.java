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
 * @Title: MinTemperatureReducer
 * @Package: com
 * @Description:
 * @Author: Yang（杨）
 * @Date: 2023/3/15 - 11:06
 */

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.mapreduce.Reducer;

import javax.xml.soap.Text;
import java.io.IOException;

public class MinTemperatureReducer extends Reducer<Text, FloatWritable,Text,FloatWritable> {
    @Override
    protected void reduce(Text key, Iterable<FloatWritable> values, Reducer<Text, FloatWritable, Text, FloatWritable>.Context context) throws IOException, InterruptedException {
        float minValue = Float.MAX_VALUE;
        for (FloatWritable value : values){
//          获取最低温度
            minValue = Math.min(minValue,value.get());
        }
        System.out.println(key+"最低气温是："+minValue);
        context.write(key,new FloatWritable(minValue));

    }
}
