import pandas as pd

# Load file
df = pd.read_csv('../data/mistral_prompt_tuning/mistral_initial_long_responses_800charonly.csv')#, delimiter=';', quotechar='"')

# # Create a new column to count characters in each row of 'counter_speech'
df['char_count'] = df['counter_speech_mistral'].apply(len)

# Calculate average length
average_length = df['char_count'].mean()

print("Durchschnittliche Zeichenanzahl:", average_length)
