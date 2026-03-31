
"""
validate input,
log that lookup started,
call adapter,
normalize returned data,
save record,
log success or failure,
return a simple result object.
"""


from utils.logger import logEvent
# from services.adapter import lookup_abn_with_playwright
# from storage.repository import save_record

def abnLookUp():
    print()  
    print("Starting ABN lookup...")
    logEvent("ABN lookup initiated")

    print()
    print("You will be promoted to enter an 11 digit ABN number.")
    print("Individual records can be exported as text files or saved to a local directory of your choice at any time")
    print()

    while True:
        savePrefernce = input("Do you want to save this record? (y/n): ")
        if savePrefernce.lower().strip() in ("y", "n"):
            break
        print("Invalid Selection. Please enter 'y' or 'n'")
        
    if savePrefernce.lower() == "y":
        print("Record will be saved to the database.")
        saveRecord = True
    else:
        print ("Record will not be saved, ensure you export your work.")
        saveRecord = False
    while True:

        abnNo = input("Enter the ABN you want to look up: ").strip()
        # Basic validation to check if the input is str (ABN format) ABNS are 11 digits
        if not abnNo.isdigit() or len(abnNo) != 11:
            break
        print("Invalid ABN. Please enter an 11-digit number.")
    try:
        logEvent(f"lookup for {abnNo} started")

        #adapter call lookUpAbnWith(passed ABN number)


        adapterResult = {
            "success": True,
            "abn": abnNo,
            "name": "Dummy Company Pty Ltd",
            "status": "Active",
            "entityType": "Company",
            "timestamp": "2024-06-01T12:00:00Z",
            "export_path": "/path/to/exported/data.txt",
            "screenshot_path": "/path/to/screenshot.png"
        }
        # if failed, log it and tell the user
        if not adapterResult["success"]:
            logEvent(f"lookup for {abnNo} failed")
            return {
                "success": False,
                "message": f"Lookup failed for ABN {abnNo}. Please try again."
                # Could parse the error message in an understandable way to guide user
            } 
        logEvent(f"lookup for {abnNo} succeeded")
   
   
   
   
   
   
   
   
   
   
    except Exception as error:
        logEvent(f"Error logging event during lookup for {abnNo}: {error}")      
        return {
            "success": False,
            "message": f"An error occurred during lookup for ABN: {abnNo}. Please try again.",
            "data": None
        }      


    
   
   

abnLookUp()
