
import pandas as pd  
from selenium import webdriver
from selenium.webdriver.common.by import By 

#URL de la página.
PAGINA_PRINCIPAL = "https://www.scrapethissite.com/pages/simple/"

# Inicializa el navegador 
navegador = webdriver.Chrome()
navegador.get(PAGINA_PRINCIPAL)  
navegador.implicitly_wait(10)

datos = []
paises = navegador.find_elements(By.CLASS_NAME, 'country')

for pais in paises:
    nombre = pais.find_element(By.CLASS_NAME, 'country-name')
    capital = pais.find_element(By.CLASS_NAME, 'country-capital')
    poblacion = pais.find_element(By.CLASS_NAME, 'country-population')
    area = pais.find_element(By.CLASS_NAME, 'country-area')    

    datos.append({
        'NOMBRE': nombre.text,
        'CAPITAL': capital.text,
        'POBLACION': poblacion.text,
        'AREA': area.text
    })

navegador.quit()

# Crear un DataFrame con los datos extraídos
df = pd.DataFrame(datos)
print(df)

# Guardar los datos en un archivo Excel
ruta = "C:/Users/Johanna UB/Downloads/Nayib_proyecto.xlsx"
df.to_excel(ruta, index=False)



#Link repositorio
#https://github.com/JohaBadilla/PracticaProgramada3Scraping.git

## Preguntas y respuestas:

#1. *¿Qué funciones del código conocían antes de hacer el script?*
#   -Conocía las funciones de pandas para manejar datos y la biblioteca webdriver_manager para gestionar el driver de Selenium.

#2. *¿Entendió algo nuevo con respecto a lo que ya conocía?*
#   -Aprendí a utilizar webdriver_manager para instalar automáticamente el driver de Chrome, lo que facilita la configuración del entorno.

#3. *¿Qué funciones nuevas aprendió? Defínalas en sus propias palabras.*
#   -Aprendí a usar webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 
# para inicializar el navegador de manera eficiente y navegador.find_elements(By.CLASS_NAME, 'team') para encontrar múltiples elementos con Selenium.

#4. *¿Necesitó nuevos conceptos para crear el script? Defínalos en sus propias palabras.*
#   -Necesité entender el concepto de web scraping con Selenium, que implica automatizar un navegador web para interactuar con páginas web y extraer datos.
#  Además, utilicé la opción de "headless" para ejecutar Chrome sin una interfaz gráfica, lo que es útil para scripts automatizados en servidores.