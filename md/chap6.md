# Chapter 6 Architectural design

## Preface 

Architectural design involves understanding how the overall software system 
should be structured and organized. The end goal of this process is to show 
how the system had main components with underlying relationships between each other. 

Figure 6.1 is an example of system architecture. The diagram is an abstract 
representation of a packing robot. Notice how there are five main components: 
a vision component to see objects, an object identification system to see that 
it is packing the correct items, an arm/gripper group to pick up the object, 
a packaging group to select what items should be packed, and a conveyor component 
to move objects delivered to the robot.

### Architecture in small vs architecture in large

Software architectures can be designed under two levels of abstraction: 

* **Architecture in the small**: Concerned with architectures of individual programs and how they can be broken down into multiple components
* **Architecture in the large**: Concerned with architectures of enterprise systems or systems compromised of other systems. 



### Advantages of documenting and designing software architecture

There are three main advantages of explicitly designing and documenting software architecture: 

* **Stakeholder communication**
  * The documentation of the architecture can be used to discuss among stakeholders of varying interests to improve the end product. 
* **System analysis**
  * Starting on designing the architecture early would require analysis. 
  * Because analysis is onde early on, a decision on whether the project should continue or how it can be improved can be made as the analysis will show if the system can meet important requirements such as maintainability, performance, and reliability. 
* **Large-scale reuse**
  * Architectural models can be reused for other similar systems. 

### Architecutral Representations

System architectures can be represented using block diagrams (shown in Figure 6.1)

Each box in the diagram represents a component and boxes within boxes represent 
components that have their subcomponents. Arrows show the direction in which data is passed. 

Box diagrams are useful because they are simple to create and show an overview 
of the system structure; however, these diagrams have been criticized for not 
showing the relationships between components nor do they show any properties of the components. 

### Usages of Architectural model

There are two ways that an architectural model is used (textbook pg. 170):
* **As a way of encouraging discussions about the system design**
  * Stakeholders can discuss high-level descriptions of the system.
  * Stakeholders can understand an abstract view and discuss  the system as a whole instead of needing to focus on specific details/implementation 
  * System architectures identify important components that need to be developed, allowing managers to divide the work appropriately. 
* **As a way of documenting an architecture that has been designed**
  *  A model can show the connections between components and what interfaces will they use. This can then be used as a baseline that developers will use to understand the product and see avenues in which the product can be evolved. 

## 6.1 Architectural design decisions

The architectural design varies depending on what type of system you are 
creating, the background of the system architect, and what are the requirements. 
Figure 6.2 shows some questions that system architects must consider. 

An important aspect of architectural design is figuring out what parts of 
architecture can be reused as systems in the same domain generally have similar 
architectures. Architectural patterns/syles answer that question of reuse; they 
are an overview of a type of architecture and show how that particular pattern/style 
can be applied to different types of software systems.

Picking an architectural style depends on which non-functional requirements of the system to prioritize:
* **Performance**
  * Architecture should minimize critical operations within a small number of localized components (meaning that the components are used in the same device rather than distributed over a network). 
  * This would involve using larger, more grouped components rather than finer components. By doing this, communication between components is minimized as most interactions would occur within the component. 
* **Security**
  * A layered architecture should be used with the most important assets are in the lowermost level and are protected with the most security validation.
* **Safety**
  * Architecture should have safety-related capabilities in a small group of components.
* **Availability**
  * Architecture should be designed so that there are multiple copies of components (or in other words redundant components)  to allow such components to be replaced and updated. 
* **Maintainability**
  * Architecture should use finer components that can easily be changed and replaced. 

## 6.2 Architectural views

There are two main issues with using the architectural model to be used as 
a basis for discussion or used as a document to outline implementation and design (textbook pg 173):
* What views or perspectives are useful when designing and documenting a system's architecture?
* What notations should be used for describing architectural models? 

It should self-explanatory that it is impossible to show every relevant information 
about the system's architecture in a single diagram as it would be too messy. 
Instead, the system architecture should be split into different modules or views. 
Figure 4.3 shows four fundamental architectural views that should be made:

* **Logical view**: shows what objects/object classes/entities should be in the system
* **Process view**: shows what processes occur in runtime
* **Development view**: shows how the development can be broken down into components
* **Physical view**: shows the hardware for the system and how components may be dis

## 6.3 Architectural patterns

