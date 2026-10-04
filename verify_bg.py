from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 480, "height": 640})

    file_path = f"file://{os.path.abspath('index.htm')}"
    page.goto(file_path)
    page.wait_for_timeout(1000)

    # Click to exit attract mode
    page.click("body")
    page.wait_for_timeout(500)

    # Click MODO HISTÓRIA
    page.click("#storyModeBtn")
    page.wait_for_timeout(500)

    # Skip cutscene
    for _ in range(8):
        if page.is_visible("#storyCutsceneNextBtn"):
            page.click("#storyCutsceneNextBtn")
            page.wait_for_timeout(200)

    # Dialogue modal - click next twice
    if page.is_visible("#nextDialogueBtn"):
        page.click("#nextDialogueBtn")
        page.wait_for_timeout(300)
    if page.is_visible("#nextDialogueBtn"):
        page.click("#nextDialogueBtn")
        page.wait_for_timeout(300)

    page.wait_for_timeout(500)
    page.screenshot(path="updated_volcano_bg.png")
    print("Screenshot saved to updated_volcano_bg.png")

    browser.close()
