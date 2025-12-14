from pathlib import Path
import json
from selenium.webdriver.common.by import By

BY_MAP = {
    "id": By.ID,
    "name": By.NAME,
    "xpath": By.XPATH,
    "css": By.CSS_SELECTOR,
    "class": By.CLASS_NAME
}

def load_locators(page_name):
    """
    Loads locators from utils/locators/<page_name>.json
    Path-safe for pytest, PyCharm, CI
    """

    base_dir = Path(__file__).resolve().parent
    locator_file = base_dir / "locators" / f"{page_name}.json"

    if not locator_file.exists():
        raise FileNotFoundError(f"Locator file not found: {locator_file}")

    with open(locator_file, "r") as file:
        raw_locators = json.load(file)

    locators = {}

    for element_name, locator_data in raw_locators.items():
        locators[element_name] = {
            "primary": (
                BY_MAP[locator_data["primary"][0]],
                locator_data["primary"][1]
            ),
            "fallbacks": [
                (BY_MAP[fallback[0]], fallback[1])
                for fallback in locator_data.get("fallbacks", [])
            ]
        }

    return locators
