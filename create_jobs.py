import boto3

client = boto3.client('batch', aws_access_key_id='AKIAZKKSUAGURNDKXKKX',
                      aws_secret_access_key='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',
                      region_name='us-east-1')

response = client.submit_job(
    jobDefinition='scripted_job_definition_v2',
    jobName='scripted_job_v1',
    jobQueue='scripted_queue',
    containerOverrides={
        'environment': [
            {
                'name': 'table_name',
                'value': 'batch-test-table',
            }
        ]
    }
)

print(response)
