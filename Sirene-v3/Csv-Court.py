"""
importe un fichier csv sirene (splité en fichiers de 100 000 lignes)
dans un fichier csv plus court en supprimant des champs inutiles
ou en les transférant dans des champs identiques mais vide
et ajoute des valeurs par défaut compatible avec le type de champ
Ex:
supprimer le nom de la commmune car il y a déja le code insee de la commune
supprimer le nom du pay car il y a déja le code insee du pay
transférer le sigle car il n'est utilisé que 6 fois sur 20 Millions de lignes
...
"""
import csv

max = 215
RepDeBase = "D:\\Mysql\\unite\\"
RepSortie = "D:\\Mysql\\unite\\court\\"
prefixe = 'StockUniteLegale_utf8_'
entete = []
csv_2 = []
csv_1 = []
for i in range(max):
    #définir les chemins de fichiers à ouvrir
    CheminFichier = RepDeBase + prefixe +str(i+1)+'.csv'
    f1 = open(CheminFichier, mode='r', encoding='utf8')
    csv_1 = csv.DictReader(f1, delimiter=',')
    CheminFichier = RepSortie + prefixe +'court_'+  str(i+1)+'.csv'
    f2 = open(CheminFichier, mode='w', encoding='utf8', newline='')
    #si entete définis
    if(entete):
        #création objet csv
        csv_2 = csv.DictWriter(f2, entete)
        #écrire ligne d'entete de colonnes
        csv_2.writeheader()
    #else:
    #si entete non encore définis, cas prévu plus loin dans le code
        
    for ligne in csv_1:        
        #déplacer le sigle dans un champ nom qui est vide
        if(ligne['sigleUniteLegale'] != ''):
            if(ligne['nomUsageUniteLegale'] == ''):
                ligne['nomUsageUniteLegale'] = ligne['sigleUniteLegale']
            else:
                if(ligne['denominationUsuelle3UniteLegale'] == ''):
                    ligne['denominationUsuelle3UniteLegale'] = ligne['sigleUniteLegale']
        #si code juridique faux ou vide, mettre sur 'non renseigné'            
        if(len(ligne['categorieJuridiqueUniteLegale']) != 4):
            ligne['categorieJuridiqueUniteLegale'] = '9999'
        #£si code effectifs faux ou vide, mettre sur 'non renseigné'
        if(len(ligne['trancheEffectifsUniteLegale']) != 2):
            ligne['trancheEffectifsUniteLegale'] = 'NR'
        #prendre la date sans l'heure dans la date de mise à jour
        if('T' in ligne['dateDernierTraitementUniteLegale']):
            ligne['dateDernierTraitementUniteLegale'] = str(ligne['dateDernierTraitementUniteLegale']).split('T')[0]
        #convertir car 'O' 'N' en int
        if(ligne['caractereEmployeurUniteLegale'] == 'O'):
            ligne['caractereEmployeurUniteLegale'] = 1
        else:
            if(ligne['caractereEmployeurUniteLegale'] == 'N'):
                ligne['caractereEmployeurUniteLegale'] = 0            
        #supprimer champs inutiles
        del ligne['nombrePeriodesUniteLegale']#inutile
        del ligne['sexeUniteLegale']#inutile
        del ligne['statutDiffusionUniteLegale']#inutile
        del ligne['unitePurgeeUniteLegale']#inutile
        del ligne['economieSocialeSolidaireUniteLegale']#inutile
        del ligne['pseudonymeUniteLegale']#jamais utilisé 
        del ligne['sigleUniteLegale']#utilisé 6 fois sur 20 Millions de lignes
        #si la liste des colonnes est vide (sera fait uniquement la 1ère fois)        
        if(not entete):
            #faire la liste des colonnes avec la liste des clés restantes
            for cle in ligne:
                entete.append(cle)
            #créer nouvel objet csv, avec nouvel entete de colonnes
            csv_2 = csv.DictWriter(f2, entete)
            #écrire les noms de colonnes en ligne 1
            csv_2.writeheader()
            
        #écrire la ligne de data en cours
        csv_2.writerow(ligne)
    
    #fermer les fichiers csv   
    f1.close()
    f2.close()
    #indiquer progression
    print(CheminFichier)
 
print("Unitélegales Terminé")   

max = 303
RepDeBase = "D:\\Mysql\\etablissement\\"
RepSortie = "D:\\Mysql\\etablissement\\court\\"
prefixe = 'StockEtablissement_utf8_'
entete = []
csv_2 = []
csv_1 = []

for i in range(max):
    #définir les chemins de fichiers à ouvrir
    CheminFichier = RepDeBase + prefixe +str(i+1)+'.csv'
    f1 = open(CheminFichier, mode='r', encoding='utf8')
    csv_1 = csv.DictReader(f1, delimiter=',')
    CheminFichier = RepSortie + prefixe +'court_'+  str(i+1)+'.csv'
    f2 = open(CheminFichier, mode='w', encoding='utf8', newline='')
    #si entete définis
    if(entete):
        #création objet csv
        csv_2 = csv.DictWriter(f2, entete)
        #écrire ligne d'entete de colonnes
        csv_2.writeheader()
    #else:
    #si entete non encore définis, cas prévu plus loin dans le code
        
    for ligne in csv_1:
        #traiter lignes
        del ligne['libelleCommuneEtablissement']#doublon
        del ligne['libelleCommuneEtrangerEtablissement']#doublon        
        del ligne['libellePaysEtrangerEtablissement']#doublon
        del ligne['nombrePeriodesEtablissement']#inutile
        del ligne['statutDiffusionEtablissement']#inutile 
        del ligne['indiceRepetitionEtablissement']#utilisé 3 fois
        del ligne['distributionSpecialeEtablissement']#utilisé 15 fois
        #‼ la voie 2 n'est utilisé qu'une fois
        del ligne['libellePaysEtranger2Etablissement']
        del ligne['libelleCommuneEtranger2Etablissement']
        del ligne['indiceRepetition2Etablissement']
        del ligne['distributionSpeciale2Etablissement']
        del ligne['codeCedex2Etablissement']
        del ligne['codeCommune2Etablissement']
        del ligne['codePaysEtranger2Etablissement']
        del ligne['codePostal2Etablissement']
        del ligne['complementAdresse2Etablissement']
        del ligne['typeVoie2Etablissement']

        if(not entete):
            #faire la liste des colonnes avec la liste des clés restantes
            for cle in ligne:
                entete.append(cle)
            #créer nouvel objet csv, avec nouvel entete de colonnes
            csv_2 = csv.DictWriter(f2, entete)          
            #écrire les noms de colonnes en ligne 1
            csv_2.writeheader()
            
        if(ligne['caractereEmployeurEtablissement'] == 'O'):
            ligne['caractereEmployeurEtablissement'] = 1
        else:
            if(ligne['caractereEmployeurEtablissement'] == 'N'):
                ligne['caractereEmployeurEtablissement'] = 0

        #etablissementSiege
        if(ligne['etablissementSiege'] == 'true'):
            ligne['etablissementSiege'] = 1
        else:
            if(ligne['etablissementSiege'] == 'false'):
                ligne['etablissementSiege'] = 0        
        #écrire la ligne de data en cours
        csv_2.writerow(ligne)
        
    #fermer les fichiers csv   
    f1.close()
    f2.close()
    #indiquer progression
    print(CheminFichier)
print("Etablissements Terminé")