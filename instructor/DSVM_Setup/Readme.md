# Linux Data Science Virtual Machine for Azure AI Camp

The button below deploys to an [Ubuntu-based Data Science VM](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro) (D, DS or NC-series) to azure and installs the relevant dependencies.

**NOTE**: An Azure subscription is required - see below.

## Deployment

Azure subscription required.

Hardware compute [fees](https://azure.microsoft.com/en-us/marketplace/partners/microsoft-ads/linux-data-science-vm/) apply. [Free Trial](https://azure.microsoft.com/free/) available for new customers.

**IMPORTANT NOTE**: Before you proceed to use the **Deploy to Azure** button you must perform a one-time task to accept the terms of the data science virtual machine on your Azure subscription. You can do this by visiting [Configure Programmatic Deployment](https://ms.portal.azure.com/#blade/Microsoft_Azure_Marketplace/LegalTermsSkuProgrammaticAccessBlade/legalTermsSkuProgrammaticAccessData/%7B%22product%22%3A%7B%22publisherId%22%3A%22microsoft-ads%22%2C%22offerId%22%3A%22linux-data-science-vm%22%2C%22planId%22%3A%22linuxdsvm%22%7D%7D)

Just click this button (see below for details).

**IMPORTANT NOTE**:  Due to JupyterHub requirements, keep your **admin name for this VM all lowercase**.

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fmichhar%2FAzure-AI-Camp%2Fmaster%2Finstructor%2FDSVM_Setup%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>

## VM size options

The default option is `DS12_v2`, a lower-end "Memory optimized" CPU VM with:

- 4 vCPU
- 28 GiB RAM
- 56 GiB Temp storage
- Premium disks supported

For infomation on pricing see the <a href="https://azure.microsoft.com/en-us/pricing/" target="_blank">Pricing calculator</a>.  Also, please see the notes in the VM sizes for CPU memory optimized VMs in this <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/sizes-memory" target="_blank">documentation</a> or for NVIDIA GPU VMs in this <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes-gpu" target="_blank">documentation</a>).

**Specifically** note that the `vCPU` core quota for `_v2` and `_v3` series VMs is initially **set to 0 in each region** for every subscription. You must [request a vCPU quota increase](https://docs.microsoft.com/en-us/azure/azure-supportability/resource-manager-core-quotas-request) for these families in an [available region](https://azure.microsoft.com/regions/services/). If you choose one of the `NCXX_v2` or `NCXX_v3` VM sizes in the template without increasing your quota, the deployment **WILL FAIL**.

## What is deployed?

You define the name of a resource group, and the following services get deployed to that resource group:
  - An [Ubuntu-based Data Science VM](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro) with your defined user name and password.
  - Storage: A storage account and 2 disks for storing data
  - A network interface, virtual network, and public IP address
  
## What do I as a user control?

When you click on the `Deploy to Azure` button above, a custom template will launch in the Azure portal that asks you for some information:

- Subscription you are creating the resources in
- Resource group you want to create all the resources in
- Location (i.e. Data Center where the resource group and resources physically live)
- DNS label prefix
- Admin Username
- Admin Password
- VmSize (`DS12_v2` as default; other options available, see note above)
- Vm Name

All of this information is controlled with the [azuredeploy.json](azuredeploy.json) file in this folder.

## What happens when I deploy?

The resources are created, and then a [custom script extension](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/custom-script-linux#template-deployment) is used to download the [dsvm-setup.sh](dsvm-setup.sh) script from this github repository and then run it. This script is run as root and takes a single argument: the name of the admin user you specify in the portal.

## What does the script do?

It does the following:

- Clones this repo into the notebooks folder so that it is accessible by JupyterHub.
- Makes sure that permissions are appropriate to the admin user.

See the [dsvm-setup.sh](dsvm-setup.sh) file for details.


## Creating the DSVM for Linux (Ubuntu) using command line and execute a post install script on the VM Instance

To create the Ubuntu DSVM with the Azure CLI Version 2, use the steps below. These use the ARM template azuredeploycli.json. This also executes a post install bash script that can configure the VM to your needs or install any additional packages you want on the VM.

Step 1: Create a Parameter file (JSON format like `params-template.json`) for the DSVM you are going to deploy. The file looks like:

```
  {
    "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
       "dnsLabelPrefix": {"value": "DNS LABEL e.g. alexandria"},
       "adminUsername": { "value" : "USERNAME e.g. cleopatra (please keep all lowercase)"},
       "adminPassword": { "value" : "PASSWORD (there are special requirements)"},
       "vmName": { "value" : "VM NAME e.g. egypt"},
       "vmSize": { "value" : "VM SIZE e.g. Standard_DS3_v2"}
    }
  }
```

Replace the parameters with values you will use for your new DSVM you are creating. A list of allowed vmSize is found in the [Ubuntu DSVM ARM template](azuredeploy.json). 

Step 2: Use the following Azure CLI to create VM:

    # Follow instructions of az login to signin to your Azure account. May need to select subscription if you have multiple
    az login
    az group create --name <NAME OF RESOURCE GROUP> --location <Data center. For eg: "West US 2">
    az group deployment create --resource-group  <NAME OF RESOURCE GROUP ABOVE>  --template-file azuredeploy.json --parameters @params.json
