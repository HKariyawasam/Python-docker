import boto3

client = boto3.client('batch')

response = client.submit_job(
    jobDefinition='scripted_job_definition_ecr3_v3',
    jobName='scripted_job_ecr3_v1',
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
