import json
import boto3
import base64
import finnhub
import datetime
from pprint import pprint
import os

def create_partition_fromDate(update):
    dt = datetime.datetime.strptime(update,"%Y-%m-%d %H:%M:%S")
    return dt
    
def handler(event,context):
    finnhub_client_data = finnhub.Client(api_key=os.environ['API_KEY'])
    ## finnhub_client_data return covid19 data as list of dict
    kinesis_client = boto3.client('kinesis')
    for covid_data in finnhub_client_data:
        partition_key = create_partition_fromDate(covid_data['updated'])
        response = kinesis_client.put_record(
            streamName=os.environ['STREAM_NAME'],
            data=json.dumps(covid_data).encode('utf-8'),
            PartitionKey=partition_key
        )
    return response
    
    
    