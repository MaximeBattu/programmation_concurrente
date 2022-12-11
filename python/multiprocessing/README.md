# Multiprocessing - S7

Dans le cadre du module "Système d'exploitation et programmation concurrente", nous avons eu à réaliser différents exercices portant sur le principe de la parallélisation de processus (multiprocessing).
Pour ce faire nous avons dû réaliser différents exercices chacun rapportant un certain nombre de point. Comme nous sommes trois dans notre groupe nous devons faire pour 30 points minimum d'exercice.

Suite aux recommandations des professeurs référents de la matière, les exercices portants sur le tri (tri rapide, tri merge ...) n'ont pas été réalisés car jugés comme s'éloignant trop de la logique du multiprocessing abordée en cours.

Fait en trinôme : 4-IRC

- BALAGUER Eileen <br>
- BATTU Maxime <br>
- LALOI Batiste <br>

# Exercices réalisés

## Courses Hippique (3pts)

Récupération du code donné, étude et compréhension de ce dernier. Plusieurs tests effectués pour comprendre le multiprocessing et son intéret dans cet exercice. Après quelques manipulations nous avons pris le code en main et rajouter différentes modifications au code donné.

Travail réalisé
- Mise en place d'un processus arbitre qui affiche en permanence le cheval qui est en tête ainsi que celui qui est dernier 
    - stack trace :
        ``` 
        Leader: [Lettre du leader] Dernier : [Lettre du dernier] 
        ```
- Faire un pari sur un cheval gagnat
    - `Entrer une lettre entre A et T :`
- Modification du dessin de base pour le remplacer par un bateau
    - `+|__A__/ `


## Faites des calculs (calculateurs & demandeurs) (3-5pts)
## Gestionnaire des Billes (5pts)
##  Estimation de PI

Le but ici était de réussir à estimer la valeur de PI à partir de différentes techniques mathématiques.
Nous devions donner un grand nombre d'itérations (100 000 000 dans notre cas) pour se rapprocher au plus possible de la valeur de PI.

Un code nous était donné, cependant il était "mono-processus" nous devions alors le modifier pour mettre en place du multiprocessing à la place

### Version Hit-Miss Monte Carlo (3pts)

Cette technique mathématique sert à déterminer la surface d'un quart du cercle trigonométrique et d'ensuite multiplier le résultat obtenu par le nombre de quart contenu dans un cercle, grâce à quoi nous pouvons obtenir une approximation de PI.

- contient un main qui appelle 2 différentes méthodes
    - multiprocess(nbIterations)
        - Découper le nombre d'itération par le nombre de processus
        - 
    - monoprocess(nbIterations)
- stack trace :
    ``` 
        Début du multiprocessing
        Temps de traitement XX.XX secondes pour X iterations en multiprocess
        Valeur estimée Pi par la méthode Hit-Miss avec 4 processus : X.XXXXXXX
        Fin du multiprocessing

        Début du monoprocessus
        Temps de traitement XX.XX secondes pour X iterations en monoprocessus
        Valeur estimée Pi par la méthode Hit-Miss en mono-processus : X.XXXXXXX
        Fin mu monoprocessus
    ```
### Version Arc-tangante
##  Un système multi-tâches de simulation d'un restaurant (5pts)
##  Game of life (5pts)
##  Fractal (3pts)