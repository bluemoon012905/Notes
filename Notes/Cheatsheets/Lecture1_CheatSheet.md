# CSE446/598 Lecture 1 Cheat Sheet (Unit 1: 1-1 to 1-5)

Use this as a searchable reference for Quiz 1 / Unit 1 style questions.

## Quick Search Tags
`endpoint` `ABC` `WSDL` `SOAP` `REST` `HTTP` `WebHttpBinding` `async` `sync` `one-way` `request-reply` `duplex` `service behaviors` `endpoint behaviors` `operation behaviors` `instancing` `concurrency` `UriTemplate` `BindByPosition` `orchestration` `choreography` `service mesh` `sidecar` `Global.asax` `controller` `configuration`

## Lecture 1-1 Core Foundations

## Course / Grading (from quiz items)
- Two lowest unit test scores are dropped automatically.
- Lowest exam score is dropped automatically.

## Software Integration Levels
- `Architecture`: high-level organization and composition.
- `Interface`: how components/services connect and communicate.
- `Behavior`: workflow transforming input to output.

Quiz wording:
- “workflow that transforms input to output” => `behavior` level.
- System levels (select all) => `architecture`, `interface`, `behavior`.

## Service Orientation Terms
- `Service-Oriented Development (SOD)` = most detailed/practical level among SOA/SOC/SOD style choices.
- Paradigm shift reasons toward service orientation:
- Internet provisioning of services.
- Interoperability across different platforms.

## SOAP vs REST Mindset
- SOAP services focus on `performing` operations (computation-oriented).
- RESTful services focus on `result` / resources (data-oriented).
- Use SOAP more for heavy computation tasks.
- Use REST more for resource/data retrieval/manipulation tasks.

## Lecture 1-2 Raw Services, Self-Hosting, Endpoints

## API and Service Basics
- A service is an `active API` (must be hosted to run).
- API interfaces may be language-dependent or language-independent.

## WCF Endpoint (ABC)
- `A` = Address
- `B` = Binding protocol
- `C` = Contract

Not part of endpoint:
- `Service hosting`
- `messageType`

## Contract Definition in C#
- Service contract is defined in an `interface`.

## WSDL Facts
- ASMX and WCF differ at language/programming level, but both are described at service level using `WSDL`.
- In WSDL, endpoint address is in the `port` element.

## Proxy / Consumption
- If WSDL is unavailable, proxy generation is not available in the typical SOAP workflow.

## Lecture 1-3 Advanced Service Development

## Communication Models
- `Request-reply` => two-way synchronous communication.
- `One-way` => asynchronous, no direct return in same call.
- `Duplex` => asynchronous with return path/callback pattern.

## Synchronous vs Asynchronous
- Synchronous: caller blocks waiting for response.
- Asynchronous: caller does not block.

Main benefit of async:
- `Non-blocking caller`.

## WCF Async Implementation Patterns (quiz-critical)
Correct patterns include:
- A pair of one-way calls.
- One-way client->server call + independent callback (or equivalent return channel).

## Channel Stack / Shape Change
- `CompositeDuplexBindingElement` handles channel shape change (important MCQ item).

## Binding Choices
- For REST endpoints in WCF use `WebHttpBinding`.

## Behavior Layers (quiz-critical)
- `Service behaviors`: instancing, concurrency, stateful service concerns.
- `Endpoint behaviors`: inspect and act on incoming/outgoing messages.
- `Operation behaviors`: per-operation manipulation/serialization details.

Common tested mappings:
- “create multiple instances” => `Service behaviors` (instancing).
- “inspect incoming/outgoing messages” => `Endpoint behaviors`.
- “implement stateful service” => `Service behaviors`.

## Instancing vs Concurrency
- `Instancing`: how service object instances are created/used.
- `Concurrency`: how many threads/requests can execute concurrently.

## Lecture 1-4 REST + Microservice Concepts

