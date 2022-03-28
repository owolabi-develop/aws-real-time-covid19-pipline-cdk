import boto3
import base64
import json

def handler(event,context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Covid19DeathRate")
    for record in event['Records']:
        record_data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(record_data)
        table.put_item(
            Item=data
        )
    