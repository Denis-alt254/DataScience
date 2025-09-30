import pandas as pd

mydataset = {
    "name" : ["Denis", "Alvin", "John"],
    "age" : [34, 35, 43]
}

cars = ["BMW", "COROLLA", "FORD"]
countries = {"Kenya": "Nairobi", "Uganda": "Kambala", "Rwanda": "Kigali"}

myvar = pd.DataFrame(mydataset)
mycars = pd.Series(cars, index=["x", "y", "z"]) #you can assign your own index although it is assigned by default
capital = pd.Series(countries, index=["Kenya", "Rwanda"]) # you can specify the keys you want to print
df = pd.read_csv('data.csv', na_values=["", "null", "NaN"])
js = pd.read_json('data.json')

# print(myvar.loc[[0, 1, 2]])
# print(mycars["y"])
# print(capital)
x = df['age'].mean()
df.fillna({"age":x}, inplace = True)
for x in df.index:
    if df.loc[x, "age"] > 100:
        df.loc[x, "age"] = 100
df.drop_duplicates(inplace=True)
print(df.corr())
# print(js.to_string())