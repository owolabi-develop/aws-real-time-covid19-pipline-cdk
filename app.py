#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags

env_US = cdk.Environment(account="730335628196",region='us-east-1')

from kinesis_stream.kinesis_stream_stack import KinesisStreamStack
from dataproducer.lambda_producer_stack import DataProducerStack
from dataconsumer.lambda_consumer_stack import DataConsumerStack
from s3_bucket.s3_bucket_athen_query_result import S3BucketAthenQueryStack
app = cdk.App()

kinesisStream = KinesisStreamStack(app, "kinesisStreamStack",env=env_US)

ProducerStack = DataProducerStack(app,"ProducerStack",env=env_US)

ConsumerStack = DataConsumerStack(app,"ConsumerStack",env=env_US)

AthenQueryStack = S3BucketAthenQueryStack(app,"S3BucketAthenQueryStack",env=env_US)

Tags.of(app).add("ProjectOwner","Owolabi akintan")
Tags.of(app).add("ProjectName","real-time-covid19-pipline")

app.synth()
