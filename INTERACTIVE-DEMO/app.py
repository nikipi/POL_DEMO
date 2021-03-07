import streamlit as st
import numpy as np

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
import seaborn as sn
import pandas as pd

# main screen title

st.title("""
 Visually Explore Voting space
""")

st.write('### [@Yulu](https://www.linkedin.com/in/yulu-niki-pi-91560617a/)')
st.write(' #### When we study political parties, we are often interested in how political ideology affects voters’and parties’behaviour. '
         
         'We assume that the political position of each party and voter can be represented as a point in a two-dimensional space and voters will vote for the party ideologically closest to them. '
         'What kind of party behaviour would that encourage? Is it clever for theparty to be ideologically in the centre, to attract a wide range of voters? Or is it smarter to find the middle ground among your current voters and solidify your position that way?')

st.write('###  In this site, you can simulate the voting process and explore how parties with different strategies search aggressively to maximise their vote.' )

st.write('You can generate parties with the following strategies:')
st.write('Sticker,Predator,Aggregator,Hunter,Random')
st.write('For more reference: [Laver(2005)](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/policy-and-the-dynamics-of-political-competition/89669AF3A2D7CA5196C72272B4AEE3BC)')

# sidebar title

st.sidebar.write('This is a project for the [POL](http://www.joselkink.net/PROG-Autumn-2020.php) at UCD')



party_num=st.sidebar.selectbox(
    'Select the number of parties',
    ('3','4','5','6','7')
)

party_num=int(party_num)


voter_num=st.sidebar.selectbox(
    'Select the number of voters',
    ('100','200','300','400','500')
)

voter_num=int(voter_num)

from simulation import Simulation
import altair as alt
import time


chart = st.empty()
chart2 = st.empty()



if st.sidebar.button('Start'):
    st.sidebar.markdown('                                              ')
    st.sidebar.markdown('# You just created {} parties!!'.format(party_num))
    sim = Simulation()
    sim.generate_parties(party_num)
    sim.generate_voters(voter_num)
    st.sidebar.markdown('                                              ')
    st.sidebar.markdown('The strategies of the {} parties are:'.format(party_num))
    for party in sim.parties:
        st.sidebar.write(party.get_name(), ':', party.get_strategy())

    sim.run(200)
    label = []
    source2 = pd.DataFrame([])

    for party, value in sim.tracker.x.items():
        label.append(party)

    for i in range(200):

        xais = []
        yais = []
        for party, value in sim.tracker.x.items():
            xais.append(value[i])

        for party, value in sim.tracker.y.items():
            yais.append(value[i])

        source = pd.DataFrame({

            'x': xais,
            'y': yais,
            'label': label
        })
        xrange = [0, 1]
        yrange = [0, 1]



        plot = alt.Chart(source).mark_circle(size=120).encode(
            x=alt.X('x',scale=alt.Scale(domain=xrange, clamp=True)),
            y=alt.X('y',scale=alt.Scale(domain=yrange, clamp=True)),
            color='label',
            tooltip=['label', 'x', 'y']
        ).interactive()

        plot.height =350
        plot.width = 700


        time.sleep(0.01)

        chart.altair_chart(plot)



        votes = []
        for party, value in sim.tracker.votes.items():
            votes.append(value[i])

        a = pd.DataFrame({
            'step': i,

            'vote': votes,
            'label': label
        })

        source2 = source2.append(a)



        xrange2 = [1, 200]
        yrange2 = [0, voter_num]

        plot2 = alt.Chart(source2).mark_line(point=True).encode(

                x=alt.X('step',scale=alt.Scale(domain=xrange2, clamp=True)),
                y=alt.X('vote',scale=alt.Scale(domain=yrange2, clamp=True)),
                color = 'label',tooltip=['label']

                     ).properties(
            width=400
        )
        plot2.height = 350
        plot2.width = 700

        chart2.altair_chart(plot2)




        # fig = plt.figure()
        # plt.scatter(xais, yais, alpha=0.8,
        #             )
        # plt.ion()
        #
        #
        # # plt.show()
        #
        # st.pyplot(fig)















from enum import Enum
from io import BytesIO, StringIO
from typing import Union

import pandas as pd
import streamlit as st

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""