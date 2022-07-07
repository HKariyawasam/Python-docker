import boto3


client = boto3.client('batch')


response = client.create_compute_environment(
    computeEnvironmentName='scripted_env',
    type='MANAGED',
    state='ENABLED',
    computeResources={
        'type': 'EC2',
        'allocationStrategy': 'BEST_FIT_PROGRESSIVE',
        'minvCpus': 0,
        'maxvCpus': 10,
        'subnets': [
            'subnet-0208bac11879c09b8',
            'subnet-027fc4b6c2207b18a',
            'subnet-0516d97f6c02a6c7d',
            'subnet-06abf0cd71ee84495',
            'subnet-0f0abda2f50728003',
            'subnet-0def59e9c6d309cb7',
        ],
        'instanceRole': 'ecsInstanceRole',
        'securityGroupIds': [
            'sg-0365261d691805a6b',
        ],
        'instanceTypes': [
            'optimal',
        ],
        'tags': {
            'Name': 'Batch Instance - EC2OnDemand',
        }
    }
)

print(response)
