"""
load configuration
initialize logging
initialize database connection/repository
initialize Playwright adapter
initialize lookup service
pass control to the CLI layer
"""

from commandLine import menuLoop

import utils.config as config
from storage.db import initDatabase
#start the application




def main():
    # Load configuration
    
    # Initialize database
    initDatabase()
    #Starts playwright service
    #initLookup()
    # Start the CLI menu loop with lookup service passed through as arg
    menuLoop()
   



if __name__ == "__main__":
    main()



