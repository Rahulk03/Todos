import json
import pandas
from urllib.request import urlopen
todos_URL = "https://jsonplaceholder.typicode.com/todos"
OpenURL = urlopen(todos_URL)
data = json.loads(OpenURL.read())
df1 = pandas.DataFrame(data)
df1 = df1[df1.completed != 1]
x = df1.drop(["id","title"],axis = 1)
df2 = x.rename(columns = {'completed' : 'pending todos'},inplace = False)
y = df2.groupby(["userId"]).count()
print(y)