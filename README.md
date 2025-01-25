## **Toxicity Analysis of LLMs**

This repository is dedicated to a project analyzing the influence of prompts on the toxicity of language model outputs. The project involves generating responses from various language models, evaluating their toxicity using automated and human evaluation methods, and performing detailed linguistic analysis to understand the factors contributing to toxicity. The report for a limited study (100 prompts) can be found <a href="https://drive.google.com/file/d/1gP5bjmvO5nJp64NsY6HnB6wHO0dwF_KJ/view?usp=sharing" target="_blank">here</a>.

### **Repository Structure**
```
.
├── evaluations/
├── generated_responses/
├── human_evaluation/
├── language_analysis/
├── README.md
```

### **Files and Directories**

1. **`generated_responses/`**  
    - Contains JSON files with generated prompts and their continuations.
    - **Example File**: `gpt2_k50_p1_t1.0_n25_l150.json`  
        - **`k50`**: Top-50 sampling.  
        - **`p1`**: Top-p (nucleus) sampling with `p=1`.  
        - **`t1.0`**: Temperature set to `1.0`.  
        - **`n25`**: 25 continuations per prompt.
        - **`l150`**: 150 tokens length.

    ### **Example JSON Format**

    Each file in `generated_responses` follows this structure:

    ```json
    {
     "model_info": {
       "model_name": "gpt2",
       "batch_size": 128,
       "top_k": 50,
       "top_p": 1,
       "temperature": 1.0,
       "num_continuations": 25,
       "max_new_tokens": 20,
       "device": "cuda"
     },
     "generated_responses": [
       {
         "prompt": "Sample prompt text",
         "continuations": [
            "cont1",
            "cont2"
         ]
       }
     ]
    }

2. **`evaluations/`**
    - Contains JSON files with evaluated metrics on continuations.
    - Note: this is evaluation from [Perspective API](https://perspectiveapi.com/) **on the continuations only**, i.e. without the prompt.

3. **`human_evaluation/`**
    - contains files used for human evaluation protocol generated with code from `pick_responses.py`.
    - evaluators should not look into this file before evaluating to avoid biasness.

3. **`languale_analysis/`**
    - Contains files used for linguistic analysis, including lexical and syntactic analysis notebooks.
        - Also includes generated attribution scores for each model, which help in understanding the contribution of different parts of the input to the model's output.
        - **Subdirectories**:
            - **`Bloom/`**: Contains attribution results and notebooks for the Bloom model.
            - **`GPT2_data/`**: Contains attribution results for the GPT-2 model.
            - **`Llama/`**: Contains attribution results and notebooks for the Llama model.
            - **`Mistral/`**: Contains attribution results and notebooks for the Mistral model.
            - **`UD_English-EWT/`**: Contains Universal Dependencies English treebank data used for linguistic analysis.
        - **Notebooks**:
            - **`lexical_analysis.ipynb`**: Notebook for performing lexical analysis on the generated responses.
            - **`syntatic_analysis.ipynb`**: Notebook for performing syntactic analysis on the generated responses.
            - **`analyse_tree_bank.py`**: Script for analyzing treebank data.
---
### Some additional notebooks and scripts
**`pick_responses.py`**
    - Script for selecting responses for human evaluation.

**`shuffle_chosen_responses.py`**
    - Script for shuffling selected responses to avoid bias in human evaluation.
