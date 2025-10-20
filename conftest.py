# # # import pytest
# # # from playwright.sync_api import sync_playwright
# # #
# # #
# # # @pytest.fixture(scope="function")
# # # def browser_page():
# # #     with sync_playwright() as p:
# # #         # Launch maximized
# # #         browser = p.chromium.launch(headless=False, args=["--start-maximized"])
# # #
# # #         # Create context with authentication + no viewport restriction
# # #         context = browser.new_context(
# # #             http_credentials={
# # #                 "username": "keuro-uat",
# # #                 "password": "G862DSDumLKqmg"
# # #             },
# # #             no_viewport=True
# # #         )
# # #
# # #         page = context.new_page()
# # #
# # #         # Navigate to your app
# # #         page.goto("https://web-uat.riyaah.com/en")
# # #
# # #         print("Clearing storage and cookies before test...")
# # #         context.clear_cookies()
# # #         page.evaluate("localStorage.clear()")
# # #         page.evaluate("sessionStorage.clear()")
# # #
# # #         yield page
# # #         context.close()
# # #         browser.close()
# # #
# # #
# # import pytest
# # from playwright.sync_api import sync_playwright
# #
# #
# # @pytest.fixture(scope="function")
# # def browser_page():
# #     with sync_playwright() as p:
# #         # Launch browser maximized
# #         browser = p.chromium.launch(
# #             headless=False,
# #             args=["--start-maximized"]
# #         )
# #
# #         # Create a context with:
# #         # - English locale and headers
# #         # - HTTP authentication
# #         # - No viewport restriction
# #         context = browser.new_context(
# #             locale="en-US",  # Force English locale
# #             extra_http_headers={
# #                 "Accept-Language": "en-US,en;q=0.9"
# #             },
# #             http_credentials={
# #                 "username": "keuro-uat",
# #                 "password": "G862DSDumLKqmg"
# #             },
# #             no_viewport=True
# #         )
# #
# #         page = context.new_page()
# #
# #         # Navigate to app
# #         page.goto("https://web-uat.riyaah.com/en")
# #
# #         # Optional: Verify language being used
# #         lang = page.evaluate("navigator.language")
# #         print(f"Browser language detected: {lang}")
# #
# #         # Ensure clean state before test
# #         print("Clearing cookies and storage before test...")
# #         context.clear_cookies()
# #         page.evaluate("localStorage.clear()")
# #         page.evaluate("sessionStorage.clear()")
# #
# #         yield page
# #
# #         # Cleanup after test
# #         context.close()
# #         browser.close()
# import os
# import pytest
# from datetime import datetime
# from playwright.sync_api import sync_playwright
# from utils.loggers import logger  # optional: for logging screenshot paths
#
#
# # This fixture launches the browser, opens the page, and handles screenshots on failure
# @pytest.fixture(scope="function")
# def browser_page(request):
#     with sync_playwright() as p:
#         # Launch the browser in maximized mode (not headless)
#         browser = p.chromium.launch(headless=False, args=["--start-maximized"])
#
#         # Create browser context with locale + login credentials
#         context = browser.new_context(
#             locale="en-US",
#             extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
#             http_credentials={
#                 "username": "keuro-uat",
#                 "password": "G862DSDumLKqmg"
#             },
#             no_viewport=True,
#         )
#
#         # Create a new page (tab)
#         page = context.new_page()
#         page.goto("https://web-uat.riyaah.com/en")
#
#         # Clean cookies and local storage before running test
#         context.clear_cookies()
#         page.evaluate("localStorage.clear()")
#         page.evaluate("sessionStorage.clear()")
#
#         # Hand over control to the test case
#         yield page
#
#         # ---- AFTER THE TEST FINISHES ----
#         # Check if the test failed
#         if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
#             # Create screenshot folder if not exist
#             screenshot_dir = os.path.join(os.getcwd(), "screenshots")
#             os.makedirs(screenshot_dir, exist_ok=True)
#
#             # Screenshot file name with test name and timestamp
#             timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             screenshot_path = os.path.join(
#                 screenshot_dir, f"{request.node.name}_{timestamp}.png"
#             )
#
#             # Take the screenshot
#             page.screenshot(path=screenshot_path, full_page=True)
#
#             # Log or print the path
#             print(f"❌ Screenshot captured: {screenshot_path}")
#             logger.error(f"❌ Screenshot captured: {screenshot_path}")
#
#         # Close context and browser at the end
#         context.close()
#         browser.close()
#
#
# # This hook tells pytest to store test results (pass/fail)
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Hook that adds test result info (passed/failed) to the 'request' object.
#     This allows the fixture above to detect failures after yield.
#     """
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)

import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.loggers import logger  # optional for logging
import allure  # optional, for Allure screenshot attachment


@pytest.fixture(scope="function")
def browser_page(request):
    """
    This fixture:
      - Launches the browser before each test
      - Yields the Playwright 'page' object
      - Automatically takes a screenshot if the test fails
    """
    with sync_playwright() as p:
        # Launch browser (non-headless for debugging)
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])

        # Create context
        context = browser.new_context(
            locale="en-US",
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
            http_credentials={
                "username": "keuro-uat",
                "password": "G862DSDumLKqmg"
            },
            no_viewport=True,
        )

        # Open new tab/page
        page = context.new_page()
        page.goto("https://web-uat.riyaah.com/en")

        # Clear previous data
        context.clear_cookies()
        page.evaluate("localStorage.clear()")
        page.evaluate("sessionStorage.clear()")

        # ✅ Yield control to test
        yield page

        # ✅ After test (teardown)
        if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
            try:
                # Create screenshot folder if missing
                screenshot_dir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)

                # Create a timestamped filename
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = os.path.join(
                    screenshot_dir, f"{request.node.name}_{timestamp}.png"
                )

                # Take screenshot
                page.screenshot(path=screenshot_path, full_page=True)

                # Log and report
                logger.error(f"❌ Test failed! Screenshot: {screenshot_path}")
                print(f"❌ Screenshot captured: {screenshot_path}")

                # Attach screenshot in Allure report (if installed)
                try:
                    allure.attach.file(
                        screenshot_path,
                        name=f"{request.node.name}_failure",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception:
                    pass

            except Exception as e:
                print(f"⚠️ Failed to capture screenshot: {e}")

        # Close browser after test
        context.close()
        browser.close()


# 🧠 Hook: This enables us to check if test passed or failed after it runs
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook adds attributes (rep_setup, rep_call, rep_teardown) to each test item.
    These attributes contain information about the test result (passed/failed/skipped).
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

