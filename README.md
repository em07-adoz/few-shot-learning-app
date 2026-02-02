# Few-Shot Learning App (Gemini + Streamlit)

This project is a simple interactive web app that demonstrates **few-shot learning** using Google’s **Gemini** large language model. The app is built with **Streamlit** and allows users to experiment with task instructions, examples, and generation parameters to observe how the model generalizes from a small number of examples.

## Overview

Few-shot learning is a prompting technique where a language model is given a small number of **Input → Output examples** in the prompt to guide its behavior on a new input, without retraining the model.

In this app, users can:
- Define a task instruction
- Provide a few labeled examples
- Test a new input
- Observe how the model follows the learned pattern

## Features

- Secure Gemini API key input
- Explicit few-shot setup (task, examples, new input)
- Adjustable generation parameters:
  - Temperature
  - Top-p
  - Top-k
  - Max output tokens
- Model selection (from available Gemini models)
- Prompt and response history
- Runs locally using Streamlit

## Tech Stack

- **Python**
- **Streamlit** – interactive web interface
- **Google Gemini API** – language model inference


## API Key Setup

This app requires a Gemini API key from Google AI Studio.

1. Visit: https://aistudio.google.com/app/apikey  
2. Create a new API key  
3. Paste the key into the app when prompted  


## Run Locally
### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies
```bash
pip install streamlit google-generativeai
```

### 3. Run the app
```bash
streamlit run app.py
```

Open the local URL displayed in your browser (usually http://localhost:8501).

## How Few-Shot Learning Is Implemented

The app automatically constructs a single prompt containing:
- A task instruction
- A small set of Input → Output examples
- A new input

This prompt is sent to the Gemini model using the generate_content() method. The model generates a response by following the pattern demonstrated in the examples.

 ## Project Structure
 
 .
├── app.py        # Main Streamlit application
├── README.md     # Project documentation
└── .gitignore    # Excludes secrets and cache files

## License

This project is licensed under the MIT License.
