import pickle

from picklachu.storage.base import BaseStorage


class Picklachu(object):
    def __init__(self, data_center: BaseStorage):
        self.data_center = data_center

    def i_pickle_you(self, data, path):
        """Transform to pickle and store data"""
        poke_ball = pickle.dumps(data)
        self.data_center.persist(path + ".pickle", poke_ball)

    def evolve(self, path):
        """Retrieve pickle and transform back"""
        poke_ball = self.data_center.retrieve(path + ".pickle")
        return pickle.loads(poke_ball)
