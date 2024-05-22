# Mapreduce-Test
This repository contains our project for Big Data Computing. The project focuses on utilizing Hadoop MapReduce on Google Cloud Platform (GCP) to analyze 2 different large datasets, one on New York City Parking and one of NBA shot logs. Our goal was to gain a better understanding of Hadoop MapReduce for distributed data processing, Hadoop Distributed File System (HDFS) for scalable storage, and the advantages of using GCP for managing and processing large datasets efficiently.

## Introduction to Hadoop
Hadoop is an open-source framework designed to store and process large datasets across clusters of computers using simple programming models. It provides a distributed storage and processing system, ensuring fault tolerance and high availability.
## Hadoop Components
1. Hadoop Distributed File System (HDFS): A distributed file system that stores data across multiple machines, providing high throughput access to application data.
2. MapReduce: A programming model for processing large data sets with a parallel, distributed algorithm on a cluster.

## Overview of MapReduce
MapReduce is the core component of Hadoop that allows for scalable and efficient processing of large datasets. It is composed of two primary functions:
1. Map Function: The Map function processes input data and produces a set of intermediate key/value pairs. Each input data element is independently processed by the map function.
2. Reduce Function: The Reduce function takes the intermediate key/value pairs produced by the map function and merges them to form a possibly smaller set of output key/value pairs. The reduce function is applied in parallel, typically after the map phase is complete.

## How MapReduce Works
1. Input Split: The input data is split into fixed-size pieces called input splits or chunks. Each split is processed by a separate map task.
2. Map Phase: Each map task processes an input split and generates intermediate key/value pairs. These pairs are grouped by key before being passed to the reduce phase.
3. Shuffle and Sort: The intermediate key/value pairs are shuffled (i.e., transferred across the network to reducers) and sorted by key. This step ensures that all values associated with a particular key are sent to the same reducer.
4. Reduce Phase: The reduce task processes the intermediate key/value pairs, merging them to produce the final output. The reduce function is applied to each unique key, aggregating its values.
5. Output: The final output is written to the HDFS, consisting of key/value pairs that are stored across the distributed file system.

Hadoop MapReduce provides a robust and scalable approach to processing vast amounts of data across distributed systems. Its simplicity and effectiveness have made it a cornerstone of big data processing, enabling organizations to derive insights from their data efficiently.

## Using Hadoop Mapreduce on Google Cloud Platform
We leveraged the Google Cloud Platform (GCP) to deploy and manage a Hadoop cluster, enabling us to utilize the power of Hadoop MapReduce for large-scale data processing.

