package com;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class MaxTemperatureReducer extends Reducer<Text, FloatWritable,Text,FloatWritable> {
    @Override
    protected void reduce(Text key, Iterable<FloatWritable> values, Context context) throws IOException, InterruptedException {

        float maxValue = Float.MIN_VALUE;

        for (FloatWritable value : values) {
//          获取最高温度
            maxValue = Math.max(maxValue, value.get());
        }

        //     气温数据的膨胀因子为10，需要将获取的气温数据除以10
        float air = maxValue/10;

        context.write(key,new FloatWritable(air));
    }
}