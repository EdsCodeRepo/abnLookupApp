"""
display menu and prompts
collect user input
validate basic menu selections
pass actions to the service layer
display results and errors in user-friendly language

This layer should not know how Playwright works internally and should not directly run SQL.


keep only menu display, input parsing, and result printing.
"""

from storage.db import getAllRecords
from services.lookupService import abnLookUp
from services.helpers import   deleteRecord, deleteAllSavedRecords, exportSavedRecord, terminalPause
from utils.logger import logEvent



def menuLoop():
       
    while True:
        
        print("\n")
        print("------------- Playwright Tool Menu ---------------")
        print("--|       Lookup ABN          Enter: 1         |--")
        print("--|       View Saved Records  Enter: 2         |--")
        print("--|       Export a Record     Enter: 3         |--")
        print("--|       Delete a Record     Enter: 4         |--")
        print("--|       Close Program       Enter: 0         |--")
        print("--------------------------------------------------")
        #another try except, with the main user input at the very start expecting an int
        try:
            choice = int(input("\n-------------- Enter your selection: "))
            # handles the program exit straight away followed by else if statements
            # each option coresponds with the functions explained in detail above
            if choice == 0:
                print("Thanks for using the Playwright Tool!")
                break
            elif choice == 1:
                lookupResult = abnLookUp()  # main input for the lookup checks for the respective function that passes it as a argument for the function
                
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
            
            elif choice == 2:
                # main input for the lookup checks for the respective function that passes it as a argument for the function
                savedRecords = getAllRecords()
                if savedRecords:
                    print("Current Saved Records:")
                    for recordData in savedRecords:
                       print(f"ID: {recordData[0]} | ABN: {recordData[1]} | Name: {recordData[2]}")
                    terminalPause()
                else:
                    print("No saved records found.")
            
            
            elif choice == 3:
                recordID = int(input("Enter the Record ID# of the item you want to export: "))
                exportSavedRecord(recordID)
                terminalPause()
            
            elif choice == 4:
                print("Enter a record ID to delete one record, or enter ALL to delete every saved record.")
                deleteChoice = input("Delete selection: ").strip().lower()

                if deleteChoice == "all":
                   deleteAllSavedRecords()
                else:                  
                    recordID = int(deleteChoice)
                    deleteRecord(recordID)
                
                terminalPause()          
            # if the user enters valid type but non existant selection, will promt and give them a heads up
            else:
                print("\n------ Please Select An Option Between 1-4. ------")
                print("--------- Or Enter 0 to close to program ---------")
        # if the wrong type is input this will trigger and give the user a heads up
        except ValueError:
            print("\n---- Invalid input, Use Numbers To Navigate. ----")
    pass