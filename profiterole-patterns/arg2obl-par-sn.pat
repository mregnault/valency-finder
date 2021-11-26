pattern { 
GOV [upos="VERB"];
GOV -[obl]-> DEP;
DEP [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
DEP -[case]-> C;
C [form="par"|"Par"|"PAR"|"per"|"Per"| "PER"]
}