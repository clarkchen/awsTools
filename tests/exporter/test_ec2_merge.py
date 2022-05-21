
from src.exporter.ec2_merge import _parse_json_to_excel

def test_ap_north_east_2():
    src_dir = "../"
    test_dir = f"{src_dir}/data/test/ec2"
    output_dir = f"{src_dir}/data/test/ec2/output"
    # test_dir = "data/ec2"
    # output_dir = "data/ec2/output"

    _parse_json_to_excel(json_dir=test_dir, output_dir=output_dir)
