# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X = data.data
y = data.target

n_iter_0 = 0
n_iter_1 = 3
random_state = 0
cv = 2
n_jobs = 1

search_config = {
    "keras.compile.0": {"loss": ["binary_crossentropy"], "optimizer": ["adam"]},
    "keras.fit.0": {"epochs": [1], "batch_size": [500], "verbose": [0]},
    "keras.layers.Dense.1": {
        "units": range(1, 10, 1),
        "activation": ["relu", "tanh", "linear", "sigmoid"],
        "kernel_initializer": ["RandomUniform"],
    },
    "keras.layers.Dense.2": {"units": [1], "activation": ["sigmoid"]},
}

warm_start = {
    "keras.compile.0": {"loss": ["binary_crossentropy"], "optimizer": ["adam"]},
    "keras.fit.0": {"epochs": [1], "batch_size": [500], "verbose": [0]},
    "keras.layers.Dense.1": {
        "units": [1],
        "activation": ["linear"],
        "kernel_initializer": ["RandomUniform"],
    },
    "keras.layers.Dense.2": {"units": [1], "activation": ["sigmoid"]},
}


def test_keras():
    from hyperactive import HillClimbingOptimizer

    opt = HillClimbingOptimizer(
        search_config,
        n_iter_0,
        random_state=random_state,
        verbosity=1,
        cv=cv,
        n_jobs=1,
        warm_start=warm_start,
    )
    opt.fit(X, y)