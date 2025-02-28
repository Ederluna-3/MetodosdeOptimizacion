import numpy as np
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.core.problem import Problem
from pymoo.factory import get_sampling, get_crossover, get_mutation, get_termination
import matplotlib.pyplot as plt

class MyProblem(Problem):
    def __init__(self):
        super().__init__(n_var=2, n_obj=2, n_constr=0, xl=np.array([-2, -2]), xu=np.array([2, 2]))
    
    def _evaluate(self, X, out, *args, **kwargs):
        f1 = X[:,0]**2 + X[:,1]**2
        f2 = (X[:,0] - 1)**2 + (X[:,1] + 1)**2
        out["F"] = np.column_stack([f1, f2])

problem = MyProblem()

algorithm = NSGA2(
    pop_size=100,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.9, eta=15),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)

res = minimize(problem, algorithm, termination=get_termination("n_gen", 100), seed=1, verbose=True)

F = res.F
plt.scatter(F[:,0], F[:,1], c='red')
plt.xlabel("f1(x,y)")
plt.ylabel("f2(x,y)")
plt.title("Frente de Pareto")
plt.show()

def print_solutions():
    print("x\ty\tf1(x,y)\tf2(x,y)")
    for i in range(len(res.X)):
        print(f"{res.X[i,0]:.4f}\t{res.X[i,1]:.4f}\t{res.F[i,0]:.4f}\t{res.F[i,1]:.4f}")
print_solutions()