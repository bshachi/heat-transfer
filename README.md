# 2D Heat Flow

2D Heat Flow Simuation in rectangular domain.

Numerical model uses the Finite Difference Method (FDM) for a steady-state 2D heat conduction problem.

The equartion used is the steady-state 2D heat conduction equation, also known as the Laplace equation, to simulate heat transfer in a rectangular domain. The equation is given by:

∇²T = 0

Where:

T is the temperature distribution in the domain.
∇² is the Laplacian operator, representing the sum of second derivatives with respect to x and y.

### $\therefore \\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2}\ = 0 $
      
This equation describes the distribution of heat when the temperature is not changing with time (steady state) and there are no heat sources or sinks, i.e., we have a closed system.

## Finite Difference Approximation
Using Taylor Series, the finite difference approximation of Laplace’s equation can br derived as follows: -

$4T(i, j) − T(i−1, j) − T(i, j−1) − T(i+1, j) − T(i, j+1) = 0$


### $\therefore T(i, j) = \frac{T(i−1, j) + T(i, j−1) + T(i+1, j) + T(i, j+1)}{4} $
