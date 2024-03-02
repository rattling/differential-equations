import numpy as np
from math import sin
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")
# NOTE : need to specify non-interactive backend when running through script or plt.plot() will block thread and script will hang


"""
Solves a system of ODEs with Forward Euler's method.
"""


class ForwardEuler:
    def __init__(self, f):
        # replace the function f with the function inside a wrapper that converts output to np array
        # I probably would have just created a new named function here, lambda is lighter and nicer though
        self.f = lambda t, u: np.asarray(f(t, u), float)

    def set_initial_condition(self, u0):
        if np.isscalar(u0):  # scalar ODE
            self.neq = 1  # no of equations
            u0 = float(u0)
        else:  # system of ODEs
            self.neq = len(u0)  # no of equations
            u0 = np.asarray(u0)
            self.u0 = u0

    def solve(self, t_span, N):
        """Compute solution for
        t_span[0] <= t <= t_span[1],
        using N steps with step size of dt"""
        t0, T = t_span
        self.dt = (T - t0) / N
        self.t = np.zeros(N + 1)
        if self.neq == 1:
            self.u = np.zeros(N + 1)
        else:
            self.u = np.zeros((N + 1, self.neq))
            msg = "Please set initial condition before calling solve"
        assert hasattr(self, "u0"), msg
        self.t[0] = t0
        self.u[0] = self.u0
        for n in range(N):
            self.n = n
            self.t[n + 1] = self.t[n] + self.dt
            self.u[n + 1] = self.advance()
        return self.t, self.u

    def advance(self):
        """Advance the solution one time step."""
        u, dt, f, n, t = self.u, self.dt, self.f, self.n, self.t
        # NOTE: the actual theta and omega are being calculated here, u being theta/omega. So we have the ingredients for the pendulum f.
        # NOTE: or more generally, could be u1, u2, u3 for any arbitrary list of parameters packed into u
        return u[n] + dt * f(t[n], u[n])


class Pendulum:
    def __init__(self, L, g=9.81):
        self.L = L
        self.g = g

    def __call__(self, t, u):
        theta, omega = u
        dtheta = omega
        domega = -self.g / self.L * sin(theta)
        return [dtheta, domega]


problem = Pendulum(L=1)
solver = ForwardEuler(problem)
theta = np.pi / 4
omega = 0
solver.set_initial_condition([theta, omega])
T = 10
N = 1000
t, u = solver.solve(t_span=(0, T), N=N)
print("Final ")
print(u[-1, :])
plt.plot(t, u[:, 0], label="theta")
plt.plot(t, u[:, 1], label="omega")
plt.xlabel("t")
plt.ylabel("Angle theta and angular velocity omega")
plt.legend()
plt.savefig("pendulum.png")


