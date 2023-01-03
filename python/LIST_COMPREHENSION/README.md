# LIST COMPREHENSION
- Doc python : https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
- Article SII sur Medium : https://medium.com/@sii-lille/python-list-comprehension-93d1bda9e25b

## 4ème cas : Test de performances
### Environnement technique
- Windows 11;
- CPU : intel core i5 8th Gen (1,8GHz 4 coeurs);
- RAM : 32 Go 2400 MHz;
- Python 3.11;
- D'autres applications tournaient en parallèles sur l'ordinateur de test.

### Tests de performance
Plusieurs tests ont été lancés à 15 secondes d'écart et voici les 10 résultats : 
- Résultats 1 : 15% de gain en utilisant la list comprehension
- Résultats 2 : 18% de gain en utilisant la list comprehension
- Résultats 3 : 6% de gain en utilisant la list comprehension
- Résultats 4 : 2% de perte en utilisant la list comprehension
- Résultats 5 : 17% de gain en utilisant la list comprehension
- Résultats 6 : 15% de gain en utilisant la list comprehension
- Résultats 7 : 20% de gain en utilisant la list comprehension
- Résultats 8 : 18% de gain en utilisant la list comprehension
- Résultats 9 : 13% de gain en utilisant la list comprehension
- Résultats 10 : 16% de gain en utilisant la list comprehension  
La list comprehension a clairement été plus performante sur l'environnement technique utilisé. Souvent >15%.