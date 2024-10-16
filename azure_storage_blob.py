
# !pip install azure-storage-blob azure-identity python-dotenv

## link for azure connection/security: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-python-get-started?tabs=account-key
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from dotenv import load_dotenv


# Load environment variables from a .env file
load_dotenv()

# Retrieve the connection string from an environment variable
account_url_link = "https://raqsblobstorage.blob.core.windows.net"
os.getenv("AZURE_STORAGE_ACCESS_KEY")


# Create the BlobServiceClient object
def get_blob_service_client_account_key():

    account_url = account_url_link
    shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
    credential = DefaultAzureCredential()   

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    return blob_service_client

    shared_access_key = os.getenv("AZURE_STORAGE_ACCESS_KEY")
    credential = shared_access_key

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=credential)

    return blob_service_client

blob_service_client = get_blob_service_client_account_key()

## function to list containers https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-containers-list-python
def list_containers(blob_service_client):
    containers = blob_service_client.list_containers(include_metadata=True)
    for container in containers:
        print(container['name'], container['metadata'])

list_containers(blob_service_client)

## function to upload blobs https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-upload-python
def upload_blob_file(blob_service_client, container_name, filepathstring, filenamestring):
    container_client = blob_service_client.get_container_client(container=container_name)
    with open(file=os.path.join(filepathstring, filenamestring), mode="rb") as data:
        blob_client = container_client.upload_blob(name=filenamestring, data=data, overwrite=True)

upload_blob_file(blob_service_client, 'raqs-container', './', 'raqs-azure-blob.txt')

## function to list all blobs in a container: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-list-python

def list_blobs_flat(blob_service_client, container_name):
    container_client = blob_service_client.get_container_client(container=container_name)

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        print(f"Name: {blob.name}")

list_blobs_flat(blob_service_client, 'raqs-container')