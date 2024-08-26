import os
from dotenv import load_dotenv
import pandas as pd
from openai import OpenAI

# Load .env file containing the API key
load_dotenv()

# Retrieve the API key and initialize OpenAI client
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Load the dataset containing conspiracy theory comments
df = pd.read_csv('../data/qanon_deepstate_comments.csv', delimiter=';', quotechar='"')


# Function to generate counter speech
def generate_counter_speech(comment):
    response = client.chat.completions.create(
        messages=[
            {"role": "system",
             "content": """You are a trained expert in generating counter speech to conspiracy theory comments.
             Follow these response guidelines: 
                1. Show empathy and positivity in your response.
                2. Do not state 'this is a conspiracy theory' directly.
                3. Use narrative storytelling, including a first-person perspective, detailed accounts of characters' internal lives, metaphors and figurative language.  Include a relatable protagonist (well-known figures only) or credible real-life examples to illustrate your point. 
                4. Ensure clarity in your argumentation with defined objectives.
                5. Challenge the statement and refute it with specific facts from reliable sources. If appropriate, ask for sources or factual basis.
                6. Maintain a respectful and calm tone throughout your response. Be cautious with sarcasm, humor, parody, and satire.
                7. Always respond concisely, directly, and clearly. Limit your response to 800 characters.
                """
             },
            {"role": "user", "content": f"Generate counter speech to the following conspiracy theory comment: {comment}."}

        ],
        model="gpt-4o",
        max_tokens=300
    )
    return response.choices[0].message.content.strip()


# Generate counter speech for each comment and save it in a new 'counter_speech' column
df['counter_speech_gpt4-o'] = df['comment_text'].apply(generate_counter_speech)

# Save results to a new file
df.to_csv('../data/counterspeech_dataset_gpt-4otest.csv', index=False)
