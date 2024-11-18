from openai import OpenAI
import json
import re
from typing import List
from termcolor import colored

def get_search_terms(video_subject,amount,script):
    prompt = f"""
    Generate {amount} search terms for stock videos,
    depending on the subject of a video. Reply in English Only.
    Subject: {video_subject}

    The search terms are to be returned as
    a JSON-Array of strings.

    Each search term should consist of 1-3 words, 
    always add the main subject of the video.

    Here is an example of a JSON-Array of strings:
    ["search term 1", "search term 2", "search term 3"]

    Obviously, the search terms should be related
    to the subject of the video.

    ONLY RETURN THE JSON-ARRAY OF STRINGS.
    DO NOT RETURN ANYTHING ELSE.

    For context, here is the full text:
    {script}
    """
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=""
    )
    response = client.chat.completions.create(
        model="llama-3.2-1b-preview",
        messages=[{"role": "user","content": prompt}]
    )
    
    search_terms = response.choices[0].message.content
    return search_terms

# Example usage:
# video_subject = "RRR movie"
# amount = 7
# script = "Experience the epic tale of RRR, directed by the visionary SS Rajamouli. Set in the turbulent times of early 20th century India, RRR follows the journey of two revolutionary heroes from different worlds, united by a common cause. Witness the breathtaking action, heart-pounding drama, and emotional depth as these heroes fight for their country's freedom. Don't miss out on this cinematic masterpiece that has taken the world by storm."

# search_terms = get_search_terms(video_subject, amount,script)

# print(search_terms)
