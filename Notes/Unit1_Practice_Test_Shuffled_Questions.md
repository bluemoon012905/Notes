# Unit 1 Practice Test (Shuffled) - Questions

Source pool: `1-1to1-3`, `1-4to1-5`, and `unit1test` (39 total).

## Q1
Which HTTP method is most frequently used for RESTful service calls?

A. DELETE
B. GET
C. HEAD
D. POST
E. PUT

## Q2
A key concept of RESTful service is to

A. hide data representation from client.
B. remove computation from the service.
C. hide computation from client.
D. hide both data representation and computation from client.

## Q3
A system is a collection of interconnected components defined at these levels: (Select all that apply)

A. architecture.
B. interface.
C. behavior.
D. requirement.

## Q4
The endpoints in ASMX and in WCF services are different at programming language level. However, they are the same at the service level. Their interfaces are both described in

A. HTTP
B. SOAP
C. WCF
D. WSDL

## Q5
What template cannot be used for developing a client to consume a WCF service?

A. ASP .Net Windows form application
B. ASP .Net Web site application
C. Console application
D. WCF

## Q6
What is NOT a part of an endpoint?

A. Service address
B. Service’s binding protocol
C. Service contract
D. Service hosting

## Q7
When we convert a SOAP service to a RESTful service in WCF, what must be removed?

A. The .cs file that implements the interfaces
B. The hosting service
C. The attribute [WebGet]
D. The endpoint

## Q8
What concept of service orientation involves most detail?

A. Service-Oriented Architecture
B. Service-Oriented Design
C. Service-Oriented Computing
D. Service-Oriented Development

## Q9
When creating a Web API using ASP .Net Web Application template without using WCF template, what files need to be created or modified?

A. Service.cs file
B. IService.cs file
C. configuration file
D. Global.asax file
E. controller file

## Q10
What is NOT a part of a WCF endpoint?

A. messageType
B. Service address
C. Service’s binding protocol
D. Service contract

## Q11
Which statements are correct in the course grading policy? Select all that apply.

A. The lowest assignment score will be dropped.
B. Two lowest quiz scores will be dropped automatically.
C. Two lowest unit test scores will be dropped automatically.
D. The lowest exam score will be dropped automatically.

## Q12
In the layers of behaviors in WCF services:

(1) What layer is in charge of inspecting and taking actions on incoming and outgoing messages? Choose one: Endpoint behaviors

(2) What layer is in charge of implementing a stateful service? Choose one: Service behaviors

## Q13
What separator is used for separating the RESTful service method name and the parameter in the default parameter passing style?

A. ?
B. /
C. &
D. Space

## Q14
What level of behaviors deals with creating multiple instances of a service to process requests?

A. Service behaviors
B. Endpoint behaviors
C. Operation behaviors.
D. Client behaviors

## Q15
What data formats does a WCF RESTful service support to return a set of data items? Select all that apply.

A. BigTable
B. JSON
C. RSS
D. Array of strings

## Q16
In RESTful service development using WCF template, we must define the UriTemplate if the service has

A. no parameter
B. one parameter
C. two parameters
D. More than two parameters

## Q17
A key idea of RESTful services is to focus on the

A. computing process to automate the Web.
B. data and resources without computing support.
C. data and resources with computing support invisible to the clients.
D. WSDL standard interface for interoperability.

## Q18
What binding protocol is used for exposing a service to be a RESTful services, instead of SOAP services?

A. BasicHttpBinding
B. WsHttpBinding
C. NetPeerTcpBinding
D. WebHttpBinding

## Q19
What are the main reasons of paradigm shift from object orientation to service orientation? Select all that apply.

A. Internet provisioning of services
B. Code migration among subsystems
C. Interoperability among different platforms
D. Architecture-level improvement

## Q20
What is the benefit of using asynchronous calls, instead of using synchronous calls?

A. Asynchronous calls take shorter time to complete.
B. Asynchronous calls do not block the callers.
C. Asynchronous calls work for RESTful services, while synchronous calls work for SOAP services only.
D. Asynchronous calls are easier to implement.

## Q21
A RESTful service can return

