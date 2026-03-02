# CSE446/598 Lecture 3 Cheat Sheet (Unit 3: 3-1 to 3-4)

Use this as a searchable reference for Unit 3 style quiz/exam questions.

## Quick Search Tags
`Antigravity` `Agent Manager` `Mission Control` `Planning mode` `Fast mode` `review policy` `workspace` `orchestration` `choreography` `BPEL` `WS-BPEL` `partnerLink` `partnerLinkType` `WSDL` `portType` `invoke` `receive` `reply` `sequence` `flow` `switch` `while` `pick` `scope` `faultHandlers` `catchAll` `correlation` `cache` `OutputCache` `fragment caching` `data caching` `Cache` `CacheDependency` `SqlCacheDependency` `absolute expiration` `sliding expiration` `recommendation` `collaborative filtering` `content-based filtering` `user-based` `item-based` `cold start` `ethics`

## Lecture 3-1 Antigravity (Agent-Based Development)

## Core Tooling Concepts
- Antigravity combines traditional code editing with agent orchestration.
- `Agent Manager / Mission Control` supports spawning and coordinating multiple agents asynchronously.
- Compared to chatbot-only IDE flow (linear/synchronous), agent model supports parallel task execution across workspaces.

## Key Configurations
- Terminal execution policy options include `Always Proceed`, `Agent Decides`, and `Request Review`.
- Review policy options include agent-driven, agent-assisted, review-driven, and custom.

Terminal execution policy mapping (exact wording often tested):
- `Always Proceed` = agent never asks for review.
- `Agent Decides` = agent decides when to ask for review.
- `Request Review` = agent always asks for review.
- "super agent performs review only" = not listed as a terminal execution policy in lecture.

Recommended in slides:
- Balanced review policy where agent decides and asks for human approval when needed.

## Conversation Modes
- `Planning mode`: deeper planning/research, more artifacts and task-structure output.
- `Fast mode`: direct execution for smaller/localized tasks.

## Mission Control High-Yield Features
- Inbox tracks conversations/task status/approvals/artifacts.
- Workspace selection allows multi-project work.
- Playground allows scratch tasks before promoting to workspace.
- Browser subagent can browse, click, scroll, inspect logs, parse page content, and capture evidence.
- Agents directly interact with developers through conversation.
- Agents can directly interact with browser via browser subagent.

## Use Cases Covered
- News extraction/highlights.
- Generate dynamic website (Python + Flask) from natural-language requirements.
- Iterative refinement via follow-up prompts.
- Generate unit tests for UUT with mocks/stubs and run verification.

## Unit Testing Terminology (from examples)
- `Stub`: state verification oriented.
- `Mock`: behavior verification oriented.
- Agent can generate mocks/stubs to isolate dependencies and validate UUT behavior.

Unit testing use-case count point:
- In the provided `order_service.py` example, two external dependencies are mocked/stubbed:
- `InventoryService`
- `PaymentGateway`
- => expected mock/stub count in quiz wording: `2`.

## Lecture 3-2 Business Process and Execution (BPEL)

## Business Process vs Workflow
- Business process: sequence/collection of business activities by humans/machines.
- Workflow: composition/flow-management technology that specifies execution order of components/services.
- Workflow frameworks describe business process precisely and support automated execution.

## Orchestration vs Choreography
- `Orchestration`: central coordinator controls involved services; strong fit for private process integration.
- `Choreography`: no central coordinator; peers coordinate with each other; fit for public/distributed collaboration.
- BPEL is presented as orchestration-style.

Orchestration wording in Antigravity context:
- Human user orchestrates by instructing Agent Manager and coordinating agent tasks.
- It does not mean terminal auto-changing agent behavior.

## BPEL Positioning
- `BPEL/WS-BPEL`: enterprise process composition language centered on service interaction.
- Defines partner services, data, control flow, partner conversation, and error handling/recovery.
- Uses SOAP/WSDL ecosystem concepts and exposes process as a composite web service.

## BPEL Basic Activities
- `<invoke>` call a service.
- `<receive>` wait for incoming message.
- `<reply>` respond to synchronous call.
- `<assign>` data/variable manipulation.
- `<throw>` raise fault.
- `<catch>` handle fault.
- `<wait>` delay.
- `<terminate>` end process.

