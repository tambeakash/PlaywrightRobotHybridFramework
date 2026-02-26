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

To capture screenshots for every keyword and attach them to Allure/Robot logs, run Robot with the screenshot listener:

```powershell
# local run (adds screenshot attachments and embeds images in Robot log)
robot --listener listeners/screenshot_listener.py tests/

# with Allure listener (CI/Allure results)
robot --listener robotframework_allure.listener --listener listeners/screenshot_listener.py tests/
```

## GitHub

Repository: https://github.com/tambeakash/PlaywrightRobotHybridFramework

## Notes

- The `keywords/ecommerce_keywords.py` file adds the project root to `sys.path` so that `core` and `pages` modules import correctly when Robot executes.
- By default the browser launches in headed mode locally.  When running on CI (or when the environment variable `HEADLESS` is set to `true`), the framework will start Chromium in headless mode.  You can override this behavior by passing a parameter to `BrowserManager` or setting `HEADLESS`.

