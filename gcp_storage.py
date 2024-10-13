from google.cloud import storage
from PIL import Image
import io
import os

# Step 1: Setting up my Google credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp-hush.json'

# Step 2: Create a Google Cloud Storage Client
client = storage.Client()

# Step 3: Used my existing bucket in Google Cloud Storage
bucket_name = 'raqs-ahi-gcp-storage'
bucket = client.bucket(bucket_name)

## Create a list of files in images with path
files_upload = []
for root, dirs, files in os.walk("dermatologyimages"):
    for file in files:
        files_upload.append(os.path.join(root, file))

for file in files_upload:
    ## print working on file
    print(f"Working on file: {file}")

    ## load the files using io into memory
    with open(file, 'rb') as f:
        file_byte_array = f.read()
    print(file)

    ## just the file name
    file = file.split("/")[-1]
    print('new file name:', file)


    ## Upload files to Google Cloud Storage
    try:
        blob = bucket.blob(file)
        blob.upload_from_string(file_byte_array)
        print(f"Image uploaded successfully to my Google Cloud Storage!")
    except Exception as e:
        print(f"Error uploading images to Google Cloud Storage: {e}")


# Step 4: Create a fake image using Pillow
image = Image.new('RGB', (100, 100), color = (73, 109, 137))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')

# Step 5: Upload the fake image to Google Cloud Storage
blob = bucket.blob('fake_image.png')
blob.upload_from_string(image_byte_array.getvalue(), content_type='image/png')

print("Image uploaded successfully to Google Cloud Storage!")

