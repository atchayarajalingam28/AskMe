"""
Runs every cases in eval_cases.py agains the assistant and prints whether passed or failed.

Usage: python run_eval.py

Exit code is 0 if every case passes and 1 otherwise, so the same script can later run automaticallu in CI ( like Github Actions ).
"""

import sys
import logging 
from dotenv import load_dotenv

from eval_cases import CASES
from loader import load_documents
from chunking import split_documents
from embeddings import build_vector_store , vector_store_rerun
from llm import answer_question

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("huggingface_hub").setLevel(logging.WARNING)

load_dotenv()

def normalise(text):
    """Lowercase and smooth over typographic differences before checking."""
    return (
        text.lower()
        .replace("\u2019", "'")
        .replace("\u2011", '-')
        .replace("\u202f", " ")
        .replace("\u00a0", " ")
        .replace(" %","%")
    )

def check(answer,case):
    """Returns a list of problems; an empty list means the case passed."""

    text = normalise(answer)
    problems=[]
    for phrase in case["must_include"]:
        if normalise(phrase) not in text:
            problems.append(f"missing: {phrase!r}")
    for phrase in case["must_exclude"]:
        if normalise(phrase) in text:
            problems.append(f"should not contains: {phrase!r}")
    return problems

def main():
    #Rebuild the vector store from scratch so duplicates from earlier runs cannot affect the results.
    vector_store_rerun()
    chunks = split_documents(load_documents())
    vector_store = build_vector_store(chunks)

    passed =0
    failures = []

    print("\n" + "=" *60)
    for i, case in enumerate(CASES, start = 1):
        answer = answer_question(vector_store, case["question"])
        problems = check(answer, case)
        status = "PASS" if not problems else "FAIL"
        print(f"{status} [{i:02d}] {case['question']}")
        if problems:
            failures.append((case, answer, problems))
        else:
            passed+=1

    print("=" *60)
    print(f"{passed}/{len(CASES)} cases.")

    if failures:
        print("\nFailures (read each answer yourself; the checks are keyword-based):")
        for case, answer, problems in failures:
            print(f"\nQuestion: {case['question']}")
            print(f"Testing : {case['note']}")
            print(f"Problems : {'; '.join(problems)}")
            print(f"Answer : {answer}")
        sys.exit(0 if not failures else 1)


if __name__ == "__main__":
    main()