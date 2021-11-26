pattern { 
ATTSUBJSASN [upos="ADJ"|"NOUN"|"PROPN"|"PRON"|"DET"|"VERB"];
ATTSUBJSASN -[cop]-> VETAT;
}
without { ATTSUBJSASN [xpos="VERcjg"|"VERinf"] }