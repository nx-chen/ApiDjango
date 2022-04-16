# ApiDjango

Un Api utilisé le plateforme **Django**, Avec un base de donnée **sqlite** local. 

Réalisé par **capucine.fortin** et **ningxi.chen**

_**Python version**_ : Python 3.7

_**Django version**_ : Django 3.2.12

_**Les packages utilisé :**_

- django-rest-framework (version 0.1.0)
- django-rest-swagger (version 2.2.0)

## Afin de lancer le projet, suivre les commandes suivant
1. ```python manage.py migrate Api```
2. ```python manage.py runserver```

la programme lance sur la porte 80

## La documentation d'API est dispo sur (Après lancer la programme)
- http://localhost:80/ 

## Problème renconté et la solution

### Un problème en utilisant le package _django-rest-swagger_

![img.png](img.png)

### _Solution_

1. ouvrir le fichier 
" **.\venv\lib\site-packages\rest_framework_swagger\tamplates\rest_framework_swagger\index.html** "

2. **à la ligne 2, change le mot <staticfiles> à <static>**

![img_1.png](img_1.png) **--->** ![img_2.png](img_2.png)
