# muller-method-Django
A web application that could find the real or complex roots of any equation with a single unknown using numerical analysis based on muller method which is an enhanced form of the secant method



# History and concept
Muller's method is a root-finding algorithm, a numerical method for solving equations of the form f(x) = 0. It was first presented by David E. Muller in 1956.Muller's method is based on the secant method, which constructs at every iteration a line through two points on the graph of f. Instead, Muller's method uses three points, constructs the parabola through these three points, and takes the intersection of the x-axis with the parabola to be the next approximation.

<p align="center">
<img  src='https://media.geeksforgeeks.org/wp-content/uploads/Muller-Method.png'></img>
</p>


# problem definition and algorithm
problem : find a root for the equation F(x) given 3 initial points x0, x1, x2 with relative error tolerance ε and with maximimum of N iterations, then plot the function f(x), for each iteration you must find the relative error by using the formula ((x3 - x2)/x3) * 100%

- inputs : 
    - f(x)
    - x0
    - x1
    - x2
    - ε
    - N

- output :
    - list of iterations containing :
      - x0
      - x1
      - x2
      - F(p0)
      - F(p1)
      - F(p2)
      - h0
      - h1
      - Ϭ0
      - Ϭ1
      - a
      - b
      - c
      - x3
      - F(p3)
      - ε
    - solution
    - plot of the function
- steps
    1. Start
    2. Define list of iterations
    3. Define n <- 0
    4. Read values of F(x), x0, x1, x2, error, N
    5. h0 <- x1 - x0
    6. h1 <- x2 - x1
    7. f0 <- F(x0)
    8. f1 <- F(x1)
    9. f2 <- F(x2)
    10. Ϭ0 <- (f1 - f0)/h0
    11. Ϭ1 <- (f2 - f1)/h1
    12. a <- (Ϭ1 - Ϭ0) / (h1 + h0)
    13. b <- a * h1 + Ϭ1
    14. c <- fp2
    15. x3 <- -2c / (b + sign(b)*root(b^2 - 4ac))
    16. f3 <- F(x3)
    17. ε <- ((x3 - x2)/x3) * 100%
    18. n = n + 1
    19. add x0,x1,x2,f0,f1,f2, Ϭ0, Ϭ1, a, b, c, x3, f3, ε, n as a dictionary to the list iterations
    19. if n > N or ε <= error
        - return to step iv
    20. return list of iterations
    21. plot F(x)
# speed of convergence
The order of convergence of Muller's method is approximately 1.84. This can be compared with 1.62 for the secant method and 2 for Newton's method. So, the secant method makes less progress per iteration than Muller's method and Newton's method makes more progress.
