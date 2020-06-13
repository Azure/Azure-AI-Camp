#!/usr/bin/env bash

# This script is intended as an initialization script used in azuredeploy.json
# See documentation here: https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/custom-script-linux#template-deployment

# see abbreviated notes in README.md
# comments below:

adminUser=$1

WD=/home/$adminUser/notebooks

echo WD is $WD

if [ ! -d $WD ]; then
    echo $WD does not exist - aborting!!
    exit
else
    cd $WD
    echo "Working in $(pwd)"
fi

## now create the env...
condapath=/home/$adminUser/.conda/envs

if [ ! -d $condapath ]; then
    mkdir -p $condapath
fi

# Clone the content for the workshop
mkdir -p /etc/skel/notebooks
cd /etc/skel/notebooks
git clone https://github.com/Azure/Azure-AI-Camp.git

## Add user to docker group
sudo usermod -aG docker $adminUser

## Reboot jupyterhub
systemctl restart jupyterhub

echo "Done!"
