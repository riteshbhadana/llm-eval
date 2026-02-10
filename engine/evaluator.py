from engine.inference import run_model
from engine.judge import judge_answer

def evaluate_item(item, prompt_template):
    prompt = prompt_template.format(
        question=item["question"],
        context=item["context"]
    )

    answer = run_model(prompt)
    score = judge_answer(answer, item["reference"])

    return {
        "id": item["id"],
        "answer": answer,
        "score": score
    }
