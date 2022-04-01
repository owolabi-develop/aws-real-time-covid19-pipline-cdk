from constructs import Construct
from aws_cdk import(
    Stack,
    aws_kinesis as kinesis,
    Duration
    
    )

class KinesisStreamStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        covid19_death_rate = kinesis.Stream(self,
                                            "Covid19DeathRate",
                                            stream_name="DeathRate",
                                            retention_period=Duration.hours(24),
                                            shard_count=1
                                            )