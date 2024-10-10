# MyGene.info Gene Metadata Recipe

Simple recipe for extracting basic gene mapping and metadata using [mygene.info](https://mygene.info/).

At present, recipe only generates metadata for a single species (human), and only retrieves a small
number of fields necessary for basic id mapping and gene summarization.

# Usage

```
python -m venv ~/venv/recipe-mygene-info

source ~/venv/recipe-mygene-info/bin/activate

pip install --file requirements.txt
python build.py
```

# Result

```
  entrez_id symbol                                            summary
0         1   A1BG  The protein encoded by this gene is a plasma g...
1         2    A2M  The protein encoded by this gene is a protease...
2         3  A2MP1
3         9   NAT1  This gene is one of two arylamine N-acetyltran...
4        10   NAT2  This gene encodes an enzyme that functions to ...
...
```
