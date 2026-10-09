import os
import time
from playwright.sync_api import sync_playwright

def run_cuj(page, file_url):
    page.goto(file_url)
    page.wait_for_timeout(1000)

    # Click attract overlay to enter menu
    page.click("#attractScreen")
    page.wait_for_timeout(500)

    # Enable developer unlock for Level 2
    page.click("#optionsBtn")
    page.wait_for_timeout(500)
    page.click("#unlockAllLevelsBtn")
    page.wait_for_timeout(500)
    page.click("#doneOptionsBtn")
    page.wait_for_timeout(500)

    # Click Story Mode and select Level 2 (Grotas de Cristal)
    page.click("#storyModeBtn")
    page.wait_for_timeout(500)

    # Click Level 2 button
    page.evaluate("() => openPreLevelDialogue(2)")
    page.wait_for_timeout(500)

    # Skip pre-level dialogue
    page.click("#skipDialogueBtn")
    page.wait_for_timeout(500)

    # First jump to enter gameplay
    page.keyboard.press("Space")
    page.wait_for_timeout(800)

    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            file_path = "file:///app/index.htm"
            run_cuj(page, file_path)
        finally:
            context.close()
            browser.close()
