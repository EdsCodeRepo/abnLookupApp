"""
receive validated ABN input from the CLI
coordinate the lookup process
call the Playwright adapter
normalize the extracted result
instruct storage to persist data
trigger optional export or screenshot operations
return a clean result object to the CLI

"""

import json
from pathlib import Path

def exportRecordJson(recordData, outputDir="exports"):
    Path(outputDir).mkdir(parents=True, exist_ok=True)

    fileName = f"abn_{recordData['abn']}.json"
    filePath = Path(outputDir) / fileName

    with open(filePath, "w") as jsonFile:
        json.dump(recordData, jsonFile, indent=4)

    return filePath

def exportRecordText(recordData, outputDir="exports"):
    Path(outputDir).mkdir(parents=True, exist_ok=True)

    fileName = f"abn_{recordData['abn']}.txt"
    filePath = Path(outputDir) / fileName

    with open(filePath, "w") as textFile:
        textFile.write(f"ABN: {recordData['abn']}\n")
        textFile.write(f"Name: {recordData['name']}\n")
        textFile.write(f"Status: {recordData['status']}\n")
        textFile.write(f"Entity Type: {recordData['entityType']}\n")
        textFile.write(f"Timestamp: {recordData['timestamp']}\n")
        textFile.write(f"Export Path: {recordData['exportPath']}\n")
        textFile.write(f"Screenshot Path: {recordData['screenshotPath']}\n ")

    return str(filePath)

def terminalPause():
    input("\nPress Enter to continue...")


def showIdNamePairs(savedRecords):
    if not savedRecords:
        print("No saved records found.")
        return
    print("Current Saved Records:")
    for recordData in savedRecords:
        print(f"ID: {recordData[0]} - Name: {recordData[2]}")




def deleteRecord():
    # Placeholder for record deletion logic
    pass
    
# Searches saved entries, checks if anything is cached, if not loads it from the database ready for other funcs


def exportMode():
    # Placeholder for export mode logic
    pass
def exportRecord():
    # Placeholder for record export logic
    pass

