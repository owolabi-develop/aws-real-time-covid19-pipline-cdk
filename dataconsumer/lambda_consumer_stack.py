from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    Duration,
    aws_lambda_event_sources,
    aws_kinesis as kinesis
    
)
STREAM_ARN= "arn:aws:kinesis:us-west-1:730335628196:stream/DeathRate"
class DataConsumerStack(Stack):
     def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope,construct_id, **kwargs)
        
        lambda_consumer_role = iam.Role(
            self,
            id="lambdaRole",
             assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
             managed_policies=[
                 iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                 iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                 iam.ManagedPolicy.from_aws_managed_policy_name("AmazonKinesisFullAccess"),
                 iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
             ]
        )
        
        
        covid19_data_Consumer = _dynamodb.Table(self,
                                               id= "Covid19DataConsumer",
                                               table_name="Covid19DeathRate",
                                               partition_key=_dynamodb.Attribute(
                                                   name='state',type=_dynamodb.AttributeType.STRING),
                                               sort_key=_dynamodb.Attribute(
                                                   name='updated',
                                                   type=_dynamodb.AttributeType.STRING
                                                   )
                                               )
        
        
        
        lambda_death_rate_data_consumer = _lambda.Function(self,
                                             "CovidLambdaDeathRateconsumer",
                                             runtime=_lambda.Runtime.PYTHON_3_10,
                                             code=_lambda.Code.from_asset("lambda"),
                                             handler="data_consumer_lambda.handler",
                                             timeout=Duration.seconds(60),
                                             role=lambda_consumer_role,
                                             )
        
        stream = kinesis.Stream.from_stream_arn(self,
                                                "covid19Stream",
                                                stream_arn=STREAM_ARN)
        
        lambda_death_rate_data_consumer.add_event_source(
            aws_lambda_event_sources.KinesisEventSource(
                stream=stream,
                batch_size=100,
                starting_position=_lambda.StartingPosition.LATEST
                
            )
        )
        
        
        
        
        
        
        