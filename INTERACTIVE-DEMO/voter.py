from location import Location

class Voter:

  def __init__(self, simulation):
    self.location = Location()
    self.simulation = simulation

  def update_vote(self):
    parties = self.simulation.get_parties()
    smallest_distance = 2
    party_index = -1
    i = 0
    for p in parties:
      distance=self.location.distance(p.location)
      if distance < smallest_distance:
        smallest_distance = distance
        party_index = i
      i += 1
    closest_party = parties[party_index]
    self.vote = closest_party
    self.vote.add_voter(self)

  def get_vote(self):
    return self.vote

  def get_location(self):
    return self.location
