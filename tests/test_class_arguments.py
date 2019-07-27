# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

from sklearn.datasets import load_iris

data = load_iris()
X = data.data
y = data.target

n_iter_0 = 0
n_iter_1 = 10
random_state = 0
cv = 2

search_config = {
    "sklearn.tree.DecisionTreeClassifier": {
        "criterion": ["gini", "entropy"],
        "max_depth": range(1, 21),
        "min_samples_split": range(2, 21),
        "min_samples_leaf": range(1, 21),
    }
}

warm_start = {"sklearn.tree.DecisionTreeClassifier": {"max_depth": [1]}}


def test_memory():
    from hyperactive import HillClimbingOptimizer

    opt0 = HillClimbingOptimizer(
        search_config, n_iter_0, verbosity=0, cv=cv, memory=True
    )
    opt0.fit(X, y)

    opt1 = HillClimbingOptimizer(
        search_config, n_iter_0, verbosity=1, cv=cv, memory=False
    )
    opt1.fit(X, y)


def test_verbosity():
    from hyperactive import HillClimbingOptimizer

    opt0 = HillClimbingOptimizer(search_config, n_iter_0, verbosity=0, cv=cv)
    opt0.fit(X, y)

    opt1 = HillClimbingOptimizer(search_config, n_iter_0, verbosity=1, cv=cv)
    opt1.fit(X, y)


def test_metrics():
    from hyperactive import HillClimbingOptimizer

    opt = HillClimbingOptimizer(
        search_config,
        n_iter_0,
        metric="neg_mean_absolute_error",
        verbosity=0,
        cv=cv,
        n_jobs=1,
    )
    opt.fit(X, y)


def test_scatter_init():
    from hyperactive import HillClimbingOptimizer

    opt = HillClimbingOptimizer(
        search_config,
        n_iter_1,
        random_state=random_state,
        verbosity=0,
        cv=cv,
        n_jobs=1,
        scatter_init=10,
    )
    opt.fit(X, y)


def test_scatter_init_and_warm_start():
    from hyperactive import HillClimbingOptimizer

    opt = HillClimbingOptimizer(
        search_config,
        n_iter_1,
        random_state=random_state,
        verbosity=0,
        cv=cv,
        n_jobs=2,
        warm_start=warm_start,
        scatter_init=10,
    )
    opt.fit(X, y)