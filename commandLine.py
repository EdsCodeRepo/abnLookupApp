"""
display menu and prompts
collect user input
validate basic menu selections
pass actions to the service layer
display results and errors in user-friendly language

This layer should not know how Playwright works internally and should not directly run SQL.


keep only menu display, input parsing, and result printing.
"""


from services.lookupService import abnLookUp
from services.helpers import  retreiveRecord, requestRecord, deleteRecord, exportRecord   



def menuLoop():
       
    while True:
        
        print("\n")
        print("------------- Playwright Tool Menu ---------------")
        print("--|       Lookup ABN          Enter: 1         |--")
        print("--|       View Saved Records  Enter: 2         |--")
        print("--|       Export a Record     Enter: 3         |--")
        print("--|       Delete a Record     Enter: 4         |--")
        print("--|       Settings            Enter: 5         |--")
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
                abnLookUp()
            elif choice == 2:
                # main input for the lookup checks for the respective function that passes it as a argument for the function
                requestRecord() 
                retreiveRecord()
            elif choice == 3:
                recordID = int(input("Enter the Record ID# of the item you want to delete: "))
                deleteRecord(recordID)
                
            
            elif choice == 4:
                if :
                    print("Current Saved Items:")
                    # feel like keeping the concurrent lists was extra work but worth it in terms of provding clear feedback for the user
                    # with time, I feel I could develop something that did use the single list of dictionaries, get and split strings,
                    # but I also enjoyed putting this together, its using the same principles described above
                    # it does turn ID into a const, and I'm not 100% but I think its because the its itterating 'values'
                    # and IDs values is always going to be 0, start of the list.
                    for recordData in :
                        ID = recordData[0]
                        name = recordData[1]
                        quantity = recordData[2]
                        price = recordData[3]
                       
                        everything = f"ID: {ID}, Name: {name}, Quantity: {quantity}, Price: ${price:.2f}"    
                        # again building the fstring as aposed to just printf("etc"), just hang up from the original implementation here
                        print(everything)
                else:
                    print("No items in inventory >:o I asked if you wanted to delete it twice!")
                
            elif choice == 5:
                # function init msg for user clarity
                print("\n To export all saved records enter 1, to export a specific record enter 2, followed by the record ID#")
                print("\n To export multiple records, seperate each ID# with a comma (e.g. 1,2,3)")
                exportMode = int(input("Enter the export mode: "))
                #exportRecord() - prints a textfile with record data/associated screenshots
                
            # if the user enters valid type but non existant selection, will promt and give them a heads up
            else:
                print("\n------ Please Select An Option Between 1-5. ------")
                print("--------- Or Enter 0 to close to program ---------")
        # if the wrong type is input this will trigger and give the user a heads up
        except ValueError:
            print("\n---- Invalid input, Use Numbers To Navigate. ----")
    pass