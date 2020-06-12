# Image Classification with Azure ML, PyTorch and AmlCompute

## Preparation

### Prerequisites

For this lab your will need the following.

- Azure ML Workspace
- Data Science Virtual Machine (Ubuntu OS version) that has been set up with a username and password (done during provisioning)
    - This VM will be used for JupyterHub - a Jupyter notebook system for running code in the browser.
    
> Note:  when provisioning the DSVM, ensure to use username and password for authentication (rather than SSH key) and that the **username is all lowercase**.

### Setup

* Navigate to the JupyterHub of the Data Science Virtual Machine (DSVM) you wish to use with the following path (use incognito or private browser window if you have multiple Azure Accounts).

`https://<public IP of VM or DNS name>.<azure region>.cloudapp.azure.com:8000`

for example:

`https://wonderwoman.eastus.cloudapp.azure.com:8000`

> Note:  if a security or certificate warning pops up, just know it is safe to proceed (expected behavior) so go ahead and do so.

* Log in with the username and password used when provisioning the DSVM.
* Open a terminal window
* Git clone this repository in the `/data/home/<username>/notebooks/` folder so that it appears in the JupyterHub home directory.
* Navigate to `day1/2.1.ImageClassificationWithPyTorch` folder


### Obtain config file Azure ML Workspace

* Download the `config.json` from Azure ML Workspace Overview pane in the Azure Portal or fill in the following and save as a json file in this folder.

```json
{
    "subscription_id": "",
    "resource_group": "",
    "workspace_name": ""
}
```

## Additional notes (for reference)

### If needing to split data for training model

1. Download the zipped "suspicious behavior" data that was saved to Azure Blob Storage on Day 1 from Databricks data prep notebook and unzip.
2. Download the `cctvFrames_train_labels.csv` label file.
3. Run the image data splitting script:
    
    `scripts/separate_to_folders.py --dir <train data folder>`


### If needing to upload data to Azure Blob Storage

1.  Locally, `pip install azure-storage-blob==2.1.0`
2.  Set the following environment variables

On Linux/MacOS:
```
export STORAGE_ACCOUNT_NAME=<name of your Storage Account>
export STORAGE_CONTAINER_NAME_TRAINDATA=<a name for the new Storage container>
export STORAGE_ACCOUNT_KEY=<Storage Account key>
```

On Windows:
```
set STORAGE_ACCOUNT_NAME=<name of your Storage Account>
set STORAGE_CONTAINER_NAME_TRAINDATA=<a name for the new Storage container>
set STORAGE_ACCOUNT_KEY=<Storage Account key>
```

3.  Run the uploader script, where the "--dir" "data" is the standard name of the split images base folder from above.

    `scripts/upload_to_blob.py --dir data`


## Credits

The sample data originates from the EC Funded CAVIAR project/IST 2001 37540, found at URL: http://homepages.inf.ed.ac.uk/rbf/CAVIAR/.  Thank you, CAVIAR team!
