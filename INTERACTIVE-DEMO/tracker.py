import csv


class Tracker:

    def __init__(self, simulation):
        self.simulation = simulation
        self.votes = {}
        self.x = {}
        self.y = {}

    def add_party(self, name):
        self.votes[name] = []
        self.x[name] = []
        self.y[name] = []

    def save_current_state(self):
        for party in self.simulation.get_parties():
            self.votes[party.get_name()].append(party.count_voters())
            self.x[party.get_name()].append(party.get_location().get_x())
            self.y[party.get_name()].append(party.get_location().get_y())

    # create Excel file with all data
    def export_to_csv(self, filename):

        fieldnames = ['time', 'party', 'strategy', 'votes', 'x', 'y']

        with open(filename, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for party in self.simulation.get_parties():
                for t in range(len(self.votes[party.get_name()])):
                    writer.writerow({'time': t, 'party': party.get_name(), 'strategy': party.get_strategy(),
                                     'votes': self.votes[party.get_name()][t], 'x': self.x[party.get_name()][t],
                                     'y': self.y[party.get_name()][t]})
