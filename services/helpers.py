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
from storage.db import getRecordById, deleteRecordById, deleteAllRecords

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


def exportSavedRecord(recordId):
    record = getRecordById(recordId)

    if not record:
        print("No saved record found with that ID.")
        return

    recordData = {
        "id": record[0],
        "abn": record[1],
        "name": record[2],
        "status": record[3],
        "entityType": record[4],
        "timestamp": record[5],
        "exportPath": record[6],
        "screenshotPath": record[7]
    }

    jsonPath = exportRecordJson(recordData)
    textPath = exportRecordText(recordData)

    print(f"Record exported to JSON: {jsonPath}")
    print(f"Record exported to text: {textPath}")


def deleteRecord(recordId):
    deletedCount = deleteRecordById(recordId)

    if deletedCount:
        print(f"Record ID {recordId} deleted successfully.")
    else:
        print("No saved record found with that ID.")

def deleteAllSavedRecords():
    firstConfirm = input("Type delete to remove ALL saved records: ").strip().lower()
    if firstConfirm != "delete":
        print("Bulk delete cancelled.")
        return

    secondConfirm = input("Type yes to confirm permanent deletion of ALL saved records: ").strip().lower()
    if secondConfirm != "yes":
        print("Bulk delete cancelled.")
        return

    deletedCount = deleteAllRecords()
    print(f"{deletedCount} saved record(s) deleted.")