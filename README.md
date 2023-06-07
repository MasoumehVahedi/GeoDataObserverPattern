# GeoDataObserverPattern

## Project description

We have a controller that has a geo-data source, which is a library with a user-friendly interface. This geo-data source constantly provides points, lines, and areas at a high frequency. Our goal is to design an access library that allows multiple consumers, such as various map-renderers within the same process, to access this geo-data source. To achieve this, we implement the observer pattern.

Here is an overview of the project description:

**Architecture Concept**: I devise an architecture concept that outlines the overall structure of the access library and how it interacts with the geo-data source. This concept will define the roles and responsibilities of the different components involved.

**Component View**: I create a visual representation of the system's component view. This illustrates the different components of the access library, their relationships, and how they interact with the geo-data source. The component view provides a high-level overview of the system's structure.

**UML Diagram**: I develop a UML diagram that captures the design of the access library and its integration with the geo-data source. The UML diagram depicts the classes, interfaces, and their relationships, showcasing the observer pattern implementation and how it facilitates communication between the geo-data source and the consumers.

By sketching the access library's architecture concept, creating a component view, and visualizing the design through a UML diagram, we will establish a clear understanding of the system's structure and enable seamless access to the geo-data source for multiple consumers in a concurrent environment.


Th  **observer** pattern is a behavioral design pattern that allows an object, called the subject, to maintain a list of its dependents, called observers, and notify them automatically of any state changes. 

**Qt** is a popular framework for building graphical user interfaces, provides support for implementing the Observer pattern through its signals and slots mechanism.
