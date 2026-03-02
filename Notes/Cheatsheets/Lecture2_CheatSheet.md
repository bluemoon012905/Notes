# CSE446/598 Lecture 2 Cheat Sheet (Unit 2: 2-1 to 2-4)

Use this as a searchable reference for Unit 2 style quiz/exam questions.

## Quick Search Tags
`ASP.NET` `MVC` `HTML5` `SPA` `Canvas` `SVG` `WebGL` `JavaScript async` `CORS` `EAI` `EAF` `EAM` `FEAF` `Zachman` `EAP` `TOGAF` `BPM` `BPMS` `SOAA` `ESB` `workflow` `WF` `WCF` `Dublin` `Power Platform` `Power Apps` `Dataverse` `Canvas app` `Model-driven app` `Power Automate` `Power BI` `Power Pages` `Copilot Studio`

## Lecture 2-1 Advanced Web App Architecture and Platforms

## Web Technology Evolution
- Movement from object-oriented/desktop-style architectures toward web-oriented and HTML-based architectures.
- Major progression shown in class: ASP.NET Framework apps -> MVC -> ASP.NET Core + Web API + HTML5 SPA patterns.

## ASP.NET Framework Web App (Classic) Review
Advantages:
- Easy transition for OO developers.
- Related files (`.aspx` + `.aspx.cs`) are placed together.

Disadvantages (high-yield):
- Mixes View and Controller tiers (added dependency).
- `ViewState` is weak for server farm/cloud scenarios.
- Windows-only development environment.

## HTML5 + JS Architecture
- HTML5 introduced semantic tags (`header`, `footer`, `article`, `section`), richer form inputs, graphics (`canvas`, `svg`), and media (`audio`, `video`).
- HTML5 + JavaScript + APIs can implement full client-side web apps.
- HTML5 Single Page Application is taught as a special case of MVC (single-page UI pattern).

## Canvas vs SVG vs WebGL
- `Canvas`: typical/default choice for many HTML5 apps; simple and fast.
- `SVG`: DOM-based graphics objects; flexible per-object manipulation and event handling.
- `WebGL`: best if OpenGL-style pipeline is needed; often overkill for simple 2D use cases.

## Service Calls and CORS
- JavaScript service call pattern in class is asynchronous (non-blocking caller).
- `CORS` lets server relax same-origin restrictions for cross-origin requests.
- Disabling browser security is for local testing only; production fix is proper CORS config (e.g., server/IIS/Web API side).

## Lecture 2-2 Enterprise Architecture and Business Process

## Core Definitions
- `Architecture`: fundamental organization of system components and relationships.
- `Enterprise Architecture`: architecture across one or more enterprises, including process, data/information, and technologies.
- `EAI (Enterprise Architecture Integration)`: seamless integration of architecture/process/data/technology within and across enterprises.

## Purposes of EAI
- Architecture integration framework for lifecycle management.
- Data/information integrity across systems.
- Application integration for interoperation.
- Vendor independence (business rules survive platform/vendor replacement).
- Common facade/single access interface over heterogeneous apps.

## EAF / EAM / FEAF
- `EAF`: organizing mechanism for developing/maintaining architecture descriptions (presented as NIST-based).
- `EAM`: layered enterprise model foundation.
- `FEAF`: federal implementation framework to improve interoperability, info sharing, IT planning/investment, and service/cost outcomes.

## FEAF High-Yield Structure
Eight key components include:
- Architecture Drivers
- Current Architecture (`as-is`)
- Future Architecture (`to-be`)
- Strategic Direction
- Transition Plan
- Architectural Segments
- Architectural Models
- Standards

FEAF viewpoints progress from high-level overview to detailed architecture/model mappings.

## Zachman, EAP, TOGAF
- `Zachman`: classification view (what/how/where/when/why/who; organizes artifacts like data/function/network/org/schedule/strategy).
- `EAP`: process for completing/operationalizing Zachman; focuses on data, application, and technology architectures.
- `TOGAF`: process-oriented framework that elaborates architectural development beyond artifact categorization.

## BPM and BPMS
- `BPM`: process-level EAI approach aligning process execution with business/client goals.
- BPM lifecycle (before service orientation emphasis): `Design -> Modeling -> Execution -> Monitoring -> Optimization`.
- `BPMS` key components:
- Process Engine
- Business Analytics
- Content Management
- Collaboration Tools

## SOAA and Dynamic Architecture
- SOAA uses service composition plus process/workflow-driven configuration.
- Composition manager controls application configuration via workflow specification.
- Workflow spec defines service connections and message transfer among services.
- Communication backbone is a logical view (can be bus or non-bus).
- Dynamic architecture enables reconfiguration without full system rewrite/shutdown.

## Platform Examples (Case Study Emphasis)
- `SAP NetWeaver`: enterprise services architecture and BPM modules (incl. BPEL support components).
- `Oracle SOA Suite`: visual process modeling -> BPEL generation -> dynamic deployment.
- `IBM ESB`: message/protocol/pattern adaptation, security propagation, WS-* support, monitoring/tracking.

## Lecture 2-3 Workflow Concepts and Workflow Foundation

## Why Workflow
- Adds abstraction layer for faster low-code/no-code style composition.
- Makes high-level application logic visible to architects and developers.
- Better separation between architecture/process design and low-level coding.
- Supports maintainability and integration with traditional code.

