from collections import Counter
import spacy
import warnings

# Suppress specific warnings from SpaCy
warnings.filterwarnings("ignore", message=r"\[W118\]")

# Load the CoNLL-U file
with open("./UD_English-EWT/en_ewt-ud-train.conllu", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Extract dependency relations
dependencies = [line.split("\t")[7] for line in lines if not line.startswith("#") and line.strip()]

# Count frequencies
dependency_counts = Counter(dependencies)

# Load SpaCy's English model for explanations
nlp = spacy.blank("en")

# Function to get explanations for dependencies
def explain_dependency(dep):
    return spacy.explain(dep) or "No explanation"

sum = 0
# Display the most frequent dependencies with explanations
for dep, count in dependency_counts.most_common():
    explanation = explain_dependency(dep)
    print(f"{dep}: {count} -> {explanation}")
    sum += count

print(f"Total number of dependencies: {sum}")




