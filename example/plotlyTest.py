import numpy as np 
from plotly.offline import plot
import plotly.graph_objs as go

import plotly.io as pio
pio.renderers.default = "browser"

fig = go.Figure(data=[{'type': 'scatter', 'y': [2, 1, 4]}])

plot(fig)