"""
Créer le fichier sql lod data pour 'unitelegale' et 'etablissement'
(car les fichiers sirene ont été splittés en fichiers de 100 000 lignes)
unitelegale = 215, sufixés de 1 à 215
etablissement = 303, sufixés de 1 à 303
"""
def load_data(RepImport,prefixe,nomTable,max):
    sql = ''
    for i in range(max):
        CheminFichier = RepImport + prefixe +str(i+1)+'.csv'
        ligne = "LOAD DATA LOCAL INFILE  '"+CheminFichier+"' INTO TABLE "+nomTable+" CHARACTER SET 'utf8' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES;"
        sql += ligne+"\n" + "\! echo '"+CheminFichier+"';\n"
    f = open(RepProjet + 'loaddata-'+nomTable+'.sql',mode='w',encoding='utf8')
    f.write(sql)
    f.close()
    
RepProjet = "D:\\GDrive\\Documents\\Sirene\\Sirene-v3\\Sql\\"

#création fichier sql LOAD DATA
max = 215
RepImport = "D:\\\\Mysql\\\\unite\\\\court\\\\"
nomTable = 'unitelegale'
prefixe = 'StockUniteLegale_utf8_court_'
load_data(RepImport,prefixe, nomTable, max)

max = 303
RepImport = "D:\\\\Mysql\\\\etablissement\\\\court\\\\"
nomTable = 'etablissement'
prefixe = 'StockEtablissement_utf8_court_'
load_data(RepImport,prefixe, nomTable, max)



