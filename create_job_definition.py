import boto3


client = boto3.client('batch', aws_access_key_id='AKIAZKKSUAGURNDKXKKX',
                      aws_secret_access_key='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',
                      region_name='us-east-1')


response = client.register_job_definition(
    jobDefinitionName='scripted_job_definition_v2',
    type='container',
    containerProperties={
        'image': '640660275625.dkr.ecr.us-east-1.amazonaws.com/mydockerrepo2:latest',
        'memory': 2048,
        'vcpus': 1,
        'command': ["python", "-c", "import main; print(main.print_range(1,2))"]

    },

)

print(response)
