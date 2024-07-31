from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Opciones de Navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--headless')


# driver_path = 'D:\\Lea\\Desarrollos\\Python\\Selenium\\chromedriver-win64\\chromedriver.exe'

# Servicio de ChromeDriver
# service = Service(driver_path)

# Inicializar el driver de Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), 
    options=options
    )

# Verifica si se abre el navegador
driver.get(rf'https://www.airbnb.com.ar/?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&search_mode=flex_destinations_search&flexible_trip_lengths%5B%5D=one_week&location_search=MIN_MAP_BOUNDS&monthly_start_date=2024-08-01&monthly_length=3&monthly_end_date=2024-11-01&price_filter_input_type=0&channel=EXPLORE&category_tag=Tag%3A8186&search_type=category_change')

# Espera 5 segundos para ver el resultado
time.sleep(3)

titulos = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
for titulo in titulos:
    print(titulo.text)
# Cierra el navegador
driver.quit()
