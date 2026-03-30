Design Document v1.2
ABN Lookup Automation Tool
1. Project Overview

This project is a Python-based command line tool designed to automate retrieval of publicly available ABN details from the ABN Lookup website using browser automation. The tool accepts an ABN from the user, performs a search, extracts relevant entity information, formats the result into structured data, and optionally saves both the result and a screenshot of the results page.

The purpose of this tool is not only to meet the technical requirements of the project brief, but also to demonstrate structured reasoning around software design, operational thinking, user care, reproducibility, and maintainability. The tool is intended to be simple, clear, and reproducible rather than overly complex or highly optimized.

This version of the design refines the original concept by introducing clearer separation of concerns between user interaction, lookup workflow, browser automation, persistence, and logging. The updated direction also confirms that SQLite is the preferred persistence mechanism over MongoDB for this version of the project, as it better supports simplicity, portability, and low operational overhead.

2. Problem Statement

A small automation tool is required to extract ABN data from the publicly available ABN Lookup webpage, structure the returned information, and save it in a form that can be reused, reviewed, or exported later.

The tool must:

accept an ABN as user input
automate the browser interaction needed to search that ABN
extract key business details from the returned page
format the result as structured data
optionally save the result to a database
optionally capture and save a screenshot of the results page
handle invalid lookups and automation failures gracefully
provide enough logging and feedback to support both the user and the developer/operator
3. Objectives

The main objectives of the tool are:

Build a working browser-automated ABN lookup process using Python and Playwright.
Design the application in a modular and industry-aligned way rather than as a single procedural script.
Persist relevant lookup data using a lightweight and reproducible database.
Implement meaningful logging and error handling suitable for a small operational tool.
Support user-friendly CLI interaction and clear export behavior.
Package the final application in Docker to improve reproducibility and setup consistency.
4. Scope
In scope
CLI-based interaction
browser automation using Playwright
lookup of a user-supplied ABN
extraction of key result fields
optional screenshot capture to directory
optional structured export such as JSON
persistence of lookup metadata and structured results in SQLite
error handling for invalid inputs, timeouts, missing selectors, and storage failures
logging of important operational events
Docker packaging and setup documentation
Out of scope for v1
web UI
multi-user authentication
remote database services
screenshot binary storage inside the database
advanced analytics/reporting
API-based lookup integration
concurrent workers or queue-based processing

This keeps the first version small enough to build and explain clearly while still reflecting realistic design practices.

5. Design Principles

This tool will be designed around the following principles:

Simplicity over unnecessary complexity
The project should remain small, understandable, and easy to operate. Technologies or patterns that increase overhead without solving a real problem will be avoided.

Reproducibility
The application should be easy to run again in a clean environment. This includes dependency management, predictable folder structure, and eventual Docker packaging.

Separation of concerns
Different responsibilities should be isolated into different modules so the codebase is easier to understand, maintain, and evolve.

User empathy
The tool should provide clear prompts, readable results, and helpful error messages. Logs should serve developers and operators; terminal feedback should serve the end user.

Operational awareness
The design should consider what needs to be logged, what needs to be stored, and what should happen when components fail.

6. Technology Choices and Rationale
Python

Python is the primary implementation language because it is suitable for scripting, automation, CLI interaction, JSON handling, and rapid development. It also aligns with the developer’s current skill level and prior project experience. The previous university submission demonstrates working familiarity with user input handling, procedural logic, class use, and basic data manipulation, while also showing where stronger modular structure is now needed.

Playwright

Playwright will be used for browser automation because the project brief specifically requires browser automation, and Playwright provides strong documentation, browser control features, selector handling, waiting behavior, and screenshot support. It is also well suited to deterministic automation flows and later debugging.

SQLite

SQLite has been selected as the persistence layer for v1. Although MongoDB was initially considered due to its natural fit with JSON-like structures and optional screenshot-related expansion, SQLite is the better fit for this project because:

it avoids the overhead of running and packaging a separate database service
it supports structured records well for this use case
it is portable and easy to reproduce
it is easier to explain and test in a student submission
screenshots do not need to be stored in the database itself

The decision reflects a deliberate tradeoff: avoid adding moving parts unless they solve a genuine problem.

Docker

Docker will be used in the final packaging stage to make the tool easier to reproduce across environments. The goal is to containerize the application once the local workflow is stable, rather than trying to solve packaging too early.

7. Data Storage Decision

A key design decision in v1.2 is to store only structured lookup data and metadata in the database, while treating screenshots and exports as filesystem artifacts.

This means:

SQLite stores structured result data and lookup metadata
JSON exports are written to an export directory
screenshots are written to a screenshots or export directory
the database may store a path, filename, or flag indicating whether a screenshot was created

This avoids the need to convert images into blobs or build an image storage workflow that the project brief does not require. It also keeps the persistence model simple and easier to maintain.

8. Proposed Architecture

The application will follow a layered design with clear module boundaries.

8.1 Entry Point Layer

This layer starts the application and wires the components together.

