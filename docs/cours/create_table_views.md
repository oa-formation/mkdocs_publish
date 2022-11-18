# Créer une Table

--8<-- "docs/snippets/connect_developpeur.md"

## :material-plus-network:{.title_icons} Créer une table vide

La manière la plus simple et la plus couramment utilisée pour créer une table est de créer une table vide à partir d'un Schéma.
Ce Schéma correspond à la définition du contenu de chacune des colonnes de la table.

Chaque colonne doit posséder un nom et être associé à un type de données.


Les types de données:

- les données de texte : `#!mysql CHAR`, `#!mysql VARCHAR`
- Les données numériques éxactes :
`#!mysql TINYINT`, `#!mysql SMALLINT`, `#!mysql INT`, `#!mysql MEDIUMINT`, `#!mysql BIGINT`, `#!mysql DECIMAL`, `#!mysql NUMERIC`
- Les données numériques approximatives : `#!mysql FLOAT`, `#!mysql REAL`, `#!mysql DOUBLE`
- les dates `#!mysql DATE`, `#!mysql TIMESTAMP`

!!! note ""
    _la liste des data types et de leur description est disponible en bas de page._ 


```mysql
CREATE TABLE invoice (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    customer_id INT(6) UNSIGNED NOT NULL,
    sale_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_payed DECIMAL(5,2) UNSIGNED NOT NULL
)
```
???+ tldr "Explication"
    Dans cet exemple je créé une table dont :

    - la première colonne est ^^**id**^^, cette colonne contient l'identifiant unique de chaque vente,
    elle ne peut pas contenir de valeur négative et la valeur de la colonne s'incrémente automatiquement à chaque nouvelle entrée.  
    - ^^**customer_id**^^ correspond à l'identifiant du client que l'on va lier à une autre table ( customer ).
    La valeur est un entier non négatif et ne peut pas être nulle.
    - ^^**sale_timestamp**^^ correspond à l'horodatage de la vente, est défini automatiquement par mysql.
    - ^^**total_payed**^^ correspond à de l'argent payé par le client lors de la vente.
    La valeur est une décimale non négative à deux chiffres après la virgule et ne peut pas être nulle.

Les options utilisées lors de la définition de la table :

`#!mysql NOT NULL`
:   Dans le cas où l'option `#!mysql NOT NULL` est spécifié, la colonne ne peut pas contenir de valeur non nulle.
    Si vous essayez d'insérer une entrée dont la colonne est nulle,
    mysql vous retourne une erreur et l'opération est abandonnée.


`#!mysql UNSIGNED`
:   S'applique uniquement aux valeurs numériques.

    la valeur ne peut être inférieure à 0. 

`#!mysql AUTO_INCREMENT`
:   S'applique uniquement aux valeurs numériques.

    Lors de l'insertion des données, il faut laisser ce champ vide,
    le contenu de la colonne est généré automatiquement par MySQL.
    La première entrée est égale à 0 puis la deuxième à 1 la troisième à 2 etc...

## :material-plus-network:{.title_icons} Créer une vue

Les vues sont des objets de la base de données au même titre que les tables,
de ce fait elles sont accessible de la même manière à l'aide d'une instruction `#!mysql SELECT `

Les vues sont créées à partir d'une requête sql mais les données qu'elles contiennent ne sont pas fixées.
En clair si je mets à jour les données des tables sources de la requête générant ma vue,
les données contenues dans la vue changent.

Les vues sont très pratiques pour accéder aux données correspondant à des besoins d'information récurrent.

```mysql

CREATE VIEW customer_invoice AS
SELECT 
       inv.id, 
       inv.customer_id,
       c.first_name,
       c.last_name,
       inv.sale_timestamp,
       inv.total_payed 
FROM invoice inv 
    LEFT JOIN customer c
    on inv.customer_id = c.id
WHERE inv.sale_timestamp  BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW()
```


???+ tldr "Explication"
    Dans cet exemple je créé une une vue pour récupérer le nom et prénom des clients associés à mes ventes des 30 derniers jours.
    
    Une fois que ma vue est créé, si je souhaite accéder à cette information je n'ai pas besoin de réécrire ma requête,
    je peux juste faire un `#!mysql SELECT * FROM customer_invoice` ce qui simplifie grandement les usages et réduit les risques d'érreurs. 


## Créer Une Table / Vue Temporaire



--8<-- "docs/cours/mysql_data_types.md"