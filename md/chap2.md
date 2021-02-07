# Chapter 2 Software processes

## Preface 

The software process is a set of activities used in order to create a software system. 
As stated in the previous chapter, all software processes, no matter how different they are, 
involve these four parts (textbook pg. 44): 
* **Specification**
* **Design and implementation**
* **Validation**
* **Evolution**

In this chapter, we will explain three software processes that can be visualized as a model. 



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
* Adding multiple changes may degrade the original system structure as code must be refactored to better optimize it or maybe everything work with the new changes. Think of this like the Telephone game. In this game there are multiple people lined up; on one end, one person tells the person adjacent to him a message.  This person must repeat the message to the other person who is adjacent to him until the message goes down the line to the last person on the opposite end. Each person could alter the message until when the final person receives the message, that message may be completely different and may not make sense in the end. Similarly, every added change to the software would require the development team to make sure the original features still work and the new features was intergrated properly to the prior version to create the new version.


### Intergration and configuration

![Reuse oriented](../images/chap/2.3_reuse_oriented.png)

## 2.2 Process activities


### Software Specification

![Requirement Engineering Process](../images/chap/2.4_requirements_engineering_process.png)

### Software design and implementation

![Design Process](../images/chap/2.5_design_process_model.png)

![Stages of testing](../images/chap/2.6_stages_of_testing.png)

### Software validation



### Software evolution

![Testing phases](../images/chap/2.7_testing_phases.png)

![Testing phases](../images/chap/2.8_software_system_evolution.png)

## 2.3 Coping with change


### Two approaches to reducde costs of rework



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
