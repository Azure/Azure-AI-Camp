# Day 2
---

The day 2 platform is Azure Databricks.

Topics covered
---
* AutoML : Build a classification model on Local Compute on Azure DataBricks with deployment to ACI.
  The purpose of this lab is to learn how to use the Azure AML AutoML feature using a Databricks notebook running on Databricks. You will learn to do the following:

*   Create Azure Machine Learning Workspace object and initialize your notebook directory to easily reload this object from a configuration file.
*   Create an Experiment in an existing Workspace.
*   Configure AutoML using AutoMLConfig.
*   Train the model using AzureDataBricks.
*   Explore the results.
*   Register the model.
*   Deploy the model.
*   Test the best fitted model.


Instruction notes
---
*    Prerequisites: 
*    Strongly suggest creating a separate cluster for running these notebooks. Directions on attaching a library to a cluster can be found here:
    https://docs.databricks.com/libraries.html

*   You can select the option to attach the library to all clusters or just one cluster. Use the just one cluster option
*   Steps:
*   Install azureml-sdk with Automated ML
*   Source: Upload Python Egg or PyPi
*   PyPi Name: azureml-sdk[automl_databricks]
*   Install the azureml-core==1.0.79 library (following above process)
*   Install the numpy==1.16.2 library (following above process).
