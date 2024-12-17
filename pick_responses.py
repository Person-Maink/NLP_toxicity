import json
import os
import random

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def pick_toxicity_responses(data, num_responses=10, mode="top"):
    """
    Picks the top or lowest toxicity responses based on the mode parameter.
    
    Parameters:
        - data: The loaded JSON data.
        - num_responses: Number of responses to return.
        - mode: "top" for highest toxicity, "lowest" for lowest toxicity.
    """
    continuations = []
    for prompt_data in data['generated_responses']:
        prompt_text = prompt_data['prompt']['text']
        max_cont = max(prompt_data['continuations'], key=lambda x: x['toxicity_score'])
        continuations.append({
            "prompt": prompt_text,
            "continuation": f"{prompt_text} ||||| {max_cont['text']}",
            "toxicity_score": max_cont['toxicity_score']
        })
    
    # Sort continuations by toxicity score
    continuations_sorted = sorted(
        continuations,
        key=lambda x: x['toxicity_score'],
        reverse=(mode == "top")
    )
    
    # Pick the top `num_responses` with the specified mode
    return continuations_sorted[:num_responses]

def generate_random_responses_in_range(data, lower_bound, upper_bound, num_responses=5):
    """
    Randomly generates `num_responses` continuations within a specified toxicity score range.
    
    Parameters:
        - data: The loaded JSON data.
        - lower_bound: Lower bound of toxicity score.
        - upper_bound: Upper bound of toxicity score.
        - num_responses: Number of random responses to return.
    """
    continuations = []
    for prompt_data in data['generated_responses']:
        prompt_text = prompt_data['prompt']['text']
        for cont in prompt_data['continuations']:
            toxicity_score = cont['toxicity_score']
            if lower_bound <= toxicity_score <= upper_bound:
                continuation_text = cont['text']

                combined_text = f"{prompt_text} ||||| {continuation_text}"

                continuations.append({
                    "prompt": prompt_text,
                    "continuation": combined_text,
                    "toxicity_score": toxicity_score
                })
    
    # Randomly sample `num_responses` from the filtered continuations
    return random.sample(continuations, min(num_responses, len(continuations)))

def save_results(data, results, output_folder="human_evaluation"):
    """
    Saves the results to a JSON file in the specified output folder.
    
    Parameters:
        - data: The loaded JSON data (for model_info).
        - results: The results to save.
        - output_folder: The folder to save the results in.
    """
    os.makedirs(output_folder, exist_ok=True)
    output_file_path = os.path.join(output_folder, f"{data['model_info']['model_name']}.json")

    with open(output_file_path, 'w') as outfile:
        json.dump(results, outfile, indent=4)

    print(f"Results saved to {output_file_path}")

file_path_llama = "evaluations/llama_eval_k50_p1_t1.0_n25_l50.json"
file_path_mistral = "evaluations/mistral_eval_k50_p1_t1.0_n25_l150.json"
file_path_gpt2 = "evaluations/gpt2_eval_k50_p1_t1.0_n25_l150.json"
file_path_bloom = "evaluations/bloom7b_eval_k50_p1_t1.0_n25_l50.json"

data = load_data(file_path_llama)

top_responses = pick_toxicity_responses(data, num_responses=7, mode="top")
lowest_responses = pick_toxicity_responses(data, num_responses=3, mode="lowest")

random_responses = generate_random_responses_in_range(data, lower_bound=0.3, upper_bound=0.7)

results = {
    "model_info": data['model_info'],
    "top_responses": top_responses,
    "lowest_responses": lowest_responses,
    # "random_responses_in_range": random_responses
}

save_results(data, results)
