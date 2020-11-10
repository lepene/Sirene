select nomUniteLegale as Nom,sigleUniteLegale as Sigle,nomUsageUniteLegale as NomUsage,denominationUniteLegale as denom,denominationUsuelle1UniteLegale as denom1
,denominationUsuelle2UniteLegale as denom2,denominationUsuelle3UniteLegale as denom3,trancheEffectifsUniteLegale as eff,categorieJuridiqueUniteLegale as catjur
from sirene.unitelegale 
#where denominationUsuelle1UniteLegale != "" and denominationUsuelle2UniteLegale != "" and denominationUsuelle3UniteLegale != "" and denominationUniteLegale != ""
#and nomUsageUniteLegale != ""
;