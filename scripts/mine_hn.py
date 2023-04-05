from __future__ import print_function
import random
from collections import Counter
import ast
import json
from tqdm import tqdm
import os
import jsonlines
import argparse

def convert2train(original, rank_file, out_file):
    with open(original, "r", encoding="utf-8") as f:
        train_gold = json.load(f)
    gold_passage={}
    for item in tqdm(train_gold):
        question=item["question"]
        if len(item["positive_ctxs"])>0:
            gold_p=item["positive_ctxs"][0]
        else:
            continue
        gold_passage[question] = gold_p

    with open(rank_file, "r", encoding="utf-8") as f:
        paq = json.load(f)
    train_data = []
    for item in tqdm(paq):
        hard_negative_ctxs=[]
        positive_ctxs=[]
        if item["question"] in gold_passage:
            positive_ctxs.append(gold_passage[item["question"]])
        for ctx in item["ctxs"]:
            if ctx["has_answer"]==False:
                hard_negative_ctxs.append(ctx)
            else:
                positive_ctxs.append(ctx)

        # random.shuffle(hard_negative_ctxs)
        hard_negative_ctxs=hard_negative_ctxs[:30]
        if positive_ctxs==[]:
            continue
        ctxs = {"question": item["question"],
                "answers": item["answers"],
                "negative_ctxs": [],
                "hard_negative_ctxs": hard_negative_ctxs,
                "positive_ctxs": positive_ctxs,
                }
        train_data.append(ctxs)
    print("data size is :{}".format(len(train_data)))
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(train_data, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Required parameters
    parser.add_argument(
        "--original_train_file", default=None, type=str, required=True, help="Path the official train json file."
    )
    parser.add_argument(
        "--rank_file", default=None, type=str, required=True, help="Path to the mined rank file."
    )
    parser.add_argument(
        "--output_file", default=None, type=str, required=True, help="Path to the output file."
    )
    args = parser.parse_args()
    convert2train(
        args.original_train_file, args.rank_file, args.output_file
    )


