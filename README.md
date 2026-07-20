# Portefeuille Famille — site personnel

Tableau de bord de finances familiales, hébergé gratuitement sur GitHub Pages. Éditable directement dans le navigateur, avec les prix des fonds mis à jour automatiquement toutes les 30 minutes par une GitHub Action.

⚠️ **Confidentialité** : ce dépôt doit être **public** pour que GitHub Pages soit gratuit. Tes données financières (`data.json`) seront donc techniquement visibles par quiconque a le lien du dépôt (valeurs de comptes, dettes, revenus). Si tu changes d'avis, tu peux passer le dépôt en privé avec un abonnement GitHub Pro (~4 $/mois).

## 1. Créer le dépôt

1. Va sur [github.com/new](https://github.com/new).
2. Nom du dépôt : par exemple `portefeuille-famille`.
3. Visibilité : **Public**.
4. Ne coche pas "Add a README" (on en a déjà un). Clique **Create repository**.

## 2. Téléverser les fichiers

Dans le dépôt vide, clique **uploading an existing file**, puis glisse-dépose **tout le contenu de ce dossier** (`site-portefeuille`), en conservant la structure :

```
index.html
data.json
prices.json
README.md
.github/workflows/update-prices.yml
scripts/update_prices.py
```

⚠️ Si l'interface de GitHub "aplati" les dossiers lors du glisser-déposer, crée les fichiers un par un via **Add file → Create new file** et tape le chemin complet (ex: `.github/workflows/update-prices.yml`) dans le champ du nom — GitHub crée les dossiers automatiquement.

Valide avec **Commit changes**.

## 3. Activer GitHub Pages

1. Dans le dépôt : **Settings → Pages**.
2. Sous "Build and deployment" → Source : **Deploy from a branch**.
3. Branche : **main**, dossier : **/ (root)**. Clique **Save**.
4. Attends 1-2 minutes. Ton site sera accessible à :
   `https://TON-NOM-UTILISATEUR.github.io/portefeuille-famille/`

C'est ce lien que tu mets dans tes favoris — accessible depuis n'importe quel appareil.

## 4. Créer un jeton d'accès (pour pouvoir modifier les données depuis le site)

1. Va sur **github.com → ton avatar (en haut à droite) → Settings → Developer settings → Personal access tokens → Fine-grained tokens**.
2. **Generate new token**.
3. Nom : `portefeuille-famille-token`. Expiration : au choix (ex: 1 an — tu pourras le renouveler).
4. Repository access : **Only select repositories** → choisis `portefeuille-famille`.
5. Permissions → **Repository permissions** → **Contents** → **Read and write**.
6. **Generate token**, puis **copie-le immédiatement** (il ne sera plus jamais affiché).

🔒 Ce jeton donne le droit de modifier ton dépôt. Garde-le secret. Tu peux le révoquer à tout moment depuis cette même page si besoin.

## 5. Connecter le site à GitHub

1. Ouvre ton site (le lien de l'étape 3).
2. Dans la barre latérale, section **🔗 Connexion GitHub**, remplis :
   - Utilisateur/organisation : ton nom d'utilisateur GitHub
   - Nom du dépôt : `portefeuille-famille`
   - Branche : `main`
   - Jeton : colle le jeton de l'étape 4
3. Clique **💾 Enregistrer la connexion**. Le statut doit passer à "🟢 Connecté".

À partir de là, toute modification que tu fais sur le site (ajouter une position, changer un montant, etc.) est automatiquement enregistrée dans `data.json` sur GitHub, quelques secondes après ta dernière frappe.

## 6. Vérifier la mise à jour automatique des prix

1. Dans le dépôt : onglet **Actions**.
2. Tu devrais voir le workflow **Mise à jour des prix**. Il tourne automatiquement toutes les 30 minutes (9h-17h heure de l'Est, du lundi au vendredi).
3. Pour le tester tout de suite sans attendre : clique sur le workflow, puis **Run workflow**.
4. Une fois terminé (coche verte), rafraîchis ton site : les prix dans l'onglet Portefeuille doivent être à jour.

## Notes

- **Sur un nouvel appareil** : ouvre simplement le lien du site, section GitHub, entre les mêmes informations (owner/repo/branche/jeton) et clique "Enregistrer" — tes données se rechargent depuis GitHub.
- **Le jeton est stocké uniquement dans le navigateur** (localStorage), jamais envoyé ailleurs qu'à l'API officielle de GitHub.
- **Sauvegarde manuelle** : les boutons Exporter/Importer restent disponibles pour une sauvegarde locale indépendante de GitHub.
- **Si les prix ne se mettent pas à jour** : vérifie l'onglet Actions du dépôt pour voir si le workflow a échoué (clique dessus pour voir le message d'erreur), et que le champ "symbole source" de chaque fonds correspond à un symbole boursier valide (suffixe `.TO` pour les titres cotés à la Bourse de Toronto, rien pour les titres américains).
