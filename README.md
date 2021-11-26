# valency-finder
Building a syntactical lexicon from a verb list a lemmatised conllu treebank.

## Steps

  1. Extract patterns from a conllu file. Use commands in scripts/grew-cmd.txt.

  2. Create list of verb forms and their arguments with lexbuilder.py

  3. Gather valency frames for OFrLex entries with enrich-lexval.py