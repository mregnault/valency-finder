pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLASINF;
OBLASINF [xpos="VERinf"];
OBLASINF -[case|mark]-> C;
C [form="à"|"a"|"A"]
}