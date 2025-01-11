# How to Set Up Lambda Layer for atproto

## How to log in from Terminal:
1. Create instance (Important: Add SSH access and allow SCP from other hosts)
2. Run the following:
	ssh -i ~/Downloads/Test-Key-Pair.pem ec2-user@ec2-3-17-160-24.us-east-2.compute.amazonaws.com
3. Update hostname if you have a new instance.

## Install PIP
1. `sudo yum install pip -y` (`-y` to auto-accept future questions)

## Create File Structure for zip file
1. `mkdir python/lib/python3.9/site-packages`
2. `cd !$`

## Pip install atproto from Linux EC2 instance to work on Lambda
pip install --upgrade atproto --platform manylinux2014_x86_64 --only-binary=:all: -t .



## SCP from EC2 to local
1. From local host: `scp -i ~/Test-Key-Pair.pem ec2-user@ec2-13-59-184-48.us-east-2.compute.amazonaws.com:/home/ec2-user/python.zip ~/dev`


