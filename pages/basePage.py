from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure

from utils.healing_store import save_healing

CONFIDENCE_THRESHOLD = 0.75

logging.basicConfig(level=logging.INFO)

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, name, locator_def):

        # 1️⃣ Try primary locator
        try:
            return self.wait.until(
                EC.presence_of_element_located(locator_def["primary"])
            )
        except Exception:
            logging.warning(f"[SELF-HEAL] Primary locator failed for '{name}'")

        best_candidate = None
        best_score = 0
        best_fb = None

        # 2️⃣ Evaluate fallbacks
        for fb in locator_def.get("fallbacks", []):
            try:
                element = self.wait.until(
                    EC.presence_of_element_located(fb)
                )

                score = self._calculate_confidence(
                    element, locator_def["primary"]
                )

                if score > best_score:
                    best_candidate = element
                    best_score = score
                    best_fb = fb

            except Exception:
                continue

        # 3️⃣ Accept only if confidence is good
        if best_candidate and best_score >= CONFIDENCE_THRESHOLD:

            logging.info(
                f"[SELF-HEAL] '{name}' healed using {best_fb} "
                f"(confidence={best_score})"
            )

            # 🔹 Allure attachment
            allure.attach(
                body=f"Primary: {locator_def['primary']}\n"
                     f"Fallback: {best_fb}\n"
                     f"Confidence: {best_score}",
                name=f"Healed locator for {name}",
                attachment_type=allure.attachment_type.TEXT
            )

            # 🔹 Persist healing
            save_healing(
                page=self.__class__.__name__,
                element=name,
                primary=locator_def["primary"],
                fallback=best_fb,
                confidence=best_score
            )

            return best_candidate

        # 4️⃣ Fail safely
        raise NoSuchElementException(
            f"Element '{name}' not healed safely "
            f"(confidence={best_score})"
        )

