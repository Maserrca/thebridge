import plotly_express as px 
import matplotlib.pyplot as plt
import os

path = os.path.dirname(__file__)

fig = px.scatter(x = [1,2,3,4,5,6,7], y = [1,3,4,6,7,7,10])
fig.show()
#fig.write_html(path + "/img/midibuja.html")

print(path)