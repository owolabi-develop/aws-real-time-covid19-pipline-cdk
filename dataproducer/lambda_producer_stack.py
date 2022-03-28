from typing import Any, Dict, Mapping
from constructs import Construct
from decouple import config
from aws_cdk import (
    Stack,
    aws_events,
    aws_events_targets,
    aws_iam as iam,
    aws_lambda as _lambda,
    Duration
    
)

ENVIRONMENT = {
    'API_KEY':"co2mespr01qp2sim3ndgco2mespr01qp2sim3ne0",
    "STREAM_NAME":"DeathRate"
}

class DataProducerStack(Stack):
     def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)
        
        lambda_role = iam.Role(
            self,
            "lambdaRole",
             assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
             managed_policies=[
                 iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                 iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                 iam.ManagedPolicy.from_aws_managed_policy_name("AmazonKinesisFullAccess"),
                 ##iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
             ]
        )
        
        finnhub_client_data_layer = _lambda.LayerVersion(
            self,
            "FinnhubClientDataLayer",
            code=_lambda.AssetCode("layer/finnhub_layer")
        )
        
        lambda_death_rate = _lambda.Function(self,
                                             "CovidLambdaSeathRate",
                                             runtime=_lambda.Runtime.PYTHON_3_10,
                                             code=_lambda.Code.from_asset("lambda"),
                                             handler="data_producer_lambda.handler",
                                             timeout=Duration.seconds(60),
                                             layers=[finnhub_client_data_layer],
                                             role=lambda_role,
                                             environment=ENVIRONMENT
                                             )
        
        
        
        