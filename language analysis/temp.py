import pandas as pd
import numpy as np 
import ast

def read_attribution_scores(file_path):
    def parse_array_or_matrix(value):
        try:
            # print(ast.literal_eval(value))
            return np.array(ast.literal_eval(value), dtype=float) # Safely convert string representation to Python list
        except (ValueError, SyntaxError):
            # print("error")
            return value  # Return as-is if it cannot be parsed

    df = pd.read_csv(
        file_path,
        converters={
            'Input Token Attributions': parse_array_or_matrix,
            'Output Token Attributions': parse_array_or_matrix,
        }
    )

    return df

file_path = "./Bloom/attribution_results_filtered.csv"
df = read_attribution_scores(file_path)
# print number of rows and columns
print(df.shape)

file_path = "./Llama/llama_attribution_results_top_100_with_tokens.csv"
df = read_attribution_scores(file_path)
print(df.shape)
