from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do driver do Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para rodar sem abrir o navegador (opcional)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL do LinkedIn
linkedin_url = "https://www.linkedin.com/jobs"

# Acessar a página de vagas do LinkedIn
driver.get(linkedin_url)
time.sleep(3)  # Espera a página carregar

# Busca de vagas: critérios definidos
job_title = "Desenvolvedor Junior ou Estágio"
keywords = "Python, JavaScript, Django, React"
location = "Presencial ou Remoto"

# Localizar os campos de pesquisa e preencher as informações
search_box = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Pesquisar vagas']")
search_box.clear()
search_box.send_keys(keywords)  # Digitar palavras-chave de busca
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Filtrando por localização (Presencial ou Remoto)
location_filter = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Pesquisar locais']")
location_filter.clear()
location_filter.send_keys(location)
location_filter.send_keys(Keys.RETURN)
time.sleep(3)

# Exemplo de como capturar as vagas encontradas
job_listings = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
for job in job_listings:
    title = job.find_element(By.CSS_SELECTOR, ".job-card-list__title").text
    company = job.find_element(By.CSS_SELECTOR, ".job-card-container__company-name").text
    location = job.find_element(By.CSS_SELECTOR, ".job-card-container__metadata-item").text
    print(f"Título: {title}\nEmpresa: {company}\nLocalização: {location}\n")

# Fechar o navegador
driver.quit()