# 1: New York City Parking Violations 
Our goal here was to analyze the parking violation data from New York City to gain insights into patterns and trends. We utilized data published by NYC OpenData. This dataset provides data on Parking Violations Issued between July 1, 2023 to June 30, 2024. It contains various features such as car model, color, location, time, and more.
![image](https://github.com/tonofclay1111/Mapreduce-Test/assets/164271616/9708e305-7b84-4336-8714-a0d684724903)

We aimed to answer the following questions:
1. When are tickets most likely to be issued?
2. What are the most common years and types of cars to be ticketed?
3. Where are tickets most commonly issued?
4. Which color of the vehicle is most likely to get a ticket?

Doing so helped us understand the distribution and frequency of parking violations across the city, which can help in guiding policy decisions and improving enforcement strategies.

## Download Data  
For downloading the NYC parking violation dataset, do the following:
1. Start 3 node cluster from Google Cloud account and connect from command line using the external IP of the Manager node (instance-1). Then use su root command and provide password.
2. Navigate to the data folder ``` cd mapreduce-test/mapreduce-test-data ```
3. Download the data using the fetch_data.sh file we created ```bash fetch_data.sh```
4. Ensure NYC_parking_violations.csv has been created and is stored within ``` cd mapreduce-test/mapreduce-test-data ```

In the fetch_data.sh, we used the curl command with NYC OpenData’s API. The API has a default limit of 1,000 rows of data that can be provided at one time. There are ways to adjust this by using offset and limit in the API call. Our script changes the limit to 100,000 rows at a time. It pulls the first 100,000 rows and writes it to the parking_violations.csv file. Then it loops through the rest of the data, adjusting the offset with every iteration and appending to parking_violations.csv. Since there are 10.7 millions rows of data and this script pulls the data in batches of 100,000 it needs to run 107 iterations. We added the iteration number and the url to the output so we can monitor the progress and confirm that the offset is updating with each iteration.

 
## Using Mapreduce to find when tickets are most likely to be issued
1. Navigate to  mapreduce-test/mapreduce-test-python/nycpark 
2. Ensure that there are 3 files there: mapper.py, reducer.py, and test.sh
3. Run the code by executing the command ```bash test.sh```
### Example Output:
![image](https://github.com/tonofclay1111/Mapreduce-Test/assets/164271616/de429581-9eb1-46f8-9006-e2b145149abe)

From our output, we can see that tickets are most likely to be issued on Thursdays with 1,561,910 parking tickets issued on that day. Tickets are least likely to be issued on Sunday with just 956,015 tickets issued.

## Using Mapreduce to find what the most common years and types of cars to be ticketed are
1. Navigate to  mapreduce-test/mapreduce-test-python/nycpark 
2. Ensure that there are 3 files there: mapper_1.py, reducer_1.py, and test_1.sh
3. Run the code by executing the command ```bash test_1.sh```
### Example Output:
![image](https://github.com/tonofclay1111/Mapreduce-Test/assets/164271616/0f19fc6b-8af6-42bc-a951-8556ac876f40)

We can see that 2021 Toyota’s had the highest number of tickets in our dataset. We can also see that Toyotas and Hondas were the most frequently ticketed vehicles as well as most tickets being issued to cars from the last few years.

## Using Mapreduce to find where tickets are most commonly issued
1. Navigate to  mapreduce-test/mapreduce-test-python/nycpark 
2. Ensure that there are 3 files there: mapper_2.py, reducer_2.py, and test_2.sh
3. Run the code by executing the command ```bash test_2.sh```
### Example Output:
![image](https://github.com/tonofclay1111/Mapreduce-Test/assets/164271616/a2a12c1d-8e34-40d6-817a-4f1e173735eb)

The street with the highest number of tickets is ‘WB N Conduit Ave @ 8’ in Queens with 193,732 parking tickets. The 2nd highest count is ‘Broadway’ in Manhattan which is one of the most popular streets in NYC. This output allows us to see which streets frequently get the highest number of tickets, giving us insight on where we should not park! 

## Using Mapreduce to find which color vehicle is most likely to get a ticket
1. Navigate to  mapreduce-test/mapreduce-test-python/nycpark 
2. Ensure that there are 3 files there: mapper_3.py, reducer_3.py, and test_3.sh
3. Run the code by executing the command ```bash test_3.sh```
### Example Output:
![image](https://github.com/tonofclay1111/Mapreduce-Test/assets/164271616/35afc6b5-bfac-418d-ad1a-97bf32be4a23)

From this output, we can see that black vehicles are the most frequently ticketed vehicles in our dataset with 2,653,385 tickets. The colors gray, white, red, and blue round out the top 5 most frequently ticketed vehicle colors. 

# 2: NBA Shot Logs
Here we utilize **Hadoop MapReduce** to analyze NBA shot logs from the 2014-2015 NBA season. The dataset was obtained from [Kaggle](https://www.kaggle.com/dansbecker/nba-shot-logs ) containing various details such as shot location, shooter, nearest defender, shot clock time, and more. Each row represents a shot, and the columns provide details of the shot.

![image](https://github.com/tonofclay1111/NBA-Shot-Log-Data/assets/164271616/6965d554-b562-4d8c-83d4-0e2f1efc2d28)

The main objective of this project was to find each players "most feared defender". We defined this through our **fear score**. The calculation goes as follows: For each pair of the players (A, B), we define the fear score of A when facing B as the hit rate of shots
out of total attempts. Based on the fear score for each defender of player A, we determined the most feared defender to be the defender with the lowest fear score, that was the closest defender at least 5 times. We set the threshold to 5 instances, so that we ensure statistical significance in our determination of the most feared defender, thereby filtering out isolated incidents.

## **Calculating Most Feared Defender**
  1. Start 3 node cluster from Google Cloud account and connect from command line using the external IP of the Manager node (instance-1). Then use su root command and provide password.
  2. Ensure that dataset is saved in mapreduce-test-data folder and named 'nba_shot_logs.csv'
  3. Navigate to /mapreduce-test/mapreduce-test-python/nba folder
  4. Ensure that there are 3 files there: mapper.py, reducer.py, and test.sh
  5. Run the code by executing the command ```bash test.sh```

### Example Output:
![image](https://github.com/tonofclay1111/NBA-Shot-Log-Data/assets/164271616/37af4da7-97df-467d-a5fc-aafbe7d5f4f8)

For each player in the first column, the player in the second column is there most feared defender. Column 3 shows the amount of field goals player A had when player B was the closest defender. Column 4 shows the field goal percentage for this permutation. Column 5 shows the total amount of field goal attempts in this permutation. This data is useful because it helps identify which defenders are most effective against specific players, allowing coaches and analysts to develop strategies for matchups and defensive assignments.
