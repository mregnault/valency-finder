pattern {
  GOV [upos="VERB"];
  GOV -[obl]-> OBJDESN;
  OBJDESN [form <> "jor"|"jur"|"jorz"|"poür"|"peor"|"joie"|"doel"|"dulur"|"pitet"|"pitié"|"enui"|"rien"];
  OBJDESN -[case]-> C;
  C [form="de"|"del"|"d'"|"d"|"del'"|"desdicts"|"desdis"|"desdites"|"desdiz"|"dudict"|"dudit"|"dels"|"des"|"dez"|"do"|"dou"|"du"|"ès"|"ez"|"desquelles"|"desquelx"|"duquel"|"esquelles"|"esquelx"|"desquelles"|"desquels"|"desquelx"|"desqueus"|"duquel"|"DE"|"De"|"D'"|"D"|"Duquel"|"Des"|"DES"|"Du"|"DU"];
  OBJDESN [upos="NOUN"|"PROPN"|"PRON"|"ADJ"|"DET"]
}