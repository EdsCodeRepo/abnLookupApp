"""
receive validated ABN input from the CLI
coordinate the lookup process
call the Playwright adapter
normalize the extracted result
instruct storage to persist data
trigger optional export or screenshot operations
return a clean result object to the CLI

"""

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

