# awsTools
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

# Features
* python based cli set to restructure aws infomation

# Env Setup
* python
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
* aws
```
# prepare your aws key and secret 
aws configure
```

# Cli List
## ec2
* List All Instances Detail and Price Info
  * fixed path ./data/ec2/
  * fixed ouputpath ./data/ec2/output/ec2Servers.xlsx
  * steps 
    * step1: get runing ec2 describe json files of each region
    * step2: query price from [ec2.shop](https://ec2.shop/)
    * step3: merge info into an excel file
  
```bash
./scripts/ec2-exports.sh
```

* List all available Ec2 Regions
```bash
cd src && python -m ec2.describe.regions

# output
# ap-east-1
# ap-southeast-1
# ap-southeast-2
# eu-central-1

```


* List EC2 instances count of a region
```bash
# cmd
cd src && python -m ec2.describe.instances
# output
# region us-east-2 servers 5


# cmd
cd src && python -m ec2.describe.instances --region ap-northeast-1
# output
# region ap-northeast-1 servers 1
```
