package com;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileSplit;
import org.apache.hadoop.mapreduce.InputSplit;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class ChinaMapper extends Mapper<LongWritable, Text,Text, NullWritable> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
//         获取当前map正在处理的文件信息
        InputSplit inputSplit = (InputSplit) context.getInputSplit();
//         获取文件名
        String fileName = inputSplit.toString().split("/")[5];
        NullWritable val = NullWritable.get();
//        String fileName = inputSplit.getPath().getName();
//        取出基站ID
        String stn = fileName.substring(0,5);
//        System.out.println(stn);

/**     获取所需字段
        year=[]   #年
        month=[]  #月
        day=[]    #日
        hour=[]   #时间
        temp=[]   #温度
        dew_point_temp=[]  #露点温度
        pressure=[]        #气压
        wind_direction=[]   #风向
        wind_speed=[]       #风速
        clouds=[]          #云量
        precipitation_1=[]   #1小时降水量
        precipitation_6=[]   #6小时降水量
*/
        String values = value.toString();
        String[] lines = values.split("\\s+");
        String year = lines[0];
        String month = lines[1];
        String day = lines[2];
        String hour = lines[3];
        String temp = lines[4];
        String dew_point_temp = lines[5];
        String pressure = lines[6];
        String wind_direction = lines[7];
        String wind_speed = lines[8];
        String cloud=lines[9];
        String precipitation_1 = lines[10];
        String precipitation_6 = lines[11];
        String line = stn+","+year+","+month+","+day+","+hour+","+temp+","+dew_point_temp
                +","+pressure+","+wind_direction+","+wind_speed+","+cloud+","+precipitation_1+","+precipitation_6;
        System.out.println(line);
        context.write(new Text(line),val);
    }



}
