# deployEC2
Deploy an AWS Linux EC2 instance.

INSTRUCTIONS:
_______________________________________________________________________________________
Edit the config.yml file to fit your needs. You will likely need to edit the following values:

key_pair,
network

IMPORTANT:
You will also need to insert the SSH-RSA public keys into the corresponding fields in the cloud-config file where you see the following:
<INSERT_YOUR_PUBLIC_KEY>

This ideally will be handled in config.yml in the future to prevent having to edit multiple files. For now, however, please edit both as instructed above.


Before running create_instance.py, make sure both cloud-config and config.yml are in the same directory. 
Run create_instance.py to create your AWS EC2 instance.
