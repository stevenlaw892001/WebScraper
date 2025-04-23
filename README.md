# Network Monitoring Report  Report Automation

This Python script automates the downloading of CPU and Disk Utilization reports from a network monitoring system using Playwright. It navigates through a web interface, sets a date range (last week's Monday to Friday), and exports reports as Excel files.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## Installation
To set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/stevenlaw892001/network-report-automation.git
   cd network-report-automation
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
3. **Set up environment variables**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and fill in your monitoring system credentials:
     ```plaintext
     MY_USERNAME=your-username
     PASSWORD=your-password
     ```

## Configuration
Before running the script, configure the following in `web_scraper.py`:

- **DOWNLOAD_DIR**: Set to a valid local directory where reports will be saved (e.g., `/path/to/your/download/directory`).
- **Network Names**: Replace `Network1` and `Network2` with the appropriate segment/network names for your monitoring system.
- **URL**: Update the monitoring system URL (e.g., `http://monitoring.example.com/`).

Ensure sensitive information (e.g., real network names, credentials) is not hardcoded in the script.

## Usage
Run the script with:
```bash
python web_scraper.py
```

The script will:
1. Log in to the monitoring system.
2. Navigate to the Reports section.
3. Download CPU and Disk Utilization reports for two network segments (Network1 and Network2) for the last week.
4. Save reports as Excel files in the specified `DOWNLOAD_DIR` with filenames like `Network1 CPU Utilization DDMonYYYY-DDMonYYYY.xls`.

**Tips**:
- Run with `headless=False` (default) to visually verify navigation.
- Set `headless=True` in `web_scraper.py` for faster, non-interactive execution.
- Replace `time.sleep()` with Playwright's `expect()` or `wait_for_selector()` for better stability (see TODO comments in the code).

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to report issues, suggest features, or submit code changes. Ensure no sensitive information (e.g., real network names) is included in contributions.

## Code of Conduct
We are committed to fostering an inclusive community. Please review our [Code of Conduct](CODE_OF_CONDUCT.md) to understand the expected behavior and reporting process for any concerns.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
