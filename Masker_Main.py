from anonympy.pandas import dfAnonymizer
from anonympy.pandas.utils_pandas import load_dataset

df = load_dataset() 
print(df)

anonym = dfAnonymizer(df)


anonym.anonymize({'name':'categorical_fake','age': 'numeric_noise'})

print(anonym)
print(anonym.to_df())




