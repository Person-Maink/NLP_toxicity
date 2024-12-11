import random
import json

file_path = "evaluations/gpt2_eval_k50_p1_t1.0_n25_l150.json"

def pick_high_toxicity_responses(file_path, num_prompts=10, toxicity_threshold=0.75):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Filter prompts that have at least one continuation with toxicity > threshold
    eligible_prompts = [
        prompt_data for prompt_data in data['generated_responses']
        if any(cont['toxicity_score'] > toxicity_threshold for cont in prompt_data['continuations'])
    ]

    # Randomly select up to 'num_prompts' eligible prompts
    selected_prompts = random.sample(eligible_prompts, min(num_prompts, len(eligible_prompts)))
    
    # For each selected prompt, pick a random continuation with toxicity > threshold
    results = []
    for prompt_data in selected_prompts:
        prompt = prompt_data['prompt']
        toxic_continuations = [
            cont['text'] for cont in prompt_data['continuations']
            if cont['toxicity_score'] > toxicity_threshold
        ]
        if toxic_continuations:
            continuation = random.choice(toxic_continuations)
            results.append({
                "prompt": prompt,
                "selected_continuation": continuation
            })

    # Display the selected results
    for i, result in enumerate(results):
        # print(f"Prompt {i + 1}: {result['prompt']}")
        print(f"{result['selected_continuation']}")
        print("-----------------")

# Run the function
pick_high_toxicity_responses(file_path)
