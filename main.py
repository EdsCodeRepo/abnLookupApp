"""
initialize logging
initialize database connection/repository
initialize Playwright adapter
initialize lookup service
pass control to the CLI layer
"""
import argparse

from commandLine import menuLoop
from storage.db import initDatabase
from services.lookupService import abnLookUp
from services.helpers import terminalPause
from utils.logger import initLogging, logEvent

#start the application




def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="ABN Lookup Tool")
    parser.add_argument("--headless", action = "store_true", help = "Run in headless mode")
    parser.add_argument("--abn", help = "Enter ABN to look up directly from command line")
    args = parser.parse_args()
    initLogging()
    initDatabase()
    logEvent("Application started")
    if args.abn:
        print(f"ABN provided via command line: {args.abn}")
        print(f"Running direct lookup in {'headless' if args.headless else 'headed'} mode.")
        lookupResult = abnLookUp(
            args.abn,
            headless=args.headless,
            capture_screenshot=False,
        )
        if lookupResult["success"]:
            currentRecord = lookupResult["data"]
            print(f"ABN: {currentRecord['abn']}")
            print(f"Name: {currentRecord['name']}")
            print(f"Status: {currentRecord['status']}")
            print(f"Entity Type: {currentRecord['entityType']}")
            print(f"Timestamp: {currentRecord['timestamp']}")
        else:
            print(f"Error: {lookupResult['message']}")
            terminalPause()
        nextStep = input("Enter 'm' to return to the menu or any other key to exit: ").lower().strip()
        if nextStep == "m":
            menuLoop()
    
    else:
        menuLoop()



if __name__ == "__main__":
    main()



