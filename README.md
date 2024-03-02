# differential-equations
Solving ordinary or partial differential equations either numerically or analytically.

For the ODEs, starting with https://sundnes.github.io/solving_odes_in_python/ode_book.pdf, a great and free book.

## Installation

Use Python 3.9 or above as it will become important later when adding CUDA or so as not to destroy your life.

``pipenv --python 3.9 install``

``pipenv shell``

So far, only numpy and matplotlib needed really.  

Note: Later on, one might want to share a virtual environment with your ML repos to avoid duplicating large installations such as PyTorch etc.

## Notes

We generally use a notebook to work through the examples, e.g. building a solver up in steps.  Then we refactor the final code(s) into a module and test it with pytest.

## Plan for this repo

1. ODEs from scratch with Sudnes' book.
2. Implemnent some of the Zill examples and exercises.
3. ODE libraries for comparison.
3. Repeat for PDEs.
4. Experiment on GPU with CuPy, CUDA, PyTorch for performance optimization and analysis.
5. Build a WebApp to expose solvers.
6. Grow wings and fly!
