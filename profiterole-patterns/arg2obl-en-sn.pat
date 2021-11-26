pattern { 
GOV [upos="VERB"];
GOV -[obl]-> DEP;
DEP [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
DEP -[case]-> C;
C [form="en"|"En"|"EN"|"an"|"An"|"AN"|"am"|"Am"|"AM"|"e"|"E"|"én"]
}