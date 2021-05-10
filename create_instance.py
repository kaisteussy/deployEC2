import boto3
import yaml

volumes = []
userdata_file = 'cloud_config_dev'

# Set the resource object to EC2
ec2 = boto3.resource('ec2')

# Open and store UserData bash script
with open(userdata_file, 'r') as file:
    userdata = file.read()

# Open the configuration file and store its contents
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# Iterate through and store the volumes listed in config.yml
for volume in config['server']['volumes']:
    volumes.append({'DeviceName': volume['device'],
                    'Ebs': {
                        'VolumeSize': volume['size_gb'],
                        'DeleteOnTermination': True
                        }
                    })


# Create the instance using stored config
try:
    instance = ec2.create_instances(
        ImageId=config['server']['ami_type'],
        MinCount=config['server']['min_count'],
        MaxCount=config['server']['max_count'],
        InstanceType=config['server']['instance_type'],
        KeyName=config['server']['key_pair'],
        BlockDeviceMappings=volumes,
        SubnetId=config['server']['network']['subnet'],
        PrivateIpAddress=config['server']['network']['ip_address'],
        SecurityGroupIds=config['server']['network']['security_groups'],
        UserData=userdata,
        #DryRun=True
    )
    iid = instance[0].id
    print(f'Instance {iid} successfully created.')
    print(f'IP Address: {instance[0].private_ip_address}')
except Exception as e:
    print('Failed to create instance:\n' + str(e))

