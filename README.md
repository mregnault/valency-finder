# valency-finder
Building a syntactical lexicon from a verb list a lemmatised conllu treebank.

## Requirements
 - grew: https://grew.fr/usage/install/
 - conllu parser: https://github.com/EmilStenstrom/conllu

## Steps

  1. Extract patterns from a conllu file. Use commands in scripts/grew-cmd.txt.

  2. Extract information with extract-json.py.

  3. Create list of verb forms and their arguments with lexbuilder.py

  4. Gather valency frames for OFrLex entries with enrich-lexval.py