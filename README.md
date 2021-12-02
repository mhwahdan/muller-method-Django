# muller-method-Django
A web application that could find the real or complex roots of any equation with a single unknown using numerical analysis based on muller method which is an enhanced form of the secant method



# History and concept
Muller's method is a root-finding algorithm, a numerical method for solving equations of the form f(x) = 0. It was first presented by David E. Muller in 1956.Muller's method is based on the secant method, which constructs at every iteration a line through two points on the graph of f. Instead, Muller's method uses three points, constructs the parabola through these three points, and takes the intersection of the x-axis with the parabola to be the next approximation.

<p align="center">
<img  src='https://media.geeksforgeeks.org/wp-content/uploads/Muller-Method.png'></img>
</p>

# speed of convergence
The order of convergence of Muller's method is approximately 1.84. This can be compared with 1.62 for the secant method and 2 for Newton's method. So, the secant method makes less progress per iteration than Muller's method and Newton's method makes more progress.

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
    3. Define n <- 0, h0, h1, f0, f1, f2, Ϭ0, Ϭ1, a, b, c x3, f3, ε
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
# flow chart
<p align='center'>
<img src='https://github.com/mhwahdan/muller-method-Django/blob/main/flowchart.png'></img>
</p>

# programming languages used
- Python: for backend and API design
- HTML (Hyper text markup language): for GUI design
- Css (Cascading style sheets): for GUI design
- java script: for making GUI dynamic and connecting the GUI with the backend

# technologies
- Django
- bootstrap
- js libraries: for plotting the function graph
    - math.js
    - plotly.js
- Jquery
- AJAX
# what is Django?
Django is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.
# what is bootstrap?
Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS and (optionally) JavaScript-based design templates for typography, forms, buttons, navigation, and other interface component
# what is Jquery?
jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling, CSS animation, and Ajax. It is free, open-source software using the permissive MIT License. As of May 2019, jQuery is used by 73% of the 10 million most popular websites. Web analysis indicates that it is the most widely deployed JavaScript library by a large margin, having at least 3 to 4 times more usage than any other JavaScript library.
# what is math.js?
Math.js is an extensive math library for JavaScript and Node.js. It features a flexible expression parser with support for symbolic computation, comes with a large set of built-in functions and constants, and offers an integrated solution to work with different data types like numbers, big numbers, complex numbers, fractions, units, and matrices. Powerful and easy to use.
# what is plotly?
Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library. plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.
# what is Ajax?
Ajax (short for "Asynchronous JavaScript and XML") is a set of web development techniques that uses various web technologies on the client-side to create asynchronous web applications. With Ajax, web applications can send and retrieve data from a server asynchronously (in the background) without interfering with the display and behaviour of the existing page. By decoupling the data interchange layer from the presentation layer, Ajax allows web pages and, by extension, web applications, to change content dynamically without the need to reload the entire page. In practice, modern implementations commonly utilize JSON instead of XML.
# Program Architicture
Since our software is a web application powered by django framework, it uses the MTV(Model, Template, View) architecture
<p align='center'>
<img src='https://miro.medium.com/max/1400/0*8ZFh-CsrMi7bQG0O.jpg'></img>
</p>

# How does the program work in simple terms
when the user enters the url of the software in his browser, an HTTP get request is sent to the server hosting the application where the url is analyzed and routed to the correct view which renders the template and returns it to the client brwoser as an HTTP response which is rendered by the client browser HTTP renderer and dispalyed in the browser window.
<p align='center'>
<img src='https://github.com/mhwahdan/muller-method-Django/blob/main/screenshots/home%20page.png'></img>
</p>

After the user enters the data and clicks submission an Ajax request is sent to the server which will read the inputs, find the roots and renders the steps and draws the function as html and returns them as HTTP response which is then rendered by the browser without reloading the page.
<p align='center'>
<img src='https://github.com/mhwahdan/muller-method-Django/blob/main/screenshots/results.png'></img></p>
# what about other developers
the above example works fine for end users who just want to solve an equation, but what about other developers or enterprises that would like to use our software as a service which can be easily integrated with their softwares and systems. thats why we made a REST api for our application
# what is an API?
An application programming interface (API) is a connection between computers or between computer programs. It is a type of software interface, offering a service to other pieces of software.A document or standard that describes how to build or use such a connection or interface is called an API specification. A computer system that meets this standard is said to implement or expose an API. The term API may refer either to the specification or to the implementation.
# what is REST api?
REST has been employed throughout the software industry and is a widely accepted set of guidelines for creating stateless, reliable web APIs. A web API that obeys the REST constraints is informally described as RESTful. RESTful web APIs are typically loosely based on HTTP methods to access resources via URL-encoded parameters and the use of JSON or XML to transmit data
# how does the api work
all you need to do as devloper is sending an HTTP request to the server with the following format
```html
http://<application url>/api/muller_method/<equation>/<x0>/<x1>/<x2>/<error margin>/<maximium number of iterations>?format=<format you want to receive in>
```
example:
if you enter in your browser http://muller-calculator.herokuapp.com/api/muller_method/x%5E2-cos(x)/1/2/3/0.001/5?format=xml your will have the following result
<p align='center'>
    <img src='https://github.com/mhwahdan/muller-method-Django/blob/main/screenshots/api.png'></img>
</p>
example:
if you use the cli of your OS you will get the same outcome which can be easily handled by any program
```bash
curl http://muller-calculator.herokuapp.com/api/muller_method/x%5E2-cos(x)/1/2/3/0.001/5?format=xml
```

<p align='center'>
    <img src='https://github.com/mhwahdan/muller-method-Django/blob/main/screenshots/curl.png'></img>
</p>

# purpose of the program
submitting a pre-final project for the numerical method project in AASTMT university college of engineering department of computer engineering

# group memebers
- Moustafa mohamed wahdan
- Toqa Mohamed Hosni
- Ahmed Tarek Soliman
- Mohamed Bassel
- Mohamed Hisham El Kafrawy