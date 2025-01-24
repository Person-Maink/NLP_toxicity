import os
import json
import random

def load_json_files_from_folder(folder_path):
    continuations = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)

                    model_info = data.get('model_info', 'Unknown model')

                    if 'top_responses' in data:
                        for resp in data['top_responses']:
                            continuations.append({
                                'model': model_info['model_name'],
                                'continuation': resp['continuation'],
                                'attribution_score': resp.get('toxicity_score', 'N/A')
                            })

                    if 'lowest_responses' in data:
                        for resp in data['lowest_responses']:
                            continuations.append({
                                'model': model_info['model_name'],
                                'continuation': resp['continuation'],
                                'attribution_score': resp.get('toxicity_score', 'N/A')
                            })

                except json.JSONDecodeError as e:
                    print(f"Error reading {filename}: {e}")

    return continuations

folder_path = "./human_evaluation/"
continuations = load_json_files_from_folder(folder_path)

# Shuffle the continuations
# random.shuffle(continuations)

for cont in continuations:
    print(f"Model: {cont['model']}")
    print(f"Continuation: {cont['continuation']}")
    print(f"Attribution Score: {cont['attribution_score']}")
    print("-" * 80)
