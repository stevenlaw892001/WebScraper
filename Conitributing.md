# Contributing to Network Monitoring Report Automation

Thank you for considering contributing to this project! This Python script automates the downloading of CPU and Disk Utilization reports from a network monitoring system using Playwright. We welcome contributions in the form of bug reports, feature requests, code improvements, and documentation updates.

## Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
  - [Reporting Issues](#reporting-issues)
  - [Suggesting Features](#suggesting-features)
  - [Submitting Code Changes](#submitting-code-changes)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Pull Request Process](#pull-request-process)
- [License](#license)

## Code of Conduct
Please be respectful and considerate in all interactions. We aim to maintain a welcoming and inclusive environment for all contributors.

## How to Contribute

### Reporting Issues
If you find a bug or issue:
1. Check the [GitHub Issues](https://github.com/stevenlaw892001/your-repo/issues) to see if it has already been reported.
2. If not, create a new issue with:
   - A clear title and description.
   - Steps to reproduce the issue.
   - Expected and actual behavior.
   - Your environment (e.g., OS, Python version, Playwright version).

### Suggesting Features
To propose a new feature:
1. Open a [GitHub Issue](https://github.com/stevenlaw892001/your-repo/issues) with the label `enhancement`.
2. Describe the feature, its use case, and any implementation ideas.
3. Discuss with the maintainers before starting work to ensure alignment.

### Submitting Code Changes
To contribute code:
1. Fork the repository and create a new branch for your changes (`git checkout -b feature-or-fix-name`).
2. Make your changes, ensuring they follow the [Code Style Guidelines](#code-style-guidelines).
3. Test your changes locally (see [Development Setup](#development-setup)).
4. Commit your changes with clear messages (e.g., `Add error handling for download failures`).
5. Push your branch to your fork (`git push origin feature-or-fix-name`).
6. Open a Pull Request (PR) following the [Pull Request Process](#pull-request-process).

## Development Setup
To set up the project locally:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/stevenlaw892001/your-repo.git
   cd your-repo
   ```
2. **Install dependencies**:
   ```bash
   pip install playwright
   playwright install
   ```
3. **Set up environment variables**:
   - Create a `.env` file in the root directory with:
     ```plaintext
     MY_USERNAME=your-username
     PASSWORD=your-password
     ```
   - Update `DOWNLOAD_DIR` in `web_scraper.py` to a valid local path.
   - Replace `Network1` and `Network2` in `web_scraper.py` with appropriate segment/network names for your system.
4. **Run the script**:
   ```bash
   python web_scraper.py
   ```
5. **Test in a safe environment**:
   - Ensure your monitoring system URL is correctly configured in `web_scraper.py`.
   - Test with `headless=False` first to verify navigation and downloads.

## Code Style Guidelines
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Use meaningful variable and function names.
- Add comments to explain complex logic.
- Avoid hardcoding sensitive information (e.g., URLs, network names).
- Use `try-except` blocks for error-prone operations (e.g., network requests, file downloads).
- Keep `time.sleep()` usage minimal; prefer Playwright's `expect()` or `wait_for_selector()` for stability.

## Pull Request Process
1. Ensure your changes are tested locally and do not introduce new issues.
2. Update documentation (e.g., README.md) if your changes affect setup or usage.
3. Follow the [Pull Request Template](.github/pull_request_template.md) when creating a PR:
   - Provide a clear description of the changes.
   - Specify the type of change (e.g., bug fix, new feature).
   - Include testing details (e.g., manual testing steps, environment).
4. Ensure no sensitive information (e.g., real network names, credentials) is included.
5. Address any feedback from maintainers during the review process.
6. Your PR will be merged once approved by the maintainers.

## License
By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE). See the LICENSE file for details.

---

We appreciate your contributions and look forward to improving this project together!