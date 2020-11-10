"""
Ecrit les requête sql de création de tables 
pour MySQL, à partir des fichier csv de descriptions des champs
de 'unité légales' et 'établissements'
"""

import csv

def CreerSql(RepProjet,NomTable,NomFichier):
        #charger le fichier csv de structure de table Sirene, dans un dictionnaire
        f = open(RepProjet +'Csv\\'+ NomFichier, mode='r', encoding='utf8')
        csv_brut = csv.DictReader(f, delimiter=',', quotechar='"')
        #trier le dictionnaire dans le même ordre que la table sirene
        csv_trier = sorted(csv_brut,key=lambda t:int(t['Ordre']))
        print(csv_trier)
        #créer une requete sql avec la liste des champs
        requeteSql = "CREATE TABLE Sirene." + NomTable + "(\n"
        clauseIndex = ""
        for ligne in csv_trier:
                #si c'est un champ texte ou liste de code texte
                if( ('Texte' in ligne['Type']) or ('Liste' in ligne['Type']) ):
                        clauseDefaut = ''
                        clauseType = " CHAR(" + ligne['Longueur']+") "
                else:
                        #si c'est une date
                        if('Date' in ligne['Type']):
                                #longueur 10 c'est une date année-mois-jour
                                if(ligne['Longueur'] == '10'):
                                        clauseDefaut = " DEFAULT '0000-00-00' "
                                        clauseType = " DATE NOT NULL "
                                else:
                                        #longeur 4 c'est une année
                                        if(ligne['Longueur'] == '4'):
                                                clauseDefaut = " DEFAULT '0000' "
                                                clauseType = " YEAR NOT NULL "
                #si le champ est un index, l'ajouter dans la clause index                         
                if('KEY' in ligne['Cle']):
                        if('PRIMARY' in ligne['Cle']):
                                clauseType = " CHAR(" + ligne['Longueur']+") NOT NULL "
                                clauseIndex += 'PRIMARY KEY ('+ligne['Nom']+ ') ,\n'
                        clauseIndex += 'INDEX ' + ligne['Nom'] + ' (' + ligne['Nom'] + ' ASC) VISIBLE ,\n'
                        
                #pour le code des effectifs de l'entreprise
                if('trancheEffectifs' in ligne['Nom']):
                        clauseDefaut = ''
                        clauseType = ' CHAR(2) NOT NULL '
                if( ('caractereEmployeur' in ligne['Nom']) or ('etablissementSiege' in ligne['Nom'])):
                        clauseDefaut = ' DEFAULT -1 '
                        clauseType = ' TINYINT NOT NULL '
                        
                # Créer requête CREATE TABLE avec Nom du champ, Type de champ, Taille, Valeur par défaut, Commentaire 
                requeteSql += ligne['Nom'] + clauseType + clauseDefaut + " COMMENT " +'"'+ ligne['Libellé'] +'"'+ ",\n"
        
        #finir la requête avec les index        
        clauseIndex = clauseIndex[0:clauseIndex.rfind(',')-1]#supprimer le dernier ',' superflu        
        requeteSql += clauseIndex + " );"
        #retirer les double espaces
        requeteSql = requeteSql.replace('  ',' ')
        f.close()
        
        #créer fichier sql
        NomFichier = 'createtable-' + NomTable + '.sql'
        f = open(RepProjet +'Sql\\'+ NomFichier,mode='w',encoding='utf8')
        f.write(requeteSql)
        f.close()
        print(requeteSql)
#-------------------------------------------------------
#Rep des fichirs sources
RepProjet = 'd:\\GDrive\\Documents\\Sirene\\Sirene-v3\\'
#pour le nom du fichier sql
NomTable = 'unitelegale'
#pour la descriptions de la table
NomFichier = 'dessinstockunitelegale-v3-court.csv'
#création du fichier
CreerSql(RepProjet, NomTable, NomFichier)

NomTable = 'etablissement'
NomFichier = 'dessinstocketablissement-v3-court.csv'
CreerSql(RepProjet, NomTable, NomFichier)

