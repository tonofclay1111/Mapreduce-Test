#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /nycpark/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/NYC_parking_violations.csv /nycpark/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../mapreduce-test-python/nycpark/mapper_1.py -mapper ../../mapreduce-test-python/nycpark/mapper_1.py \
-file ../../mapreduce-test-python/nycpark/reducer_1.py -reducer ../../mapreduce-test-python/nycpark/reducer_1.py \
-input /nycpark/input/* -output /nycpark/output/
/usr/local/hadoop/bin/hdfs dfs -cat /nycpark/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /nycpark/output/
../../stop.sh
~                  