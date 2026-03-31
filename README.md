
## ABN Lookup Tool

A small Python command-line tool that automates ABN Lookup searches using Playwright
Extracts key business details and saves results in structured formats.
This tool was built as a lightweight internal utility.

## Tool Description

Given an 11-digit ABN, the tool will:

Navigate to the ABN Lookup website

Perform a search

Extract key result fields

Save the result to JSON

Optionally store records in a local SQLite database

Capture a screenshot of the lookup session

Write application logs for traceability
 
 
## Features

CLI-based workflow,
ABN input validation,
Browser automation with Playwright,

Extraction of:

--Entity name

--ABN status

--Entity type

--JSON export

--Text export

SQLite record storage,

Screenshot capture,

Persistent logging with log export support.

## Project Structure 

abnLookupApp/
 
 ├── main.py
 
 ├── commandLine.py
 
 ├── services/
 
 │       ├── adapter.py
 
 │       ├── helpers.py
 -
 │       └── lookupService.py
 
 ├── storage/
 
 │        └── db.py
 
 ├── utils/
 
 │        └── logger.py
 
 ├── Docs/
 
 ├── Exports/
 
 ├── screenshots/
 
 └── logs/



## Requirements

Python 3.11 or newer (must install venv)
Playwright for Python

Docker installed - optional

## Installation
Make sure you have virtual environment installed:

apt install python3.13-venv

Clone the repository:
git clone https://github.com/yeahpryme/abnLookupApp

cd abnLookupApp

Create and activate a virtual environment:
python -m venv .venv source .venv/Scripts/activate

Install dependencies:
pip install playwright
python -m playwright install

## Usage

CLI usage: (remove headless to open browser and insert 11 ABN of choice)

    Run a lookup directly from the command line:

    python main.py --abn 51824753556 --headless

OR

Run the interactive menu:

python main.py

Use 0-5 and y/n/enter to navigate and execute operations. 

Menu explicitly explains operation and runs on a loop until exited.


## Run With Docker

Build image(include . to denote local folder):

docker build -t abnlookup-app:dev .

Run with interactive menu:

docker run -rm -it abnlookup-app:dev

Run Directly as CLI (replace ABN):

docker run --rm -it abnlookup-app:dev python main.py --abn 51824753556 --headless

Run CLI with browser opening:

docker run --rm -it abnlookup-app:dev python main.py --abn 11111111111

## Example Output

Example JSON export:

{
    "success": true,
    "abn": "51824753556",
    "name": "AUSTRALIAN TAXATION OFFICE",
    "status": "Active from 01 Nov 1999",
    "entityType": "Commonwealth Government Entity",
    "timestamp": "2026-03-31T17:19:09.152555",
    "exportPath": "Exports/abn_51824753556.json",
    "screenshotPath": "screenshots/abn_51824753556.png",
    "error": null
}

## Logging

Application events are written to a log file in the logs/ directory.
The CLI also provides an option to export the current log file for review or sharing.

## Notes and Limitations
This tool depends on the current structure and availability of the ABN Lookup website.
If the website layout changes, extraction logic may need updating.
This project is intended as a lightweight automation utility, not a production-grade data service.
Internet access is required during lookup.

## AI Usage Statement

Codex 5.4 has been used both in discussion during planning and at moments throughout development
Nothing has been used that I do not comphrehend and have completed a vast majority myself.

That said, predictive autocomplete has been substantial as I have worked in VScode the entire time.

Codex (5.4) was used in 2 clean up passes prior to pushing to main, as the commit history shows.
Dev branch contains a folder titled Development Snapshots. GPT 5.4 Helped write V1 of this README.md
This has my prompt history (bar the codex requests)
This folder also contains v1 of the design doc I wrote myself from the delivered specsheet myself.
Prompt history shows the regeneration that became v1.1.
This folder also contains an example code piece
This was written in a similar manner and was adapted for the outline of this projects menu
As I write this, I expect I am coming up on 8~ hours give or take a lecture earlier in the day.

## This Design Assumes:

The user has access to Python and project dependencies - preferably built from docker image.
The target ABN Lookup webpage is reachable during runtime.
Playwright can interact successfully with the target site.
Screenshots only need to be saved as files, not stored as binary objects in the database.
