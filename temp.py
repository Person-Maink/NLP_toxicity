import random 
import json 

file_path = "generated_responses/gpt2_k50_p1_t1.0_n25_l150.json"

def pick_random_responses(file_path, num_prompts=10):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Select 10 random prompts with their continuations
    selected_prompts = random.sample(data['generated_responses'], num_prompts)
    
    # For each selected prompt, pick one random continuation
    results = []
    for prompt_data in selected_prompts:
        prompt = prompt_data['prompt']
        continuation = random.choice(prompt_data['continuations'])
        results.append({
            "prompt": prompt,
            "selected_continuation": continuation['text']
        })

    # Display the selected results
    for i, result in enumerate(results):
        print(f"{result['selected_continuation']}")
        print("-----------------")

# Run the function
pick_random_responses(file_path)
