from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)


from .hitcounter import HitCounter

class CdkworkshoppyStack(Stack):

     def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defining our Downstream Lambda
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        # Add Hit Counter to Stack
        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        # Whenever our endpoint is hit, API Gateway will route the request to our hit counter handler, 
        # which will log the hit and relay it over to the my_lambda function. 
        # Then, the responses will be relayed back in the reverse order all the way to the user.
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )