import boto3
import click


def _get_instance_list(region):
    # print('start handle', region)
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    instance_info = response['Reservations']
    print('region', region, 'servers',len(instance_info))
    return instance_info

@click.command()
@click.option("--region", default='us-east-2', help="region you hope to quer")
def get_instance_list(region):
    return _get_instance_list(region)

if __name__ == '__main__':
    get_instance_list()
