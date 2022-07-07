import boto3

client = boto3.client('batch')

response = client.submit_job(
    jobDefinition='scripted_job_multi_node_def_v1',
    jobName='scripted_job_v1',
    jobQueue='scripted_queue',
)

print(response)
