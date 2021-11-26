pattern { 
GOV [upos="VERB"];
GOV -[obl]-> DEP;
DEP [xpos="VERinf"];
DEP -[case|mark]-> C;
C [form="à"|"a"|"A"]
}