import json
import yaml
import os
import numpy as np
from engine.evaluator import evaluate_item

# Optional MLflow
USE_MLFLOW = True

if USE_MLFLOW:
    import mlflow
    mlflow.set_experiment("llm-evaluation")

def load_dataset():
    with open("dataset/golden.json") as f:
        return json.load(f)

def load_prompt():
    with open("prompts/v1.yaml") as f:
        return yaml.safe_load(f)["template"]

dataset = load_dataset()
prompt_template = load_prompt()

os.makedirs("runs", exist_ok=True)

def run_pipeline():

    results = []

    for item in dataset:
        r = evaluate_item(item, prompt_template)
        results.append(r)

    scores = [r["score"] for r in results]
    avg_score = np.mean(scores)

    print("Average score:", avg_score)

    with open("runs/results.json", "w") as f:
        json.dump(results, f, indent=2)

    return avg_score

if USE_MLFLOW:
    with mlflow.start_run():
        avg_score = run_pipeline()
        mlflow.log_metric("average_score", avg_score)
        mlflow.log_artifact("runs/results.json")
        print("MLflow run logged ✅")
else:
    run_pipeline()
    print("Evaluation complete ✅")
