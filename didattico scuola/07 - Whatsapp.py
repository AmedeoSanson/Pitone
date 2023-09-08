from logger import Logger as LG
import datetime

print("Ciao, stai usando whatsapp!")

whatsappLog = LG.Logger("LOW")

whatsappLog.log("L'utente si è appena connesso")


datetime.datetime.now()