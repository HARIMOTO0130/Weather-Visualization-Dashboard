package com;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class ChinaDriver {
    public static void main(String[] args) {
        Configuration conf = new Configuration();
        Job job = null;

        try {
            // 读取filename文件内容获取inputpath
            BufferedReader br = new BufferedReader(new FileReader("/home/filename.txt"));
            String line = null;
            ArrayList list = new ArrayList();
            while((line=br.readLine())!=null){
                list.add(line);
            }
            Path[] inputPath = new Path[list.size()];
            for(int i = 0;i< inputPath.length;i++){
                inputPath[i] = new Path(list.get(i).toString());
                System.out.println(inputPath[i]);
            }



            job = Job.getInstance(conf);

            job.setJarByClass(ChinaDriver.class);
            job.setJobName("ChinaDriver");

            job.setMapperClass(ChinaMapper.class);
            job.setReducerClass(ChinaReducer.class);
            job.setMapOutputKeyClass(Text.class);
            job.setMapOutputValueClass(NullWritable.class);

            job.setOutputKeyClass(Text.class);
            job.setOutputValueClass(NullWritable.class);


            FileInputFormat.setInputPaths(job, inputPath);


            FileOutputFormat.setOutputPath(job, new Path("hdfs://master:9000/china_all/"));
            System.exit(job.waitForCompletion(true) ? 0 : 1);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
