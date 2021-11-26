pattern { 
GOV [upos="VERB"];
GOV -[obl]-> DEP;
DEP [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
DEP -[case]-> C;
C [form="contre"|"Contre"|"CONTRE"|"contra"|"cuntre"|"Contra"|"Cuntre"]
}