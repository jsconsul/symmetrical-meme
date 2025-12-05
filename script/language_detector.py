"""Detect languages from `post_content` and update the `language` field."""

import os
import sys

from dotenv import load_dotenv
from langdetect import LangDetectException, detect
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
    print("Supabase client initialized.")

    print("\n--- Retrieving post_content rows ---")
    response = supabase.table("post_content").select("id, extracted_text").execute()
    data = response.data or []

    print(f"Retrieved {len(data)} rows")

    # Detect languages
    detected_languages = []
    for record in data:
        text = record.get("extracted_text", "")
        if text:
            try:
                lang = detect(text)
            except LangDetectException:
                lang = "unknown"
        else:
            lang = "None"
        detected_languages.append(lang)

    print("Detected languages:")
    print(detected_languages)
    print("\n--- Updating records ---")
    update_results = []
    for record, lang in zip(data, detected_languages):
        record_id = record.get("id")
        if record_id is None:
            continue
        update_response = (
            supabase.table("post_content")
            .update({"language": lang})
            .eq("id", record_id)
            .execute()
        )
        update_results.append(
            {
                "id": record_id,
                "language": lang,
                "status": "success",
                "response_data": getattr(update_response, "data", None),
            }
        )
    print("Update process complete.")
    for result in update_results:
        print(result)


if __name__ == "__main__":
    main()