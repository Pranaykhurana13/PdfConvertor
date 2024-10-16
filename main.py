import pandas as pd 

CSV = pd.read_csv("main.csv")  

CSV.to_html("csv.html")

with open('main.json', 'r') as json_file:
    json_data = json_file.read()

dataframe = pd.read_json(json_data)

html_data = dataframe.to_html()

with open('json.html', 'w') as f:
    f.write(html_data)
