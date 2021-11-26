pattern {
  V [upos="VERB"];
  V -[obl]-> OBJDEVINF;
  OBJDEVINF -[case|mark]-> C;
  C [form="de"|"del"|"d'"|"d"|"del'"|"desdicts"|"desdis"|"desdites"|"desdiz"|"dudict"|"dudit"|"dels"|"des"|"dez"|"do"|"dou"|"du"|"ès"|"ez"|"desquelles"|"desquelx"|"duquel"|"esquelles"|"esquelx"|"desquelles"|"desquels"|"desquelx"|"desqueus"|"duquel"|"DE"|"De"|"D'"|"D"];
  OBJDEVINF [upos="VERB"];
  OBJDEVINF [VerbForm="Inf"]
}