Arhecteural patterns/styles are means to represent and reuse knowledge; they are 
stylized descriptions of what is considered good design practices. Patterns should 
include information about their strengths and their weaknesses and can be represented 
with graphical or tabular descriptions. 

Figures 6.4 and 6.5 describe the Model-View-Controller pattern which is used 
to manage interactions in web-based systems. 

### Layered architecture 

The Layered Architecture pattern is a way to separate system functionalities 
into layers where each layer relies only on services from the layer directly 
underneath it. This architecture works well with incremental development as if 
an interface of the layer changes, only that layer is affected. 

Figure 6.7 describes the Layered Architecture pattern more. 

Figure 6.8 is an example of using the Layered Architecture pattern with 4 layers. 

Figure 6.9 is an example of the practical usage of 4 layered architecture 
patterns for a system; this figure outlines what components are in each layer. 

### Repository architercture

The Repository architecture shows how data may be shared between components. 
The premise of this approach is to use a singular main repository that will store 
all the necessary data; every component that needs access to the data will then 
connect with the repository to fetch and edit the data.

Figure 6.10 describes the Repository architecture approach.

Figure 6.11 is an example of a Repository architecture used for an IDE. 

### Client-server architecture 

The Client-Server pattern is used to organize and show how components use and 
process data over a distributed system. 

Figure 6.12 describes the Client-server architecture approach.

The major components of the system are:
* A set of servers that have services that are used by the components. 
* A set of clients that rely on these services. typically clients will work on different computers and thus be using the services concurrently.
* A network that allows the clients to access the services. 

Figure 6.13 is an example of a Client-Server architecture. 

### Pipe and filter architecture

Pipe and Filter patterns are used to show how inputs are processed to form outputs during runtime. 

Figure 6.14 describes the pipe and filter architecture. Inputs are "filtered" 
to the right component that will "pipe" it into its correct destination. 

Figure 6.15 shows an example of the Pipe and Filter architecture. 

## 6.4 Application architectures

Application systems are designed to meet organizational or business needs. 
Many businesses in the same sphere have commonalities; for example phone companies 
all need systems that can connect calls and uphold their networks. because of this, 
application systems often have similar architectures.  Generic application 
architecture is an architecture for a software system that can be configured and 
adapted to create a system with specific requirements. 

### Usages of application architectures 

Models of application architectures can be used in several ways (textbook pg. 185):
* As a starting point for the architectural design process
* As a design checklist 
* As a way of organizing the work of the development team
* As a means of assessing components for reuse 
* As a vocabulary for talking about application

There are two main types of generic application architectures:
* **Transaction processing systems**
  * Transaction processing applications center around a database. These application process requests from users to receive information or to update the information. 
  * Examples include reservation systems and e-commerce systems 
* **Language processing systems**
  * Language processing systems are systems that express intentions as a language.
  * Examples include compilers and command interpreters. 

### Transaction processing systems 

Transactions are considered any sequence of operations that has a clear goal 
(for example retrieving flight times from NYC to LA).  Transaction processing 
systems are systems where users make asynchronous requests for services; 
figure 6.16 is an overview of a transaction processing system. 

Figure 6.17 is an example of a transaction processing system. 


### Information systems

Information systems typically use a layered architecture and are a type of 
transaction-based system. The interactions within these systems are generally 
database transactions. The layers include a user interface, user communications, 
information retrieval, and a system database. Figure 6.18 shows a general example 
of an information system. 

Figure 6.19 is an example of an information system. 

Figure 6.20 is an example of a web-based information system. 

### Language processing systems 

Language processing systems accept a language as an input and generates a 
representation of that language. These systems may have an interpreter that 
will act in a specific way depending on the instructions contained in the 
language that is being processed. 

For example, a compiler is a form of a language processing system. 
A compiler is composed of the following parts:
* **Lexical analyzer**: takes input language and converts them to something the compiler can understand 
* **Synmnbol table**: holds information about entities (variables, class names, etc.)
* **Syntax analyzer**: checks the syntax of the language being translated
* **Syntax tree**: represents the program being compiled 
* **Semantic analyzer**: uses information from the symbol tabke and the syntax tree to check if the input language is correct 
* **Code generator**: generates machine code from the syntax tree

Figure 6.20 is an overview of a language processing system. 

Figure 6.21 shows an example of how a repository architecture is used for a language processing system. 

Figure 6.22 shows an example of a pipe and filter computer architecture. 


