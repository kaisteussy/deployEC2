import boto3
import yaml

volumes = []

# Set the resource object
ec2 = boto3.resource('ec2')

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
        KeyName='ec2-keypair',
        BlockDeviceMappings=volumes,
        SubnetId=config['server']['security_group'],
        # PrivateIpAddress='10.255.6.16',
        SecurityGroupIds=config['server']['subnet'],
        DryRun=True
    )
    iid = instance[0].id
    print(f'Instance {iid} successfully created.')
    print(f'IP Address: {instance.private_ip_address}')
except Exception as e:
    print('Failed to create instance:\n' + str(e))

