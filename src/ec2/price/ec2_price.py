import json

import requests


def get_ec2_price(region, types):
    '''

    :param region:
    :param types:
    :return:
    {
        "Prices":[
            {
                "InstanceType":"m5zn.metal",
                "Memory":"192 GiB",
                "VCPUS":48,
                "Storage":"EBS only",
                "Network":"100 Gigabit",
                "Cost":3.9641,
                "MonthlyPrice":2893.793,
                "SpotPrice":"0.4789"
            }, ]
    }

    '''
    url='https://ec2.shop'
    url_full = f"{url}/?region={region}&filter={types}"
    res =requests.get(url_full, headers={'accept':'json'})
    res_json = json.loads(res.content)
    print(res.content)
    for x in res_json['Prices']:
        print(x)
    return res_json['Prices']

if __name__ == '__main__':
    get_ec2_price('us-east-2', 'm5.xlarge,m5.4xlarge')