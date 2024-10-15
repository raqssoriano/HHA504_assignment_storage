from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
import io

# Step 1: Set up your Azure Storage connection string
# Replace the below with your connection string
connection_string = "BlobEndpoint=https://raqsblobstorage.blob.core.windows.net/;QueueEndpoint=https://raqsblobstorage.queue.core.windows.net/;FileEndpoint=https://raqsblobstorage.file.core.windows.net/;TableEndpoint=https://raqsblobstorage.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bf&srt=sco&sp=rwctfx&se=2024-10-18T03:00:00Z&st=2024-10-15T08:03:09Z&spr=https&sig=s%2BnFYyT1MPPauqXmPCww5YK4rgNGxw20h3OA2%2B2Wxtc%3D"

# Step 2: Create a BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Step 3: Create a container or use an existing one
container_name = "raqs-container" 
try:
    container_client = blob_service_client.create_container(container_name)
except Exception as e:
    print(f"Container already exists or an error occurred: {e}")

# Step 4: Create a fake image using Pillow
image = Image.new('RGB', (100, 100), color = (150, 100, 200))
image_byte_array = io.BytesIO()
image.save(image_byte_array, format='PNG')
image_bytes = image_byte_array.getvalue()

# Step 5: Upload the fake image to Azure Blob Storage
blob_client = blob_service_client.get_blob_client(container=container_name, blob="000595.png")
blob_client.upload_blob(image_bytes, blob_type="BlockBlob", overwrite=True)

print("Image uploaded successfully to Azure Blob Storage!")