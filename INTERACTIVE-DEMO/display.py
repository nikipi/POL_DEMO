import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


class Display:

    def __init__(self, simulation):
        self.simulation = simulation

    def vote_plot(self):
        plt.clf()

        for party in self.simulation.get_parties():
            plt.text(party.get_location().get_x(), party.get_location().get_y(), party.get_name())

        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.ion()
        plt.show()
        plt.pause(.001)
        st.pyplot(plt)

