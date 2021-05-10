import boto3
import yaml
import paramiko

volumes = []
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

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
        SubnetId=config['server']['network']['subnet'],
        # PrivateIpAddress='10.255.6.16',
        SecurityGroupIds=config['server']['network']['security_groups'],
        UserData='userdata.sh'
        #DryRun=True
    )
    iid = instance[0].id
    print(f'Instance {iid} successfully created.')
    print(f'IP Address: {instance[0].private_ip_address}')
except Exception as e:
    print('Failed to create instance:\n' + str(e))


# Function to SSH into the EC2 instance
def ssh_connect(ssh, ip_address):
    privkey = paramiko.RSAKey.from_private_key_file('ec2-keypair.pem')
    try:
        print('SSH into the instance: {}'.format(ip_address))
        ssh.connect(hostname=ip_address,
                    username='ec2-user', pkey=privkey)
        return True
    except Exception as e:
        print(str(e))


#ssh_connect(ssh, instance[0].private_ip_address)
