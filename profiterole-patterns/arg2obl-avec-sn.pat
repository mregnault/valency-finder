pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLAVECSN;
OBLAVECSN [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
OBLAVECSN -[case]-> C;
C [form="avec"|"avoec"|"Avec"|"Avoec"|"avuec"|"Avuec"]
}