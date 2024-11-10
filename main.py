from twilio.rest import Client


#Infos de login
account_sid = "SEU ACCOUNT SID"
token = "SEU TOKEN"
client = Client(account_sid, token)

#Infos de envio
remetente = "SEU NÚMERO TWILIO"
destino = "NÚMERO QUE VAI RECEBER"

#Mensagem
mensagem = client.messages.create(
    to = destino,
    from_ = remetente,
    body = "SUA MENSAGEM")
print(mensagem.sid)