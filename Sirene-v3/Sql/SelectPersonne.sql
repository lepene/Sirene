select siren,nomUniteLegale as Nom,dateCreationUniteLegale as date
from sirene.unitelegale 
where nomUniteLegale != ""
;