import re
import time
from datetime import datetime, timedelta
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration: Set the download directory (modify as needed)
DOWNLOAD_DIR = "path/to/your/download/directory"  # Update this to your desired path

# Get last week's date range (Monday to Friday)
def get_last_week_range():
    """Calculate the date range for last week (Monday to Friday)."""
    today = datetime.now()
    days_to_last_monday = today.weekday()
    last_monday = today - timedelta(days=days_to_last_monday)
    last_friday = last_monday + timedelta(days=4)
    return last_monday.strftime("%m/%d/%Y"), last_friday.strftime("%m/%d/%Y")

# Format date for filename (DDMonYYYY format)
def format_date_for_filename(date_str):
    """Convert date string from MM/DD/YYYY to DDMonYYYY for filenames."""
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    return date_obj.strftime("%d%b%Y")

# Fill date range in the web form
def fill_date_range(page, start_date, end_date):
    """Fill start and end date fields in the web form."""
    page.locator("[id=\"_sStartDate\"]").fill(start_date)
    page.locator("[id=\"_sEndDate\"]").fill(end_date)

# Download report and save with formatted filename
def download_report(page, report_name, start_date, end_date):
    """Handle report export and download with formatted filename."""
    formatted_start_date = format_date_for_filename(start_date)
    formatted_end_date = format_date_for_filename(end_date)
    filename = f"{report_name} {formatted_start_date}-{formatted_end_date}.xls"
    save_path = os.path.join(DOWNLOAD_DIR, filename)

    # Trigger export and download
    page.get_by_role("link", name="Export").click()
    time.sleep(1)  # TODO: Replace with expect() for better stability
    page.get_by_text("Export to Excel").click()
    time.sleep(1)

    # Save the downloaded file
    with page.expect_download() as download_info:
        page.get_by_role("button", name="OK").click()
    download = download_info.value
    time.sleep(1)
    download.save_as(save_path)
    time.sleep(1)

# Main function to run the Playwright automation
def run(playwright: Playwright) -> None:
    """Automate report downloading from a network monitoring website."""
    # Initialize browser and page
    browser = playwright.chromium.launch(headless=False)  # Set headless=True for production
    context = browser.new_context()
    page = context.new_page()

    # Login to the website
    page.goto("http://monitoring.example.com/")  # Update URL to your monitoring system
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill(os.getenv("MY_USERNAME"))
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(os.getenv("PASSWORD"))
    page.get_by_role("button", name="Log In").click()

    # Navigate to Reports section
    page.get_by_role("link", name="Reports").click()
    time.sleep(1)  # TODO: Replace with expect() for better stability

    # Network1 CPU Utilization
    page.get_by_role("button", name="CPU Utilization").click()
    time.sleep(1)
    page.get_by_role("link", name="All Devices").click()
    time.sleep(1)
    page.get_by_role("link", name="Network1 Segment").click()  # Replace with your segment name
    time.sleep(1)
    page.get_by_role("link", name="Web Server").click()
    time.sleep(1)
    page.get_by_role("button", name="OK").click()
    time.sleep(1)

    # Set date range and time
    start_date, end_date = get_last_week_range()
    fill_date_range(page, start_date, end_date)
    page.locator("[id=\"_sStartTime\"]").fill("00:00")
    time.sleep(1)
    page.locator("[id=\"_sEndTime\"]").fill("23:59")
    time.sleep(1)
    page.get_by_role("button", name="Go").click()
    time.sleep(1)

    # Download Network1 CPU Utilization report
    download_report(page, "Network1 CPU Utilization", start_date, end_date)

    # Network1 Disk Utilization
    page.get_by_role("button", name="Disk Utilization").click()
    time.sleep(1)
    download_report(page, "Network1 Disk Utilization", start_date, end_date)

    # Network2 Disk Utilization
    page.get_by_role("link", name="Web Server").click()
    time.sleep(1)
    page.get_by_role("link", name="Network2").click()  # Replace with your network name
    time.sleep(1)
    page.get_by_role("link", name="Dotcom Servers").click()
    time.sleep(1)
    page.get_by_role("button", name="OK").click()
    time.sleep(1)
    download_report(page, "Network2 Disk Utilization", start_date, end_date)

    # Network2 CPU Utilization
    page.get_by_role("button", name="CPU Utilization").click()
    time.sleep(1)
    download_report(page, "Network2 CPU Utilization", start_date, end_date)

    # Logout
    page.get_by_role("link", name="user_profile").click()  # Replace with actual profile link text
    time.sleep(1)
    page.get_by_role("link", name="Log Out").click()

    # Clean up
    context.close()
    browser.close()

# Entry point
if __name__ == "__main__":
    """
    Main entry point for the script.
    Ensure .env file contains MY_USERNAME and PASSWORD.
    Update DOWNLOAD_DIR to your desired directory.
    Replace 'Network1' and 'Network2' with appropriate segment/network names.
    """
    with sync_playwright() as playwright:
        run(playwright)