"""Extract text from posts and insert into post_content table."""

import os
import sys

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

# Configuration
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://omiaednmxvekojyflhgi.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_KEY:
    print("Error: SUPABASE_KEY environment variable not set")
    sys.exit(1)

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def main():
    # Fetch all posts
    response = supabase.table("post").select("*").execute()
    posts = response.data

    # Get next available ID
    existing = supabase.table("post_content").select("id").order("id", desc=True).limit(1).execute()
    next_id = existing.data[0]["id"] + 1 if existing.data else 1

    # Extract text and prepare rows
    rows = []
    for post in posts:
        post_data = post.get("data", {})
        if not isinstance(post_data, dict):
            continue

        rows.append(
            {
                "id": next_id,
                "post_id": post["id"],
                "extracted_text": post_data.get("text", ""),
                "intent": "",
                "topics": [],
                "keywords": [],
                "entities": [],
            }
        )
        next_id += 1

    # Insert in batches
    batch_size = 100
    for i in range(0, len(rows), batch_size):
        batch = rows[i : i + batch_size]
        supabase.table("post_content").insert(batch).execute()
        print(f"Inserted {len(batch)} records")

    print(f"Done! Inserted {len(rows)} total records")


if __name__ == "__main__":
    main()
