# Day 1

The day 1 platform is a Data Science Virtual Machine.  Please log in to Jupyterhub using the credentials and URL provided by instructor.

Topics covered
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

Instruction notes
---

* For the Data Science Virtual Machine, it's ok to get a "unsecure connection"-type warning for the https://<vm name>:8000 link you are given.  This is a known issue due to a certificate error.  Please proceed with the credentials given as this Azure site can be trusted.

* If you are using a local setup, set up a Python virtual environment and ensure you have the packages in the `requirements-local.txt` file installed into your Python 3 environment by running the following commands.

    python -m venv env

On macOS and Linux:

    source env/bin/activate

On Windows:

    .\env\Scripts\activate
    
Check with, on macOS and Linux:

    which python

On Windows:

    where python

Install necessary Python packages:

    pip install -r requirements-local.txt


* At the end of the day use the Jupyterhub terminal to zip up the notebooks folder and download it locally to save for future use.  The DSVM that was used will disappear into the sunset after approximately 24 hours of adjourning and will no longer be accesible.

* The YOLO v3 repo can be found here:  https://github.com/michhar/azureml-keras-yolov3-custom



