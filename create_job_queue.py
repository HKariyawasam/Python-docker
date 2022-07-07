import boto3

client = boto3.client('batch')

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
