import boto3


client = boto3.client('batch', aws_access_key_id='AKIAZKKSUAGURNDKXKKX',
                      aws_secret_access_key='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',
                      region_name='us-east-1')


response = client.register_job_definition(
    jobDefinitionName='scripted_job_multi_node_def_v1',
    type='multinode',
    # containerProperties={
    #     'image': '640660275625.dkr.ecr.us-east-1.amazonaws.com/mydockerrepo2:latest',
    #     'memory': 2048,
    #     'vcpus': 1,
    #     'command': ["python", "-c", "import main; print(main.print_range(1,2))"]

    # },
    nodeProperties={
        "numNodes": 1,
        "mainNode": 0,
        "nodeRangeProperties": [
            {
                "targetNodes": "0:",
                "container": {
                    "image": "640660275625.dkr.ecr.us-east-1.amazonaws.com/mydockerrepo2:latest",
                    "vcpus": 1,
                    "memory": 2048,
                    "command": [
                        "python", "-c", "import main; print(main.print_range(1,2))"
                    ]
                }
            }
        ]
    },
    retryStrategy={
        "attempts": 1,
    }
)

print(response)
