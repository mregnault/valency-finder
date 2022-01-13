pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLDESN;
OBLDESN [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
OBLDESN -[case]-> C;
C [form="de"|"d'"|"d"|"DE"|"De"|"D'"|"D"]
}