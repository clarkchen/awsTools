import boto3


def get_regions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    ret = [x['RegionName'] for x in response['Regions']]
    print('\n'.join(ret))
    return ret

if __name__ == '__main__':
    get_regions()