from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/pridej")

assert "Pepes pizza-Pridej" in driver.title

driver.find_element(By.NAME, "nazev").clear()
driver.find_element(By.NAME, "nazev").send_keys("LMAO")
driver.find_element(By.NAME, "cena").clear()
driver.find_element(By.NAME, "cena").send_keys("789")
driver.find_element(By.TAG_NAME, "button").click()

driver.find_element(By.LINK_TEXT, "Picy").click()
assert "Picy" in driver.title
assert driver.find_element(By.TAG_NAME, "h2").text == "Nabídka pic"
info_prvni_picy = driver.find_element(By.XPATH, "//ol/li[last()]")
assert info_prvni_picy.text == "LMAO: 789"

driver.close()


"""
assert "Pepes pizza-Home page" in driver.title

driver.find_element(By.LINK_TEXT, "Picy").click()
nadpis_druhe_urovne = driver.find_element(By.TAG_NAME, "h2").text
assert nadpis_druhe_urovne == "Nabídka pic"

info_prvni_picy = driver.find_element(By.XPATH, "//ol/li[1]")
assert info_prvni_picy.text == "čoky: 123"

-------------------------------------------------------------------------------------------------

driver.find_element(By.NAME, "nazev").clear()
driver.find_element(By.NAME, "nazev").send_keys("čoky")

driver.find_element(By.NAME, "mnozstvi").clear()
driver.find_element(By.NAME, "mnozstvi").send_keys("123")
driver.find_element(By.TAG_NAME, "button").click()

-------------------------------------------------------------------------------------------------

driver.find_element(By.NAME, "nazev").clear()
driver.find_element(By.NAME, "nazev").send_keys("LMAO")
driver.find_element(By.NAME, "cena").clear()
driver.find_element(By.NAME, "cena").send_keys("789")
driver.find_element(By.TAG_NAME, "button").click()
-------------------------------------------------------------------------------------------------

class ChromeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_first_recipe(self):
        self.driver.get("http://127.0.0.1:5000/nabidka")
        text_prvniho_receptu = self.driver.find_element(By.XPATH, "//ol/li[1]").text
        self.assertEqual(text_prvniho_receptu, "LMAO: 789")

    def tearDown(self):
        self.driver.cole()
"""