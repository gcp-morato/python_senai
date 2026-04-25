import requests

topico = "Cleisson"

url = f"https://ntfy.sh/{topico}"

requests.post(url, data = "Alerta enviado por Cleisson".encode('utf-8'))

print ('Mensagem Enviada! Confira o seu celular ou Site')