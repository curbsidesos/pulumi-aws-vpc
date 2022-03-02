from cssos_pulumi_aws_vpc import Vpc, VpcArgs
from pulumi import export
from pulumi_aws import get_availability_zones

zones = get_availability_zones(state="available")

vpc = Vpc("dev-python-api", VpcArgs(
    #extra name tag component not always used WIP
    description="dev-python-api",
    # extra tags
    base_tags={
        "Evironment": "dev",
        "Owner": "engineering",
        "Project": "python-api",
    },
    base_cidr="10.11.0.0/16",
    availability_zone_names=zones.names,
    zone_name="example.local",
    create_s3_endpoint=False,
    create_dynamodb_endpoint=False,
    #cssos specific infra count number (ie, 001, 002, etc.)
    infra_number = "002",
    public_subnet_count = 2,
    private_subnet_count = 2
))


export("vpcId", vpc.vpc.id)
export("publicSubnetIds", [subnet.id for subnet in vpc.public_subnets])
export("privateSubnetIds", [subnet.id for subnet in vpc.private_subnets])
