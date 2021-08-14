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


st.write('When we study political parties, we are often interested in how political ideology affects voters’ and parties’ behaviour. '
         
         'We assume that the political position of each party and voter can be represented as a point in a two-dimensional space and voters will vote for the party ideologically closest to them. '
         'What kind of party behaviour would that encourage? Is it clever for the party to be ideologically in the centre, to attract a wide range of voters? Or is it smarter to find the middle ground among your current voters and solidify your position that way?')

st.write('###  On this interactive website, you can reproduce the analysis by [Laver(2005)](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/policy-and-the-dynamics-of-political-competition/89669AF3A2D7CA5196C72272B4AEE3BC), simulating the voting process and explore how parties with different strategies search aggressively to maximise their vote.' )

st.write("This project was developed in the module [Programming for Social Scientists](http://www.joselkink.net/PROG-Autumn-2020.php) by Prof.Jos Elkink and the module's students at the School of Politics and International Relations, University College Dublin")

st.write('#### Author of this website: [Yulu Pi](https://www.linkedin.com/in/yulu-niki-pi-91560617a/)')
st.write(' ')



# sidebar title




st.sidebar.write('#### You can generate parties with the following strategies:')
st.sidebar.write('')
st.sidebar.write('Sticker: never change party policy;')
st.sidebar.write('Predator: move party policy toward the policy position of the largest party;')
st.sidebar.write('Aggregator: adapt party policy to the ideal policy positions of party supporters; ')
st.sidebar.write('Hunter: repeat policy moves that were rewarded; otherwise make random moves;')
st.sidebar.write('Random: move party policy randomly.')





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

full = pd.DataFrame()

if st.sidebar.button('Start'):
    st.sidebar.markdown('                                              ')
    st.sidebar.markdown('## You just created {} parties!!'.format(party_num))
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

    for party  in sim.parties:
        a = party.get_name()+":"+party.get_strategy()
        label.append(a)

    for i in range(200):

        xais = []
        yais = []

        for party, value in sim.tracker.x.items():
            xais.append(value[i])

        for party, value in sim.tracker.y.items():
            yais.append(value[i])

        source = pd.DataFrame({

            'Socialist < ---------- > Capialist': xais,
            'Traditional < ---------- > Libertarian': yais,
            'label': label
        })
        xrange = [0, 1]
        yrange = [0, 1]



        plot = alt.Chart(source,title='Simulated party policy changes in a two-demensional voting space').mark_circle(size=120).encode(
            x=alt.X('Socialist < ---------- > Capialist',scale=alt.Scale(domain=xrange, clamp=True)),
            y=alt.X('Traditional < ---------- > Libertarian',scale=alt.Scale(domain=yrange, clamp=True)),
            color='label',
            tooltip=['label', 'Socialist < ---------- > Capialist', 'Traditional < ---------- > Libertarian']
        ).interactive()

        plot.height =350
        plot.width = 700


        time.sleep(0.01)

        chart.altair_chart(plot)


        votes = []
        for party, value in sim.tracker.votes.items():
            votes.append(value[i])

        a = pd.DataFrame({
            'Time (simulation cycles)': i,

            'Party Support (number of voters)': votes,
            'label': label
        })

        source2 = source2.append(a)



        xrange2 = [1, 200]
        yrange2 = [0, voter_num]

        plot2 = alt.Chart(source2,title='Simulated time series of party support').mark_line(point=True).encode(

                x=alt.X('Time (simulation cycles)',scale=alt.Scale(domain=xrange2, clamp=True)),
                y=alt.X('Party Support (number of voters)',scale=alt.Scale(domain=yrange2, clamp=True)),
                color = 'label',tooltip=['label']

                     ).properties(
            width=400
        )
        plot2.height = 350
        plot2.width = 700

        chart2.altair_chart(plot2)



        b=a.pivot_table(values='Party Support (number of voters)',columns='label',index='Time (simulation cycles)')
        b.index.name = 'Time (simulation cycles)'
        frames = [full,b]
        full = pd.concat(frames)
