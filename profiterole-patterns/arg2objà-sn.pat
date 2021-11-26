pattern {
  V [upos="VERB"];
  V -[obl]-> OBJASN;
  OBJASN -[case]-> C;
  C [form="a"|"à"|"á"|"audict"|"audictz"|"audit"|"ausdictes"|"ausdicts"|"ausdiz"|"oudit"|"al"|"al'"|"ál"|"als"|"as"|"ás"|"au"|"aulx"|"aus"|"ax"|"az"|"auquel"|"auquel"|"auxquels"|"A"|"Au"|"AU"];
  OBJASN [upos="NOUN"|"PROPN"|"PRON"|"ADJ"|"DET"]
}
