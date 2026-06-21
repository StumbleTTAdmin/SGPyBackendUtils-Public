
from StumbleUtils import Backend

Backend.switchServer("live")

login = Backend.login(version="0.99")
print(login)
