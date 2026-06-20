import os
import json
import uuid
import hashlib
import hmac
import base64
import random
import secrets
import jwt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv
load_dotenv()
class CryptoUtils:
    OmeySalt = os.getenv("OmeySalt", "")
    LoginSalt = os.getenv("LoginSalt", "vAOUf4i4VSfnRPTzdUL9IB2a2IQR2kFz")
    Salt = os.getenv("Salt", "uLRYVTQiYfokTij2sHLrIQYYv4y6zaoM")

    @staticmethod
    def WriteJson(Patch, Json):
        with open(f"{Patch}.json", 'w', encoding='utf-8') as f:
            json.dump(Json, f, indent=2)

    @staticmethod
    def OmeyEncrypt(text):
        pass # stripped due to skids
    @staticmethod
    def OmeyDecrypt(encryptedString):
        pass # stripped due to skids

    @staticmethod
    def Hash(type_name, input_str):
        h = hashlib.new(type_name)
        h.update(input_str.encode('utf-8'))
        return h.hexdigest()

    @staticmethod
    def CreateJWT(Payload, Secret):
        pass
    @staticmethod
    def gerarAverageMmr():
        min_val = 0xd00000
        max_val = 0xdfffff
        mmr = random.randint(min_val, max_val)
        return hex(mmr)[2:].upper()

    @staticmethod
    def createJWTV2(payload, signature):
        pass # stripped due to skids
    @staticmethod
    def DecodeJWT(Encoded):
        pass # stripped due to skids

    @staticmethod
    def CreateLoginHash(DeviceId, Version, Timestamp="", StumbleId="", SteamTicket="", ScopelyId=""):
        text = (
            str(CryptoUtils.LoginSalt) +
            str(DeviceId) +
            str(Version) +
            str(SteamTicket) +
            str(Timestamp) +
            str(StumbleId) +
            str(ScopelyId)
        )
        return CryptoUtils.Hash("sha1", text)

    @staticmethod
    def CreateRegularHash(deviceId, googleid, token, timestamp, stumbleid, url, body):
        if body is None:
            body = ""
        
        text = (
            str(CryptoUtils.Salt) +
            str(deviceId) +
            str(googleid) +
            str(token) +
            str(timestamp) +
            str(url) +
            str(body) +
            str(stumbleid)
        )
        return CryptoUtils.Hash("sha1", text)

    @staticmethod
    def VerifyHash(Auth, url, body):
        if isinstance(Auth, str):
            Auth = json.loads(Auth)
        
        DeviceId = Auth.get('DeviceId', '')
        GoogleId = Auth.get('GoogleId', '')
        Token = Auth.get('Token', '')
        Timestamp = Auth.get('Timestamp', '')
        StumbleId = Auth.get('StumbleId', '')
        
        text = (
            str(CryptoUtils.Salt) +
            str(DeviceId) +
            str(GoogleId) +
            str(Token) +
            str(Timestamp) +
            str(url) +
            str(body) +
            str(StumbleId)
        )
        
        calculated_hash = CryptoUtils.Hash("sha1", text)
        return Auth.get('Hash') == calculated_hash

    @staticmethod
    def CreateParms(type_name):
        main_parms = str(uuid.uuid4())
        if type_name == "event":
            event_parms = str(uuid.uuid4())
            return event_parms
        return main_parms

    @staticmethod
    def CreateParmsV2(type_name):
        def gen_text():
            chars = "0123456789abcdefghijklmnopqrstuvwxyz"
            random_str = "".join(random.choice(chars) for _ in range(34))
            return base64.b64encode(random_str.encode('utf-8')).decode('utf-8')

        return gen_text()

    @staticmethod
    def CreateGameId(type_name):
        pass # stripped due to skids

    @staticmethod
    def SessionToken():
       pass # stripped due to skids

    @staticmethod
    def GenCaracters(amount):
        pass # stripped due to skids

    @staticmethod
    def GenAndroidId():
        return str(uuid.uuid4()).replace("-", "")

    @staticmethod
    def GenWebGlId():
        return "webgl_" + CryptoUtils.GenAndroidId()

    @staticmethod
    def GenIosId():
        return str(uuid.uuid4()).upper()

    @staticmethod
    def formatNumber(number):
        if not isinstance(number, (int, float)):
            return "undefined"
        return "{:,}".format(number)

