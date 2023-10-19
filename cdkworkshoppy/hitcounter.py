from constructs import Construct
from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
)

class HitCounter(Construct):

    # Decorator - lets us define a "getter" method - a special kind of attribute. Allows us to access a method like an attribute without the need to
    # explicitly call it as a function. 
    @property
    def handler(self):
        return self._handler    

    def __init__(self, scope: Construct, id: str, downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        # DynamoDB Table
        table = ddb.Table(
            self, 'Hits',
            partition_key={'name': 'path', 'type': ddb.AttributeType.STRING}
        )

        # Our Hitcount Lambda function is defined here 
        self._handler = _lambda.Function(
            self, 'HitCountHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler='hitcount.handler',
            code=_lambda.Code.from_asset('lambda'),
            environment={
                'DOWNSTREAM_FUNCTION_NAME': downstream.function_name, # Late-Bound Value - only defined at deployment
                'HITS_TABLE_NAME': table.table_name,
            }
        )

        # Give permissions so our Lambda function has the IAM role to R/W to DynamoDB Table
        table.grant_read_write_data(self._handler)