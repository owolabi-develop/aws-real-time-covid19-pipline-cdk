import os
import aws_cdk as cdk
from aws_cdk import Tags
from kinesis_stream.kinesis_stream_stack import KinesisStreamStack
from dataproducer.data_producer_stack import ProducerStack
from dataconsumer.data_consumer_stack import ConsumerStack
from s3_bucket.s3_bucket_athen_query_result import S3BucketAthenQueryStack
from glue.glue_crawler_stack import GlueCrawlerStack

env_US = cdk.Environment(account="521427190825",region='us-east-1')
app = cdk.App()

kinesisStream = KinesisStreamStack(app, "kinesisStreamStack",env=env_US)

Producer = ProducerStack(app,"ProducerStack",env=env_US)

Consumer= ConsumerStack(app,"ConsumerStack",env=env_US)

dbCrawler= GlueCrawlerStack(app,"GlueCrawlerStack",env=env_US)

AthenQueryStack = S3BucketAthenQueryStack(app,"S3BucketAthenQueryStack",env=env_US)

Tags.of(app).add("ProjectOwner","Owolabi akintan")
Tags.of(app).add("ProjectName","real-time-covid19-pipline")

app.synth()
