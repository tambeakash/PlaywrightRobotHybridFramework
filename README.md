# Playwright Robot Framework Hybrid Framework

A hybrid test automation framework combining Playwright for browser automation with Robot Framework for test orchestration and keyword reuse.

## Project Structure

- `tests/` - Robot Framework test suites
- `keywords/` - Custom Python libraries used as Robot keywords
- `pages/` - Page object models encapsulating UI interactions
- `core/` - Core utilities such as the browser manager
- `resources/` - Additional test resources

## Setup

1. Create and activate a Python virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1   # Windows PowerShell
   # or source .venv/bin/activate     # macOS/Linux
   ```
2. Install dependencies:
   ```powershell
   pip install robotframework playwright
   playwright install
   ```
3. Install any Robot Framework libraries if needed (`robotframework-browser`, etc.).

## Running Tests

Run all tests from the repository root:

```powershell
robot tests/
```

You can specify single test files or tags as usual with Robot Framework.

## GitHub

Repository: https://github.com/tambeakash/PlaywrightRobotHybridFramework

## Notes

- The `keywords/ecommerce_keywords.py` file adds the project root to `sys.path` so that `core` and `pages` modules import correctly when Robot executes.
- Playwright is configured to launch Chromium in headed mode; adjust `headless` in `core/browser_manager.py` if desired.
