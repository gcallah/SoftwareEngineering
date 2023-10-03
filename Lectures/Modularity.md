
## What is modularity?
### Dividing software into distinct components with a single purpose.
* Examples from a car.
* What represents a component in software:
	* A function
	* An class
	* A file (module)
	* A directory (package)
	* An executable program
		* UNIX versus IBM 360
* What's a "single purpose"? Can you say what the component does in a short sentence? This will repeat at lower and lower levels. Example:
	* The engine powers the car.
		* The pistons are where the power is generated.
			* The spark plugs produce sparks.
			* The fuel injector sends fuel to the spark plug.
		* The crankshaft transmits the power to the wheels.


### *Narrow interfaces* between components

* Components should have the minimum number of connections possible.
	* Could this be zero?
	* Think of your headphones.
	* Contrast that with:

![[Screenshot 2023-10-03 at 10.45.43 AM.png]]
### *Strong cohesion* within components

Don't have one component that "reads the file, removes the newlines, and substitutes 'St.' for 'Street'."

##  Why is it important?

* We can divide our work into teams more easily.
* Each time has a smaller chance of breaking an other team's work.
* We can release modules confidently, knowing that if the interface hasn't changed, things should work. (Think of getting some higher end headphones!)
* That means we can release new features rapidly.

## How do we practice it?

A great technique is to code top-down. **Do not** worry about the details of components to start.
