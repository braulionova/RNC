from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def createDriver() -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    prefs = {"profile.managed_default_content_settings.images":2}
    chrome_options.headless = True


    chrome_options.add_experimental_option("prefs", prefs)
    myDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    return myDriver

def getGoogleHomepage(driver: webdriver.Chrome) -> str:
    driver.get("https://www.google.com")
    return driver.page_source

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
    
def getRNC(driver: webdriver.Chrome) -> str:
    #buscamos el rnc
    driver.get("https://www.dgii.gov.do/app/WebApps/ConsultasWeb/consultas/rnc.aspx")

    # Fill in the text field
    text_field = driver.find_element(By.ID, 'ctl00_cphMain_txtRNCCedula')
    text_field.send_keys("101013702")

    # Click the button
    button = driver.find_element(By.ID, 'ctl00_cphMain_btnBuscarPorRNC')
    button.click()

    # Wait for the results page to load
    driver.implicitly_wait(10)

    # Get the results page title
    results_page_title = driver.title

    # Print the results page title
    print("Results page title:", results_page_title)

    #RNC
    rnc_empresa = driver.find_element(By.XPATH, '//*[@id="ctl00_cphMain_dvDatosContribuyentes"]/tbody/tr[1]/td[2]')

    print(rnc_empresa.text)
    #nombre empresa
    nombre_empresa = driver.find_element(By.XPATH, '//*[@id="ctl00_cphMain_dvDatosContribuyentes"]/tbody/tr[2]/td[2]')
    
    return nombre_empresa
