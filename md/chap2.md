# Chapter 2 Software processes

## Preface 

The software process is a set of activities used in order to create a software system. 
As stated in the previous chapter, all software processes, no matter how different they are, 
involve these four parts (textbook pg. 44): 
* **Specification**
* **Design and implementation**
* **Validation**
* **Evolution**

In this chapter, we will explain three software processes that can be visualized as a model. Note that in practice, development will most likely not solely follow one model; instead it will use a mixture of some elements from each model.



## 2.1 Software process models

The three generic software processes are:
* **the waterfall model**
* **incremental development**
* **integraton and configuration**

### Waterfall model

![Waterfall Model](../images/chap/2.1_waterfall_model.png)

As seen in the image above, the waterfall model has 5 main stages (textbook pg.47):
* **Requirements definition**
* **System and software design**
* **Implementation and unit testing**
* **Integration and system testing**
* **Operation and maintenance**

The waterfall model is a straight forward model where the software process follows a linear pattern; 
in order for it to advance to the next stage, the prior stage must be completed. 
Only after the "operation and maintence" step is completed can the project go to earlier steps as it sees fit. 
The waterfall model is commonly known as a **plan-driven** model as the requirement specification phase and the development phase are distinct from each other; 
the requirement specification phase must be completed before the development of the product begins.
As a result, one drawback of this model is that it should only be used if the problem 
is fully understood in order to limit potential changes to customer needs and wants. 

However, this strict step-by-step processes and lack of foreseight into 
potential future changes does not mean that this mdoel is useless. 
Because each stage must be fully completed and understood, this model is very beneficial 
for large projects that multiple teams from multiple sperate locations work on as workflow 
would be more efficient if each team was on the same page/understanding as each other. 

### Incremental development 

![Incremental development](../images/chap/2.2_incremental_development.png)

Incremental development is a softwware process model that is as what its name implies; 
the process is conducted in multiple increments. In a way, this model is more natural as 
it is similar to how people actually solve problems. 
If the problem is not something that be solved in one instance, we work toward the answer through 
multiple steps of iteratations of attempts. 
The first step of this process involves outlining the initial product specification. 
A first draft of the product is then made and at the same time, prodcut feedback is taken. 
This feedback will allow for another round of  product specification in which the previous 
product specification is built ontop of and an an intermediate product version is made. 
This process repeats until a final version is made that meets all the requirements. 

Incremental development can be either plan-driven or agile-developed. 
The difference between the two is that the increments are pre-determined in the plan-driven version 
whereas in the agile-development, later increment versions are determined by what new or 
changed prodcut specifications are made. 

Inceremental development has three main benefits:
* Cost of development due to change is lowered as change is accounted for in this process. In other words, you are expecting change to happen; any new changes will not undermine previous versions to the popint where the product and other such documentation must be redone.
* Important features are usually prioritzied first in order to have usable software. This in turn makes a working version (although not necesarrily one that is complete and meets all the requirements) of the product can be deployed earlier 
* With faster delivery, customers can comment on the product earlier.

Incremental development has two main drawbacks:
* The process is not clearly visible as mutliple versions of the product may be happening at the same time and thier may not be one "main" version. It will also cost a lot in order to create a lot of versions of the product.
* Adding multiple changes may degrade the original system structure as code must be refactored to better optimize it or maybe everything work with the new changes. Think of this like the Telephone game. In this game there are multiple people lined up; on one end, one person tells the person adjacent to him a message.  This person must repeat the message to the other person who is adjacent to him until the message goes down the line to the last person on the opposite end but each person cannot ask the prior person to repeat the message. Each person could alter the message until when the final person receives the message, that message may be completely different and may not make sense in the end. Similarly, every added change to the software would require the development team to make sure the original features still work and the new features was intergrated properly to the prior version to create the new version.


### Intergration and configuration

Integration and configuration is the process of using already existing code. Instead of building from the ground up, the already existing code would be modified and added to wahtegver prototype development has produced so far.  

Examples of when this model is used for is for (textbook pg. 52): 

* Stand-alone applications
* Collections of objects that are bundled into a package that will be used for a framework 
* Web services that have to follow a standard 

![Reuse oriented](../images/chap/2.3_reuse_oriented.png)

