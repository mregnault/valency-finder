pattern { 
ATTSUBJSCOMPL [upos="VERB"];
ATTSUBJSCOMPL -[cop]-> VETAT;
%DEP -[mark|case]-> C;
%C [form="à"|"a"|"de"|"d'"]
}
without { ATTSUBJSCOMPL [xpos="VERinf"|"VERppe"|"VERppa"] }