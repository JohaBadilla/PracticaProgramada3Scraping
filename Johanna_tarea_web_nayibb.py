
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
ruta = "C:/Users/Johanna UB/esktop/martes/PracticaProgramada3Scraping"
df.to_excel(ruta, index=False)
