# **HHA504 || Working with Cloud Storage in Azure and GCP**
---

- **🎯** This task is part of my assignment focused on familiarizing myself with cloud storage services. This repository contains codes and documentation on how I learned and gained hands-on experience uploading files to **`Azure Blob Storage`** and **`Google Cloud Platform (GCP) Cloud Storage`** using both **`Python`** scripts and the platform's **`GUI`**.

- **📝** Please refer to [**gcp_storage.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/gcp_storage.py) for the python scripts, which I created using **`Python`** in **`Visual Studio Code`** to upload files/images to GCP storage.

- **💡** Any feedback or suggestions are welcome to improve the content of this repository.

---

# _*Steps Taken to Complete this Assignment*_

# _*☞ AZURE*_

## Step 1: Setting up Storage Account
- Create a Storage Account
  - Navigate to Storage accounts by searching in the top search bar.
  - Click + Create to make a new Storage Account.
  - Select a Resource Group or create a new one.
  - Provide a Storage account name (it must be unique).
  - Select a Region and a Performance/Replication type based on requirements.
  - Click Review + create and then Create.
  
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/1.png" width="350" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/2.png" width="350" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/3.png" width="350" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/4.png" width="350" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/5.png" width="350" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/6%20-%20blob%20storage%20deployment%20completed!.png" width="500" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/7%20-%20blob%20storage%20overview%201.png" width="500" />.

  - Upload a sample file (e.g., a text file or image) to the Blob container using the Azure portal.

     <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/11%20-%20upload%20file%20or%20image.png" width="450" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/12%20-%20successfully%20uploaded%20a%20file%20inside%20blob.png" width="450" />.

## Step 2: Setting Up Access Credentials
-Create a Shared Access Signature (SAS) Token
  - In the Azure Portal, go to Storage Account.
  - Navigate to Settings > Shared access signature.
  - Set the permissions you need (in this case, Read, Write, Create).
  - Set the Start and Expiry Date/Time as needed.
  - Click Generate SAS and connection string.
  - Copy the SAS Token and Connection String—this will be needed in the script.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/8-%20blob%20overview%202.png" width="350" />.
  
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/9%20-%20creating%20container.png" width="280" />.
  
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/12%20-%20successfully%20uploaded%20a%20file%20inside%20blob.png" width="450" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/13%20-%20choose%20generate%20SAS.png" width="350" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/14%20-%20generate%20token.png" width="350" />.


## Step 3: Upload Files Using Python
- Write a Python script using [**Colab**](https://colab.research.google.com/drive/11xPrBx4gD230cUSt_bTNuJTP2iCXatl5) that uploads a file to the Blob container I created. Use the [**azure_storage_blob.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/azure_storage_blob.py) library to handle the upload.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/15%20-%20access%20key.png" width="350" />.
   
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/16%20-%20vsc%20-%20storage%20key%20-%20.env.png" width="500" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/17%20-%20vsc%20-%20to%20list%20container.png" width="500" />.
   
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/18%20-%20azure%20-%20list%20of%20containers%20after%20vsc.png" width="500" />.
   
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/19%20-%20vsc%20-%20upload%20blob%20-%20file.png" width="500" />.

   <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/20%20-%20azure%20-%20list%20of%20uploaded%20blob-file.png" width="500" />.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/21%20%20-%20vsc%20-%20another%20list%20of%20blob-file.png" width="500" />  

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/26%20-%20shared%20access%20signature%201.png" width="500" />.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/27%20-%20shared%20access%20signature%202.png" width="500" />.


## Step 4: Explore Storage Features
  - Explore and document the options for managing and securing data in Azure Blob Storage (e.g., access policies, tiers).
  
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/22%20-%20access%3Astorage%20tiers.png" width="500" />.
    
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/23%20-%20how%20to%20start%20to%20change%20blob%20tiers%20(hot-cold-cool).png" width="500" />  

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/24%20-%20changing%20blob%20tiers%20(hot-cold-cool).png" width="500" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/25%20-%20blob%20-%20access%20policy.png" width="500" />.

    
## Step 5: Create a fake image using Pillow and Run the Python Script
- The script created in my [**azure_blob_image.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/azure_blob_image.py) will generate a fake image and upload it to my Azure Blob Storage account.
  
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/28%20-%20vsc%20-%20image%20uploaded.png" width="500" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/29%20-%20azure%20-%20image%20uploaded!.png" width="500" />.




  
  <img src="" width="500" />  
  <img src="" width="500" />  
<img src="" width="500" />  
<img src="" width="500" />  
