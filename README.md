# **HHA504 || Working with Cloud Storage in Azure and Google Cloud Platform (GCP)**
---

- **🎯** This task is part of my assignment focused on familiarizing myself with cloud storage services. This repository contains codes and documentation on how I learned and gained hands-on experience uploading files to **`Azure Blob Storage`** and **`Google Cloud Platform (GCP) Cloud Storage`** using both **`Python`** scripts and the platform's **`GUI`**.

- **📌** Please refer to the following python scripts for uploading my files/images to GCP storage and Azure Blob Storage.
  - [**gcp_storage.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/gcp_storage.py) - created using **`Python`** in **`Visual Studio Code`**
  - [**azure_storage_blob.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/azure_storage_blob.py) - created using **`Python`** in both **`Visual Studio Code`** and **`Colab`**.
    
- **💡** Any feedback or suggestions are welcome to improve the content of this repository.

---

# _*Steps Taken to Complete this Assignment*_

---

# _*☞ AZURE*_
---

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
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/7%20-%20blob%20storage%20overview%201.png" width="600" />.

  - Upload a sample file (e.g., a text file or image) to the Blob container using the Azure portal.

     <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/11%20-%20upload%20file%20or%20image.png" width="500" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/12%20-%20successfully%20uploaded%20a%20file%20inside%20blob.png" width="500" />.

## Step 2: Setting Up Access Credentials
- Create a Shared Access Signature (SAS) Token
  - In the Azure Portal, go to Storage Account.
  - Navigate to Settings > Shared access signature.
  - Set the permissions you need (in this case, Read, Write, Create).
  - Set the Start and Expiry Date/Time as needed.
  - Click Generate SAS and connection string.
  - Copy the SAS Token and Connection String—this will be needed in the script.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/8-%20blob%20overview%202.png" width="500" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/9%20-%20creating%20container.png" width="350" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/12%20-%20successfully%20uploaded%20a%20file%20inside%20blob.png" width="500" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/13%20-%20choose%20generate%20SAS.png" width="500" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/14%20-%20generate%20token.png" width="350" />.