## BPEL Constructs
- `<sequence>` sequential execution.
- `<flow>` parallel execution.
- `<switch>` branching.
- `<while>` loop.
- `<pick>` event/timeout style “first available” branch.
- `<partnerLink>` partner definition.
- `<variable>` variable declaration.

## Communication in BPEL
- Two-way synchronous: request + block wait for response.
- Two-way asynchronous: request + callback later; caller must expose service endpoint (`portType`) for callback.
- In partner link model, synchronous style commonly maps to one role while asynchronous callback style commonly maps to two roles.

## WSDL in BPEL (quiz-critical)
- Each BPEL process is typically a composite web service with its own WSDL.
- Process WSDL defines how clients/services invoke the process.
- Process may expose multiple `portType`s (e.g., client-facing + callback-facing).
- `partnerLinkType` is an extension element used in BPEL process WSDL to map partner roles to port types.

Partner link quiz-critical details:
- A `partnerLink` is defined between the BPEL process and an interacting party.
- Valid patterns:
- client <-> BPEL process
- service <-> BPEL process
- Not defined as direct link between two external clients.
- Not typically modeled as direct link between two external services "used by BPEL" without the BPEL process as the partner in that link.

Where `partnerLinkType` is defined:
- In the WSDL file of the BPEL process (with `plnk` extension), not in client code and not necessarily in partner services' WSDL files.

## Variables, Scope, and Fault Handling
- BPEL variables maintain process/intermediate state.
- Variable declaration types: `messageType` (WSDL message), `element` (XML schema element), `type` (XML schema simple type).
- `scope` enables local variables, local correlations, compensation handlers, and event handlers.
- Fault handling uses `faultHandlers` with `catch` and optional `catchAll`.

WSDL synchronous interface recognition (very common MCQ):
- If a `portType` operation has both `<input .../>` and `<output .../>`, it defines request/response interface (synchronous two-way interface) in WSDL.
- Example pattern:
- `<portType ...><operation ...><input .../><output .../></operation></portType>`
- This is interface definition in WSDL, not a BPEL call statement by itself.

## Lecture 3-3 Message-Based Integration
- `Lecture3_3.pdf` in this repository is corrupted/unreadable (broken xref/trailer), so content could not be extracted in this workspace.

## Lecture 3-4 Web Caching and Recommendation

## Why Caching
- Motivated by locality, slow/costly data access, repeated user interests, and resilience (data availability even if source is down).
- Caching improves performance but adds cost/complexity; choose what to cache based on business logic.

## Caching Types
- `Output caching`: cache fully rendered page.
- `Fragment caching`: cache part of page (e.g., user control).
- `Data caching`: cache application data objects for business logic.
- `Multilayer caching`: combine output + fragment + data + API/service caching.

## Output/Fragment Caching Essentials
- ASP.NET directive example: `<%@ OutputCache duration=\"10\" varybyparam=\"None\" %>`.
- `varybyparam` creates separate cache entries for different input parameter values.
- Client-side cache location can be specified (tradeoff: speed vs freshness/control).
- Fragment caching can be placed on user controls (`.ascx`) for partial-page performance.

## Data Caching with ASP.NET Cache Classes
- `System.Web.Caching.Cache` provides managed cache lifecycle and shared app-level availability.
- Useful operations: `Add`, `Insert`, `Get`, `Remove`.
- Supports absolute expiration (`DateTime`), sliding expiration (`TimeSpan`), priorities, eviction callbacks, and dependencies.
- `CacheDependency` can bind cache entries to file/db/key/other dependencies and auto-invalidate on change.
- `SqlCacheDependency` supports DB-backed invalidation scenarios.

## Recommendation Systems
- Recommendation = information filtering that predicts rank/rating/preference/purchase probability.
- Goal in business context: increase sales and value.

Caching vs recommendation:
- Caching stores recent data.
- Recommendation ranks/selects likely useful items.
- They reinforce each other: cache data can feed recommendation inputs/features, and recommendation signals can guide cache replacement priorities.

