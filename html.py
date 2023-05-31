from selenium import webdriver


s = Service('D:\\YERSON\\chromedriver.exe')
ruta_descarga = "D:\\Usuario\\Downloads\\"

db = base_datos()

file_name = ""

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {
    "download.default_directory": "D:\\Usuario\\Downloads\\",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
chromeOptions.add_argument("--headless")
self.driver = webdriver.Chrome(service=s, options=chromeOptions)

# Abrir la página web deseada
driver.get("https://www.google.com/")

# Obtener el HTML de la página
html = driver.page_source

# Cerrar el controlador del navegador
driver.quit()

# Guardar el HTML en un archivo
with open("pagina.html", "w", encoding="utf-8") as archivo:
    archivo.write(html)