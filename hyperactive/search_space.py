# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import random
import numpy as np


class SearchSpace:
    def __init__(self, search_space, verb):
        self.search_space = search_space
        self.pos_space_limit()
        self.verb = verb

    def pos_space_limit(self):
        dim = []

        for pos_key in self.search_space:
            dim.append(len(self.search_space[pos_key]) - 1)

        self.dim = np.array(dim)

    def get_random_pos(self):
        pos_new = np.random.uniform(np.zeros(self.dim.shape), self.dim, self.dim.shape)
        pos = np.rint(pos_new).astype(int)

        return pos

    def get_random_pos_scalar(self, hyperpara_name):
        n_para_values = len(self.search_space[hyperpara_name])
        pos = random.randint(0, n_para_values - 1)

        return pos

    def pos2para(self, pos):
        values_dict = {}
        for i, key in enumerate(self.search_space.keys()):
            pos_ = int(pos[i])
            values_dict[key] = self.search_space[key][pos_]

        return values_dict