## Workflow in Architecture
- Added workflow layer for high-level composition above service/component layer.
- Can orchestrate existing components/services rather than rewriting all logic.

## WF Built-in Activities (high-yield groups)
Control flow:
- `DoWhile`, `ForEach`, `If`, `Parallel`, `ParallelForEach`, `Pick`, `PickBranch`, `Sequence`, `Switch`, `While`

Flowchart:
- `Flowchart`, `FlowDecision`, `FlowSwitch`

Messaging:
- `CorrelationScope`, `Receive`, `ReceiveAndSendReply`, `Send`, `SendAndReceiveReply`

Other important activities:
- `Persist`, `Assign`, `InvokeMethod`, `Compensate`, `TransactionScope`, `TryCatch`, `Throw`, `Rethrow`, collection ops.

## Control Flow vs Data Flow
- Control flow: sequence-style execution assumption (single processor model).
- Data flow: execution triggered when data is ready (multi-processor friendly model).
- WF supports both, plus parallel and finite state machine/event-driven models.

## WF + WCF Integration
- WF can implement business logic; WCF exposes service interfaces.
- Workflow service can expose SOAP/REST interfaces via WCF.
- Workflow services generate a `WSDL` interface.

## WF Hosting
- Self-hosting
- IIS hosting
- `Dublin` hosting (IIS/WAS extension), with emphasis on persistence + tracking/monitoring support.

## Lecture 2-4 Software Integration Using Power Platform

## Power Platform Components
- `Power Apps`: app creation.
- `Power Automate`: workflow automation.
- `Power BI`: analytics/visualization.
- `Power Pages`: external business websites.
- `Copilot Studio`: AI agent/copilot design.

## Power Apps
- Low-code app suite using apps/services/connectors/data platform.
- Connects to sources like Excel, SharePoint, Microsoft 365, Dynamics 365, SQL Server, etc.

Templates:
- `Dataverse` template: data-oriented abstraction layer (virtual cloud datastore).
- `Canvas` template: drag-and-drop UI-first with strong design freedom; broad connector use.
- `Model-driven` template: structure-driven approach around data, UI, logic, visualization; can use Power Automate and Power BI.

Model-driven vs Canvas:
- Model-driven: Dataverse-only, faster standardized generation.
- Canvas: more UI/control flexibility, broader data connectors.

## Power Automate
- Workflow service that automates actions/events across apps and services.
- Typical pattern: trigger/event + connectors + actions/conditions.
- Desktop flow path: create flow -> add/configure actions -> define I/O -> test -> link with cloud flow if needed.
- Cloud flow path: create flow -> choose trigger -> add actions/conditions.

## Power BI
- Combines services/apps/connectors to turn data into interactive insights.
- Components: Power BI Desktop, Power BI Service (SaaS), Power BI Mobile.

## Power Pages
- Low-code SaaS for secure external business websites.
- Template-driven and Bootstrap-based responsive site capabilities.

## Copilot Studio + LLM Services
- Low-code graphical environment for building AI agents.
- Agents coordinate models, instructions, context, actions, and triggers.
- Course notes tie this ecosystem to Copilot and OpenAI-based services.

## High-Yield Answer Bank

## Architecture & Integration
- EAI = seamless enterprise-level integration across architecture, process, data, and tech.
- BPM lifecycle = design -> model -> execute -> monitor -> optimize.
- Zachman classifies artifacts; TOGAF/EAP emphasize process for creating architecture.

## Workflow & WF
- WF supports both control-flow and data-flow styles.
- `SendAndReceiveReply` models asynchronous request/response with correlated activities.
- `Persist` saves workflow state for later reload/resume.
- WF service can generate `WSDL`; WCF commonly used as the service interface layer.
- Hosting options: self-host, IIS, Dublin.

## Web Architecture & HTML5
- Classic ASP.NET app couples View + Controller more tightly than MVC.
- HTML5 SPA = single-page client-heavy architecture.
- Async JS service calls are non-blocking.
- CORS is the standards-based fix for cross-origin requests.
- Canvas/SVG/WebGL choice depends on speed vs flexibility vs graphics complexity.

## Power Platform
- Power Apps = app creation.
- Power Automate = workflow automation.
- Power BI = data analysis/visualization.
- Power Pages = low-code business websites.
- Copilot Studio = low-code AI agent creation.

## Memory Traps (Common Wrong Choices)
- Don’t confuse `Zachman` (classification framework) with `TOGAF`/`EAP` (process-heavy guidance).
- Don’t assume Canvas and Model-driven apps have identical data-source constraints.
- Don’t treat disabling browser security as a deployment solution for CORS.
- Don’t assume workflow is only sequential; parallel/dataflow/event-driven constructs are core.

## 30-Second Pre-Quiz Review
- EAI = enterprise-wide integration of architecture/process/data/tech.
- FEAF includes `as-is`, `to-be`, transition planning, standards, and models.
- BPM loop: design -> model -> execute -> monitor -> optimize.
- WF: sequence/parallel/state machine + messaging + persistence.
- WF + WCF: workflow logic exposed as service (`WSDL` possible).
- Power Platform map: Apps (build), Automate (flows), BI (insights), Pages (sites), Copilot Studio (AI agents).
