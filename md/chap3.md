# Chapter 3 Agile software development


## Preface

Agile methods were created to put more on an emphasis on the end product rathar than the documentation that may be made along the way. In other words, of working long hours on documentation, the aim of the agile approach was to cut the overhead caused by the documentation and focus on development.

### Common characteristics of Agile Methods 

Every agile methods share these characteristics:
* SPecification, design, and implementation are mixed together as system specification, design documentation, and user eruiqrements are usually minimilzed to save time during development or are automatically generated. 
* Systems are usually developed in increments so that  consumers and other stakeholders can give their input during the development phase 
* Many tools are used to aid during development. Examples of such tools are tools that automatically test your code, help you make the process of designing and creating the user interface easier, etc.  

### Distinction between plan-driven processes and agile development

![Plan-based vs Agile](../images/chap/3.1_plan_vs_agile.png)

The image above outlines how plan-driven processes and agile development are different. Plan-driven processes have their own iterations within seperate stages. DOcumentation is then created to move to the next stage. However in the agile approach, the activities requirements and implementation are done at the same time.

Do note that these approaches to development are not so black-and-white; doing one does not mean you cannot do the other as generally during actual development, one approach would be mainly used but will draw some elements from the other appraoch. 

## 3.1 Agile methods


### Agile Manifesto 

The agile manifesto is a collection of principles that 
explain the reasoning behind the agile approach. These principles include: 
* Customer involvement
    * Stakeholders should give their input in all stages of the development process in order to show what components should be priorttized and give input that can be analyzed to evaluate the progress of every iteration. 
* Embrace change
    * Change is inevtiable therefore the system should be designed in such a way to relieve the potential stress caused by change. 
* Incremental delivery
    * Software should be incrementally developed in small batches to test components and allow for feedback.
* Maintain simplicity
    * Systems should be simple in where apllicable.
* People, not process
    * People's skills should be recognized and used.
 
### Product Development and Custom System Development 

Agile methods work best in two system development methodologies: 
* Product-development 
    * This is when the software is small or medium sized intended to be sold.
* CUstom-System development
    * This occurs within an organization with few stakeholders and dedicated customers that can provide ample feedback. 

Agile methods works best in these scenarios because the software created generally are not used to be integrated with others systems and there can be feedback provided about the software. 


## 3.2 Agile development techniques



### Extreme Programming 

![Plan-based vs Agile](../images/chap/3.3_XP.png)

Extreme Programming, also known as XP programming, is as what is sounds; agile methodogies taken to an "extreme" level. The goal of this development technique was to create several increments within a day and be able to test them. 

Instead of creating a document regarding requirement specifications, scnearios known as user stories are used instead. Pair programming is conducted and tests are created before the code is written. All tests must be passed succesffuly in order for the tested code to be added to the system. 

Extreme programming includes the following practices:
* Collective ownership
* COntinuous integration 
* Incremental planning
* On-site customer
* Pair programming 
* Refactoring
* SImple design
* Small releases 
* Sustainable pace 
* Test-first development 

Because of this long list of practices, generally not XP practices can be implemented ofr a project. Because of this, only a select feew are used during development depending on thier usefulness. 

### User Stories 

![User stories](../images/chap/3.5_story.png)

In order to combine requirements elicitation with development, user stories are used. User stories are what the name implies: a story on how the user interacts with the software. "Story card" are developed from these stories and focus on what stakeholders need from the software. These stories and needs will then be broken down to specific fucntionalities of the software or tasks that need to be implemented. Stories that provide the most important functionalities will be prioritzied first as they are the ones that are more useful and can help create and deliver a working version of the software earlier. 

Benefits of user stories include: 
* Stories are more relatable than documentation
* Sotries can suggest what are key requirements the software must have or do. In other words, they are helpful for requirements elicitiation

Problems of user stories include:
* Users may not go over all the reuiqrements they need from one story 
* Stories may not give a good view of the requirements 
* Terminology differ from developer and consumer as consumers are more familiar with the software
    * This may lead to consumers leaving out details when describing how they use an application as they are used to using it and may deem actions useless or forgettable. 

![Task Cards](../images/chap/3.6_task_cards.png)

### Refactoring 

Extreme programming believes that you should not design systems to cope with change. Instead, code should be refactored/improved immediately. Ractoring includes: renaming names of methods and attributes, removing duplicate code to reorganize class hierachys and relationships, replacing code that are similar to each other, etc. 

Problems of refactoring include:
* 

### Test-first Development

![Test Cases](../images/chap/3.7_test_case.png)
Extreme Programming included new ideas of testing . FOur key pricniples of testing in extremem programming is (textbook pg 81):
* test-first development / test-driven development 
* incremental test development from scenarios
* user involvement in the test development and validation
* automated testing frameworks 

In test-first development/test-driven development, tests are written first before any code is written. This will allow develoeprs to run tests alongside the development of code to preamturely find any errors with their code. This means that developers must fully understand specifications as they need to write tests that can adequtely test for potential problems. This implies that user stories/scenarios have been made as each story can provide implentation that sould be tested. Users are then also more involed in the testing process as their own data (or possibly dummy data) will be used to test the system. 

To help faciliate testing, there are automated testing tools that can be used. These tools can be used to simulate adding input and crosscheck if the end result matches the desired result. Examples of such software include Junit, Travis CI, etc. 

Problems of test-first development include:
* Incomplete tests may be made as it is impossible to test for all exceptions. In other words, tests can be written incompletely or haphazardly.
* Tests may be diffuclt to be written incrementally.  

### Pair Programming

Pair programming is the idea that programmers will dynamically develop softawre by working together. 

Benefits of paired programming include:
* Reflects the idea of collective ownership where responbility falls on the whole team rather than a single person 
* It is informal code review as two or more people have read the code which makes finding softawre errors easier and cheaper than having formal inspections of code. 
* It encrourages refactoring and discussing about the software before its implementation. 

## 3.3 Agile project management


### Scrum Agile Method 

![Scrum Sprints](../images/chap/3.9_Scrum_Sprint.png)

### Distributed Scrum

![Distributed Scrum](../images/chap/3.10_Distributed_Scrum.png)

## 3.4 Scaling agile methods


### Scaling agile methods features 



### Practical problems with agile methods



### When to use agile and/or plan-driven methods 

![Scrum Sprints](../images/chap/3.12_factors.png)

### Agile methods for large systems

![large project characteristics](../images/chap/3.13_large_agile.png)

### IBM's Agility at Scale Model

![IBM Agility at Scale model](../images/chap/3.14_IBM.png)

### Multi-team Scrum



### Agile Methods acorss Organizations


