pattern {
  GOV [upos = VERB];
  GOV -[advmod]-> DLOC;
  DLOC [form="ici"|"ci"|"chi"|"íci"|"ící"|"ichi"|"yci"|"ycy"|"la"|"lai"|"laj"|"là"|"lá"|"lo"|"lou"];
  DLOC -[case]-> C;
  C [form="de"|"d"|"d'"]
}

%Loc ne semble pas cliticisé