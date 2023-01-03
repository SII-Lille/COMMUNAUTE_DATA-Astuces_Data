import time

# Création d'un dictionnaire de fournisseurs avec leur pays d'activité
suppliers = {"Supplier1": "China", "Supplier2": "USA", "Supplier3": "France", "Supplier4": "Germany"}
print(f"Données d'exemple : \n {suppliers}")
# output: {'Supplier1': 'China', 'Supplier2': 'USA', 'Supplier3': 'France', 'Supplier4': 'Germany'}

# *************************************** 1er CAS **********************************************************************
# -> On souhaite obtenir le nom des fournisseurs sous forme de liste
supplier_names = [name for name in suppliers]
print(f"1er cas : \n {supplier_names}")
# output: ['Supplier1', 'Supplier2', 'Supplier3', 'Supplier4']

# *************************************** 2ème CAS *********************************************************************
# -> On souhaite obtenir le nom des différents pays d'activité sous forme de liste
countries = [suppliers[name] for name in suppliers]
print(f"2ème cas : \n {countries}")
# output: ['China', 'USA', 'France', 'Germany']

# *************************************** 3ème CAS *********************************************************************
# -> On souhaite obtenir le nom des fournisseurs hors France
supplier_names_without_france = [name for name in suppliers if suppliers[name] != "France"]
print(f"3ème cas : \n {supplier_names_without_france}")
# output: ['Supplier1', 'Supplier2', 'Supplier4']

# *************************************** 4ème CAS *********************************************************************
# → On souhaite tester les performances de la list comprehension versus une simple boucle for. Les résultats sont
# valables uniquement pour ce cas.
# J'utilise un dict comprehension pour générer les données dont nous allons avoir besoin.
print("4ème cas :")
dict_suppliers = {f"supplier{number}": f"country{number}" for number in range(1, 10000000)}

# On veut garder les suppliers avec un numéro pair
# → Boucle for
start = time.time()

list_supplier_pair = []
for name in dict_suppliers:
    if int(dict_suppliers[name][7:]) % 2 == 0:
        list_supplier_pair.append(dict_suppliers[name])

end = time.time()
time_for_loop = end - start
print(f"Temps d'exécution boucle for : {time_for_loop}")
# print(list_supplier_pair[:10])

# → List comprehension
start = time.time()
list_supplier_pair = [dict_suppliers[name] for name in dict_suppliers if int(dict_suppliers[name][7:]) % 2 == 0]
end = time.time()
time_list_comprehension = end - start
print(f"Temps d'exécution list comprehension : {time_list_comprehension}")
# print(list_supplier_pair[:10])

ecart = (time_for_loop - time_list_comprehension) / time_for_loop * 100
print(f"Ecart de la list comprehension comparé à une boucle for : {ecart}%")
# L'utilisation de la list comprehension est souvent plus performante (voir le README.md pour les résultats de tests).

# *************************************** 5ème CAS *********************************************************************
# -> On souhaite parcourir 2 listes en simultanée pour créer des tuples dans une liste
suppliers = ['Supplier1', 'Supplier2', 'Supplier3', 'Supplier4']
countries = ['China', 'USA', 'France', 'Germany']

new_suppliers_dict = [(supplier, country) for supplier in suppliers for country in countries]
print(f"5ème cas : \n {new_suppliers_dict}")
