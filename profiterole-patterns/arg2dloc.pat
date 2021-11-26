pattern {
  GOV [upos = VERB];
  GOV -[advmod]-> DEP;
  DEP [form="ici"|"ci"|"chi"|"íci"|"ící"|"ichi"|"yci"|"ycy"|"la"|"lai"|"laj"|"là"|"lá"|"lo"|"lou"];
  DEP -[case]-> C;
  C [form="de"|"d"|"d'"]
}

%Loc ne semble pas cliticisé