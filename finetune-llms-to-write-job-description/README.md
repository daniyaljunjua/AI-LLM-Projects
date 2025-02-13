# Job Description Generator with Google Gemma 7B

This project fine-tunes the **Google Gemma 7B** model to generate job descriptions based on job titles. The model is optimized using **Low-Rank Adaptation (LoRA)** and quantized with **BitsAndBytes** for efficient training and inference.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Dataset](#dataset)
- [Fine-Tuning Process](#fine-tuning-process)
- [Inference](#inference)
- [Results](#results)
- [License](#license)

## Overview
This project leverages Hugging Face's **transformers** and **TRL** libraries to fine-tune the **Google Gemma 7B** model for generating job descriptions. The process involves:

1. **Data Preparation** – Formatting job titles and summaries into a structured dataset.
2. **Model Fine-Tuning** – Applying LoRA for efficient adaptation with reduced computational cost.
3. **Inference** – Using the fine-tuned model to generate job descriptions from input job titles.

## Features
✅ Fine-tuning with LoRA for lower memory consumption.  
✅ 4-bit quantization with BitsAndBytes for efficient model loading.  
✅ Generates structured job descriptions based on job titles.  
✅ Compatible with **Hugging Face Transformers & TRL libraries**.

## Installation
### Prerequisites
Ensure you have Python installed (>= 3.8) and set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Required Libraries
```bash
pip install -r requirements.txt
```

## Dataset
The dataset consists of job titles and their corresponding descriptions stored in:
```
data/cleaned_50k-merged_job_data.csv
```
The dataset is loaded using pandas and converted into a structured dataset for fine-tuning.

## Fine-Tuning Process
1. **Load Data:** Reads the CSV file and formats data into structured prompt-response pairs.
2. **Load Pretrained Model:** Fetches the Google Gemma 7B model from Hugging Face.
3. **Quantization:** Uses **BitsAndBytesConfig** for 4-bit precision to optimize memory usage.
4. **LoRA Configuration:** Applies LoRA with specific hyperparameters.
5. **Training:** Fine-tunes the model using `SFTTrainer`.

## Inference
Once the model is fine-tuned, it can generate job descriptions using:

```python
from transformers import AutoTokenizer
import torch

def generate_text(model, tokenizer, prompt, max_length=128):
    inputs = tokenizer(prompt, return_tensors="pt", max_length=max_length, padding=True, truncation=True).to("cuda")
    with torch.no_grad():
        output = model.generate(inputs.input_ids, attention_mask=inputs.attention_mask, max_length=max_length, do_sample=True, temperature=0.7)
    return tokenizer.decode(output[0], skip_special_tokens=True)

prompt = "Job title: Senior Web Developer Generate job posting description:"
print(generate_text(model, tokenizer, prompt))
```

## Results
Example Output:
```
Job title: Senior Web Developer Generate job posting description: Senior Web Developer

Salary: $100,000 - $150,000

Job Description:
We are looking for an experienced and skilled Senior Web Developer. We are a small and fast-growing startup with a friendly and dynamic work environment.
```

## License
This project is licensed under the **MIT License**.


