import pandas as pd


# VALEURS
suppliers = ['Supplier1', 'Supplier2', 'Supplier3', 'Supplier4']
countries = ['China', 'USA', 'France', 'France']
target = [0, 0, 1, 0]

# NOMS COLONNES
cols = ["supplier_name", "country_name", "target"]

# CREATION DATAFRAME
df = pd.DataFrame(list(zip(suppliers, countries, target)),
                  columns=cols)
print(df)

# TRANSFORMATION AVEC LE ONE HOT ENCODING
one_hot_df = pd.get_dummies(df, columns=["country_name"])
print(f"\n {one_hot_df.to_string()}")
