import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# reading the database

"""
# everything in the table
data = supabase.table("todos").select("*").execute()

# certain columns only
data2 = supabase.table("todos").select("id, name").execute()

# applying filters to the data - where the name is item 1
data3 = supabase.table("todos").select("id, name").eq("name", "item 1").execute()
"""


# insert to the database
"""
created_at = datetime.utcnow() - timedelta(hours=2) # the time will be two hours earlier than utcnow
data = supabase.table("todos").insert({"name":"item 3", "created_at":str(created_at)}).execute()

data = supabase.table("todos").select("*").execute()
print(data)
"""

# updating data
"""
# update the name to new_name where the id is 1
data = supabase.table("todos").update({"name": "new_name"}).eq("id", 1).execute()
data = supabase.table("todos").select("*").execute()
print(data)
"""

# deleting data
"""data = supabase.table("todos").delete().eq("id", 1).execute()
data = supabase.table("todos").select("*").execute()
print(data)"""
