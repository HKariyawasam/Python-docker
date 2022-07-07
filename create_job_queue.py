import boto3

client = boto3.client('batch', aws_access_key_id='AKIAZKKSUAGURNDKXKKX',
                      aws_secret_access_key='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',
                      region_name='us-east-1')

response = client.create_job_queue(
    jobQueueName='scripted_queue',
    state='ENABLED',
    priority=100,
    computeEnvironmentOrder=[
        {
            'order': 1,
            'computeEnvironment': 'scripted_env'
        },
    ],
)
print(response)
