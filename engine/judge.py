import re
from difflib import SequenceMatcher
from engine.inference import run_model

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def judge_answer(answer, reference):

    # heuristic similarity score
    sim = similarity(answer, reference)

    # convert to 1–10 scale
    heuristic_score = sim * 10

    # ask LLM judge
    prompt = f"""
Reference: {reference}
Answer: {answer}

Score correctness from 1–10.
Only return number.
"""

    result = run_model(prompt)

    match = re.search(r"\d+", result)

    if match:
        llm_score = float(match.group())
    else:
        llm_score = 6

    # combine both signals
    final_score = (heuristic_score + llm_score) / 2

    return round(final_score, 1)
