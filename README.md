## **Toxicity Analysis of LLMs**

### **Repository Structure**
```
.
├── evaluations/
├── generated_responses/
├── human_evaluation/
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
    - Contains JSON files with evaluated metrics on prompts.

3. **`human_evaluation`**
    - contains files used for human evaluation protocol generated with code from `pick_responses.py`.
