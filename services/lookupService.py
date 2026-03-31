
"""
validate input,
log that lookup started,
call adapter,
normalize returned data,
save record,
log success or failure,
return a simple result object.
"""

from storage.db import saveRecord 
from utils.logger import logEvent
from services.adapter import runAbnLookup
# from services.adapter import lookup_abn_with_playwright
# from storage.repository import save_record
from services.helpers import exportRecordJson, exportRecordText

def abnLookUp(abn=None, headless=False, capture_screenshot=True):
    print()  
    print("Starting ABN lookup...")
    logEvent("ABN lookup initiated")

    print()
    print("You will be promoted to enter an 11 digit ABN number.")
    print("Individual records can be exported as text files or saved to a local directory of your choice at any time")
    print()

   
    
    
    if abn is None:
        while True:
            abnNo = input("Enter the ABN you want to look up: ").strip()
            # Basic validation to check if the input is str (ABN format) ABNS are 11 digits
            if abnNo.isdigit() and len(abnNo) == 11:
                break
            print("Invalid ABN. Please enter an 11-digit number.")
    else:
        abnNo = abn.strip()
        if not (abnNo.isdigit() and len(abnNo) == 11):
            print("Invalid ABN provided via command line. Please ensure it's an 11-digit number.")
            return {
                "success": False,
                "message": "Invalid ABN provided via command line. Please ensure it's an 11-digit number.",
                "data": None
            }
    
    while True:
        savePreference = input("Do you want to save this record? (y/n): ").lower().strip()
        if savePreference in ("y", "n"):
            break
        print("Invalid Selection. Please enter 'y' or 'n'")
        
    if savePreference == "y":
        print("Record will be saved to the database.")
        saveData = True
    else:
        print ("Record will not be saved, ensure you export your work.")
        saveData = False
    
    
    try:
        logEvent(
            f"lookup for {abnNo} started | headless={headless} | capture_screenshot={capture_screenshot}"
        )
        adapterResult = runAbnLookup(
            abnNo,
            headless=headless,
            capture_screenshot=capture_screenshot,
        )

        if not adapterResult["success"]:
            logEvent(f"lookup for {abnNo} failed")
            return {
                "success": False,
                "message": adapterResult["error"] or f"Lookup for ABN: {abnNo} failed. Please try again.",
                "data": None
            }
        # Export first so the record carries the final artifact path before any
        # optional database save persists the metadata.
        jsonPath = exportRecordJson(adapterResult)
        adapterResult["exportPath"] = jsonPath
        logEvent(f"Record for {abnNo} exported to JSON at: {jsonPath}")

        textPath = exportRecordText(adapterResult)
        logEvent(f"Record for {abnNo} exported to text at: {textPath}")

        if saveData:
            logEvent(f"Saving record for {abnNo} to database")
            recordId = saveRecord(adapterResult)
            logEvent(f"Record for {abnNo} saved successfully with ID: {recordId}")

        logEvent(f"lookup for {abnNo} succeeded")
        return {
            "success": True,
            "message": f"Lookup for ABN: {abnNo} succeeded.",
            "data": adapterResult
        }
        
    
    
    except Exception as error:
        logEvent(f"Error during lookup for {abnNo}: {error}")
        return {
            "success": False,
            "message": f"An error occurred during lookup for ABN: {abnNo}. Please try again.",
            "data": None
        }   
       
       
       
       
