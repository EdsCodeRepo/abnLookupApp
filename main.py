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
import storage.db as db
#start the application




def main():
    # Load configuration
    
    # Initialize database
    from storage.db import initDatabase
    initDatabase()

    menuLoop()
   



if __name__ == "__main__":
    main()



