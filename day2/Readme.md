# Day 2
---

The day 2 platform is a Data Science Virtual Machine.  Please log in to Jupyterhub using the credentials and URL provided by instructor.

Topics covered
---
* 1.1:  Azure ML with AML Compute for Image Classification
* 1.2:  Real world example with YOLO v3
* 2.0:  Deploy an Azure ML model as an Edge Module

Instruction notes
---

* For the Data Science Virtual Machine, it's ok to get a "unsecure connection"-type warning for the https://<vm name>:8000 link you are given.  This is a known issue due to a certificate error.  Please proceed with the credentials given as this Azure site can be trusted.

* If you are using a local setup, set up a Python virtual environment and ensure you have the packages in the `requirements.txt` file installed into your Python 3 environment by running the following commands.

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

    pip install -r requirements.txt


* At the end of the day use the Jupyterhub terminal to zip up the notebooks folder and download it locally to save for future use.  The DSVM that was used will disappear into the sunset after approximately 24 hours of adjourning and will no longer be accesible.

* The YOLO v3 repo can be found here:  https://github.com/michhar/azureml-keras-yolov3-custom



