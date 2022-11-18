Il est possible de se connecter aux différents serveurs git par ssh, cette solution est la plus sécurisée et est fortement recommandée.
Pour github et gitlab, il est recommandé d’utiliser des clefs au format ed25519, plus robuste. Azure devops ne supportant pas les clefs dans ce format, il faut se résigner à utiliser des clefs au format RSA.

Une fois la clef générée on peut se connecter au serveur git et réaliser ses commits par ssh, pour éviter réécrire sa passphrase à chaque commit il est possible d’ajouter la clef à un trousseau. 

???+ warning "Attention"
    La génération de clefs s’accompagne systématiquement de la création d’une passphrase. Les clefs ssh permettant l’accès total à l’ordinateur, il ne faut surtout pas la négliger.


=== ":material-console: ed25519"
    ```shell
    ssh-keygen -t ed25519 -C "olivier@gmail.com"re
    ```
=== ":material-console: rsa "
    ```shell
    ssh-keygen -C "olivier@gmail.com"
    ```

Une fois la clef générée on peut se connecter au serveur git et réaliser ses commits par ssh, pour éviter réécrire sa passphrase à chaque commit il est possible d’ajouter la clef à un trousseau. 

=== ":material-console: terminal"
    ```shell
    $ ssh-add ~/.ssh/id_ed25519
    ```