import os
import sys
import time

# Ensure project root is on path
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from robot.api import logger


def _get_browser_manager():
    try:
        from keywords import ecommerce_keywords as ek
        return getattr(ek, "_browser_manager", None)
    except Exception:
        return None


class ScreenshotListener:
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, output_dir="allure-results"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def end_keyword(self, name, attributes):
        # Capture only user keywords and library keywords (skip teardown/control keywords if desired)
        bm = _get_browser_manager()
        if not bm:
            return
        page = getattr(bm, "page", None)
        if not page:
            return

        ts = int(time.time() * 1000)
        safe_kw = attributes.get("kwname", "keyword").replace(" ", "_")
        filename = f"{safe_kw}_{ts}.png"
        path = os.path.join(self.output_dir, filename)
        try:
            page.screenshot(path=path)
        except Exception as e:
            logger.warn(f"Screenshot failed: {e}")
            return

        # Attach to Allure if available
        try:
            import allure
            from allure_commons.types import AttachmentType
            try:
                allure.attach.file(path, name=attributes.get("kwname", "keyword"), attachment_type=AttachmentType.PNG)
            except Exception:
                with open(path, "rb") as f:
                    allure.attach(f.read(), name=attributes.get("kwname", "keyword"), attachment_type=AttachmentType.PNG)
        except Exception:
            # Fallback: embed into Robot log so it's visible in Robot reports
            try:
                rel = os.path.relpath(path, os.getcwd())
            except Exception:
                rel = path
            logger.info(f'<img src="{rel}" alt="{attributes.get("kwname","keyword")}">', html=True)


def get_listener(output_dir="allure-results"):
    return ScreenshotListener(output_dir)
