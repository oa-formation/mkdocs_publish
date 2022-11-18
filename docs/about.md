=== "azure"

    ```shell
    Host formation_azure
        Hostname ssh.dev.azure.com
        AddKeysToAgent yes
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa_formation
        IdentitiesOnly yes
        User git
    ```    

=== "github"

    ```shell
    Host github.com
        AddKeysToAgent yes
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_ed25519
    ```


![product owner](media/vignettes/vignette_influencer.png){ align:right }
![product owner](media/vignettes/vignette_homme.png){ align:left }
![product owner](media/vignettes/vignette_femme.png){ align:right }