## Step 3: Upload Files Using Python
- Write a Python script using [**Colab**](https://colab.research.google.com/drive/11xPrBx4gD230cUSt_bTNuJTP2iCXatl5) that uploads a file to the Blob container I created. Use the [**azure_storage_blob.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/azure_storage_blob.py) library to handle the upload.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/15%20-%20access%20key.png" width="500" />.
   
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/16%20-%20vsc%20-%20storage%20key%20-%20.env.png" width="550" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/17%20-%20vsc%20-%20to%20list%20container.png" width="550" />.
   
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/18%20-%20azure%20-%20list%20of%20containers%20after%20vsc.png" width="550" />.
   
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/19%20-%20vsc%20-%20upload%20blob%20-%20file.png" width="550" />.

   <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/20%20-%20azure%20-%20list%20of%20uploaded%20blob-file.png" width="550" />.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/21%20%20-%20vsc%20-%20another%20list%20of%20blob-file.png" width="550" />  

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/26%20-%20shared%20access%20signature%201.png" width="550" />.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/27%20-%20shared%20access%20signature%202.png" width="550" />.

## Step 4: Create a fake image using Pillow and Run the Python Script
- The script created in my [**azure_blob_image.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/azure_blob_image.py) will generate a fake image and upload it to my Azure Blob Storage account.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/28%20-%20vsc%20-%20image%20uploaded.png" width="550" />.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/29%20-%20azure%20-%20image%20uploaded!.png" width="550" />.

## Step 5: Explore Storage Features
  - Explore and document the options for managing and securing data in Azure Blob Storage (e.g., access policies, tiers).
  - _**Tiers:**_ it allows me to choose the frequency of the project depending on how often I need to access it.
    
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/22%20-%20access%3Astorage%20tiers.png" width="550" />.
    
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/23%20-%20how%20to%20start%20to%20change%20blob%20tiers%20(hot-cold-cool).png" width="550" />  

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/24%20-%20changing%20blob%20tiers%20(hot-cold-cool).png" width="550" />.

  - _**Access Policy:**_ it allows me to manage permissions on the Shared Access Signature (SAS) in my container/blob. I was able to specify permissions, such as expiration time and then connect it to a SAS token.
    
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/Azure-storage/25%20-%20blob%20-%20access%20policy.png" width="550" />.

    
---
# _*☞ GCP*_
---

## Step 1: Upload Files Using the GUI
- Access the Google Cloud Console and create a new Cloud Storage bucket.
- Upload a similar sample file to the bucket using the GCP Console.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/1.png" width="500" />.
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/2.png" width="500" />.
  
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/3.png" width="500" />.
  
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/4.png" width="500" />.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/5.png" width="500" />.
  
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/8.png" width="500" />.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/9%20-%20successful%20creation%20of%20storage%20bucket.png" width="550" />.


## Step 2: Setting Up Authentication and Download Access Keys
1. Create a Service Account
- Go to the IAM & Admin Dashboard.
- Click + Create Service Account.
- Fill in the details and click Create and Continue.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/15%20-%20IAM.png" width="550" />.
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/16%20-%20service%20acct.png" width="550" />.
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/17%20-%20create%20service%20acct.png" width="550" />.

2. Grant Permissions to the Service Account
- Click on the newly created service account.
- Assign the role Storage Admin to give permissions to manage Google Cloud Storage.
- Click on Add Key and create a new key in JSON format.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/19%20-%20role%20(compute%20storage%20admin).png" width="550" />.
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/19%20-%20storage%20obj%20editor%20-%20new%20role.png" width="550" />.

3. Download the Key File
- Download the JSON key file and save it securely on your local machine.
- This key file will be used to authenticate your application to Google Cloud Storage.
- I ensured that I added this file to my `.gitignore` file.

  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/20%20-%20click%20manage%20keys.png" width="550" />.
  
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/21%20-%20click%20create%20new%20key.png" width="550" />.
  
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/22%20-%20create%20priv%20key%20-%20json.png" width="550" />.
  
  <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/23%20-%20private%20key%20(HIDDEN).png" width="550" />.

## Step 3: Upload Files Using Python
- Write a Python script that uploads a file to the GCP Cloud Storage bucket you created. Use the [**gcp_storage.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/gcp_storage.py) library to handle the upload.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/24%20-%20codes%20from%20professor.png" width="550" />.


- Initially I uploaded any files from my local machine. Then, I uploaded some images I downloaded from [**Stanford Dataset**](https://stanfordaimi.azurewebsites.net/datasets/35866158-8196-48d8-87bf-50dca81df965)

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/10%20-%20uploaded%20my%20.py%20file.png" width="550" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/26%20-%20fake%20image%20uploaded.png" width="550" />.
  
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/27%20-%20check.png" width="600" />.
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/28%20-%20check.png" width="600" />.

## Step 4: Write Python Code to Upload Fake Images
- Create a Python script.
    
    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/29%20-%20vsc%20-%20files%3AImages%20uploaded%20successfully.png" width="600" />.

## Step 5: Run the Python Script
- Run the Python script using [**gcp_storage.py**](https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/gcp_storage.py)
- Check Google Cloud Storage bucket to see if the fake image was uploaded successfully.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/30%20-%20successful%20images%20uploaded%20to%20gcp%20storage.png" width="550" />    


## Step 6: Explore Storage Features
  - Explore and document the options for managing and securing data in GCP Cloud Storage (e.g., IAM permissions, lifecycle rules).
  - _**IAM permissions:**_ I was able to assigned role like "Storage Object Creator"--to create custom role with specific permissions depending on my need.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/19%20-%20storage%20obj%20editor%20-%20new%20role.png" width="550" />.

  - _**Lifecycle Rules:**_ It allows me to see previous versions depending on the rules I set.

    <img src="https://github.com/raqssoriano/HHA504_assignment_storage/blob/main/GCP-storage/31%20-%20lifecycle%20rules.png" width="550" />  

