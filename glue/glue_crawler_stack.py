from constructs import Construct
import aws_cdk as cdk

from aws_cdk import (
    aws_iam as _iam,
    aws_glue as _glue,
    aws_lakeformation as _lakeformation,
    Stack,
    aws_s3,
    RemovalPolicy,
    aws_sqs as _sqs,
    aws_s3_notifications as s3n,
    aws_lambda as _lambda
    
)


class GlueCrawlerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        glue_role = _iam.Role(self,
                              "GlueRole",
                               role_name="GlueServicDeathRole",
                               description='Role for Glue services to access dynamodb',
                               assumed_by= _iam.ServicePrincipal('glue.amazonaws.com'),
                               managed_policies=[
                                _iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                                _iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                                _iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"),
                                #_iam.ManagedPolicy.from_aws_managed_policy_name("AWSGlueServiceRole"),
                                _iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
                                ]
                              )
                
        glue_queue = _sqs.Queue(self, 'glue_queue')
        
        ### create glue catalog database
        glue_database = _glue.CfnDatabase(self,"covid19Death",
                                          catalog_id=cdk.Aws.ACCOUNT_ID,
                                          database_input=_glue.CfnDatabase.DatabaseInputProperty(
                                              name="covid-death-rate",
                                              description="database to store death rate of covid19"
                                          ))
        
        ## create glue lakeformation_permission
        _lakeformation.CfnPermissions(self, 'lakeformation_permission',
              data_lake_principal=_lakeformation.CfnPermissions.DataLakePrincipalProperty(
                  data_lake_principal_identifier=glue_role.role_arn),
              resource=_lakeformation.CfnPermissions.ResourceProperty(
                  database_resource=_lakeformation.CfnPermissions.DatabaseResourceProperty(
                      catalog_id=glue_database.catalog_id,
                      name='covid-death-rate')),
              permissions=['ALL'])
        
        ## create glue crawler
        _glue.CfnCrawler(self,"glue_crawler",
                         name='covid_crawler',
                         role=glue_role.role_arn,
                         database_name='covid-death-rate',
                          targets=_glue.CfnCrawler.TargetsProperty(
                           s3_targets=[
                               _glue.CfnCrawler.S3TargetProperty(
                                path=f's3://death-rate-bucket/',
                                event_queue_arn=glue_queue.queue_arn
                                )]),
                          
                      recrawl_policy=_glue.CfnCrawler.RecrawlPolicyProperty(
                      recrawl_behavior='CRAWL_EVENT_MODE')
                         )
        
        
        glue_workflow = _glue.CfnWorkflow(self, 'glue_workflow',
                                  name='glue_workflow',
                                  description='Workflow to process the covid19 data.')

        _glue.CfnTrigger(self, 'glue_crawler_trigger',
                 name='glue_crawler_trigger',
                 actions=[_glue.CfnTrigger.ActionProperty(
                     crawler_name='covid_crawler',
                     notification_property=_glue.CfnTrigger.NotificationPropertyProperty(notify_delay_after=3),
                     timeout=3)],
                 type='EVENT',
                 workflow_name=glue_workflow.name)