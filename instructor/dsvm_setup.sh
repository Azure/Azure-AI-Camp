#!/usr/bin/env bash

# This script is intended as an initialization script used in azuredeploy.json
# See documentation here: https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/custom-script-linux#template-deployment

# see abbreviated notes in README.md
# comments below:

# Input args
adminUser=$1
echo $adminUser >> "/home/userscript.log"
publicIP=`dig +short myip.opendns.com @resolver1.opendns.com`
echo $publicIP >> "/home/userscript.log"

# Script to update Notbook metadata
cat << EOF > /tmp/changenbmeta.py
#!/usr/bin/python
import json,sys
if len(sys.argv) < 2 :
        print "Usage: python changenbmeta.py <filename>"
        exit()
with open(sys.argv[1], "r") as jsonFile:
    data = json.load(jsonFile)
data["metadata"]["kernelspec"]["display_name"] = "Python 3.6 - PyTorch 1.1"
data["metadata"]["kernelspec"]["name"] = "pytorch1_1"
with open(sys.argv[1], "w") as jsonFile:
    json.dump(data, jsonFile)
EOF

# Clone the content
mkdir -p /etc/skel/notebooks/AICamp
cd /etc/skel/notebooks/AICamp
# git clone <repp>

# Change metadata on notebook to match kernel name in the fast.ai notebooks
find . -name \*.ipynb -exec /usr/bin/python /tmp/changenbmeta.py {} \;

# Save host public ip address to the users text file
echo $publicIP >> "/home/usersinfo.csv"

## declare an array of user names to create on vm
declare -a arr=("temp" "storm" "jeangrey" "spiderman" "captainmarvel" "quake" "wolverine" "thor" "ironman" "firestar" "rogue")
## now loop through the above array
for u in "${arr[@]}";
# Create users and generate random password with uppercase and punc chars. Run as root:
do
    sudo useradd -m $u
    p=`openssl rand -hex 4`
    p="P$p!"
    printf "$p\n$p" | sudo passwd $u
    echo $u, $p >> "/home/usersinfo.csv"

    # add user to sudoers
    sudo adduser $u sudo

    ## now create the env...
    condapath=/home/$u/.conda/envs

    if [ ! -d $condapath ]; then
        sudo mkdir -p $condapath
    fi

    ## Update appropriate permissions
    sudo chown -R ${u}:${u} ${condapath}

    ## Add user to docker group
    sudo usermod -aG docker $u
done
echo "Created users" >> "/home/userscript.log"

# # copy the notebooks to the users' profiles
# for filename in /home/*; do
#   dir=$filename/notebooks
#   user=${filename:6}
#   cp -r /etc/skel/notebooks/Workshop $dir
#   chown -R $user $dir/Workshop/*
#   chown $user $dir/Workshop
# done

# echo "Copied Workshop notebooks into user directories" >> "/home/userscript.log"

## now create the env...
condapath=/home/$adminUser/.conda/envs

if [ ! -d $condapath ]; then
    mkdir -p $condapath
fi

#### PYTORCH 1.1 ####

/data/anaconda/bin/conda create --name pytorch1 python=3.6 ipykernel conda

## update appropriate permissions
chown -R ${adminUser}:${adminUser} ${condapath}

# Install PyTorch 1.x into environment with cuda 9.2 support as DSVM is on this now
/data/anaconda/envs/pytorch1/bin/python -m conda install pytorch==1.1.0 torchvision cudatoolkit=9.0 -c pytorch -y
/data/anaconda/envs/pytorch1/bin/python -m pip install --yes bs4 jdc jupyter numpy requests scipy sklearn tqdm
/data/anaconda/envs/pytorch1/bin/python -m pip install --yes azureml-sdk[automl]==1.0.74

# LibTorch - install into /usr/local/lib
wget https://download.pytorch.org/libtorch/nightly/cu92/libtorch-shared-with-deps-latest.zip
unzip libtorch-shared-with-deps-latest.zip
sudo mv libtorch /usr/local/lib/python3.5/dist-packages/torch

## Install it as a kernel
/data/anaconda/envs/pytorch1/bin/python -m ipykernel install --name pytorch1_1 --display-name "Python 3.6 - PyTorch 1.1"

echo "Done setting up PyTorch 1.1" >> "/home/userscript.log"

## Update appropriate permissions
chown -R ${adminUser}:${adminUser} ${condapath}

## Reboot jupyterhub
systemctl restart jupyterhub

echo "Done!" >> "/home/userscript.log"
