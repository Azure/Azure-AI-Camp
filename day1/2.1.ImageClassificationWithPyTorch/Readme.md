# Image Classification with Azure ML, PyTorch and AmlCompute

## Preparation

### Split data for training model

1. Download the zipped "suspicious behavior" data that was saved to Azure Blob Storage on Day 1 from Databricks data prep notebook and unzip.
2. Download the `cctvFrames_train_labels.csv` label file.
3. Run the image data splitting script:
    
    `scripts/separate_to_folders.py --dir <train data folder>`


### Upload data to Azure Blob Storage

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


### Obtain config file Azure ML Workspace

* Download the `config.json` from Azure ML Workspace in the Azure Portal or fill in the following and save as a json file.

```json
{
    "subscription_id": "",
    "resource_group": "",
    "workspace_name": ""
}
```

## Credits

The sample data originates from the EC Funded CAVIAR project/IST 2001 37540, found at URL: http://homepages.inf.ed.ac.uk/rbf/CAVIAR/.  Thank you, CAVIAR team!
