from party import Party
from voter import Voter
from tracker import Tracker
from display import Display
from log import Log
from datetime import datetime




# create a simulation class, which creates parties & voters and runs the simulation
# voters,parties,numbers of simulations
class Simulation:

    def __init__(self):
        self.voters = []
        self.parties = []
        self.log = Log("simulation.log")
        self.tracker = Tracker(self)
        self.display = Display(self)

    def generate_parties(self, n):
        for i in range(1,n+1):
            name = "Party" + format(i, 'd')
            self.parties.append(Party(self, name, i))
            self.log.write("Created party: " + name)
            self.tracker.add_party(name)

    def generate_voters(self, n):
        for i in range(n):
            self.voters.append(Voter(self))
        self.log.write("Created {} voters".format(n, "d"))

    def get_parties(self):
        return self.parties

    def get_voters(self):
        return self.voters

    def set_tracker(self, tracker):
        self.tracker = tracker

    def run(self, number_of_steps):

        self.log.write("Starting simulation for {} loops".format(number_of_steps, "d"))
        for i in range(number_of_steps):

            print("\nStep {}:".format(i))

            for party in self.parties:
                party.reset_voters()

            for voter in self.voters:
                voter.update_vote()

            for party in self.parties:
                print("Party {} with the {} strategy has {} votes.".format(party.name, party.strategy,
                                                                           party.count_voters()))
                party.update_location()



            self.tracker.save_current_state()

        self.log.write("Finishing simulation")

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = timestamp + "_party_movement.csv"
        filename='isatry'
        self.log.write("Writing CSV file: " + filename)
        self.tracker.export_to_csv(filename)
