## **Toxicity Analysis of LLMs**

### **Repository Structure**
```
.
├── evaluations/
├── generated_prompts/
├── README.md
```

### **Files and Directories**

1. **`generated_prompts/`**  
    - Contains JSON files with generated prompts and their continuations.
    - **Example File**: `gpt2_k50_p1_t1.0_n25.json`  
        - **`k50`**: Top-50 sampling.  
        - **`p1`**: Top-p (nucleus) sampling with `p=1`.  
        - **`t1.0`**: Temperature set to `1.0`.  
        - **`n25`**: 25 continuations per prompt.

    ### **Example JSON Format**

    Each file in `generated_prompts` follows this structure:

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
           {"seed": 12345, "text": "Generated response 1"},
           {"seed": 67890, "text": "Generated response 2"}
         ]
       }
     ]
    }

2. **`evaluations/`**
    - Contains JSON files with evaluated metrics on prompts.
