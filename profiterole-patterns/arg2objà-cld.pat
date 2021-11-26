pattern { 
GOV [upos="VERB"];
GOV -[iobj]-> IOBJA;
IOBJA [upos="PRON"] 
}
without { IOBJA [form = "en"|"an"|"am"|"En"|"EN"|"An"|"AN"|"Am"|"AM"] }