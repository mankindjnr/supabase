import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from supabase import create_client

load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

# sign up
"""
email: str = "amosandmovies@gmail.com"
password: str = "123456789amos"
user = supabase.auth.sign_up({ "email": email, "password": password })
"""

# sign in
email: str = "amosandmovies@gmail.com"
password: str = "123456789amos"

data = supabase.table("todos").select("*").execute()
print("data before sing in", data)
# keeps the user signed since it will be open
try:
    session = supabase.auth.sign_in_with_password({ "email": email, "password": password })
except Exception as e:
    print("login failed")

#print(session.session.access_token)
supabase.postgrest.auth(session.session.access_token)
data = supabase.table("todos").select("*").execute()
print("data after sign in", data)
# this kills the sessionclear
# supabase.auth.sign_out()