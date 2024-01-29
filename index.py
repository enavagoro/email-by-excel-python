import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Ruta a tu archivo JSON de credenciales
json_keyfile = './credentials.json'

# Alcance de acceso requerido
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Autenticación usando las credenciales
creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile, scope)
client = gspread.authorize(creds)

# Abre la hoja de cálculo por URL
url = 'https://docs.google.com/spreadsheets/d/1us5R4KL1ArEa2wh39Zu6CFN2EcTbiQey9cospgyILY4/edit#gid=0'
sheet = client.open_by_url(url)

# Selecciona la hoja de trabajo (worksheet) que deseas leer
worksheet = sheet.get_worksheet(0)  # Suponiendo que es la primera hoja (índice 0)

# Lee la columna de correos electrónicos en un arreglo
emails = worksheet.col_values(1)  # Suponiendo que los correos están en la primera columna (columna 1)

# Imprime los correos electrónicos como un arreglo

# Usar un bucle for para recorrer el arreglo, comenzando desde el segundo elemento
for email in emails[1:]:
    print(email)
