#!/bin/bash

dataDir="$(pwd)/data/ec2/"
for region in `aws ec2 describe-regions --output text | awk '{print $4}'`
do
     echo  "\nListing Instances in region:'$region'..."
	   aws ec2 describe-instances \
       --region $region \
      --filters Name=instance-state-name,Values=running \
      --query 'Reservations[*].Instances[*].{Name:Tags[?Key==`Name`]|[0].Value, TypeName:Tags[?Key==`Type`]|[0].Value, Instance:InstanceId,Type:InstanceType, SubnetId:SubnetId, State:State.Name, PrivateIpAddress:PrivateIpAddress,PublicIpAddress: PublicIpAddress, region:Placement.AvailabilityZone}' \
      --output json > $dataDir/instances-$region.json
done

# cd src && python exporter/ec2_merge.py --json_dir $dataDir
PYTHONPATH="$(pwd):$(pwd)/src"
cd src && python -m "exporter.ec2_merge" --json_dir $dataDir --output_dir $dataDir/output