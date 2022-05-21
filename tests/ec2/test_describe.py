import json

from src.ec2.describe.instances import _get_instance_list


def test_ec2_instances():
    region = "ap-northeast-1"
    instances = _get_instance_list(region)
    print(instances)
    # s = json.dumps(instances)
    # print( 'Provider-ETH-EXE-01' in s)
    print(len(instances))
