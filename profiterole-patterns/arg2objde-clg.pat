pattern { 
GOV [upos="VERB"];
GOV -[iobj|obl]-> IOBJDE;
IOBJDE [upos="PRON"|"ADV"];
IOBJDE [form="en"|"an"|"am"|"En"|"EN"|"An"|"AN"|"Am"|"AM"]
}
without { IOBJDE -[case]-> C;
C [upos="ADP"] }