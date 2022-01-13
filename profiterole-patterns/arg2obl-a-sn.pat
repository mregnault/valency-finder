pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLASN;
OBLASN [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
OBLASN -[case]-> C;
C [form="à"|"a"|"A"]
}


% a-sinf, de-sinf, sinf, sur-sn, par-sn, avec-sn, en-sn, contre-sn, 
% pour-sinf, dans-sn