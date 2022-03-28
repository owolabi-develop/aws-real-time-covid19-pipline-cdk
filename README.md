#  Real time Covid19 Death Rate Pipline

The idea of this Project was extracting covid19 data in real time from finnhub api endpoint using aws lambda function as producer to extract the data from the api then produce it to kinesis datastream. then tigger another aws lambda function to consume the data and load to dynamodb.
Second process to query the data in real time using real-time kinesis data analytics with apache flink.
last using glue crawler and catalog the dynamodb and use anthena to query the data



## Architecture Diagram
![Architecture Diagram](image.jpg)




