#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /nycpark/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/NYC_parking_violations.csv /nycpark/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/nycpark/mapper.py -mapper ../../mapreduce-test-python/nycpark/mapper.py \
-file ../../mapreduce-test-python/nycpark/reducer.py -reducer ../../mapreduce-test-python/nycpark/reducer.py \
-input /nycpark/input/* -output /nycpark/output/
/usr/local/hadoop/bin/hdfs dfs -cat /nycpark/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/output/
../../stop.sh