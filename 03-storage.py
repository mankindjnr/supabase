import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
client = create_client(url, key)

# retrieving an image
"""
resp = client.storage.from_("image_bucket").get_public_url("DSC_6303.jpg")
print(resp)
"""

# uploading an image
resp = client.storage.from_("image_bucket").upload("zero.jpg", "zero.jpg",
{
    "content-type": "image/jpg"
    })
print(resp)