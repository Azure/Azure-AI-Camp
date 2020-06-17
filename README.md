<img src="assets/azure_camp.jpg" width="100%">

Through the Azure AI Camp, the ML practitioner will learn how to use Azure ML, Databricks, ML on the Edge and other Microsoft AI technologies to unlock insights on big datasets and deploy AI services to the cloud and edge.  It is designed as a hands-on workshop experience, recommended in instructor-led format or on-demand learning by using the [documentation](#on-demand-learning) and resources provided for guidance.

## Prerequisites

Required

1.  Python proficiency - <a href="https://rheartpython.github.io/navigating-ml/learning-python/" target="blank_">Resources</a>
2.  Azure Subscription
    - <a href="https://azure.microsoft.com/en-us/free/" target="blank_">Free trial</a>
    - <a href="https://github.com/siriuscomputersolutions/azure-cie/blob/master/1-GovMonSec/2-Exercise%20-%20Create%20an%20Azure%20Pass%20subscription%20-%2010%20mins.md" target="blank_">Redeem Azure Pass</a>
3.  Git proficiency and installed locally -  <a href="https://guides.github.com/introduction/git-handbook/" target="blank_">Git Handbook</a>

Recommended

1.  Machine learning and computer vision basics - <a href="https://cs231n.github.io/classification/" target="blank_">Course material on image classification</a>
1.  Python 3.6+ installed locally - <a href="https://docs.anaconda.com/anaconda/install/" target="blank_">Installation of Anaconda</a>
2.  Code editor like VSCode - <a href="https://code.visualstudio.com/download" target="blank_">Download Visual Studio Code</a>

## Resources provisioned

In this workshop, the following resources will get provisioned.  In practice, most are shared amongst an organization or group.  For this workshop it will depend upon the Azure Subscription setup.

1.  Azure Storage Account - <a href="https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal" target="blank_">Docs</a>
2.  Azure ML Workspace - <a href="https://docs.microsoft.com/en-us/azure/machine-learning/service/how-to-manage-workspace" target="blank_">Docs</a>
3.  Azure Databricks Workspace (<a href="https://docs.databricks.com/" target="_blank">Docs</a>) including:
    - ML runtime cluster
    - Non-ML runtime cluster
4.  Ubuntu Data Science Virtual Machine - <a href="https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro#jupyterhub-and-jupyterlab" target="_blank">Docs</a>


## Agenda

### Day 1
---
1. AI at MS Overview
    - Data Science and Azure
    - Cog Servs overview
    - Azure ML overview
    - Databricks overview
2. Azure ML on DSVM
    - Image classification with PyTorch estimator
    - Object detection with YOLO 
    - Azure ML with IoT
3. Video Analytics discussion
 

### Day 2
---
1. Deep dive into Databricks
2. ETL with Databricks
3. Auto ML with Databricks
4. Parallel and distributed training with Horovod and Databricks


## Technologies

1. Azure Databricks
2. Azure ML
3. Azure Storage
4. IoT Edge
5. Data Science Virtual Machine

## Setup on day-of

1. Git clone repo

    `git clone https://github.com/Azure/Azure-AI-Camp.git`

2. Create or download Azure ML Workspace configuration file (`config.json`) locally - <a href="https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#workspace" target="blank_">Doc</a>

## On-demand learning

Browse through day 1 and day 2 folders, noting that there are individual `Readme.md` documents in each section.  The day 1 platform is an Azure Data Science Machine and for day 2, the work will be done on a Databricks Workspace.  Various datasets in computer vision and related fields are used in conjuction with tools like Jupyter notebooks, Databricks notebooks, the Azure ML Python SDK and more.

For day 1, most of the hands-on work will be in Jupyter notebooks run locally or on an Azure Data Science Virtual Machine.  Whether local or on the VM, the learner will need to set this up for themselves.  More information on provisioning the Ubuntu Data Science Virtual Machine can be found <a href="https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro" target="blank_">here</a> and using Jupyterhub in the section on that tool <a href="https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-ubuntu-intro#jupyterhub-and-jupyterlab" target="blank_">here</a>.

For day 2, the hands-on work will be in the form of Databricks notebooks which are very similar to Jupyter notebooks, utilizing a cluster on an Azure Databricks Workspace.  The notebooks for day 2 are all stored as archives with the `.dbc` extension.  It is straightforward to import these notebooks into the Databricks workspace - instructions can also be found <a href="https://docs.databricks.com/notebooks/notebooks-manage.html#import-a-notebook" target="blank_">here</a> (import under workspace or individual user).

## Additional notes

In using and contributing to this repo, please adhere to <a href="https://opensource.microsoft.com/codeofconduct" target="_blank">Microsoft Open Source Code of Conduct</a>.

## Contributing

For contributing, guidelines may be found in [CONTRIBUTING.md](CONTRIBUTING.md).
