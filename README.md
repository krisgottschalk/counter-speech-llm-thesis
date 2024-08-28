# Counter Speech LLM Thesis
Repository for the bachelor thesis "Automatic generation of counter speech to conspiracy theory comments with the help of LLMs"

This project explores the automatic generation of counter speech using large language models (LLMs) to address comments rooted in conspiracy theories. It evaluates the capabilities of advanced LLMs such as GPT-4o, Meta Llama 3, and Mistral in generating effective counter narratives.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Data](#data)
5. [Model Information](#model-information)
6. [Evaluation](#evaluation)
7. [Contributing](#contributing)

## Introduction

This project aims to address the challenge of countering conspiracy theory narratives in online discussions by leveraging the sophisticated capabilities of modern language models. By experimenting with different LLMs, the project seeks to identify effective strategies for crafting responses by using prompting techniques. 
The goal is to create counter speech which is not only empathetic, but also adheres to facts and uses narrative elements to counteract harmful conspiracy theories.

## Setup

Follow these instructions to set up the project on your local machine.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/krisgottschalk/counter-speech-llm-thesis.git
    cd counter-speech-llm-thesis
    ```

2. **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Authenticate with Hugging Face:**

    To access the necessary models and datasets, log in to your Hugging Face account:

    ```bash
    huggingface-cli login
    ```

    Enter your Hugging Face API token when prompted. You can create a token [here](https://huggingface.co/settings/tokens).


## Usage

This section outlines how to utilize the scripts and Jupyter notebooks included in this project to generate counter speech using different language models.

### Running Scripts:

1. **GPT-4o Script:**
   - This script utilizes the OpenAI API to interact with the GPT-4o model. Before running the script, ensure you have obtained an API key from OpenAI.
   - To run the script, use the following command:
     ```bash
     python scripts/GPT-4o.py --api_key your_openai_api_key
     ```
   - Replace `your_openai_api_key` with your actual OpenAI API key. This script sends prompts to the GPT-4o model and receives generated text in response.

### Running Jupyter Notebooks:

1. **Meta Llama 3 and Mistral Notebooks:**
   - These notebooks use the Hugging Face Transformers Library to interact with the Meta Llama 3 and Mistral models.
   - Ensure you have a suitable GPU environment set up as these models require significant computational resources.
   - To start the Jupyter Notebook server, run:
     ```bash
     jupyter notebook
     ```
   - Navigate to the `models/` directory and open either `Meta-Llama-3-8B.Instruct.ipynb` or `Mistral-7B-Instruct-v0.3.ipynb` to view and run the steps for generating counter speech.
   - These notebooks contain detailed code that guides you through the process of loading the models, setting up prompts, and generating responses.

    
## Data

- **Data Source:** The conspiracy theory comments were collected from the platform X. The comments are all related to QAnon and Deep State.
- **Data Files:**
    - `data/qanon_deepstate_comments.csv`: Main dataset which contains 100 conspiracy theory comments.
    - `data/counterspeech_all_models_dataset.csv`: Contains the comments from X alongside the counter speech that was created by the models GPT-4o, Llama 3 and Mistral.
    - `data/test_dataset_20_comments.csv`: Test dataset which contains 20 additional conspiracy theory comments.
    - `data/evaluation/counterspeech_90_samples_evaluated.csv`: This dataset contains 90 conspiracy theory comments and counter speech pairs that were evaluated using five evaluation criteria like empathy factor and fidelity to facts.

## Model Information

This project utilizes the following LLMs:

- **Meta-Llama-3-8B:** A robust LLM known for its deep contextual comprehension.
- **Mistral-7B:** Tailored for nuanced language generation tasks.
- **GPT-4o**: The latest iteration with advanced reasoning capabilities.

## Evaluation
The evaluation process involves:

- **Qualitative Assessment:** Using a Likert scale from 1 to 5 based on criteria like empathy, factual accuracy, tone, clarity, and storytelling.
- **Quantitative Analysis:** Statistical methods to validate the effectiveness of responses.

## Contributing

Contributions to this project are welcome! You can suggest enhancements, report issues, or submit pull requests.


