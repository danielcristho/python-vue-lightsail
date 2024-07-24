from aws_cdk import (
    Stack,
    aws_lightsail as lightsail
    # Duration,
    # aws_sqs as sqs,
)
from constructs import Construct

class LightsailStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        """
        Create Lightsail Container Service
        """
        container_service = lightsail.CfnContainer(
            self, "flaskAPI",
            power="nano",
            scale=1,
            service_name="flask-api-container"
        )

        container_service.add_property_override(
            "APIDeployment",
            {
                "containers":{
                    "api": {
                        "image": "<url>",
                        "ports": {
                            "5000": "HTTP"
                    }
                }
            },
            "publicEndpoint": {
                "containerName": "api",
                "containerPort": 5000
                }
            }
        )
