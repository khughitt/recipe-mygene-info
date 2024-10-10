List of human hg38 entrez IDs retrieved from [annotables](https://github.com/stephenturner/annotables) oct24.

In R:

```
writeLines(as.character(sort(unique(annotables::grch38$entrez))), "entrez-ids.txt")
```
