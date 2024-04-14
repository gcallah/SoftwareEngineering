# An Introduction to Agile and DevOps Development

## The Background

### The Ford / Taylor Factory Model

#### Taylorism

[Frederick Winslow Taylor](https://en.wikipedia.org/wiki/Frederick_Winslow_Taylor)

![A machinist at a Taylorist
plant](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Musterarbeitsplatz.png/500px-Musterarbeitsplatz.png)

All intelligence was in management and resesarch departments: the workers were human machines.

#### Ford

![Ford assembly
line](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Ford_assembly_line_-_1913.jpg/440px-Ford_assembly_line_-_1913.jpg)

* Huge batches (economy of scale)
* Push model of production
* Don't respond to customer preferences: shape them!

Ford: "Any customer can have a car painted any color that he wants so long as it is black."

These approaches were taken to be the best practice for production, so naturally managers tried to apply it to software.

The result was:

### The Waterfall Model

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Waterfall_model.svg/700px-Waterfall_model.svg.png" width="600" height="400">

"The waterfall development model originated in the manufacturing and
construction industries, where the highly structured physical
environments meant that design changes became prohibitively expensive much
sooner in the development process." -- Wikipedia

All of the intelligence was supposedto reside in the "analysts," while the programmers merely knew howto type those
requirements out in their chosen programming language.

The programmers never met the users.

Building a new Walmart warehouse vs. building a new piece of software.

If we need to "stamp out" new software, what do we do?

[Failed waterfall projects](https://en.wikipedia.org/wiki/List_of_failed_and_overbudget_custom_software_projects)

Some failed project stories.

Contrast with working with option traders.

Why did the Waterfall Model fail so often and so spectacularly?

* Users often don't know what they want until they see a product.
* The competitive environment changes as the product is being developed.
* The legal environment changes as the product is being developed.
* The natural environment changes as the product is being developed.
* Wordy specifications written in English don't translate nicely to commands in a software language.
* Programmers who are expected to be mere typing machines will not understand what the requirements mean, since they
    lack context.


## The Alternative

How did an alternative to the waterfall model arise? It will be useful to follow some history to understand what
happened.

### Toyota

Interestingly, the way forward from these rigid production methods was actually pioneered in the auto industry, by the
Japanese company Toyota, and its
[Toyota Production System](https://en.wikipedia.org/wiki/Toyota_Production_System), one of the earliest examples of
[lean production](https://en.wikipedia.org/wiki/Lean_manufacturing).

Notable features:

* Pull rather than push system.
* All employees contribute ideas, not just "plant engineers" or managers.
* Catch defects early.
* Work in small batches.
* Limit work in progress.

Note: small batch foods are based on the same "small batch" idea!

### UNIX

Development on the UNIX operating system began at AT&T in 1969. It is almost certainly the world's most successful
software project: it was developed very cheaply at first, by only a handful of developers, has been in continuous
development every since, and today, UNIX and its descendants, such as Linux, MacOS, Andriod, and iOS, dominate the world
of operating systems.

What accounts for the success of UNIX?

* Deliver an MVP (Minimum Viable Product) as soon as possible.
* Get user feedback.
* Just add the features users really want.
* Develop incrementally: create multiple small tools that each do a small job.

[Knuth vs. McIlroy](https://matt-rickard.com/instinct-and-culture)


### Lean

Mary Popendieck was a product development manager at 3M, a company which had adopted lean manufacturing and product
development. When she was put in charge of the software project, she was shocked at the idea that the team should begin
by writing a huge requirements document. She miss used to product developers building simple versions of an idea getting
feedback from customers right away. She and her husband, Tom adapted this approach to software development, pioneering
the concept of [Lean software development](https://en.wikipedia.org/wiki/Lean_software_development).

### Agile

At roughly the same time as Lean was being developed, a group of developers, often from the UNIX world, were developing
the concept of [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development).

Key agile principles:

* Individuals and interactions over processes and tools
* Working software over comprehensive documentation
* Customer collaboration over contract negotiation
* Responding to change over following a plan

[Agile Manifesto](https://agilemanifesto.org)

I would say that Lean and Agile are basically two different names for the same approach to developing software.

### DevOps

<img src="http://www.thedevopscourse.com/static/devops/devops_inter.png" height="300" width="600">

By the early 2000s, many development teams had embraced agile and lean processes. But operations was lagging behind.

Operations dreaded new releases of software. Often, such releases meant many months of system crashes and late night
pages.

But some forward thinking operations people decided that, rather than fighting agile development, they would embrace
agile operations. Patrick Debois in 2009 organized a conference to bring such operations people together with
agile developers. Since he was bringing together DEVelopment and OPerations, he called the conference... ?

[DevOps](https://en.wikipedia.org/wiki/DevOps)

The name caught on and was applied to an entire movement.

I have suggested a definition of DevOps as "Agile carried over to operations."

In the early 2000s, participants at a conference were shocked to hear that one group was releasing software *several
time per day*.

By 2013, Amazon was pushing new code into production *every 11 seconds*.

The heuristic: "If releasing new software versions is painful... keep doing it, often, until it is easy!"

(Helped by small batches, automated testing, version control, easy rollbacks.)

### Chaos Engineering

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Mandel_zoom_00_mandelbrot_set.jpg/644px-Mandel_zoom_00_mandelbrot_set.jpg" height="300" width="400">

Amazon East crash of 2011: brought down Foursquare and Reddit, among other major sites.

Netflix kept running.

Why? [Chaos Monkey](https://en.wikipedia.org/wiki/Chaos_engineering)!

See Nassim Taleb's book [Antifragile](https://en.wikipedia.org/wiki/Antifragile_%28book%29).

## Practices

* Continuous Integration
* Continuous Delivery
* Incremental Development (small batches)
* Infrastructure-as-Code
* Automated testing
* Test-Driven Development
* Limit work in progress
* Kanban
* Version control
* Automated builds
* Automated deploys

Note: Continuous Integration means **first** integrate all of the parts of 
a system, and then gradually refine them, while making sure they still work together. Quite the opposite of
how Summerville defines it!

## Demo

Let's do some actual Agile / DevOps work!

## Other Material

[The Modern Software Engineering Way of Work](http://www.thedevopscourse.com/devops/work)


## Quiz

1. What company was at the forefront of lean production?
a. Google
b. Ford
c. Microsoft
d. Toyota

2. In Agile, the primary measure of progress is?
a. requirements documents
b. diagrams
c. working software
d. a progress report sent to the customer

3. In software development, an MVP refers to a?
a. Most Valuable Programmer
b. Modular Variable Programming
c. Multiply Vector Probability
d. Minimum Viable Product

4. Waterfall projects often fail because?
a. It is very difficult to fully understand what a program needs to do without building it.
b. The competitive environment may change.
c. The regulatory environment may change.
d. All of the above.

5. The Waterfall Model works well when one is?
a. Breaking new ground with a product.
b. Solving a brand new problem.
c. Replicating an existing solution.
d. All of the above.

6. DevOps essentially arose from applying ____ principles to ____.
a. waterfall, development
b. operations, testing
c. agile, operations
d. lean, development

7. DevOps could be defined as?
a. Agile applied to operations
b. A total waste of time.
c. A return to Waterfall methods.
d. Developing operations to a greater extent.

8. In Taylorism, process input from workers was?
a. encouraged
b. the most important part of design
c. not wanted
d. All of the above.

9. When practicing Continuous Integration, we should?
a. First integrate our components, and then build them.
b. Integrate our components as soon as we are done building them.
c. Make sure their is continuity in our integrated components.
d. All of the above.

10. Why were many operations people fearful of Agile develpment?
a. They disliked the word "agile."
b. In the past, releases had been high-stress events for them.
c. They just didn't like developers.
d. None of the above.
