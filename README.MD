#Most Active Cookie Quantcast Challenge

Given a cookie log file in the following format:

>cookie,timestamp 
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00

Write a command line program in your preferred language to process the log file and return the most active
cookie for specified day. 

## To run the file
>./run.sh

##Algorithm
1. Parse the command line arguments to get the name of log file and date.
2. Preprocess the log file to check if it is formmated correctly.
3. Retrieve all the data for the specified date
4. Get the most frequent cookies by using a dictionary (O(N) Algorithm).
