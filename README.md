# counter-speech-llm-thesis
Repository for bachelor thesis "Automatic generation of counter speech to conspiracy theory comments with the help of LLMs"

A brief description of what this project does and its purpose. Include any relevant context or background information.

## Table of Contents

1. [Introduction](#introduction)
2. [Setup](#setup)
3. [Usage](#usage)
4. [Data](#data)
5. [Model Information](#model-information)
6. [Evaluation](#evaluation)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

Provide a more detailed introduction to the project. Explain the goals, the problem it addresses, and the significance of the work. Mention the key components or methodologies used in the project.

## Setup

Follow these instructions to set up the project on your local machine.

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
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

Instructions on how to run the scripts or notebooks.

1. **Running Scripts:**

    Describe how to execute scripts for generating counter speech or other tasks. For example:

    ```bash
    python scripts/GPT-4o.py
    ```

2. **Running Jupyter Notebooks:**

    If using Jupyter Notebooks, start Jupyter:

    ```bash
    jupyter notebook
    ```

    Then open the relevant notebook, such as `models/GPT-4o.ipynb`, and follow the instructions provided.

## Data

- **Data Source:** Explain where the data comes from, how it's organized, and what preprocessing steps are necessary (if any).
- **Data Files:**
    - `data/qanon_deepstate_comments.csv`: Description of this file.
    - `data/counterspeech_all_models_dataset.csv`: Description of this file.
    - `data/evaluation/counterspeech_sample_to_evaluate.csv`: Description of this file.

## Model Information

Details about the models used in the project:

- **Meta-LLaMA-3-8B:** Brief description of the model, purpose, and link to more information.
- **Mistral-7B:** Brief description of the model, purpose, and link to more information.
- **GPT-4o:** Brief description of the model, purpose, and link to more information.

## Evaluation

Describe the evaluation process, including how the models are assessed and what metrics or criteria are used.

- **Evaluation Files:**
    - `data/evaluation/counterspeech_90responses_5categories.csv`: Details of this evaluation dataset.
    - `data/evaluation/intra_rater_reliability_20samples_first_eval.csv`: Details of this dataset.
    - `data/evaluation/intra_rater_reliability_20samples_second_eval.csv`: Details of this dataset.

## Contributing

Guidelines for contributing to this project. Mention how others can report issues, suggest features, or submit pull requests.

## License

State the project's license. For example:

