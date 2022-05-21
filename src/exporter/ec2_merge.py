
import os, json

import click
import pandas as pd

from ec2.price.ec2_price import get_ec2_price

# PYTHONPATH=os.environ.get('PYTHONPATH')
# print(PYTHONPATH)
# PATH=os.environ.get('PATH')
# print(PATH)

def _full_fill_price(df_instances: pd.DataFrame):
    if df_instances.empty:
        return
    regions = list(df_instances.region)
    regions = list(set([x[:-1] for x in regions]))
    types = set(list(df_instances.Type))
    region, instances = regions[0], types
    price_list = get_ec2_price(region, ','.join(instances))
    price_df = pd.DataFrame.from_records(price_list)
    merge_df = df_instances.merge(price_df, left_on=['Type'], right_on=['InstanceType'])
    return merge_df

def _parse_json_to_excel(json_dir, output_dir):
    json_files = [pos_json for pos_json in os.listdir(json_dir) if pos_json.endswith('.json')]
    # print(json_files)  # for me this prints ['foo.json']
    df_list = []
    for i in json_files:
        fpath = f"{json_dir}/{i}"
        print('handle file', fpath)
        with open(fpath, 'r') as f:
            content = f.read()
            if content=='': continue
            instances = json.loads(content)
            if not instances: continue
            data = []
            for x in instances:
                data.extend(x)
            df = pd.DataFrame.from_records(data)
            df =_full_fill_price(df)
            df_list.append(df)

            print('handle file ', i, 'json', len(instances), 'handle', len(df), 'handled file', len(df_list))

    df = pd.concat(df_list)
    # print(df.columns)
    df = df.sort_values(by=['region', 'TypeName', 'SubnetId', 'Type'])
    df.reset_index(drop=True, inplace=True)
    # print(df)
    print('total servers', len(df))
    output_file = f'{output_dir}/ec2Servers.xlsx'
    print(output_file)
    df.to_excel(output_file, index_label='Index')
    print(df.head())
    return output_file


@click.command()
@click.option("--json_dir", default='data/ec2', help="Describe output JsonDir")
@click.option("--output_dir", default='data/ec2/output', help="Merge Result OutputDir")
def parse_json_to_excel(json_dir, output_dir):
    '''
    批量处理, 由下面语句导出的 ec2 信息

    aws ec2 describe-instances \
       --region $region \
      --filters Name=instance-state-name,Values=running \
      --query 'Reservations[*].Instances[*].{Name:Tags[?Key==`Name`]|[0].Value, TypeName:Tags[?Key==`Type`]|[0].Value, Instance:InstanceId,Type:InstanceType, SubnetId:SubnetId, State:State.Name, PrivateIpAddress:PrivateIpAddress,PublicIpAddress: PublicIpAddress, region:Placement.AvailabilityZone}' \
      --output json > $outputDir/instances-$region.json


    :param json_dir:
    :param output_dir:
    :return:
    '''
    print('json_dir', json_dir)
    print('output_dir', output_dir)
    return _parse_json_to_excel(json_dir, output_dir)


if __name__ == '__main__':
    parse_json_to_excel()
