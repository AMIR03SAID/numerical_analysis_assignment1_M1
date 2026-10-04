import numpy as np
import matplotlib.pyplot as plt

#Function 1

def f1(x):
    return x**4 - 5*x**2 + 4

# 3 points
def f1_lagrange_3(x):
    return 2*x**2 + 6*x + 4


def f1_newton_3(x):
    return 2*x**2 + 6*x + 4


def f1_hermite_3(x):
    return x**4 - 5*x**2 + 4


# 4 points
def f1_lagrange_4(x):
    return -2*x**3 - 4*x**2 + 2*x + 4


def f1_newton_4(x):
    return -2*x**3 - 4*x**2 + 2*x + 4


def f1_hermite_4(x):
    return x**4 - 5*x**2 + 4

#Function 2

def f2(x):
    return (x**3 - x) / 6


# 3 points
def f2_lagrange_3(x):
    return -(x**2 + x) / 2


def f2_newton_3(x):
    return -(x**2 + x) / 2


def f2_hermite_3(x):
    return (x**3 - x) / 6


# 4 points
def f2_lagrange_4(x):
    return (x**3 - x) / 6


def f2_newton_4(x):
    return (x**3 - x) / 6


def f2_hermite_4(x):
    return (x**3 - x) / 6

# x values

x = np.linspace(-2, 1, 500)


# FUNCTION 1 — 3 POINTS

plt.figure(figsize=(10, 6))

plt.plot(x, f1(x), label="Original function")
plt.plot(x, f1_lagrange_3(x), "--", label="Lagrange - 3 points")
plt.plot(x, f1_newton_3(x), ":", label="Newton - 3 points")
plt.plot(x, f1_hermite_3(x), "-.", label="Hermite - 3 points")

x_points = np.array([-2, -1, 0])
plt.scatter(x_points, f1(x_points), label="Interpolation points", zorder=5)

plt.xlim(-2.1, 1.1)
plt.ylim(-3, 13)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function 1: Interpolation with 3 points")
plt.legend()
plt.grid(True)

plt.show()


# FUNCTION 1 — 4 POINTS

plt.figure(figsize=(10, 6))

plt.plot(x, f1(x), label="Original function")
plt.plot(x, f1_lagrange_4(x), "--", label="Lagrange - 4 points")
plt.plot(x, f1_newton_4(x), ":", label="Newton - 4 points")
plt.plot(x, f1_hermite_4(x), "-.", label="Hermite - 4 points")

x_points = np.array([-2, -1, 0, 1])
plt.scatter(x_points, f1(x_points), label="Interpolation points", zorder=5)

plt.xlim(-2.1, 1.1)
plt.ylim(-3, 13)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function 1: Interpolation with 4 points")
plt.legend()
plt.grid(True)

plt.show()


# FUNCTION 2 — 3 POINTS

plt.figure(figsize=(10, 6))

plt.plot(x, f2(x), label="Original function")
plt.plot(x, f2_lagrange_3(x), "--", label="Lagrange - 3 points")
plt.plot(x, f2_newton_3(x), ":", label="Newton - 3 points")
plt.plot(x, f2_hermite_3(x), "-.", label="Hermite - 3 points")

x_points = np.array([-2, -1, 0])
plt.scatter(x_points, f2(x_points), label="Interpolation points", zorder=5)

plt.xlim(-2.1, 1.1)
plt.ylim(-1.2, 0.3)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function 2: Interpolation with 3 points")
plt.legend()
plt.grid(True)

plt.show()


# FUNCTION 2 — 4 POINTS

plt.figure(figsize=(10, 6))

plt.plot(x, f2(x), label="Original function")
plt.plot(x, f2_lagrange_4(x), "--", label="Lagrange - 4 points")
plt.plot(x, f2_newton_4(x), ":", label="Newton - 4 points")
plt.plot(x, f2_hermite_4(x), "-.", label="Hermite - 4 points")

x_points = np.array([-2, -1, 0, 1])
plt.scatter(x_points, f2(x_points), label="Interpolation points", zorder=5)

plt.xlim(-2.1, 1.1)
plt.ylim(-1.2, 0.3)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function 2: Interpolation with 4 points")
plt.legend()
plt.grid(True)

plt.show()