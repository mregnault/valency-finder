pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLPARSN;
OBLPARSN [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
OBLPARSN -[case]-> C;
C [form="par"|"Par"|"PAR"|"per"|"Per"| "PER"]
}