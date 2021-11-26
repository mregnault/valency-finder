pattern { 
GOV [upos="VERB"];
GOV -[iobj|obl|advmod]-> CLY;
CLY [xpos="PROadv"];
CLY [form="y"|"i"|"Y"|"I"]
}
without { CLY -[case]-> C;
C [upos="ADP"] }