**Reuse-Oriented software engineering** is based around this software process model and has 5 main steps:
* Requriements specifciation 
* Software discovery and evaluation 
* Refinement of requirements 
* Configuration and adpation of software
  * If the software is an application system, configure it
  * If the software is a component(s), adapt the components and develop new ones if neccessary to prepare for integration.
* Integrate the discovered system into the current protoype/iteration

Benefits | Cons
------------ | -------------
Because less new software is made, development costs are lowered| Reusing code instead of creating from scratch may mean that those reused code may not work with future addtions of features. 
Faster deployment of software | May have to worry about liscnesning of borrowed code which may increase cost


## 2.2 Process activities

![Requirement Engineering Process](../images/chap/2.4_requirements_engineering_process.png)

In this section, we will discusse what the four process activities (specification, development, validation, and evolution) entail. 

### Software Specification


Software specification, also known as the requirement engineering process, is the stage where developers will figure out and outline what features are required by stakeholders. The end result of this process is to create documentation that stakeholders understand and add upon to aid developers know what features they (the developers) need to create to meet the needs of the client. Software specification can be visualized as the top 3 bubbles in figure 2.4. 

Note that stakeholder requirements and whereas ystem requirements are not interchangeable with each other;this difference will be explained in a later section. 


The requirements engineering process is composed of three main stages (textbook pg 55):
* **Requirements elicitation and analysis**
* **Requirements specification**
* **Requirements validation**

### Software design and implementation

Software design and implementation can be visuzalized as the layer that is comprised of the bottom 3 rectangles in figure 2.4. 


![Design Process](../images/chap/2.5_design_process_model.png)

Figure 2.5 outlines the process in which a software design is made. Design inputs are the foundation to the software as they are the required parts that the software must either include or adhere to. Platform information is the information regarding what other software systems the product will interact with. Examples of these other systems include operating system, database, and other applications. Requirement specifications is the specification of what the system will require and what functionalities the clients want in the product. Data descriptions are what datasets the product might rely on.

After taken into consideration the inputs, developers will then consider four designs to make (textbook pg 57): 
* **Architectural design**
* **Database design**
* **Interace design**
* **Component selection and design**


### Software validation

Softare validation, also known as V & V (Verification and validation), is used to test whether or not the current version of the software meets the demands of the consumers and any such specification. This process may involve using dummy/fake data or specific test cases to simulate usage of the software.

![Stages of testing](../images/chap/2.6_stages_of_testing.png)

In a simple software testing process, there are 3 main stages (textbook pg 59):
* **Component testing**
  * In this phase, individual functions are components are tested as single parts; in other words each component is tested isolated from each other. 
* **System testing**
  * The whole entire system will be tested to make sure each component works with each other.
* **Customer testing**
  * The consumer tests the system to give their opinions in order to see if the system meets the consumer's needs.

![Testing phases](../images/chap/2.7_testing_phases.png)

Figure 2.7 shows a more complicated form of testing that is mostly used in plan-driven software processes such as in the waterfall model. 

### Software evolution

Software evolution is also known as software maintence as software has to be flexible; changes to requirements are consistent and software must be able to evolve or be maintainable to address those changes. Figure 2.8 outlines the thought process that occurs during software evolution.  

![Software Evolution](../images/chap/2.8_software_system_evolution.png)

## 2.3 Coping with change

It should be apparent that change is inevitable. We see in the last two decades physical techonology has evolved and advanced greatly and software is the same as well; with gfrowing times, the needs and wants of people change. Software projects will eventually need to be reworked to account for different business changes, new technologies and techniques being used, and the obsolescence of platforms. 

Change therefore is expensive as it means the current working version must be redone in order to meet the new changes. Two ways to reduce the cost of reworking include:
* **Change anticipation**
* **Incremental delivery**

### Prototyping 

![Prototype development](../images/chap/2.9_prototype_development.png)

### Incremental delivery

![Incremental delivery](../images/chap/2.10_incremental_delivery.png)

## 2.4 Process improvement



### Two approaches to process improvement and changes 



### Cyclical Process

![Process improvement](../images/chap/2.11_process_improvement_cycle.png)

### The Software Engineering Institute (SEI) Model of Process Capability Maturity

![Capability Maturity Model](../images/chap/2.12_capability_maturity_levels.png)
