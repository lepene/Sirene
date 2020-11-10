CREATE TABLE Sirene.etablissement(
siren CHAR(9) COMMENT "Numéro Siren",
nic CHAR(5) COMMENT "Numéro interne de classement de l'établissement",
siret CHAR(14) NOT NULL COMMENT "Numéro Siret",
dateCreationEtablissement DATE NOT NULL DEFAULT '0000-00-00' COMMENT "Date de création de l’établissement",
trancheEffectifsEtablissement CHAR(2) NOT NULL COMMENT "Tranche d’effectif salarié de l’établissement",
anneeEffectifsEtablissement YEAR NOT NULL DEFAULT '0000' COMMENT "Année de validité de la tranche d’effectif salarié de l’établissement",
activitePrincipaleRegistreMetiersEtablissement CHAR(6) COMMENT "Activité exercée par l’artisan inscrit au registre des métiers",
dateDernierTraitementEtablissement DATE NOT NULL DEFAULT '0000-00-00' COMMENT "Date du dernier traitement de l’établissement dans le répertoire Sirene",
etablissementSiege TINYINT NOT NULL DEFAULT -1 COMMENT "Qualité de siège ou non de l’établissement",
complementAdresseEtablissement CHAR(38) COMMENT "Complément d’adresse",
numeroVoieEtablissement CHAR(4) COMMENT "Numéro de voie",
typeVoieEtablissement CHAR(4) COMMENT "Type de voie",
libelleVoieEtablissement CHAR(100) COMMENT "Libellé de voie",
codePostalEtablissement CHAR(5) COMMENT "Code postal",
codeCommuneEtablissement CHAR(5) COMMENT "Code commune de l’établissement",
codeCedexEtablissement CHAR(9) COMMENT "Code cedex",
libelleCedexEtablissement CHAR(100) COMMENT "Libellé du code cedex",
codePaysEtrangerEtablissement CHAR(5) COMMENT "Code pays pour un établissement situé à l’étranger",
numeroVoie2Etablissement CHAR(4) COMMENT "Numéro de la voie de l’adresse secondaire",
libelleVoie2Etablissement CHAR(100) COMMENT "Libellé de voie de l’adresse secondaire",
libelleCedex2Etablissement CHAR(100) COMMENT "Libellé du code cedex de l’adresse secondaire",
dateDebut DATE NOT NULL DEFAULT '0000-00-00' COMMENT "Date de début d'une période d'historique d'un établissement",
etatAdministratifEtablissement CHAR(1) COMMENT "État administratif de l’établissement",
enseigne1Etablissement CHAR(50) COMMENT "Première ligne d’enseigne de l’établissement",
enseigne2Etablissement CHAR(50) COMMENT "Deuxième ligne d’enseigne de l’établissement",
enseigne3Etablissement CHAR(50) COMMENT "Troisième ligne d’enseigne de l’établissement",
denominationUsuelleEtablissement CHAR(100) COMMENT "Dénomination usuelle de l’établissement",
activitePrincipaleEtablissement CHAR(6) COMMENT "Activité principale de l'établissement pendant la période",
nomenclatureActivitePrincipaleEtablissement CHAR(8) COMMENT "Nomenclature d’activité de la variable activitePrincipaleEtablissement",
caractereEmployeurEtablissement TINYINT NOT NULL DEFAULT -1 COMMENT "Caractère employeur de l’établissement",
INDEX siren (siren ASC) VISIBLE ,
INDEX nic (nic ASC) VISIBLE ,
PRIMARY KEY (siret) ,
INDEX siret (siret ASC) VISIBLE ,
INDEX dateCreationEtablissement (dateCreationEtablissement ASC) VISIBLE ,
INDEX trancheEffectifsEtablissement (trancheEffectifsEtablissement ASC) VISIBLE ,
INDEX activitePrincipaleRegistreMetiersEtablissement (activitePrincipaleRegistreMetiersEtablissement ASC) VISIBLE ,
INDEX etablissementSiege (etablissementSiege ASC) VISIBLE ,
INDEX codePostalEtablissement (codePostalEtablissement ASC) VISIBLE ,
INDEX codeCommuneEtablissement (codeCommuneEtablissement ASC) VISIBLE ,
INDEX enseigne1Etablissement (enseigne1Etablissement ASC) VISIBLE ,
INDEX enseigne2Etablissement (enseigne2Etablissement ASC) VISIBLE ,
INDEX enseigne3Etablissement (enseigne3Etablissement ASC) VISIBLE ,
INDEX denominationUsuelleEtablissement (denominationUsuelleEtablissement ASC) VISIBLE ,
INDEX activitePrincipaleEtablissement (activitePrincipaleEtablissement ASC) VISIBLE ,
INDEX caractereEmployeurEtablissement (caractereEmployeurEtablissement ASC) VISIBLE );