A. one resource only.
B. a set of resources.
C. a leave node of a resource tree only.
D. the root node of a resource tree only.

## Q22
How are asynchronous communications implemented in WCF? Select all that apply

A. A two-way call from client to server.
B. A two-way call from client to server, and another two-way call from server to client.
C. A one-way call from client to server, and an independent call back from the server.
D. A pair of one-way calls from the client to server.

## Q23
To create a complete URI, we often need to combine a base URI address, a parameter name, and a parameter value. What is the proper way to create a complete URI?

A. Use library classes such as Uri and UriTempalte to create the complete URI.
B. Use string appending operation, e.g., completeUri = baseUri + parameterName + paramaterValue;
C. Use appending and casting, e.g., completeUri = (Uri) baseUri + parameterName + paramaterValue;
D. Use completeUri = Convert.ToUri(baseUri + parameterName + paramaterValue);

## Q24
What part of the C# code is used for defining the service contract in the WCF endpoint?

A. class
B. interface
C. method
D. implementation

## Q25
The BindByPosition(baseUri, parameterValue) method in UriTemplate

A. puts the parameterValue in the place where the parameter name is given in the URI template.
B. appends baseUri and parameter name.
C. appends baseUri and parameterValue.
D. downloads data from the complete URI, which is baseUri + parameterValue.

## Q26
Which layer in the WCF Channel Stack is responsible for a shape change?

A. Transport Channel
B. CompositeDuplexBindingElement
C. HTTP over TCP
D. SOAP over HTTP
E. IInputChannel/IOutputChannel

## Q27
In what WSDL element is the “address” part of a WCF endpoint contained?

A. binding
B. port
C. portType
D. operation

## Q28
What is the application level protocol employed in RESTful services?

A. HTTP
B. SOAP over HTTP
C. TCP
D. TCP over IP

## Q29
Given the following piece of code:

using var channel = GrpcChannel.ForAddress("https://localhost:5001");
var client =  new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(new HelloRequest {Name = "GreeterClient"});

The service call in this code is

A. one-way synchronous call
B. two-way synchronous call
C. one-way asynchronous call
D. two-way asynchronous call

## Q30
Which of the following statements are correct? Select all that apply.

A. SOAP services focus on "performing".
B. SOAP services focus on "result".
C. RESTful services focus on "performing".
D. RESTful services focus on "result".

## Q31
A sidecar in a service mesh is

A. a service implementation.
B. a proxy to a microservice service.
C. container that contains a communication protocol.
D. a hosting service.

## Q32
How can asynchronous communications between a client and a server be implemented in WCF? Select all that apply.

A. Use two one-way calls.
B. Use two two-way calls.
C. Use a one-way call and then a two-way call.
D. Use a two-way call and then a one-way call.

## Q33
Service mesh in microservice platforms is a configurable infrastructure layer that makes

A. the translation possible between a RESTful service and multiple microservices.
B. the integration possible between service instances and a database.
C. data storage among service instances flexible, reliable, and fast.
D. communication between service instances flexible, reliable, and fast.

## Q34
The composition architecture style choreography allows all the services to communicate with

A. a central process only.
B. each other.
C. no any partner.
D. hosting worker only.

## Q35
The workflow that transforms input to output refers to software integration at the level of

A. architecture
B. interface
C. behavior
D. system

## Q36
You are given the operation contract definition of a RESTful service:

[WebGet(UriTemplate = &quot;add2/{x}/{y}&quot;]

What is the correct way of embedding the parameters into the URI?

A. add2?x=7&x=12
B. add2/7/12
C. add2(x=5, y=12)
D. add2(5, 12)

## Q37
The synchronous communication between the client and server requires

A. the client to block-wait for the response.
B. an independent callback after each request.
C. a second call to retrieve the data.
D. no return value.

## Q38
The composition architecture style orchestration requires all the services to communicate with

A. a central process only.
B. each other.
C. no any partner.
D. hosting worker only.

## Q39
The standards and protocols SOAP, WSDL, UDDI and XML are mostly related to

A. Web services
B. RESTful services
C. Remote procedure call
D. Multithreading

