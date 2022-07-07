import boto3

client = boto3.client('batch', aws_access_key_id='AKIAZKKSUAGURNDKXKKX',
                      aws_secret_access_key='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',
                      region_name='us-east-1')


def createjob(table_name):
    response = client.submit_job(
        jobDefinition='scripted_job_definition_ecr3_v3',
        jobName='scripted_job_ecr3_v1',
        jobQueue='scripted_queue',
        containerOverrides={
            'environment': [
                {
                    'name': 'table_name',
                    'value': table_name,
                }
            ]
        }

    )
    return response


for num in range(0, 10):
    createjob('tab-'+str(num))