## Recommendation Strategies
- Collaborative (social) filtering.
- Content-based filtering.
- User-profile filtering.
- Situation-aware filtering.

## Collaborative Filtering Concepts
- User-based CF: infer from similar users.
- Item-based CF: infer from similar items.
- Model-based CF: learned/statistical model.
- Memory-based CF: direct use of observed ratings.
- Rating-oriented vs ranking-oriented CF are distinct optimization perspectives.

## Quality Criteria for Recommendations
- Accuracy.
- Diversity.
- Non-hot-spot coverage.
- Avoid cold-start failure.
- Real-time performance.

## Legal and Ethics (high-yield)
- Access rights/copyright still apply to cached and recommended data.
- Do not cache/recommend illegal content.
- Privacy and consent concerns for profile/history/email/social/phone-derived recommendations.
- Integrating multiple “public” sources can still raise legal/ethical issues.

## High-Yield Answer Bank

## Unit 3 Architecture/Process
- BPEL = orchestration-centric process composition.
- Choreography has no central coordinator.
- Composite process typically has its own WSDL and partner mappings.
- SWF three-party model (from lecture slide):
- Activity developer writes/registers activities.
- Workflow developer writes/registers workflow/decider.
- Client is end user side consumer of workflow execution.
- Quiz answer: SWF workflow client is for `End user`.

## BPEL Mechanics
- Core activity trio in many processes: `receive -> invoke(s) -> reply`.
- `sequence` = ordered; `flow` = parallel.
- `partnerLinkType` connects roles to `portType`s.
- `scope` controls local variables/handlers/correlation boundaries.
- BPEL language composition style = `orchestration`.
- `partnerLink` anchors around BPEL process interactions (client-BPEL or service-BPEL).
- `partnerLinkType` location = BPEL process WSDL.
- WSDL `portType` with input+output = synchronous interface definition.

## Antigravity Quiz Bank
- Antigravity does not work exactly like a plain chatbot IDE; key difference is multi-agent async orchestration and Mission Control.
- Agents are used for:
- implementation planning
- direct interaction with developer conversation
- code generation
- direct browser interaction through browser subagent
- Terminal policies: never ask / decide / always ask.
- Orchestration in Antigravity quiz context = instructing and coordinating through agent manager.

## Rapid Q/A (Exam Style)
- Q: In SWF, workflow client is designed for?
- A: End user.
- Q: BPEL composition style?
- A: Orchestration.
- Q: Where is `partnerLinkType` defined?
- A: WSDL file of the BPEL process.
- Q: `partnerLink` can be defined between?
- A: Client and BPEL process, or service and BPEL process.
- Q: WSDL `portType` + `operation` + `input` + `output` defines?
- A: Synchronous interface in WSDL.
- Q: In unit-testing use case, how many mock/stub dependency interfaces in given program?
- A: 2.
- Q: Antigravity terminal policies supported?
- A: Always Proceed / Agent Decides / Request Review.
- Q: “Antigravity works the same as plain LLM chatbot IDE.”
- A: False.

## Caching + Recommendation
- Output vs fragment vs data caching differ by granularity.
- `CacheDependency` is key for correctness under data changes.
- Recommendation systems are filtering/ranking engines, not just “recent item lists.”
- Collaborative filtering can suffer from cold start.

## Memory Traps (Common Wrong Choices)
- Orchestration and choreography are not identical in control model.
- `flow` is not sequential execution.
- Caching and recommendation are complementary, not substitutes.
- Faster response from caching is not free; staleness/invalidations must be managed.
- Publicly viewable data is not automatically legal/ethical for unrestricted caching/recommendation reuse.

## 30-Second Pre-Quiz Review
- Antigravity: agent orchestration + conversation-driven coding + policy modes.
- BPEL: orchestration, WSDL/partner links, activity constructs, faults/scopes.
- BPEL process is usually a composite web service.
- Cache layers: output, fragment, data, multilayer.
- `Cache` + `CacheDependency` handle expiration and invalidation.
- Recommendation: collaborative/content/profile/situation-aware with accuracy/diversity/performance/privacy tradeoffs.
