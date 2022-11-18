# Ajouter un Administrateur

La sécurisation d'un serveur **Mysql** passe impérativement par la création de différents types d'utilisateurs. D'un coté les comptes d'administration et de l'autre les comptes utilisés pour la lecture et l'écriture des données.

La première chose à faire est de créer un nouveau compte administrateur, c'est avec ce compte que l'on va réaliser la gestion des droits sur les bases de données.

[comment]: <> (## :material-orbit:{.title_icons} Création d'un nouvel administrateur)

[comment]: <> (## :material-play-speed:{.title_icons} Création d'un nouvel administrateur)

[comment]: <> (## :material-penguin:{.title_icons} Création d'un nouvel administrateur)
## :material-plus-network:{.title_icons} Création d'un nouvel administrateur

Avant toutes choses, connectons-nous en **root** à la console **Mysql**,
en effet lors de sa création la base de données va automatiquement créer un utilisateur **root**.
Cet Utilisateur dispose de tous les privilèges sur la base de données
dont notamment les droits d'administration :

```shell
mysql -u root -p
Enter password:
```

???+ tldr "Explication"

    - **-u root** : connexion avec l'utilisateur **root**
    - **-p** : connexion avec mot de passe.
    - **Enter password** : mysql nous demande alors notre mot de passe.

Résultat : nous avons désormais accès à la console de Mysql,
qui nous permet d'interagir directement avec notre base de données.

```shell
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 8.0.17 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```
Ensuite on créé un utilisateur qui sera identifié par un nom, une adresse et un mot de passe.

=== "inline :material-console:"
    ```mysql
    CREATE USER 'olivier'@'localhost' IDENTIFIED BY 'RJ1gbel9K+VzoSLApWo1Zu+3qcX1XOcB9SXf5w9+9jI';
    ```

=== "pretty :material-shimmer:"
    ```mysql
    CREATE USER
        'olivier'@'localhost'
    IDENTIFIED BY
        'RJ1gbel9K+VzoSLApWo1Zu+3qcX1XOcB9SXf5w9+9jI';
    ```

???+ tldr "Explication"
    dans cet exemple je crée un compte dont :

    - le nom est **olivier**
    - l'utilisateur se connecte depuis **localhost**
    - le mot de passe pour cette utilsateur est **RJ1gbel9K+VzoSLApWo1Zu+3qcX1XOcB9SXf5w9+9jI**
    
    Lorsque j'essaie de me connecter à la base de données,
    la validation de ces trois éléments est nécessaire pour que la connexion soit établie,
    si j'essaie de me connecter avec ce nom et ce mot de passe depuis une autre machine que _localhost_, **la connexion sera refusé**.

Il peut être utile de remplacer le nom **olivier** par **admin_olivier** puisqu'il s'agit d'un compte administrateur,
par ailleurs le mot de passe utilisé içi a été généré aléatoirement. À noter que l'adresse a été remplacé par **localhost** qui est un mot réservé et désigne l'ordinateur sur lequel est installé le serveur **Mysql**, nous verrons d'autres options par la suite.

## :material-plus-network:{.title_icons} Assignation des privilèges au nouvel utilisateur

Maintenant que le compte est créé, il est nécessaire de lui assigner les authorisations pour l'administration des bases de données.

Toujours dans la console **Mysql** :

=== "inline :material-console:"
    ```mysql
    GRANT ALL PRIVILEGES ON *.* TO 'olivier'@'localhost';
    ```

=== "pretty :material-shimmer:"
    ``` mysql
    GRANT
    ALL PRIVILEGES
    ON *.*
    TO 'olivier'@'localhost';
    ```

???+ tldr "Explication"

    - **GRANT** sert à definir les privilèges
    - **ALL PRIVILEGES** est un paramètre regroupant tous les privileges possibles ( *CREATE*, *DROP*, *DELETE*, *INSERT*, *SELECT*, *UPDATE* )
    - __ON * . *__ indique que le GRANT des  privlèges s'applique sur toutes les tables de toutes les bases de données. La valeur à gauche du point indique la ou les base(s) de donnée(s) affectée(s) et la valeur à droite du point indique la ou les table(s) concernée(s).

Voilà nous avons desormais un nouvel administrateur et c'est avec ce compte que nous allons desormais administrer nos bases de données.

Actuellement connecté avec l'utilisateur **root**,
on se déconnecte pour utiliser le compte du nouvel administrateur **olivier**,
mais avant on recharge les privilèges pour appliquer les modifications.

Recharge des privilèges et deconnexion à la console **Mysql**:

```sql
FLUSH PRIVILEGES;
exit
```
reconnexion avec le compte du nouvel administrateur:
```shell
mysql -u olivier@localhost -p
Enter password:
```
résultat
```shell
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 23
Server version: 8.0.17 MySQL Community Server - GPL

Copyright (c) 2000, 2019, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

Voilà, maintenant que nous avons créé un nouvel administrateur nous allons pouvoir passer à la gestion des utilisateur et des droits.