import numpy as np
import pandas as pd
import time
import altair as alt
import random
from simulation import Simulation

a=dict(
    r=[random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22),
       random.randint(0,22)] )

print(a)

sim = Simulation()
sim.generate_voters(1000)
sim.generate_parties(5)
sim.run(100)




import altair as alt
import pandas as pd
label=[]

for party, value in sim.tracker.x.items():
    label.append(party)

from matplotlib import pyplot as plt
import plotly.express as px

source= pd.DataFrame([])

for i in range(5):
     time.sleep(0.01)
     votes=[]
     for party, value in sim.tracker.votes.items():
        votes.append(value[i])

     a = pd.DataFrame({
         'step':i,

        'vote': votes,
        'label': label
     })

     source=source.append(a)
     print(source)

chart = alt.Chart(source).mark_line(point=True).encode(
        x='step',
        y='vote',
        color='label')
chart.show()











