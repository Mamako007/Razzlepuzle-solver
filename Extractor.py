from bs4 import BeautifulSoup
import os

# Leer el archivo HTML
# Definir la ruta al archivo HTML
folder_path = os.path.dirname(os.path.abspath(__file__))
file_name = "html.html"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parsear el HTML con BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Almacenar las listas extraídas
# Los números aparecen en varias secciones del HTML.
numbers_grid = []  # Para la cuadrícula grande
number_lists = []  # Para las listas inferiores

# Extraer la cuadrícula de números (primera tabla o sección)
for row in soup.find_all("tr"):  # Asumiendo que la cuadrícula está en una tabla
    grid_row = [int(cell.text) for cell in row.find_all("td") if cell.text.isdigit()]
    if grid_row:
        numbers_grid.append(grid_row)

# Extraer las listas inferiores de números
for paragraph in soup.find_all("p"):  # Ajusta si las listas están en etiquetas diferentes
    text = paragraph.get_text(strip=True)
    if text:
        list_numbers = [int(num) for num in text.split() if num.isdigit()]
        if list_numbers:
            number_lists.append(list_numbers)

# Imprimir los resultados
print("Cuadrícula de números:", numbers_grid)
print("Listas inferiores:", number_lists)
