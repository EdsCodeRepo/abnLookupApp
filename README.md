
ABN Lookup Tool

A small Python command-line tool that automates ABN Lookup searches using Playwright
Extracts key business details, and saves results in structured formats.

This tool was built as a lightweight internal utility.

AI usage statement

Codex 5.4 has been used both in discussion during planning and at moments throughout development
Nothing has been used that I do not comphrehend and have completed a vast majority myself.
That said, predictive autocomplete has been substantial as I have worked in VScode the entire time.

Codex (5.4) was used in 2 clean up passes prior to pushing to main, as the commit history shows.
Dev branch contains a folder titled Development Snapshots
This has my prompt history (bar the codex requests)
This folder also contains v1 of the design doc I wrote myself from the delivered specsheet myself.
Prompt history shows the regeneration that became v1.1.
This folder also contains an example code piece
This was written in a similar manner and was adapted for the outline of this projects menu
As I write this, I expect I am coming up on 8~ hours give or take a lecture earlier in the day.




Given an 11-digit ABN, the tool will:

navigate to the ABN Lookup website
perform a search
extract key result fields
save the result to JSON
optionally store records in a local SQLite database
capture a screenshot of the lookup session
write application logs for traceability
 
 
Features

CLI-based workflow
ABN input validation
Browser automation with Playwright
Extraction of:
Entity name
ABN status
Entity type
JSON export
Text export
SQLite record storage
Screenshot capture
Persistent logging with log export support

Project Structure - GPT 5.4

abnLookupApp/
├── main.py
├── commandLine.py
├── services/
│   ├── adapter.py
│   ├── helpers.py
│   └── lookupService.py
├── storage/
│   └── db.py
├── utils/
│   └── logger.py
├── Docs/
├── Exports/
├── screenshots/
└── logs/



Requirements
Python 3.11 or newer
Playwright for Python
Docker installed - optional



Installation
Clone the repository:
git clone <your-repo-url>
cd abnLookupApp
Create and activate a virtual environment:
python -m venv .venv
source .venv/Scripts/activate
Install dependencies:
pip install playwright
python -m playwright install
Usage


CLI usage: example

    Run a lookup directly from the command line:

    python main.py --abn 51824753556

OR

Run the interactive menu:

python main.py


Example Output

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

Logging

Application events are written to a log file in the logs/ directory.
The CLI also provides an option to export the current log file for review or sharing.

Notes and Limitations
This tool depends on the current structure and availability of the ABN Lookup website.
If the website layout changes, extraction logic may need updating.
This project is intended as a lightweight automation utility, not a production-grade data service.
Internet access is required during lookup.

This design assumes:

the user has access to Python and project dependencies
the target ABN Lookup webpage is reachable during runtime
Playwright can interact successfully with the target site
the project brief accepts CLI interaction
screenshots only need to be saved as files, not stored as binary objects in the database
SQLite is sufficient for the expected scale of use in this submission