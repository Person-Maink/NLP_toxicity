from collections import Counter

# Load the CoNLL-U file
with open("./UD_English-EWT/en_ewt-ud-train.conllu", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Extract dependency relations
dependencies = [line.split("\t")[7] for line in lines if not line.startswith("#") and line.strip()]

# Count frequencies
dependency_counts = Counter(dependencies)

# Display the most frequent dependencies
for dep, count in dependency_counts.most_common():
    print(f"{dep}: {count}")
