# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

from hyperactive import Hyperactive

data = load_iris()
X, y = data.data, data.target


def model(para, X, y):
    dtc = DecisionTreeClassifier(
        max_depth=para["max_depth"],
        min_samples_split=para["min_samples_split"],
        min_samples_leaf=para["min_samples_leaf"],
    )
    scores = cross_val_score(dtc, X, y, cv=2)

    return scores.mean()


search_space = {
    "max_depth": range(1, 21),
    "min_samples_split": range(2, 21),
    "min_samples_leaf": range(1, 21),
}


def test_n_jobs():
    n_jobs_list = [1, 2, 4, 10, 100, -1]
    for n_jobs in n_jobs_list:
        search = {
            "model": model,
            "search_space": search_space,
            "n_iter": 3,
            "n_jobs": 1,
        }

        hyper = Hyperactive(X, y)
        hyper.add_search(**search)


def test_positional_args():
    hyper = Hyperactive(X, y)
    hyper.add_search(model, search_space)


def test_random_state():
    opt0 = Hyperactive(X, y, random_state=False, memory=memory)
    opt0.search(search_config)

    opt1 = Hyperactive(X, y, random_state=0, memory=memory)
    opt1.search(search_config)

    opt2 = Hyperactive(X, y, random_state=1, memory=memory)
    opt2.search(search_config)


def test_max_time():
    opt0 = Hyperactive(X, y, memory=memory)
    opt0.search(search_config, max_time=0.00001)


def test_memory():
    opt0 = Hyperactive(X, y, memory=True)
    opt0.search(search_config)

    opt1 = Hyperactive(X, y, memory=False)
    opt1.search(search_config)

    opt2 = Hyperactive(X, y, memory="short")
    opt2.search(search_config)

    opt3 = Hyperactive(X, y, memory="long")
    opt3.search(search_config)

    opt4 = Hyperactive(X, y, memory="long")
    opt4.search(search_config)

    opt = Hyperactive(X, y, memory=memory, verbosity=0)
    opt.search(search_config)


"""
def test_dill():
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF, Matern
    from hypermemory import reset_memory

    reset_memory(
        meta_path="/home/simon/git_workspace/Hyperactive/hyperactive/meta_data/",
        force_true=True,
    )

    def model(para, X, y):
        gpc = GaussianProcessClassifier(kernel=para["kernel"])
        scores = cross_val_score(gpc, X, y, cv=2)

        return scores.mean()

    search_config = {model: {"kernel": [RBF(), Matern()]}}

    opt0 = Hyperactive(X, y, memory="long")
    opt0.search(search_config)

    print("\n\n ------------------------------------------------------- \n\n")

    opt1 = Hyperactive(X, y, memory="long")
    opt1.search(search_config)
"""


def test_verbosity0():
    opt = Hyperactive(X, y, verbosity=0, memory=memory)
    opt.search(search_config)


def test_verbosity1():
    opt = Hyperactive(X, y, verbosity=0, memory=memory)
    opt.search(search_config, n_jobs=2)


def test_verbosity2():
    opt = Hyperactive(X, y, verbosity=1, memory=memory)
    opt.search(search_config, n_jobs=2)


def test_verbosity3():
    opt = Hyperactive(X, y, verbosity=1, memory=memory)
    opt.search(search_config)


def test_verbosity4():
    opt = Hyperactive(X, y, verbosity=2, memory=memory)
    opt.search(search_config)


def test_verbosity5():
    opt = Hyperactive(X, y, verbosity=2, memory=memory)
    opt.search(search_config, n_jobs=2)


def test_scatter_init():
    init_config = {model: {"scatter_init": 10}}
    opt = Hyperactive(X, y, memory=memory)
    opt.search(search_config, init_config=init_config)

    opt = Hyperactive(X, y, memory=memory, verbosity=0)
    opt.search(search_config, init_config=init_config)


def test_warm_start():
    init_config = {
        model: {"max_depth": 10, "min_samples_split": 2, "min_samples_leaf": 5}
    }
    opt = Hyperactive(X, y, memory=memory)
    opt.search(search_config, n_iter=0, init_config=init_config)

    assert opt.results[model] == init_config[model]


def test_warm_start_multiple():

    opt = Hyperactive(X, y, memory="short")
    opt.search(search_config, n_iter=10, n_jobs=2)


def test_partial_warm_start():
    init_config = {model: {"min_samples_split": 2, "min_samples_leaf": 5}}
    opt = Hyperactive(X, y, memory=memory)
    opt.search(search_config, n_iter=0, init_config=init_config)

    opt = Hyperactive(X, y, memory=memory, verbosity=0)
    opt.search(search_config, n_iter=0, init_config=init_config)


def test_optimizer_args():
    opt = Hyperactive(X, y, memory=memory)
    opt.search(search_config, optimizer={"HillClimbing": {"epsilon": 0.1}})


"""
def test_ray_1():
    ray.init()
    opt = Hyperactive(X, y, memory=memory)
    opt.search(search_config, n_jobs=1)


def test_ray_2():
    ray.init()
    opt = Hyperactive(X, y, memory=memory)
    opt.search(search_config, n_jobs=2)
"""
