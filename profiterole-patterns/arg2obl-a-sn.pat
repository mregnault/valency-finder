pattern { 
GOV [upos="VERB"];
GOV -[obl]-> DEP;
DEP [upos="NOUN"|"PROPN"|"PRON"|"DET"|"ADJ"];
DEP -[case]-> C;
C [form="à"|"a"|"A"]
}


% a-sinf, de-sinf, sinf, sur-sn, par-sn, avec-sn, en-sn, contre-sn, 
% pour-sinf, dans-sn