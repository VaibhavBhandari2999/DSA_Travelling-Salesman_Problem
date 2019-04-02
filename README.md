# DSA_Travelling-Salesman_Problem
Part of the Data Structures and Algorithms course. Uses Simulated Annealing and 2-opt.

Initially a greedy algorithm is used, just to provide a representative of the (often) most inefficient path.
Then the simulated Annealing algorithm is used and its improvement over greedy algorithm is shown.

In simulated annealing, we define an initial temperature, often set as 1, and a minimum temperature, on the order of 10^-4. 
The current temperature is multiplied by some fraction alpha and thus decreased until it reaches the minimum temperature. 
For each distinct temperature value, we run the core optimization routine a fixed number of times. The optimization routine 
consists of finding a neighboring solution and accepting it with probability e^(f(c) – f(n)) where c is the current solution 
and n is the neighboring solution. A neighboring solution is found by applying a slight perturbation to the current solution. 
This randomness is useful to escape the common pitfall of optimization heuristics — getting trapped in local minima. By potentially 
accepting a less optimal solution than we currently have, and accepting it with probability inverse to the increase in cost, the 
algorithm is more likely to converge near the global optimum. Designing a neighbor function is quite tricky and must be done on a 
case by case basis, but below are some ideas for finding neighbors in locational optimization problems.

Then , 2 -opt is used to optimize the path even more.

This is the mechanism by which the 2-opt swap manipulates a given route:

   2optSwap(route, i, k)  
  
+       1. take route[0] to route[i-1] and add them in order to new_route  
+       2. take route[i] to route[k] and add them in reverse order to new_route  
+       3. take route[k+1] to end and add them in order to new_route  
+       return new_route;  

The cities are taken from the http://www.math.uwaterloo.ca/tsp/ and more specifically http://www.math.uwaterloo.ca/tsp/world/countries.html.

The time taken for the program to run increases exponentially for the 2-opt algorithm based on number of cities, but it improves the path
exponentially as well.

[Here](https://www.youtube.com/watch?v=UGGPZnAUjPU) is a great visualization of 2 opt and how it works.  
[This video](https://www.youtube.com/watch?v=q6fPk0--eHY) shows Simulated Annealing and Greedy Algorithm
