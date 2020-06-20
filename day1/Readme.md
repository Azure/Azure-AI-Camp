# Day 1

The day 1 platform is a Data Science Virtual Machine.  Please log in to Jupyterhub using the credentials and URL provided by instructor.

Topics covered
---
1. AI at Microsoft Overview
    - Azure ML overview
    - Cognitive Services overview
    - Data in Azure and Databricks overview
    - AI and ML on Azure overview
2. Azure ML deep dive and hands-on labs with the DSVM
    - Image classification with PyTorch estimator hands-on lab
    - Object detection with YOLO walkthrough
    - Azure ML with IoT with hands-on lab

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



