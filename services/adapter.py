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

def extractField(pageText, label):
    lines = [line.strip() for line in pageText.splitlines() if line.strip()]
#struggle streeet - If a line contains the label, checks that value appears on the same line after a colon - codex MVP
    for index, line in enumerate(lines):
        if label.lower() in line.lower():
            if ":" in line:
                afterColon = line.split(":", 1)[1].strip()
                if afterColon:
                    return afterColon
            if index + 1 < len(lines):
                return lines[index + 1]

    return None

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
           


            name = extractField(pageText, "Entity Name:")
            if name and "Current details for ABN" in name:
                name = None
            
            status = extractField(pageText, "ABN Status:")
            if not status:
                status = extractField(pageText, "Status")
            
            entityType = extractField(pageText, "Entity Type")


            result = {
                "success": True,
                "abn": abn,
                "name": name or "Not Found",
                "status": status or f"parse failed - URL: {currentUrl}",
                "entityType": entityType or "Not Found",
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

    

