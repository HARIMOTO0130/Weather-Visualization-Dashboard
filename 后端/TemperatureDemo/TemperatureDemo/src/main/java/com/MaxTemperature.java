package com;

import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class MaxTemperature {
    public static void main(String[] args) {
        Configuration conf = new Configuration();

        Job job = null;
        try {
            job = Job.getInstance(conf);
            job.setJarByClass(MaxTemperature.class);
            job.setJobName("Max temperature");
            job.setMapperClass(MaxTemperatureMapper.class);
            job.setReducerClass(MaxTemperatureReducer.class);
            job.setMapOutputKeyClass(Text.class);
            job.setMapOutputValueClass(FloatWritable.class);
            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(FloatWritable.class);

            FileInputFormat.addInputPath(job,new Path("hdfs://master:9000/china_all/"));
            FileOutputFormat.setOutputPath(job,new Path("hdfs://master:9000/output/maxtemp/"));

            System.exit(job.waitForCompletion(true) ? 0 : 1);
//            job.submit();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}