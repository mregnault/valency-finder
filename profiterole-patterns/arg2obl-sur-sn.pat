pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLSURSN;
OBLSURSN [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
OBLSURSN -[case]-> C;
C [form="sur"|"Sur"|"súr"|"Súr"|"SUR"]
}