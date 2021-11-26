pattern { 
GOV [upos="VERB"];
GOV -[obl]-> OBLDESINF;
OBLDESINF [xpos="VERinf"];
OBLDESINF -[case|mark]-> C;
C [form="de"|"d'"|"d"|"DE"|"De"|"D'"|"D"]
}