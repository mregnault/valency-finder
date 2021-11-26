pattern {
  V [upos="VERB"];
  V -[obl]-> OBJAVINF;
  OBJAVINF -[case|mark]-> C;
  C [form="a"|"à"|"á"|"audict"|"audictz"|"audit"|"ausdictes"|"ausdicts"|"ausdiz"|"oudit"|"al"|"al'"|"ál"|"als"|"as"|"ás"|"au"|"aulx"|"aus"|"ax"|"az"|"auquel"|"auquel"|"auxquels"|"A"];
  OBJAVINF [upos="VERB"];
  OBJAVINF [VerbForm="Inf"]
}
