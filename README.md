
# Real-Time-Covid19 Death rate Tracking Piplines!

The idea of this Project was extracting covid19 data in real time from finnhub api endpoint using aws lambda function as producer to extract the data from the api then produce it to kinesis datastream. then tigger another aws lambda function to consume the data and load to dynamodb. Second process to query the data in real time using real-time kinesis data analytics for apache flink

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.


Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

## Architechure Diagram
<img width="3926" alt="aws_digram_project1" src="https://github.com/owolabi-develop/aws-real-time-covid19-pipline-cdk/assets/94055941/d6c9b752-5f1a-4432-aa34-987107c9f09e">


## Kinesis Stream data
![deathrateinkinese](https://github.com/owolabi-develop/aws-real-time-covid19-pipline-cdk/assets/94055941/63fcc579-0b13-4f04-927b-b70af8d172a6)


## Dynamodb  data
![desthrateindynamodb](https://github.com/owolabi-develop/aws-real-time-covid19-pipline-cdk/assets/94055941/67c7d4f3-7e92-4895-a786-5d236e3ea60f)



## Athena sample query  data
![athenaQuerypick](https://github.com/owolabi-develop/aws-real-time-covid19-pipline-cdk/assets/94055941/f1705f0b-dd11-4908-900e-e1925004af7c)


## Apache Flink applications Zeppline query
![sample_analytic_query](https://github.com/owolabi-develop/aws-real-time-covid19-pipline-cdk/assets/94055941/263aa09a-adfd-4341-ba4b-fe992cd34211)



## Apache Flink applications Zeppline real-time data
![sample_analytic_querydata](https://github.com/owolabi-develop/aws-real-time-covid19-pipline-cdk/assets/94055941/67bda186-9eba-4497-8356-3ce1f058cc9e)




## Apache Flink applications Zeppline real-time chart visulization

![alt text](digramphoto/sample_analytic_querylife.jpg)






