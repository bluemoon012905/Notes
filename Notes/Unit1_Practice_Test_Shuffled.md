# Unit 1 Practice Test (Shuffled)

Source pool: all questions from `1-1to1-3`, `1-4to1-5`, and `unit1test` (39 total).

## Questions

### Q1
What are the main reasons of paradigm shift from object orientation to service orientation? Select all that apply.
- Internet provisioning of services
- Code migration among subsystems
- Interoperability among different platforms
- Architecture-level improvement



### Q2
A key concept of RESTful service is to

hide data representation from client.


remove computation from the service.


- hide computation from client.

- hide both data representation and computation from client.



### Q3
When creating a Web API using ASP .Net Web Application template without using WCF template, what files need to be created or modified?

- Service.cs file
- IService.cs file
- configuration file
- Global.asax file
- controller file



### Q4
What is NOT a part of an endpoint?
- Service address
- Service’s binding protocol
- Service contract
- Service hosting



### Q5
The composition architecture style orchestration requires all the services to communicate with

- a central process only.


each other.


no any partner.


hosting worker only.


### Q6
You are given the operation contract definition of a RESTful service:

[WebGet(UriTemplate = &quot;add2/{x}/{y}&quot;]

What is the correct way of embedding the parameters into the URI?

- add2?x=7&x=12
- add2/7/12
- add2(x=5, y=12)
- add2(5, 12)



### Q7
What binding protocol is used for exposing a service to be a RESTful services, instead of SOAP services?




BasicHttpBinding


WsHttpBinding


NetPeerTcpBinding

- WebHttpBinding



### Q8
Given the following piece of code:

using var channel = GrpcChannel.ForAddress("https://localhost:5001");
var client =  new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(new HelloRequest {Name = "GreeterClient"});

The service call in this code is

- one-way synchronous call
- two-way synchronous call
- one-way asynchronous call
- two-way asynchronous call

### Q9
The workflow that transforms input to output refers to software integration at the level of
- architecture
- interface
- behavior
- system



### Q10
Which statements are correct in the course grading policy? Select all that apply.
- The lowest assignment score will be dropped.
- Two lowest quiz scores will be dropped automatically.
- Two lowest unit test scores will be dropped automatically.
- The lowest exam score will be dropped automatically.



### Q11
In what WSDL element is the “address” part of a WCF endpoint contained?
- binding
- port
- portType
- operation



### Q12
How are asynchronous communications implemented in WCF? Select all that apply
- A two-way call from client to server.
- A two-way call from client to server, and another two-way call from server to client.
- A one-way call from client to server, and an independent call back from the server.
- A pair of one-way calls from the client to server.



### Q13
In the layers of behaviors in WCF services:

(1) What layer is in charge of inspecting and taking actions on incoming and outgoing messages? Choose one: Endpoint behaviors

(2) What layer is in charge of implementing a stateful service? Choose one: Service behaviors

Endpoint behaviors
Service behaviors



### Q14
Which of the following statements are correct? Select all that apply.
- SOAP services focus on "performing".
- SOAP services focus on "result".
- RESTful services focus on "performing".
- RESTful services focus on "result".



### Q15
To create a complete URI, we often need to combine a base URI address, a parameter name, and a parameter value. What is the proper way to create a complete URI?

- Use library classes such as Uri and UriTempalte to create the complete URI.


Use string appending operation, e.g., completeUri = baseUri + parameterName + paramaterValue;


Use appending and casting, e.g., completeUri = (Uri) baseUri + parameterName + paramaterValue;

- Use completeUri = Convert.ToUri(baseUri + parameterName + paramaterValue);



### Q16
What is the benefit of using asynchronous calls, instead of using synchronous calls?



Asynchronous calls take shorter time to complete.


- Asynchronous calls do not block the callers.


Asynchronous calls work for RESTful services, while synchronous calls work for SOAP services only.


Asynchronous calls are easier to implement.




### Q17
A key idea of RESTful services is to focus on the
- computing process to automate the Web.
- data and resources without computing support.
- data and resources with computing support invisible to the clients.
- WSDL standard interface for interoperability.



### Q18
In RESTful service development using WCF template, we must define the UriTemplate if the service has

no parameter


one parameter


- two parameters


- More than two parameters




### Q19
The composition architecture style choreography allows all the services to communicate with

a central process only.


- each other.


no any partner.

- hosting worker only.



### Q20
The synchronous communication between the client and server requires
- the client to block-wait for the response.
- an independent callback after each request.
- a second call to retrieve the data.
- no return value.



### Q21
What data formats does a WCF RESTful service support to return a set of data items? Select all that apply.
- BigTable
- JSON
- RSS
- Array of strings



### Q22
What part of the C# code is used for defining the service contract in the WCF endpoint?
- class
- interface
- method
- implementation



### Q23
A RESTful service can return
- one resource only.
- a set of resources.
- a leave node of a resource tree only.
- the root node of a resource tree only.



### Q24
The endpoints in ASMX and in WCF services are different at programming language level. However, they are the same at the service level. Their interfaces are both described in
- HTTP
- SOAP
- WCF
- WSDL



### Q25
The BindByPosition(baseUri, parameterValue) method in UriTemplate

- puts the parameterValue in the place where the parameter name is given in the URI template.
- appends baseUri and parameter name.
- appends baseUri and parameterValue.
- downloads data from the complete URI, which is baseUri + parameterValue.



### Q26
Service mesh in microservice platforms is a configurable infrastructure layer that makes
- the translation possible between a RESTful service and multiple microservices.
- the integration possible between service instances and a database.
- data storage among service instances flexible, reliable, and fast.
- communication between service instances flexible, reliable, and fast.



### Q27
Which layer in the WCF Channel Stack is responsible for a shape change?
- Transport Channel
- CompositeDuplexBindingElement
- HTTP over TCP
- SOAP over HTTP
- IInputChannel/IOutputChannel



### Q28
What is the application level protocol employed in RESTful services?
- HTTP
- SOAP over HTTP
- TCP
- TCP over IP



### Q29
A sidecar in a service mesh is
- a service implementation.
- a proxy to a microservice service.
- container that contains a communication protocol.
- a hosting service.



### Q30
What level of behaviors deals with creating multiple instances of a service to process requests?
- Service behaviors
- Endpoint behaviors
- Operation behaviors.
- Client behaviors



### Q31
What separator is used for separating the RESTful service method name and the parameter in the default parameter passing style?
- ?
- /
- &
- Space



### Q32
The standards and protocols SOAP, WSDL, UDDI and XML are mostly related to
- Web services
- RESTful services
- Remote procedure call
- Multithreading



### Q33
How can asynchronous communications between a client and a server be implemented in WCF? Select all that apply.
- Use two one-way calls.
- Use two two-way calls.
- Use a one-way call and then a two-way call.
- Use a two-way call and then a one-way call.


### Q34
What is NOT a part of a WCF endpoint?
- messageType
- Service address
- Service’s binding protocol
- Service contract



### Q35
A system is a collection of interconnected components defined at these levels: (Select all that apply)
- architecture.
- interface.
- behavior.
- requirement.



### Q36
What template cannot be used for developing a client to consume a WCF service?
- ASP .Net Windows form application
- ASP .Net Web site application
- Console application
- WCF



### Q37
Which HTTP method is most frequently used for RESTful service calls?
- DELETE
- GET
- HEAD
- POST
- PUT



### Q38
When we convert a SOAP service to a RESTful service in WCF, what must be removed?
- The .cs file that implements the interfaces
- The hosting service
- The attribute [WebGet]
- The endpoint



### Q39
What concept of service orientation involves most detail?
- Service-Oriented Architecture
- Service-Oriented Design
- Service-Oriented Computing
- Service-Oriented Development



## Answer Key

### Q1
- Internet provisioning of services
- Interoperability among different platforms

### Q2
- hide computation from client.

### Q3
- configuration file
- Global.asax file
- controller file

### Q4
- Service hosting

### Q5
- a central process only.

### Q6
- add2/7/12

### Q7
- WebHttpBinding

### Q8
- two-way asynchronous call

### Q9
- behavior

### Q10
- Two lowest unit test scores will be dropped automatically.
- The lowest exam score will be dropped automatically.

### Q11
- port

### Q12
- A one-way call from client to server, and an independent call back from the server.
- A pair of one-way calls from the client to server.

### Q13
- (1) Endpoint behaviors
- (2) Service behaviors

### Q14
- SOAP services focus on "performing".
- RESTful services focus on "result".

### Q15
- Use library classes such as Uri and UriTempalte to create the complete URI.

### Q16
- Asynchronous calls do not block the callers.

### Q17
- data and resources with computing support invisible to the clients.

### Q18
- two parameters
- More than two parameters

### Q19
- each other.

### Q20
- the client to block-wait for the response.

### Q21
- JSON
- RSS

### Q22
- interface

### Q23
- a set of resources.

### Q24
- WSDL

### Q25
- puts the parameterValue in the place where the parameter name is given in the URI template.

### Q26
- communication between service instances flexible, reliable, and fast.

### Q27
- CompositeDuplexBindingElement

### Q28
- HTTP

### Q29
- a proxy to a microservice service.

### Q30
- Service behaviors

### Q31
- ?

### Q32
- Web services

### Q33
- Use two one-way calls.
- Use a one-way call and then a two-way call.

### Q34
- messageType

### Q35
- architecture.
- interface.
- behavior.

### Q36
- WCF

### Q37
- GET

### Q38
- The endpoint

### Q39
- Service-Oriented Development

