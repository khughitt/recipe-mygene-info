#!/bin/python
"""
mygene.info gene metadata (human)
"""
import os
import time
import numpy as np
import pandas as pd
from biothings_client import get_client, MyGeneInfo

if not os.path.exists("output"):
    os.makedirs("output", mode=0o755)

batch_size = 100
sleep_time = 3

entries = []

def main():
    mg = get_client("gene")

    # load list of human entrez ids
    with open("data/entrez-ids.txt") as fp:
        entrez_ids = [x.strip() for x in fp.readlines()]

    batches = list(chunks(entrez_ids, batch_size))

    # iterate over batches and retrieve gene info
    for batch in batches:
        res = mg.querymany(batch, scopes="entrezgene", species=9606, 
                           fields="symbol,summary", as_dataframe=True)

        # summary field may not be present if none of the queried genes has a corresponding summary
        summary = res["summary"] if "summary" in res else [""] * res.shape[0]

        df = pd.DataFrame({"entrez_id": res["_id"], "symbol": res["symbol"], "summary": summary})

        entries.append(df)

        time.sleep(sleep_time)

    # save result
    mdat = pd.concat(entries).reset_index(drop=True)
    mdat.summary = mdat.summary.fillna("")

    mdat.to_feather("output/mygeneinfo-human.feather")

# chunk list
# https://stackoverflow.com/a/312464/554531
def chunks(lst, n):
  for i in range(0, len(lst), n):
      yield lst[i:i + n]

if __name__ == "__main__":
    main()
