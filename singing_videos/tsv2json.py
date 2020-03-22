import pandas as pd
import json
import sys

key = sys.argv[1]
value = sys.argv[2]
output = sys.argv[3]

data_df = pd.read_table("data.tsv")
result_map = {}

for k in data_df[key].unique():
	result_map[k] = list(data_df[data_df[key] == k][value].unique())

with open(output, "w") as f:
	json.dump(result_map, f, ensure_ascii=False, indent=2)