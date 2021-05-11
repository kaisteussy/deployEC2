import boto3
ec2 = boto3.resource('ec2')

# call the boto ec2 function to create a key pair
key_pair = ec2.create_key_pair(KeyName='ec2-keypair2')

# Capture the key and store it in a file
with open('ec2-keypair2.pem', 'w') as outfile:
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)
