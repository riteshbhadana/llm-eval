import json
from engine.regression import compare_runs

with open("runs/results_old.json") as f:
    old = json.load(f)

with open("runs/results.json") as f:
    new = json.load(f)

diffs = compare_runs(old, new)

print("Score changes:", diffs)
