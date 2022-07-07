import boto3


client = boto3.client('batch')


response = client.register_job_definition(
    jobDefinitionName='scripted_job_definition_ecr3_v3',
    type='container',
    containerProperties={
        'image': '640660275625.dkr.ecr.us-east-1.amazonaws.com/mydockerrepo3:latest',
        'memory': 2048,
        'vcpus': 1,
        'command': ["python", "-c", "import main; print(main.print_range(1,2))"]

    },

)

print(response)
