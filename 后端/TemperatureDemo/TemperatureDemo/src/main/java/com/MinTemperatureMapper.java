package com;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class MinTemperatureMapper extends Mapper<LongWritable, Text,Text, FloatWritable> {
    private static final int MISSING = -9999;
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        if (!"".equals(line)) {
            String[] values = line.split(",");
//          获取年份
            String year = values[1];
//          获取月份
            String month = values[2];
//          拼接年份和月份，作为输出key
            String textKey = year + "-" + month;
//          获取气温数据
            float temp = Float.parseFloat(values[5]);
            if (temp != MISSING) {
                System.out.println(textKey+":"+temp);
                context.write(new Text(textKey), new FloatWritable(temp));
            }
        }

    }
}
