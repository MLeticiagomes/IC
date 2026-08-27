# 51 participantes
# 3 sessões 
# 2 classes
# 59 canais
# 100 tiragens

from moabb.datasets import Yang2025
import plotly.express as px
import plotly.graph_objects as go

dataset = Yang2025()
data = dataset.get_data(subjects=[1])
print(data[1])