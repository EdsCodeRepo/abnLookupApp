"""
receive validated ABN input from the CLI
coordinate the lookup process
call the Playwright adapter
normalize the extracted result
instruct storage to persist data
trigger optional export or screenshot operations
return a clean result object to the CLI

"""
from storage.db import recordList, dbList


def getSavedRecords():
    return []


def retreiveRecord():
    # Placeholder for record retrieval logic
    pass




def deleteRecord():
    # Placeholder for record deletion logic
    pass
    
# Searches saved entries, checks if anything is cached, if not loads it from the database ready for other funcs
def requestRecord():
    int(input("Enter the record ID# of the item you want to update: "))
# Actually presents the cached records to the user, this is where the user can select a specific record to view, update or export
def retreiveRecord():
    # Placeholder for record retrieval logic
    pass


def exportMode():
    # Placeholder for export mode logic
    pass
def exportRecord():
    # Placeholder for record export logic
    pass

