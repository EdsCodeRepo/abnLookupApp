"""

launch browser
navigate to ABN Lookup page
submit ABN search
wait for expected elements
extract required result fields
capture screenshot when requested
translate automation outcomes into structured results or errors



accept an ABN
open browser - headless?
navigate to ABN Lookup
submit the ABN
wait for result state
extract the fields you care about
optionally capture screenshot
return structured data or a clear failure

"""
from playwright.sync_api import sync_playwright
from datetime import datetime


# This is the adapter layer
def runAbnLookup(abn, headless=True):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=headless)
            page = browser.new_page()
            page.goto("https://abr.business.gov.au/", wait_until="domcontentloaded")

            searchBox = page.locator('input[type="text"]').first
            searchBox.fill(abn)
            searchBox.press("Enter")
            
            page.wait_for_load_state("domcontentloaded")
            page.wait_for_timeout(3000)  # Wait for 3 seconds to ensure content is loaded

            currentUrl = page.url
            pageText = page.locator("body").inner_text()

            result = {
                "success": True,
                "abn": abn,
                "name": pageText,
                "status": f"debugUrl: {currentUrl}",
                "entityType": "debugBodyCapture",
                "entityType": "TODO: Extracted Entity Type",
                "timestamp": datetime.now().isoformat(),
                "exportPath": None,
                "screenshotPath": None,
                "error": None
            }
            browser.close()
            return result


    except Exception as error:
        return {
            "success": False,
            "abn": abn,
            "name": None,
            "status": None,
            "entityType": None,
            "timestamp": datetime.now().isoformat(),
            "exportPath": None,
            "screenshotPath": None,
            "error": str(error)
        }

    