## HTTP in REST
- Application-level protocol for RESTful services: `HTTP`.
- Common methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`.

High-frequency test point:
- Most frequently used REST method: `GET`.

POST vs PUT:
- `POST`: append/create subordinate resource.
- `PUT`: replace or create at target URI.

## REST Key Concept
- REST focuses on resources/data while hiding server-side computing details from client.
- RESTful service can return a `set of resources`.

## SOAP to REST in WCF
Typical conversion steps include:
- Add REST attributes like `[WebGet]` where needed.
- Remove SOAP endpoint access from config (quiz answer often simplified as “remove endpoint”).
- Use HTTP URI-based access (instead of SOAP proxy-style).

## URI Templates and Parameters
Default parameter-passing style often tested:
- method and query separated by `?`
- Example: `add2?x=7&y=12`

Path-style template example:
- `[WebGet(UriTemplate = "add2/{x}/{y}")]`
- Correct URI: `add2/7/12`

Building full URI safely:
- Use `Uri` + `UriTemplate` classes (not string concatenation).
- `BindByPosition(baseUri, ...)` fills values into template placeholders by position.

## Composition Styles
- `Orchestration`: services communicate through a central process.
- `Choreography`: services communicate with each other directly.

## Microservices / Service Mesh
- A service mesh is infrastructure that makes service-to-service communication flexible/reliable/fast.
- `Sidecar` = proxy adjacent to a microservice instance.

## Lecture 1-5 RESTful Development and Cases

## Building Web API Without WCF Template
Key files to create/modify:
- `configuration` file/class (route mapping)
- `Global.asax`
- `controller` file

Typical route pattern:
- `api/{controller}/{id}`

## gRPC Recognition (from quiz style)
Code with `await client.SayHelloAsync(...)` indicates:
- `two-way asynchronous call`.

## High-Yield Quiz Answer Bank

## Endpoint / WSDL / Binding
- WCF endpoint = Address + Binding + Contract.
- NOT endpoint parts: `Service hosting`, `messageType`.
- Contract defined in C# `interface`.
- ASMX/WCF interface description at service level: `WSDL`.
- WSDL element containing address: `port`.
- REST exposure binding in WCF: `WebHttpBinding`.

## Communication / Behaviors
- Synchronous => client block-waits.
- Async benefit => non-blocking caller.
- Async WCF patterns => pair of one-way calls; or one-way + callback channel.
- Shape change layer => `CompositeDuplexBindingElement`.
- Multiple instances/stateful control => `Service behaviors`.
- Message inspection => `Endpoint behaviors`.

## REST / HTTP / URI
- REST app-level protocol => `HTTP`.
- Frequent REST method => `GET`.
- REST can return set of resources.
- REST key idea => resource/data oriented; computing support hidden from client.
- SOAP->REST conversion in WCF => remove SOAP endpoint access.
- URI separator in default query style => `?`
- For `UriTemplate = "add2/{x}/{y}"` => `add2/7/12` style.
- Create URIs with `Uri` + `UriTemplate`; use `BindByPosition` for placeholder substitution.

## Architecture Style
- Orchestration => central coordinator only.
- Choreography => peers communicate with each other.

## Memory Traps (Common Wrong Choices)
- Async does NOT mean “always faster”; it mainly means “non-blocking”.
- REST is not “no computation”; computation is present but hidden behind resource interface.
- Don’t build URIs by raw string concatenation for template-based patterns.
- WCF is not a client app template choice when asked which template cannot be used to consume WCF service.

## 30-Second Pre-Quiz Review
- Endpoint = `ABC`.
- Contract code = `interface`.
- WSDL address element = `port`.
- Sync = blocking; async = non-blocking.
- One-way/duplex = async; request-reply = sync.
- REST in WCF = `WebHttpBinding` + URI/HTTP access.
- REST common verb = `GET`.
- URI query separator = `?`.
- Orchestration = central; choreography = peer-to-peer.
- Service behavior = instancing/state; endpoint behavior = message inspection.
