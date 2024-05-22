#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /nba/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-python/nba/nba_shot_logs.csv /nba/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/nba/mapper.py -mapper ../../mapreduce-test-python/nba/mapper.py \
-file ../../mapreduce-test-python/nba/reducer.py -reducer ../../mapreduce-test-python/nba/reducer.py \
-input /nba/input/* -output /nba/output/
/usr/local/hadoop/bin/hdfs dfs -cat /nba/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nba/output/
../../stop.sh
