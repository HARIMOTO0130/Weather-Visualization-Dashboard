package com;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class MinTemperatureReducer extends Reducer<Text, FloatWritable,Text,FloatWritable> {
    @Override
    protected void reduce(Text key, Iterable<FloatWritable> values, Context context) throws IOException, InterruptedException {

        float minValue = Float.MAX_VALUE;

        for (FloatWritable value : values) {
//          获取最低温度
            minValue = Math.min(minValue, value.get());
        }

        //     气温数据的膨胀因子为10，需要将获取的气温数据除以10
        float air = minValue/10;

        context.write(key,new FloatWritable(air));
    }
}
