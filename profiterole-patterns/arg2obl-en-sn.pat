pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLENSN;
OBLENSN [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
OBLENSN -[case]-> C;
C [form="en"|"En"|"EN"|"an"|"An"|"AN"|"am"|"Am"|"AM"|"e"|"E"|"én"]
}