Responsibilities

load configuration
initialize logging
initialize database connection/repository
initialize Playwright adapter
initialize lookup service
pass control to the CLI layer

This file should remain minimal and should not contain business logic, SQL, or selector handling.

8.2 CLI Layer

This layer is the user-facing terminal interface.

Responsibilities

display menu and prompts
collect user input
validate basic menu selections
pass actions to the service layer
display results and errors in user-friendly language

This layer should not know how Playwright works internally and should not directly run SQL.

8.3 Service Layer

This layer owns the business workflow of the tool.

Responsibilities

receive validated ABN input from the CLI
coordinate the lookup process
call the Playwright adapter
normalize the extracted result
instruct storage to persist data
trigger optional export or screenshot operations
return a clean result object to the CLI

This layer is important because it acts as the stable centre of the application. If a later version replaces Playwright with another integration method, the rest of the application should require minimal change.

8.4 Adapter Layer

This layer wraps the external browser automation tool.

Responsibilities

launch browser
navigate to ABN Lookup page
submit ABN search
wait for expected elements
extract required result fields
capture screenshot when requested
translate automation outcomes into structured results or errors

This should be the only part of the application that knows about Playwright selectors, browser launch options, or page timing details.

8.5 Storage Layer

This layer manages persistence and retrieval.

Responsibilities

initialize SQLite database and schema
insert lookup records
retrieve prior records by ABN or recent history
store metadata such as timestamps, status, export path, and screenshot path

The storage layer should hide SQL details from the service and CLI layers.

8.6 Logging and Configuration Layer

This layer centralizes application-level settings and operational events.

Responsibilities

configure logger format and output
manage log level
define configurable paths and defaults
support reproducibility through predictable setup
9. Proposed File Structure
abn_lookup/
├─ main.py
├─ cli.py
├─ services/
│  └─ lookup_service.py
├─ adapters/
│  └─ playwright_adapter.py
├─ storage/
│  ├─ db.py
│  └─ repository.py
├─ utils/
│  ├─ logger.py
│  ├─ config.py
│  └─ validators.py
├─ exports/
├─ screenshots/
├─ README.md
├─ requirements.txt
└─ Dockerfile

This structure is intentionally small but layered. It supports maintainability without introducing unnecessary abstraction.

10. Functional Requirements

The tool should support the following features:

Accept ABN input from the user through the CLI.
Validate that the supplied input is in a usable format before attempting lookup.
Launch browser automation and perform an ABN search.
Extract at minimum:
entity name
ABN status
entity type
timestamp of access
Save structured result data in a consistent format.
Optionally export result data as JSON.
Optionally save a screenshot of the result page to a directory.
Log important events, including success and failure paths.
Allow users to retrieve or review prior lookup records.
Fail gracefully with readable messaging if the lookup cannot be completed.

These directly evolve from the original v1.1 design requirements.

11. Non-Functional Requirements
Reproducibility

The application should be able to run consistently on another system using documented setup steps and later a Docker container.

Maintainability

The codebase should be split into modules with clear responsibilities rather than a single file with mixed concerns.

Readability

The project should be understandable to another student, marker, or future maintainer.

Reliability

The application should handle common failure conditions such as invalid ABNs, missing selectors, navigation errors, and database write issues without crashing unexpectedly.

Usability

The CLI should provide clear prompts and understandable outcomes.

12. Logging Design

Logging is an important part of the design because this tool has both user-facing and operational behavior.

12.1 User-facing output

The user should see plain-language messages such as:

lookup started
ABN found
no result returned
screenshot saved
export completed
database save failed
browser automation timed out

These messages should be concise and understandable.

12.2 Operational logs

The logger should capture structured operational events such as:

application start
user action selected
ABN submitted
browser launched
target page reached
selector found or missing
lookup succeeded or failed
screenshot saved path
database write success or failure
export success or failure
runtime duration
error class and context

This separation helps support user empathy while still providing enough information for debugging and review.

12.3 Logging strategy

For v1, normal logs should be lightweight and useful. Debug-level logs can be more detailed during development. Logs should avoid dumping large volumes of browser detail unless troubleshooting is enabled.

13. Error Handling Strategy

The tool should anticipate both expected and unexpected failures.

Expected failures
invalid ABN format
no result returned
selector not found
page layout changed
timeout during lookup
export directory unavailable
screenshot path invalid
SQLite file or write failure
Error handling goals
avoid raw crashes where possible
log the technical event
show the user a readable message
preserve enough context to investigate the issue later

The original design already identified the need for graceful handling of invalid ABNs and missing page selectors. v1.2 expands that to include storage and export failures as well.

14. Data Model Considerations

For v1, the persisted lookup record should contain structured fields such as:

internal lookup ID
ABN queried
entity name
ABN status
entity type
lookup timestamp
screenshot saved flag
screenshot path if created
export path if created
source metadata
optional raw result text or JSON snapshot

This is enough to support lookup history, debugging, and export tracking without overcomplicating the schema.