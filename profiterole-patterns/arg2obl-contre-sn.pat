pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLCONTRESN;
OBLCONTRESN [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
OBLCONTRESN -[case]-> C;
C [form="contre"|"Contre"|"CONTRE"|"contra"|"cuntre"|"Contra"|"Cuntre"]
}