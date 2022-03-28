from constructs import Construct
from aws_cdk import(
    Stack,
    aws_s3,
    RemovalPolicy
    )

class S3BucketAthenQueryStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        athena_query_result = aws_s3.Bucket(self,"S3BucketAthenQueryStack",
                                            bucket_name="queryResult",
                                            removal_policy=RemovalPolicy.DESTROY,
                                            auto_delete_objects=True,
                                            encryption=aws_s3.BucketEncryption.KMS
                                            )
        