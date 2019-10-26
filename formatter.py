import json

with open("data.json") as f:
	json_map = json.load(f)

with open("data.json", "w") as f:
	json.dump(json_map, f, ensure_ascii=False, indent=2)