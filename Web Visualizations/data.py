import pandas as pd
df= pd.read_csv("Web Visualizations/resources/cities.csv")
df.to_html("datafied.html",index=False)
Table=df.html()
print (Table)