def compare_runs(old, new):
    diffs = []

    for o, n in zip(old, new):
        diffs.append(n["score"] - o["score"])

    return diffs
