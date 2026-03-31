
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
        if savePrefernce.lower() in ("y", "n"):
            break
        print("Invalid Selection. Please enter 'y' or 'n'")
        
        if savePrefernce.lower() == "y":
            print("Record will be saved to the database.")
        elif savePrefernce.lower() == "n":
            print("Record will not be saved, ensure you export your work.")
    
    abnNo = input("Enter the ABN you want to look up: ")
    # Basic validation to check if the input is str (ABN format) ABNS are 11 digits
    if not abnNo.isdigit() or len(abnNo) != 11:
        print("Invalid ABN. Please enter an 11-digit number.")




    # Placeholder for ABN lookup logic
    # This is where you would integrate with the Playwright adapter to perform the actual lookup
    # For now, we'll just return a dummy result
    result = {
        "abn": abnNo,
        "name": "Dummy Company Pty Ltd",
        "status": "Active",
        "timestamp": "2024-06-01T12:00:00Z",
        "export_path": "/path/to/exported/data.txt",
        "screenshot_path": "/path/to/screenshot.png"
    }
   

abnLookUp()
