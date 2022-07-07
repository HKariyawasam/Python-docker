import boto3

client = boto3.client('batch', aws_access_key_id='AKIAZKKSUAGURNDKXKKX',
                      aws_secret_access_key='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',
                      region_name='us-east-1')

response = client.submit_job(
    jobDefinition='scripted_job_multi_node_def_v1',
    jobName='scripted_job_v1',
    jobQueue='scripted_queue',
)

print(response)
