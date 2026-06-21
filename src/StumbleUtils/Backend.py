import os 
import json 
import time 
import random 
import requests 
from datetime import datetime 
from dotenv import load_dotenv 

try:
    from .CryptoUtils import CryptoUtils
except ImportError:
    from CryptoUtils import CryptoUtils

load_dotenv ()
class Console :
    @staticmethod 
    def log (prefix ,message ,color =None ):
        print (f"[{prefix }] {message }")

    @staticmethod 
    def warn (prefix ,message ):
        print (f"[WARN] [{prefix }] {message }")

    @staticmethod 
    def error (prefix ,message ):
        print (f"[ERROR] [{prefix }] {message }")

class Backend :
    baseUrl ="https://api.stumbleguys.com"
    LogsDebug =False 
    FarmMode =False 
    proxy =None 
    User ={
    "id":None ,
    "deviceId":None ,
    "stumbleId":None ,
    "username":None ,
    "country":None ,
    "token":None ,
    "version":None ,
    "created":None ,
    "skillRating":None ,
    "experience":None ,
    "crowns":None ,
    "balances":[],
    "skins":[],
    "battlePass":{},
    "rewards":[],
    "xpRoad":{}
    }

    PhotonJwt =None 

    Timestamps ={
    "LastLogin":None ,
    "LastFinishRound":{},
    "LastFinishRoundV4":{},
    }

    TournamentX ={
    "id":None ,
    "minVersion":None ,
    "rounds":None ,
    "awards":None ,
    "entryCurrencyType":None ,
    "entryCurrencyCost":None ,
    "entryCurrencyType2":None ,
    "entryCurrencyCost2":None ,
    }

    EquippedCosmetics ={
    "skin":None ,
    }

    ActionEmotes =None 

    PlayerRank ={
    "RankId":0 ,
    "RankName":"Unranked",
    "RankIcon":"<:Ranked:1272235135428722719>",
    }

    FinishRound =None 

    Event ={
    "Id":None ,
    "StartDateTime":None ,
    "EndDateTime":None ,
    "EventRounds":[],
    }

    Ranked ={
    "Id":None ,
    "StartDateTime":None ,
    "EndDateTime":None ,
    "MapPools":None ,
    }

    BattlePass =[]
    RoundLevels_v2 =[]
    Skins_v4 =[]
    MissionObjectives =[]
    PurchasableItems =[]
    SharedType ="LIVE"
    GameVersion ="0.99"

    OmeySalt =CryptoUtils .OmeySalt 
    TourXJwtSecret ="???"
    RankedJwtSecret ="???"
    RankedPlaySettings ={}



    @classmethod 
    def Timestamp (cls ):
        return int (time .time ())
    

    @classmethod 
    def getTimestamp (cls ):
        return int (time .time ())

    @classmethod 
    def SendWebHook (cls ,content ,webhook ):
        try :
            requests .post (webhook ,json =content ,headers ={"Content-Type":"application/json"})
        except Exception :
            pass 

    @classmethod 
    def SendToDiscord (cls ,RequestData ):
        rewards =RequestData ["Rewards"]
        profile =RequestData ["Profile"]
        extra =RequestData ["Extra"]
        balances =RequestData ["Balances"]
        xp_road =RequestData ["XpRoad"]

        def build_rewards_text ():
            text =""
            if int (str (rewards ["Crowns"]).replace (",",""))>0 :
                text +=f"<:BF:1343647536144973894>  {rewards ['Crowns']} Crowns <:crown:1343642077245734955>\n"
            if int (str (rewards ["Trophys"]).replace (",",""))>0 :
                text +=f"<:BF:1343647536144973894>  {rewards ['Trophys']} Trophys <:trophy:1343642129280401460>\n"
            if int (str (rewards ["XP"]).replace (",",""))>0 :
                text +=f"<:BF:1343647536144973894>  {rewards ['XP']} XP <:xp:1343642179968434309>\n"
            if int (str (rewards ["Gems"]).replace (",",""))>0 :
                text +=f"<:BF:1343647536144973894>  {rewards ['Gems']} Gems <:gems:1343642328157520013>\n"
            if int (str (rewards ["Tokens"]).replace (",",""))>0 :
                text +=f"<:BF:1343647536144973894>  {rewards ['Tokens']} Tokens <:token:1343642454301081652>\n"
            if int (str (rewards ["AbilityTokens"]).replace (",",""))>0 :
                text +=f"<:BF:1343647536144973894>  {rewards ['AbilityTokens']} Ability Tokens <:AEC:1354891711461068942>"
            return text 

        embed ={
        "username":".gg/sgpriv",
        "avatar_url":"https://images-ext-1.discordapp.net/external/9I7XIptjKwFakineibY56EYIB994rer4LD7-I24ws9A/%3Fsize%3D2048/https/cdn.discordapp.com/icons/1340058694271893575/12fe986c2a5545404bc96d2630b08e1e.png",
        "embeds":[
        {
        "title":"[Auto Get Crowns <:crown:1343642077245734955>]",
        "fields":[
        {
        "name":"Profile",
        "value":f"<:BF:1343647536144973894> Username - {profile ['Username']} <:id:1343644382456447117>\n<:BF:1343647536144973894> Country - {profile ['Country']} :flag_{profile ['Country'].lower ()}:\n<:BF:1343647536144973894> Crowns - {profile ['Crowns']} <:crown:1343642077245734955>\n<:BF:1343647536144973894> Trophys - {profile ['Trophys']} <:trophy:1343642129280401460>\n<:BF:1343647536144973894> Version - {extra ['GameVersion']} <:Settings:1354891517738619020>",
        "inline":True ,
        },
        {
        "name":"Rewards",
        "value":build_rewards_text (),
        "inline":True ,
        },
        {"name":"ㅤ","value":"ㅤ","inline":True },
        {
        "name":"Balances",
        "value":f"<:BF:1343647536144973894> Gems - {balances ['Gems']} <:gems:1343642328157520013>\n<:BF:1343647536144973894> Tokens - {balances ['Tokens']} <:token:1343642454301081652>\n<:BF:1343647536144973894> Ability Tokens - {balances ['AbilityTokens']} <:AEC:1354891711461068942>",
        "inline":True ,
        },
        {
        "name":"Xp-Road",
        "value":f"<:BF:1343647536144973894> XP - {xp_road ['XP']} <:xp:1343642179968434309>\n<:BF:1343647536144973894> Level - {xp_road ['Level']}",
        "inline":True ,
        },
        {"name":"ㅤ","value":"ㅤ","inline":True },
        {
        "name":"Dev",
        "value":f"<:BF:1343647536144973894> Owner - <@1038590507149951077> <a:WhiteCrown:1354891781749346405>\n<:BF:1343647536144973894> Script Version - {os .getenv ('version','Unknown')} <:Dev:1354891862019674253>\n``` {extra ['Auth']} ```",
        },
        ],
        "footer":{"text":"📅"},
        "timestamp":extra ['DateTimestamp'],
        "thumbnail":{
        "url":f"https://cdn.glitch.global/efae7c5b-36f6-4b8b-86c4-dcc2d7153909/{extra ['SkinID']}_icon.png",
        },
        }
        ],
        }


        if RequestData ['Rewards']['Total']!=0 :
            cls .SendWebHook (embed ,extra ['WebHook'])

    @classmethod 
    def wait (cls ,ms =1000 ):


        if ms <=60 :
            ms =ms *1000 
        time .sleep (ms /1000.0 )

    @classmethod 
    def GetLevel (cls ,xp ):
        return int ((xp +1032700 )/30000 )-9 

    @classmethod 
    def _save_user_file (cls ):
        try :
            safe_username =cls .User .get ('username','unknown').replace ('/','_')
            os .makedirs ('Users',exist_ok =True )
            with open (f"Users/{safe_username }#{cls .SharedType }.json",'w')as f :
                json .dump (cls .User ,f ,indent =2 )
        except Exception :
            pass 

    @classmethod 
    def Get (cls ,Patch ):
        if cls .User .get ('stumbleId'):
            Authorization =cls .getAuthHeader (Patch )
            headers ={
            "authorization":Authorization ,
            "Content-Type":"application/json",
            "User-Agent":"Unity-2022.3.59f1",
            }
            try :
                response =requests .get (cls .baseUrl +Patch ,headers =headers )
                if response .ok :
                    try :
                        data =response .json ()
                        if 'User'in data :
                            cls .User =data ['User']
                            cls ._save_user_file ()
                        return {"message":"Sucess",**data }
                    except json .JSONDecodeError :
                        return {"message":"Sucess","text":response .text }
                else :
                    if cls .LogsDebug and "/user/unlink"not in Patch :
                        Console .error ("GET",f"{Patch } Failed : {response .status_code } | {response .text }")
                    return {"message":"Error","status":response .status_code }
            except Exception as e :
                return {"message":"Error","details":str (e )}
        else :
            Console .warn ("Backend","Login in one acc first")
            return {"message":"Error"}

    @classmethod 
    def Delete (cls ,Patch ):
        if cls .User .get ('stumbleId'):
            Authorization =cls .getAuthHeader (Patch )
            headers ={
            "authorization":Authorization ,
            "Content-Type":"application/json",
            "User-Agent":"Unity-2022.3.59f1",
            }
            try :
                response =requests .delete (cls .baseUrl +Patch ,headers =headers )
                if response .ok :
                    try :
                        data =response .json ()
                        if 'User'in data :
                            cls .User =data ['User']
                            cls ._save_user_file ()
                        return {"message":"Sucess",**data }
                    except json .JSONDecodeError :
                        return {"message":"Sucess"}
                else :
                    if cls .LogsDebug and "/user/unlink"not in Patch :
                        Console .error ("DELETE",f"{Patch } Failed : {response .status_code } | {response .text }")
                    return {"message":"Error","status":response .status_code }
            except Exception :
                return {"message":"Error"}
        else :
            Console .warn ("Backend","Login in one acc first")
            return {"message":"Error"}

    @classmethod 
    def GetV2 (cls ,Patch ):
        try :
            headers ={
            "Content-Type":"application/json",
            "User-Agent":"Unity-2022.3.59f1",
            }
            response =requests .get (cls .baseUrl +Patch ,headers =headers )
            if response .ok and "application/json"in response .headers .get ("Content-Type",""):
                return response .json ()
            return response .text 
        except Exception :
            return ""

    @classmethod 
    def GetV3 (cls ,endpoint ):
        if not cls .User .get ('stumbleId'):
            print ("[Backend] Login in one account first")
            return 

        try :
            Authorization =cls .getAuthHeader (endpoint )
            headers ={
            "authorization":Authorization ,
            "User-Agent":"Unity-2022.3.59f1",
            "Content-Type":"application/json",
            }
            response =requests .get (cls .baseUrl +endpoint ,headers =headers )

            if response .ok :
                try :
                    data =response .json ()
                except :
                    data =response .text 

                if isinstance (data ,dict )and 'User'in data :
                    cls .User =data ['User']
                    cls ._save_user_file ()

                if isinstance (data ,dict ):
                    return {"message":"Success",**data }
                return {"message":"Success","data":data }
            else :
                if cls .LogsDebug and "/user/unlink"not in endpoint :
                    Console .error ("GETV3",f"{endpoint } Failed : {response .status_code } | {response .text }")
                return {"message":"Error","status":response .status_code ,"details":response .text }

        except Exception as err :
            print ("GETV3 Exception:",err )
            return {"message":"Exception","error":str (err )}

    @classmethod 
    def Post (cls ,Patch ,Body =""):
        if cls .User .get ('stumbleId'):
            if Body is None :Body =""
            Authorization =cls .getAuthHeader (Patch ,Body )
            headers ={
            "authorization":Authorization ,
            "Content-Type":"application/json",
            "User-Agent":"Unity-2022.3.59f1",
            }
            try :

                response =requests .post (cls .baseUrl +Patch ,headers =headers ,data =Body )

                if response .ok :
                    data ={}
                    if response .text :
                        try :
                            data =response .json ()
                            if 'User'in data :
                                cls .User =data ['User']
                                cls ._save_user_file ()
                        except :
                            pass 
                    return {"StatusCode":response .status_code ,**data }
                else :
                    if cls .LogsDebug :
                        if "/user/link"not in Patch and "/battlepass/claimv3"not in Patch :
                            Console .error ("POST",f"{Patch } Failed : {response .status_code } | {response .text }")
                    return {"message":"Error","status":response .status_code }
            except Exception :
                return {"message":"Error"}
        else :
            Console .warn ("Backend","Login in one acc first")
            return {"message":"Error"}

    @classmethod 
    def Put (cls ,Patch ,Body =""):
        if cls .User .get ('stumbleId'):
            if Body is None :Body =""
            Authorization =cls .getAuthHeader (Patch ,Body )
            headers ={
            "authorization":Authorization ,
            "Content-Type":"application/json",
            "User-Agent":"Unity-2022.3.39f1",
            }
            try :
                response =requests .put (cls .baseUrl +Patch ,headers =headers ,data =Body )
                if response .ok :
                    data =response .json ()
                    if 'User'in data :
                        cls .User =data ['User']
                    if 'equippedCosmetics'in data :
                        ec =data ['equippedCosmetics']
                        cls .EquippedCosmetics ={
                        "skin":ec .get ("skin")or "SKIN1",
                        "color":ec .get ("color")or "COLOR1",
                        "animation":ec .get ("animation")or "animation1",
                        "footsteps":ec .get ("footsteps")or "footsteps_smoke",
                        "emote1":ec .get ("emote1")or "emote_cry",
                        "emote2":ec .get ("emote2")or "emote_hi",
                        "emote3":ec .get ("emote3")or "emote_gg",
                        "emote4":ec .get ("emote4")or "emote_haha",
                        "actionEmote1":ec .get ("actionEmote1"),
                        "actionEmote2":ec .get ("actionEmote2"),
                        "actionEmote3":ec .get ("actionEmote3"),
                        "actionEmote4":ec .get ("actionEmote4"),
                        }
                    return {"StatusCode":response .status_code ,**data }
                else :
                    if cls .LogsDebug :
                        Console .error ("PUT",f"{Patch } Failed : {response .status_code } | {response .text }")
                    return {"message":"Error","status":response .status_code }
            except Exception :
                return {"message":"Error"}
        else :
            Console .warn ("Backend","Login in one acc first")
            return {"message":"Error"}

    @classmethod 
    def switchServer (cls ,url ):
        mapping ={
        "live":"https://api.stumbleguys.com",
        "stage":"https://api.stage.stumbleguys.com",
        "beta":"https://api.beta.stumbleguys.com",
        "test":"https://api.test.stumbleguys.com",
        "dev":"https://api.dev1.stumbleguys.com"
        }
        cls .baseUrl =mapping .get (url ,url )
        Console .log ("Backend",f"Server successfully switched to: {cls .baseUrl }\n")

    @classmethod 
    def onlinecheck (cls ):
        retryCount =0 
        retryDelay =30000 
        while True :
            response =cls .GetV2 ("/onlinecheck")

            if response =="OK":
                if retryCount >0 :
                    Console .log ("Backend","Server is back online!")
                return 

            retryCount +=1 
            Console .warn ("Backend",f"Game in maintenance, retrying in {retryDelay /1000 } seconds... (Attempt {retryCount })")
            cls .wait (retryDelay )

    @classmethod 
    def updateshared (cls ):
        try :

            LoginResponse =cls .login ("",CryptoUtils .GenAndroidId (),True )
            response =cls .Post ("/game-config")
            sharedData =response 


            if response .get ("message")!="Error":

                Config =sharedData .get ("Config",{})
                Versions =Config .get ("Versions",{})
                LastSharedGameVersion =Versions .get ("MinimumVersionToPlay","0.0").replace (".","_")

                if cls .LogsDebug :
                    os .makedirs (f"Save/{LastSharedGameVersion }",exist_ok =True )
                    with open (f"Save/{LastSharedGameVersion }/User.json",'w')as f :
                        json .dump (LoginResponse ,f ,indent =2 )

                    shared_ver =sharedData .get ("_SharedVersion","unknown")
                    with open (f"Save/{LastSharedGameVersion }/Shared-{shared_ver }.json",'w')as f :
                        json .dump (sharedData ,f ,indent =2 )


                cls .User ={k :None for k in cls .User }

                cls .BattlePass =sharedData .get ("BattlePassesV3",[])
                cls .GameVersion =Versions .get ("AndroidLastVersionAvailable",cls .GameVersion )

                if "api.stumbleguys.com"in cls .baseUrl :cls .SharedType ="LIVE"
                elif "stage"in cls .baseUrl :cls .SharedType ="STAGE"
                elif "beta"in cls .baseUrl :cls .SharedType ="BETA"
                elif "test"in cls .baseUrl :cls .SharedType ="TEST"
                else :cls .SharedType ="undefined"

                cls .RoundLevels_v2 =sharedData .get ("RoundLevels_v2",[])
                cls .Skins_v4 =sharedData .get ("Skins_v4",[])
                cls .MissionObjectives =sharedData .get ("MissionObjectives",[])
                cls .ActionEmotes =[]
                cls .PurchasableItems =sharedData .get ("PurchasableItems",[])
                cls .RankedPlaySettings =sharedData .get ("RankedPlaySettings",{})

                Console .log ("Backend","Shared Updated")
                Console .log ("Backend",f"Game Version : {cls .GameVersion }")

                now =datetime .now ()
                game_events =sharedData .get ("GameEvents",[])


                if isinstance (game_events ,list ):
                    activeEvents =[]
                    for event in game_events :
                        start =datetime .fromisoformat (event ["StartDateTime"].replace ('Z','+00:00'))
                        end =datetime .fromisoformat (event ["EndDateTime"].replace ('Z','+00:00'))

                        if start .timestamp ()<=now .timestamp ()<=end .timestamp ():
                            activeEvents .append (event )

                    if activeEvents :
                        def get_max_reward (ev ):
                            return sum (r .get ("max",0 )for r in ev ["WinnerRewards"]["Rewards"])

                        def getEventWithBestWinnerRewards (events ):
                            if not events :return None 
                            return max (events ,key =get_max_reward )

                        def prioritizeEvents (events ):
                            eventsWithCrowns =[e for e in events if any (r ["type"]=="CROWNS"for r in e ["WinnerRewards"]["Rewards"])]
                            return getEventWithBestWinnerRewards (eventsWithCrowns )if eventsWithCrowns else getEventWithBestWinnerRewards (events )

                        eventsByRounds =[
                        [e for e in activeEvents if len (e ["EventRounds"])==3 ],
                        [e for e in activeEvents if len (e ["EventRounds"])==2 ],
                        [e for e in activeEvents if len (e ["EventRounds"])==1 ],
                        ]

                        selectedEvent =None 
                        for events in eventsByRounds :
                            if events :
                                selectedEvent =prioritizeEvents (events )
                                if selectedEvent :break 

                        if selectedEvent :
                            cls .Event ["Id"]=selectedEvent ["Id"]
                            cls .Event ["StartDateTime"]=selectedEvent ["StartDateTime"]
                            cls .Event ["EndDateTime"]=selectedEvent ["EndDateTime"]
                            cls .Event ["EventRounds"]=selectedEvent ["EventRounds"]
                            cls .Event ["WinnerRewards"]=selectedEvent ["WinnerRewards"]

                            Console .log ("Backend","Event Found ⤵️")

                            rewardStrings =[]
                            for reward in cls .Event ["WinnerRewards"]["Rewards"]:
                                if reward .get ("chance")==100 :
                                    rewardStrings .append (f"{CryptoUtils .formatNumber (reward .get ('max'))} {reward .get ('type')}")

                            Console .log ("Backend",f"Id : {cls .Event ['Id']}")
                            Console .log ("Backend",f"Rounds : {len (cls .Event ['EventRounds'])}")
                            Console .log ("Backend","Rewards : "+" | ".join (reversed (rewardStrings )))
                            Console .log ("Backend",f"Start : {cls .Event ['StartDateTime']}")
                            Console .log ("Backend",f"Finish : {cls .Event ['EndDateTime']}")
                    else :
                        Console .warn ("Backend","No active events currently\n")


                if cls .RankedPlaySettings :
                    seasons =cls .RankedPlaySettings .get ("Seasons",[])
                    activeSeasons =[]
                    for season in seasons :

                         start =datetime .fromisoformat (season ["StartDateTime"].replace ('Z','+00:00'))
                         end =datetime .fromisoformat (season ["EndDateTime"].replace ('Z','+00:00'))
                         if start .timestamp ()<=now .timestamp ()<=end .timestamp ():
                             activeSeasons .append (season )

                    if activeSeasons :
                        Season =random .choice (activeSeasons )
                        cls .Ranked ["Id"]=Season ["Id"]
                        cls .Ranked ["StartDateTime"]=Season ["StartDateTime"]
                        cls .Ranked ["EndDateTime"]=Season ["EndDateTime"]
                        cls .Ranked ["MapPools"]=Season ["MapPools"]
                    else :
                        Console .warn ("Backend","No active ranked season currently\n")
            else :
                 Console .error ("Backend",f"Shared Update Error: {response .get ('status')}")

        except Exception as error :
             Console .error ("Backend",f"Shared Update Exception: {error }")

    @classmethod 
    def login (cls ,StumbleId ="",DeviceId ="", version="", DontLogs =False ,ScopelyId ="",SteamTicket =""):
        try :
            LoginTimestamp =cls .Timestamp ()
            AndroidId =CryptoUtils .GenAndroidId ()

            if not StumbleId and not DeviceId :
                StumbleId =""
                DeviceId =AndroidId 

            if StumbleId and not DeviceId :

                DeviceId =CryptoUtils .Hash ("md5",StumbleId +cls .OmeySalt )

            loginBody ={
            "AdvertisingId":None ,
            "AppleId":"",
            "Version":version,
            "DeviceId":DeviceId ,
            "FacebookId":"",
            "GoogleId":"",
            "Hash":CryptoUtils .CreateLoginHash (DeviceId ,version ,LoginTimestamp ,StumbleId ,SteamTicket ,ScopelyId ),
            "Id":0 ,
            "ScopelyId":ScopelyId ,
            "StumbleId":StumbleId ,
            "Timestamp":LoginTimestamp ,
            "SteamTicket":SteamTicket ,
            }

            if cls .LogsDebug and not DontLogs :
                Console .log ("Crypto",f"Login Hash : {loginBody ['Hash']}\n")

            if cls .Timestamps ["LastLogin"]is not None :
                elapsedTime =(time .time ()*1000 )-cls .Timestamps ["LastLogin"]
                waitTime =max (5000 -elapsedTime ,0 )
                if waitTime >0 :
                    cls .wait (waitTime )

            headers ={
            "Content-Type":"application/json",
            "User-Agent":"Unity-2022.3.39f1",
            }

            response =requests .post (cls .baseUrl +"/user/login/v2",json =loginBody ,headers =headers )

            if response .ok :
                data =response .json ()
                cls .User =data .get ('User',cls .User )
                cls .EquippedCosmetics =data .get ('equippedCosmetics',cls .EquippedCosmetics )
                cls .Timestamps ["LastLogin"]=time .time ()*1000 
                cls .PhotonJwt =data .get ('PhotonJwt')

                if not DontLogs :
                     Console .log ("Backend",f"Logged In : {cls .User .get ('username')} | {cls .User .get ('stumbleId')} | {datetime .now ().strftime ('%d/%m/%Y, %H:%M:%S')}\n")
                return data 
            else :
                errorText =response .text 
                if response .status_code ==403 :
                    print (errorText )
                    Console .error ("Backend","Login Failed : Banned account\n")
                else :
                    Console .error ("Backend",f"Login Failed : {response .status_code } - {errorText }\n")
                    cls .Timestamps ["LastLogin"]=time .time ()*1000 
        except Exception as error :
            Console .error ("Network Error",f"An error occurred during login: {error }")

    @classmethod 
    def deleteaccount (cls ):
        RequestResponse =cls .Get ("/user/deleteaccount")
        Console .log ("Backend","Account deleted successfully \n")
        return RequestResponse 

    @classmethod 
    def search (cls ,username ):
        try :
            body =json .dumps ({"UserName":username })
            response =cls .Post ("/friends/search",body )
            if os.environ.get("StumbleLabs_Api_Key") is not None:
                labs_response = requests.post(
                    "https://api.stumblelabs.net/api/live/users/search",
                    json={"username": username},
                    headers={"x-api-key": os.environ.get("StumbleLabs_Api_Key")},
                )
                Console.log("Backend", f"StumbleLabs Search Response: {labs_response.json()}\n")
            if not response or "message" not in response:
                return {"message": "Error"}
            return response 
        except :
            return {"message":"Error"}

    @classmethod 
    def purchase (cls ,item ):
        return cls .Get ("/economy/purchase/"+item )

    @classmethod 
    def purchaseluckyspinwheel (cls ):
        default_free_spins =cls .getBalanceAmount ("default_free_spins")
        default_free_ad_spins =cls .getBalanceAmount ("default_free_ad_spins")

        if default_free_spins >0 or default_free_ad_spins >0 :
            response =cls .Post ("/economy/purchaseluckyspinwheel","")
            if response .get ("message")!="Error":
                Console .log ("Backend",f"🎉 {cls .User .get ('username')} used a Lucky Spin!")

                if 'User'in response and 'Rewards'in response ['User']:
                    for reward in response ['User']['Rewards']:
                        if reward .get ('type')=="CURRENCY":
                            Console .log ("Backend",f"✨ Type: {reward .get ('type')} | Balance: {reward .get ('typeInfo')} | 💸 Amount: {reward .get ('amount')} | 💰 Balance: {cls .getBalanceAmount (reward .get ('typeInfo'))}\n")
                        elif reward .get ('type')=="SKIN":
                            Console .log ("Backend",f"✨ Type: {reward .get ('type')} | 🎭 Skin: {reward .get ('typeInfo')}\n")
                        return True 
        else :
            Console .log ("Backend","🚫 Insufficient funds to use the Lucky Spin.")
            return False 

    @classmethod 
    def purchaseV2 (cls ,item ,log =True ):
        resp =cls .Post ("/economy/purchaseV2",json .dumps ({
        "ExtraParameters":{"reference":"shop"},
        "GachaPulls":1 ,
        "GemsTopUpAmount":0 ,
        "IsOneStopShopPurchase":True ,
        "ItemId":item ,
        "WithGemsTopUp":False ,
        }))




        if log and 'Rewards'in cls .User :

             for reward in cls .User .get ('Rewards',[]):
                print (reward )
                if reward .get ('type')=="CURRENCY":
                    Console .log ("Backend",f"✨ Type: {reward .get ('type')} | Balance: {reward .get ('typeInfo')} | 💸 Amount: {reward .get ('amount')} | 💰 Balance: {cls .getBalanceAmount (reward .get ('typeInfo'))}\n")
                elif reward .get ('type')=="SKIN":
                    Console .log ("Backend",f"✨ Type: {reward .get ('type')} | 🎭 Skin: {reward .get ('typeInfo')}\n")
                return True 
        return resp 

    @classmethod 
    def GetFreeBattlePass (cls ):
        if not cls .User .get ('stumbleId'):return False 
        return cls .login (cls .User ['stumbleId'],"steam_76561199258142222",False ,"140000003E04012132E5B4B80E065C4D010010013CDCF967180000000100000002000000135A55230BB6837DA3AE0A0002000000B800000038000000040000000E065C4D01001001AC991900A6E089B1BF222C1A0000000030D9F967B08815680100211B0900010046831D00000000004D6F53793961C46CBEC01FB20C40B36A5415C08CBF81BF90BB15A3E2762AFB5714FD091C99F8BF00AE2DA63F1A5B88DE8145280120934DBC891F7CDA26B6ABCFE0718CCA865C42A55033C3A14FDDDC2EED2237BD1E35ADE42B0A632A7840EB0A2C3110FAB1899834EC711D0B73990F9AD7ABD8B1DA49DF3304EC4113B45FAAB5")

    @classmethod 
    def purchasebattlepass (cls ):
        bp =cls .User .get ('battlePass',{})

        has_purchased =bp .get ('haspurchased')if bp else False 

        if not has_purchased :
            if cls .getBalanceAmount ("gems")>=1200 :
                if cls .BattlePass and cls .BattlePass [0 ].get ('Bundles'):
                     name =cls .BattlePass [0 ]['Bundles']['Bundles'][0 ]['Name']
                     return cls .purchase (name )
            else :
                 needed =1200 -cls .getBalanceAmount ("gems")
                 Console .warn ("Backend",f"not enough gems, you need more {CryptoUtils .formatNumber (needed )}")
        else :
             Console .warn ("Backend","BattlePass already owned!")

    @classmethod 
    def set_proxy (cls ,proxy ):
        """Set proxy for all requests"""
        cls .proxy =proxy 
        if proxy :
            Console .log ("Backend",f"Proxy set: {proxy }")
        else :
            Console .log ("Backend","Proxy cleared")

    @classmethod 
    def _get_proxies (cls ):
        """Get proxies dict for requests"""
        if hasattr (cls ,'proxy')and cls .proxy :
            return {
            'http':f'http://{cls .proxy }',
            'https':f'http://{cls .proxy }'
            }
        return None 

    @classmethod 
    def updateusername (cls ,username ):
        try :
            body =json .dumps ({"Username":username })
            proxies =cls ._get_proxies ()
            Patch ="/user/v2/updateusername"
            Authorization =cls .getAuthHeader (Patch ,body )
            headers ={
            "authorization":Authorization ,
            "Content-Type":"application/json",
            "User-Agent":"Unity-2022.3.39f1",
            }
            response =requests .put (
            cls .baseUrl +Patch ,
            headers =headers ,
            data =body ,
            proxies =proxies ,
            timeout =30 
            )
            if response .ok :
                data =response .json ()
                if 'User'in data :
                    cls .User =data ['User']
                if 'equippedCosmetics'in data :
                    ec =data ['equippedCosmetics']
                    cls .EquippedCosmetics ={
                    "skin":ec .get ("skin")or "SKIN1",
                    "color":ec .get ("color")or "COLOR1",
                    "animation":ec .get ("animation")or "animation1",
                    "footsteps":ec .get ("footsteps")or "footsteps_smoke",
                    "emote1":ec .get ("emote1")or "emote_cry",
                    "emote2":ec .get ("emote2")or "emote_hi",
                    "emote3":ec .get ("emote3")or "emote_gg",
                    "emote4":ec .get ("emote4")or "emote_haha",
                    "actionEmote1":ec .get ("actionEmote1"),
                    "actionEmote2":ec .get ("actionEmote2"),
                    "actionEmote3":ec .get ("actionEmote3"),
                    "actionEmote4":ec .get ("actionEmote4"),
                    }
                return {"StatusCode":response .status_code ,**data }
            else :
                if cls .LogsDebug :
                    Console .error ("PUT",f"{Patch } Failed : {response .status_code } | {response .text }")
                return {"message":"Error","status":response .status_code }
        except Exception as e :
            Console .error ("Backend",f"❌ Error updating username: {e }")
            return {"message":"Error","error":str (e )}

    @classmethod 
    def UnlinkPlatform (cls ,Platform ):
        valid ={"scopely","google","apple","facebook"}
        if Platform not in valid :
            Console .warn ("Backend","Invalid Platform")
            return False 

    @classmethod 
    def UnlinkPlatform (cls ,Platform ):
        valid ={"scopely","google","apple","facebook"}
        if Platform not in valid :
            Console .warn ("Backend","Invalid Platform")
            return False 

        if Platform =="apple":
            Response =cls .Post ("/user/unlinkapple",json .dumps ({}))
        else :
            Response =cls .Get ("/user/unlink"+Platform )

        if Response .get ("message")!="Error":
             Console .log ("Backend",f"{cls .User .get ('username')} has been disconnected from {Platform }")
             return True 
        else :
             Console .warn ("Backend",f"{cls .User .get ('username')} is not linked on {Platform }")
             return False 

    @classmethod 
    def LinkPlatform (cls ,platform ,platformId ):
        valid ={"google","apple","facebook","scopely"}
        if platform not in valid :
             Console .warn ("Backend","Invalid Platform")
             return False 

        payload ={
        "UserId":cls .User .get ("id"),
        "Token":cls .User .get ("token")
        }
        print (payload )
        if platformId =="random":
             platformIdMD5 =CryptoUtils .Hash ("md5",f"{platform }-{cls .User .get ('username')}-{cls .OmeySalt }")
        else :
             platformIdMD5 =CryptoUtils .Hash ("md5",platformId )

        if platform =="google":payload ["GoogleId"]=platformIdMD5 
        elif platform =="apple":payload ["AppleId"]=platformIdMD5 
        elif platform =="facebook":payload ["FacebookId"]=platformIdMD5 
        elif platform =="scopely":payload ["ScopelyId"]=platformIdMD5 

        response =cls .Post (f"/user/link{platform }",json .dumps (payload ))
        if response .get ("message")!="Error":
            Console .log ("Backend",f"{cls .User .get ('username')} has been linked from {platform } | {platformIdMD5 }")
            return response 
            return payload 
        else :
            Console .warn ("Backend",f"{cls .User .get ('username')} is already linked on {platform }")
            return response 
            print (payload )

    @classmethod 
    def HandleActionEmotesShop (cls ):
        if not cls .ActionEmotes :
            Console .warn ("Backend","Theres no Action Emotes!")
            return False 

        Console .log ("Backend","Welcome to the Action Emotes Shop!")
        for i ,emoteData in enumerate (cls .ActionEmotes ):
            Console .log ("Action Emotes Shop",f"{i +1 }. {emoteData .get ('FriendlyName')} ({emoteData .get ('Rarity')})")

        try :
            Choice =int (input ("Choose by number: "))
        except :
            Choice =0 

        if Choice <1 or Choice >len (cls .ActionEmotes ):
            Console .warn ("Action Emotes Shop","Invalid choice!")
            return False 

        chosenEmote =cls .ActionEmotes [Choice -1 ]
        Console .log ("Action Emotes Shop",f"You chose: {chosenEmote .get ('FriendlyName')}")

        unlock_methods =chosenEmote .get ("UnlockMethodPurchasableItemIds",{})
        prog_unlock =unlock_methods .get ("ProgressionUnlock")
        purch_unlock =unlock_methods .get ("PurchaseUnlock")

        if not prog_unlock and not purch_unlock :
             Console .warn ("Action Emotes Shop","No Available purchase types!")
             return False 
        else :
             Console .log ("Action Emotes Shop","Available purchase types ⤵️")
             Types ={}
             if prog_unlock :
                  info =cls .GetPurchasableItemsInfo (prog_unlock )
                  if isinstance (info ,dict ):
                       price =info ['prices'][0 ]['amount']
                       curr =info ['prices'][0 ]['currency']
                       Types [0 ]={"Id":prog_unlock ,"Price":price ,"Currency":curr }
                       Console .log ("Action Emotes Shop",f"0. Price : {price } {curr }")
             if purch_unlock :
                  info =cls .GetPurchasableItemsInfo (purch_unlock )
                  if isinstance (info ,dict ):
                       price =info ['prices'][0 ]['amount']
                       curr =info ['prices'][0 ]['currency']
                       Types [1 ]={"Id":purch_unlock ,"Price":price ,"Currency":curr }
                       Console .log ("Action Emotes Shop",f"1. Price : {price } {curr }")

             Console .log ("Backend","Your Balance ⤵️")
             for t in Types .values ():
                  Console .log ("Backend",f"{cls .User .get ('username')} | {t ['Currency']}: {cls .getBalanceAmount (t ['Currency'])}")

             try :
                 TypeChoise =int (input ("Choose type by number: "))
             except :
                 TypeChoise =-1 

             if TypeChoise in Types :
                  selected =Types [TypeChoise ]
                  if cls .getBalanceAmount (selected ['Currency'])>selected ['Price']:
                       response =cls .purchaseV2 (selected ['Id'])
                       if response .get ("message")!="Error":
                            Console .log ("Action Emotes Shop",f"{cls .User .get ('username')} | New Action Emote Adquired: {chosenEmote .get ('FriendlyName')}")
                            return True 
                       else :
                            Console .log ("Action Emotes Shop",f"{cls .User .get ('username')} | Action Emote: {chosenEmote .get ('FriendlyName')}, already owned.")
                            return True 
                  else :
                       needed =selected ['Price']-cls .getBalanceAmount (selected ['Currency'])
                       Console .warn ("Action Emotes Shop",f"You need more {needed } {selected ['Currency']}.")
                       return False 
             else :
                  Console .warn ("Action Emotes Shop","Invalid type!")

    @classmethod 
    def completebattlepass (cls ):
        bp =cls .User .get ('battlePass',{})
        claimedSlots =bp .get ('slotsClaimed',[])
        userCoins =bp .get ('coins',0 )
        hasPurchased =bp .get ('hasPurchased',False )
        userExperience =bp .get ('experience',0 )

        if not cls .BattlePass :
             Console .warn ("Backend","No BattlePass data available.")
             return 

        xpToLevelUp =cls .BattlePass [0 ].get ('XPToLevelUp',1000 )

        def calculateLevel (exp ,req ):
             return int (exp /req )

        def isSlotClaimed (page ,section ,slot ):
             return f"{page },{section },{slot }"in claimedSlots 

        requests_list =[]

        for pass_data in cls .BattlePass :
             pages =pass_data .get ('Content',{}).get ('Pages',[])
             for pageIndex ,page in enumerate (pages ):
                  sections =page .get ('Sections',[])
                  if not isinstance (sections ,list ):continue 

                  for sectionIndex ,section in enumerate (sections ):
                       slots =section .get ('Slots',[])
                       if not isinstance (slots ,list ):continue 

                       sectionUnlockLevel =section .get ('UnlockLevel',0 )
                       for slotIndex ,slot in enumerate (slots ):
                            slotClaimed =isSlotClaimed (pageIndex ,sectionIndex ,slotIndex )
                            playerLevel =calculateLevel (userExperience ,xpToLevelUp )+1 

                            if not slotClaimed and userCoins >=slot ['UnlockCost']and playerLevel >=sectionUnlockLevel :
                                 if slot .get ('IsPremium')and not hasPurchased :
                                      continue 

                                 requestBody ={
                                 "IsPremium":slot .get ('IsPremium'),
                                 "TierIndex":0 ,
                                 "Page":pageIndex ,
                                 "Section":sectionIndex ,
                                 "Slot":slotIndex 
                                 }
                                 requests_list .append ({
                                 "body":json .dumps (requestBody ),
                                 "cost":slot ['UnlockCost'],
                                 "pageIndex":pageIndex ,
                                 "sectionIndex":sectionIndex ,
                                 "slotIndex":slotIndex 
                                 })

        requests_list .sort (key =lambda x :x ['cost'])

        for req in requests_list :
             response =cls .Post ("/battlepass/claimv3",req ['body'])
             if response .get ("message")!="Error":
                  Console .log ("Backend",f"Page {req ['pageIndex']}, Slot {req ['slotIndex']} successfully collected")
             cls .wait (1000 )

        if not cls .FarmMode :
             Console .log ("Backend",f"{cls .User .get ('username')} | BattlePass completion process finished.")

    @classmethod 
    def completemissions (cls ):
        r =cls .Get ("/missions")
        if r .get ("message")!="Error":
             Missions =r 
             missionObjectiveId =Missions ['missionObjectiveProgressionUpdated']['missionObjectiveId']
             MissionObjective =cls .GetMissionsInfo (missionObjectiveId )


             if isinstance (MissionObjective ,str ):return False 

             missionsProgress =Missions .get ('missionsProgressionsUpdated',[])
             currentPoints =Missions ['missionObjectiveProgressionUpdated'].get ('currentPoints',0 )
             milestonesProgress =Missions ['missionObjectiveProgressionUpdated'].get ('milestoneProgressions',[])

             unclaimedMilestones =[m for m in milestonesProgress if not m .get ('claimed')]
             unclaimedRewardsMissions =[
             m for m in missionsProgress 
             if m .get ('missionActive')and not m .get ('rewardsClaimed')and any (req .get ('completed')for req in m .get ('requirementProgressions',[]))
             ]

             for mission in unclaimedRewardsMissions :
                  cls .Post (f"/missions/{mission ['missionId']}/rewards/claim/v2","{}")

             for milestone in unclaimedMilestones :
                  milestoneInfo =next ((m for m in MissionObjective .get ('Milestones',[])if m .get ('MilestoneId')==milestone ['milestoneId']),None )
                  if milestoneInfo and currentPoints >=milestoneInfo .get ('PointsToClaim',0 ):
                       cls .Post (f"/missions/objective/{missionObjectiveId }/{milestone ['milestoneId']}/rewards/claim/v2","{}")
        return True 

    

    @classmethod 
    def updateinfos (cls ):
        cls .Event ={"Id":None ,"StartDateTime":None ,"EndDateTime":None ,"EventRounds":[]}

        cls .onlinecheck ()
        cls .updateshared ()

    @classmethod 
    def addplayer (cls ,PlayerUsername ):
        SearchResponse =cls .search (PlayerUsername )
        if SearchResponse .get ("message")!="Error":
             Console .log ("Backend",f"{cls .User .get ('username')} added {PlayerUsername }\n")
             return cls .Post ("/friends/request",json .dumps ({"UserId":SearchResponse .get ("userId")}))

    @classmethod 
    def addplayerange (cls ,PlayerUsername ,BaseUsername ,GenCaracters ):
         cls .login ()
         SearchResponse =cls .search (PlayerUsername )
         if SearchResponse .get ("message")!="Error":
              NewPlayerUsername =BaseUsername +CryptoUtils .GenCaracters (GenCaracters )
              cls .updateusername (NewPlayerUsername )
              if NewPlayerUsername ==cls .User .get ("username"):
                   Console .log ("Backend",f"{cls .User .get ('username')} added {PlayerUsername }\n")
                   return cls .Post ("/friends/request",json .dumps ({"UserId":SearchResponse .get ("userId")}))

    @classmethod 
    def getAuthHeader (cls ,url ,body =""):
        if body is None :body =""
        if not cls .User .get ('stumbleId'):
             Console .log ("Backend","Login in one acc first")
             return ""

        AuthTimestamp =cls .Timestamp ()-2 
        authHeader ={
        "DeviceId":cls .User .get ('deviceId'),
        "GoogleId":cls .User .get ('googleId',""),
        "FacebookId":cls .User .get ('facebookId',""),
        "AppleId":cls .User .get ('appleId',""),
        "Token":cls .User .get ('token'),
        "Timestamp":AuthTimestamp ,
        "StumbleId":cls .User .get ('stumbleId'),
        }
        authHeader ["Hash"]=CryptoUtils .CreateRegularHash (
        authHeader ["DeviceId"],
        authHeader ["GoogleId"],
        authHeader ["Token"],
        authHeader ["Timestamp"],
        authHeader ["StumbleId"],
        url ,
        body 
        )
        return json .dumps (authHeader )

    @classmethod 
    def finishRound (cls ,round_num ):
        cls .FinishRound =round_num 
        regularPatch =cls .CreateRoundFinishPacth ("regular")
        eventPatch =cls .CreateRoundFinishPacth ("event")
        regularBody =cls .CreateRoundFinishBody ("regular")
        eventBody =cls .CreateRoundFinishBody ("event")

        response ={
        "Request":{
        "Normal":False ,
        "Event":False ,
        "AutoLose":round_num <=2 
        },
        "User":cls .User ,
        "EquippedCosmetics":cls .EquippedCosmetics 
        }

        eventResponseRaw ={"message":"Error"}
        if cls .Event .get ("Id"):
             eventResponseRaw =cls .Post (eventPatch ,eventBody )
             if eventResponseRaw .get ("message")!="Error":
                  response ["Request"]["Event"]=True 

        regularResponseRaw =cls .Post (regularPatch ,regularBody )
        if regularResponseRaw .get ("message")!="Error":
             response ["Request"]["Normal"]=True 

        lastClaimedLevel =cls .User .get ('xpRoad',{}).get ('lastClaimedLevel')
        current_xp =cls .User .get ('experience',0 )
        if lastClaimedLevel is None :lastClaimedLevel =cls .GetLevel (current_xp )

        if lastClaimedLevel !=cls .GetLevel (current_xp ):
             cls .Post ("/xp-road/rewards/claim")

        if regularResponseRaw .get ("message")!="Error"or eventResponseRaw .get ("message")!="Error":
             try :
                 rb_parsed =json .loads (regularBody )
                 Console .log ("Backend",f"{cls .User .get ('username')} | Crowns : {CryptoUtils .formatNumber (cls .User .get ('crowns'))} | Trophys : {CryptoUtils .formatNumber (cls .User .get ('skillRating'))} | Level : {CryptoUtils .formatNumber (lastClaimedLevel )} | Round : {rb_parsed .get ('Round')}")
                 cls .Timestamps ["LastFinishRound"][cls .User .get ("stumbleId")]=time .time ()*1000 
             except :pass 

        return response 

    @classmethod 
    def FinishRoundV4 (cls ,round_num ,event =True ):
        cls .FinishRound =round_num 
        BotsResponse =cls .GetV2 ("/bots")
        Bots =BotsResponse if isinstance (BotsResponse ,list )else []

        BodyLevelIds =json .loads (cls .CreateRoundFinishBody ("regular"))
        UserId =str (cls .User .get ('id')or 0 )

        eliminatedPlayers =[]
        placements ={}
        roundPayloads ={}
        UsersLastRound ={}


        regularLevelIds =BodyLevelIds .get ("LevelIds")

        def handleRound1 (levelIds ):
             eliminated =[cls .User .get ('id')]+[b ['id']for b in Bots [:15 ]]
             placements [UserId ]=16 
             UsersLastRound [UserId ]=1 
             for i ,b in enumerate (Bots [:15 ]):
                  placements [b ['id']]=17 +i 

             roundPayloads ["1"]={
             "EliminatedPlayers":eliminated ,
             "LevelId":levelIds [0 ],
             "Placements":placements .copy (),
             "RoundMissionProgression":None ,
             "Type":"SoloRound"
             }

        def handleRound2 (levelIds ):
             eliminated =[cls .User .get ('id')]+[b ['id']for b in Bots [:7 ]]
             placements [UserId ]=2 
             UsersLastRound [UserId ]=2 
             for i ,b in enumerate (Bots [7 :15 ]):
                  placements [b ['id']]=3 +i 

             roundPayloads ["1"]={
             "EliminatedPlayers":[],
             "LevelId":levelIds [0 ],
             "Placements":placements .copy (),
             "RoundMissionProgression":None ,
             "Type":"SoloRound"
             }
             roundPayloads ["2"]={
             "EliminatedPlayers":eliminated ,
             "LevelId":levelIds [1 ],
             "Placements":placements .copy (),
             "RoundMissionProgression":None ,
             "Type":"SoloRound"
             }

        def handleRound3 (levelIds ):
             placements [UserId ]=1 
             UsersLastRound [UserId ]=3 



             roundPayloads ["1"]={
             "EliminatedPlayers":[],
             "LevelId":levelIds [0 ],
             "Placements":placements .copy (),
             "RoundMissionProgression":None ,
             "Type":"SoloRound"
             }
             roundPayloads ["2"]={
             "EliminatedPlayers":[],
             "LevelId":levelIds [1 ],
             "Placements":placements .copy (),
             "RoundMissionProgression":None ,
             "Type":"SoloRound"
             }
             lid3 =levelIds [2 ]if len (levelIds )>2 else levelIds [1 ]
             roundPayloads ["3"]={
             "EliminatedPlayers":[],
             "LevelId":lid3 ,
             "Placements":placements .copy (),
             "RoundMissionProgression":None ,
             "Type":"SoloRound"
             }

        if round_num ==1 :handleRound1 (regularLevelIds )
        if round_num ==2 :handleRound2 (regularLevelIds )
        if round_num ==3 :handleRound3 (regularLevelIds )

        Finishv4Body ={
        "ClientViewPayload":{
        "AverageMmr":None ,
        "CurrentRound":round_num ,
        "ExpectedRounds":3 ,
        "FrameNumber":7814 ,
        "GameId":CryptoUtils .CreateGameId ("regular"),
        "GameType":"Regular",
        "Placements":None ,
        "RoundPayloads":roundPayloads ,
        "StartingUsers":32 ,
        "UsersLastRound":UsersLastRound ,
        "VariantId":None ,
        },
        "ClientViewPlacements":None ,
        "FriendsCount":0 ,
        "LevelIds":regularLevelIds ,
        "MissionsProgression":{},
        "SignedPayload":""
        }

        eventBodyStr =cls .CreateRoundFinishBody ("event")
        eventLevelIds =json .loads (eventBodyStr ).get ("LevelIds",[])
        eventPayloads ={}

        EventRound =len (cls .Event .get ("EventRounds",[]))
        EventRoundFinish =EventRound if round_num >=EventRound else 1 



        for index ,levelId in enumerate (eventLevelIds [:EventRoundFinish ]):

             eliminated =[b ['id']for b in Bots [index *5 :(index +1 )*5 ]]
             if index ==EventRoundFinish -1 :








                  pass 









             eventPlacements ={cls .User .get ('id'):1 }
             eventPayloads [str (index +1 )]={
             "EliminatedPlayers":eliminated ,
             "LevelId":levelId ,
             "Placements":eventPlacements ,
             "RoundMissionProgression":None ,
             "Type":"SoloRound"
             }


        Finishv4BodyEvent ={
        "ClientViewPayload":{
        "AverageMmr":None ,
        "CurrentRound":EventRoundFinish ,
        "ExpectedRounds":EventRound ,
        "FrameNumber":7814 ,
        "GameId":CryptoUtils .CreateGameId ("event"),
        "GameType":"Event",
        "Placements":None ,
        "RoundPayloads":eventPayloads ,
        "StartingUsers":32 ,
        "UsersLastRound":{str (UserId ):EventRoundFinish },
        "VariantId":cls .Event .get ("Id"),
        },
        "ClientViewPlacements":None ,
        "FriendsCount":0 ,
        "LevelIds":eventLevelIds ,
        "MissionsProgression":{},
        "SignedPayload":""
        }

        regularResponse =cls .Post ("/round/finish/v4",json .dumps (Finishv4Body ))
        eventResponse ={"message":"Error"}
        if event :
             eventResponse =cls .Post ("/round/eventfinish/v4",json .dumps (Finishv4BodyEvent ))

        if regularResponse .get ("message")!="Error"or eventResponse .get ("message")!="Error":
             Console .log ("Backend",f"{cls .User .get ('username')} | Crowns : ... | Round : {BodyLevelIds .get ('Round')}")
             cls .Timestamps ["LastFinishRoundV4"][cls .User .get ("stumbleId")]=time .time ()*1000 

        return True 

    @classmethod 
    def CreateRoundFinishPacth (cls ,type_name ):
        region ="EU"
        if cls .User and cls .User .get ('settings'):
             region =cls .User ['settings'].get ('photonServerRegion',"EU")

        if type_name =="event"and cls .Event .get ("Id"):
             return f"/round/eventfinish/v3/{region }/{CryptoUtils .CreateParms ('event')}/{CryptoUtils .CreateParmsV2 ('event')}/{cls .Event ['Id']}"
        return f"/round/finish/v3/{region }/{CryptoUtils .CreateParms ('regular')}/{CryptoUtils .CreateParmsV2 ('regular')}"

    @classmethod 
    def CreateRoundFinishBody (cls ,type_name ):
        if not cls .FinishRound :cls .FinishRound =3 

        base ={
        "CollectedCurrencies":{},
        "FriendsCount":0 ,
        "GameId":CryptoUtils .CreateGameId ("regular"),
        "GameType":"REGULAR",
        "GameTypeId":"",
        "LevelIds":[],
        "MissionsProgression":{},
        "PartyType":"NORMAL",
        "Round":cls .FinishRound ,
        "SignedPayload":None ,
        }

        def getUniqueLevelID (levelIds_set ,possibleIds ):
             if not possibleIds :return "level_1"
             while True :
                  selected =random .choice (possibleIds )
                  if selected not in levelIds_set :
                       return selected 
                  if len (levelIds_set )>=len (possibleIds ):return selected 

        if type_name =="event"and cls .Event .get ("Id"):
             EventRound =len (cls .Event ["EventRounds"])
             EventRoundFinish =EventRound if cls .FinishRound >=EventRound else 1 
             cls .FinishRound =EventRoundFinish 

             base ["GameType"]="EVENT"
             base ["PartyType"]="CUSTOM"
             base ["GameTypeId"]=cls .Event ["Id"]
             base ["GameId"]=CryptoUtils .CreateGameId ("event")

             levelIDsForRounds =[]
             uniqueLevelIds =set ()

             for round_num in range (1 ,cls .FinishRound +1 ):
                  eventRound =next ((r for r in cls .Event ["EventRounds"]if r .get ("RoundNumber")==round_num ),None )
                  if eventRound :
                       if eventRound .get ("LevelID"):
                            if not eventRound .get ("RandomLevels")or eventRound ["LevelID"]not in uniqueLevelIds :
                                 levelIDsForRounds .append (eventRound ["LevelID"])
                                 uniqueLevelIds .add (eventRound ["LevelID"])
                       elif eventRound .get ("RandomLevels"):
                            selected =getUniqueLevelID (uniqueLevelIds ,eventRound ["RandomLevels"])
                            levelIDsForRounds .append (selected )
                            uniqueLevelIds .add (selected )

             base ["LevelIds"]=levelIDsForRounds 
             base ["Round"]=len (levelIDsForRounds )or cls .FinishRound 
             return json .dumps (base )
        else :
             uniqueLevelIds =set ()
             for round_num in range (cls .FinishRound +1 ):



                  roundLevels =[
                  rl for rl in cls .RoundLevels_v2 
                  if rl and rl .get ("AllowedRounds")and any (ar ["RoundNumber"]==round_num and ar ["Chance"]>0 for ar in rl ["AllowedRounds"])
                  ]
                  if roundLevels :
                       possible =[l ["LevelID"]for l in roundLevels ]
                       selected =getUniqueLevelID (uniqueLevelIds ,possible )
                       uniqueLevelIds .add (selected )

             base ["LevelIds"]=list (uniqueLevelIds )
             base ["Round"]=len (base ["LevelIds"])
             return json .dumps (base )

    @classmethod 
    def parserank (cls ,Id ):
        ranks ={
        1 :{"RankId":1 ,"RankName":"Wood","RankIcon":"<:Wood:1272235179338891385>"},
        2 :{"RankId":2 ,"RankName":"Bronze","RankIcon":"<:Bronze:1272235236100669534>"},
        3 :{"RankId":3 ,"RankName":"Silver","RankIcon":"<:Silver:1272235291796701184>"},
        4 :{"RankId":4 ,"RankName":"Gold","RankIcon":"<:Gold:1272235344393408553>"},
        5 :{"RankId":5 ,"RankName":"Platinum","RankIcon":"<:Platinum:1272235384251613265>"},
        6 :{"RankId":6 ,"RankName":"Master","RankIcon":"<:Master:1272235431173296139>"},
        7 :{"RankId":7 ,"RankName":"Champion","RankIcon":"<:Champion:1272235475028938837>"},
        }
        cls .PlayerRank =ranks .get (Id ,{
        "RankId":0 ,"RankName":"Unranked","RankIcon":"<:Ranked:1272235135428722719>"
        })
        return cls .PlayerRank 

    @classmethod 
    def GetSkinInfo (cls ,SkinId ):
        info =next ((s for s in cls .Skins_v4 if s .get ("SkinID")==SkinId ),None )
        return info if info else f"Skin with ID {SkinId } not found."

    @classmethod 
    def GetMissionsInfo (cls ,Id ):
        info =next ((m for m in cls .MissionObjectives if m .get ("Id")==Id ),None )
        return info if info else f"Missions with ID {Id } not found."

    @classmethod 
    def GetPurchasableItemsInfo (cls ,Id ):
        info =next ((i for i in cls .PurchasableItems if i .get ("Name")==Id ),None )
        return info if info else f"PurchasableItem with ID {Id } not found."

    @classmethod 
    def getBalanceAmount (cls ,name ):
        if not cls .User .get ('stumbleId'):return 0 
        balance =next ((b for b in cls .User .get ('balances',[])if b .get ('name')==name ),None )
        return balance ['amount']if balance else 0 

    @classmethod 
    def JoinClub (cls ,Id ):
        return cls .Post (f"/clans/{Id }/join",{})

    @classmethod 
    def GetRankedSeason (cls ,Season ):
        s_id ="LIVE_RANKED_SEASON_"+str (Season )
        seasonData =next ((s for s in cls .RankedPlaySettings .get ("Seasons",[])if s .get ("Id")==s_id ),None )

        if not seasonData :

             print (f"Season {Season } not found.")
             return None 

        content =f"=== RANKED MAPS SEASON {Season } ===\n\n"

        for pool in seasonData .get ("MapPools",[]):
             ranksRange =[r for r in cls .RankedPlaySettings .get ("Ranks",[])if pool ["RankIdFrom"]<=r ["Id"]<=pool ["RankIdTo"]]
             if not ranksRange :continue 

             startName =ranksRange [0 ]["NameKey"].replace ("RANK_","").lower ().capitalize ()
             endName =ranksRange [-1 ]["NameKey"].replace ("RANK_","").lower ().capitalize ()
             rangeName =f"{startName } to {endName }"

             content +=f"{rangeName }:\nMaps:\n"
             content +="\n".join ([f"- {m ['MapId']}"for m in pool .get ("Maps",[])])+"\n\n"

        bannedEmotes =seasonData .get ("ActionEmotesAccessibility",{}).get ("BannedActionEmotes",[])
        content +="=== BANNED EMOTES ===\n"
        for eId in bannedEmotes :
             emote =next ((a for a in cls .ActionEmotes if a .get ("Id")==eId ),None )
             if emote :
                  content +=f"- {emote .get ('FriendlyName')} ({emote .get ('Rarity')})\n"

        fileName =f"RankedSeason_{Season }.txt"
        with open (fileName ,"w",encoding ="utf-8")as f :
             f .write (content )

        return {"fileName":fileName ,"bannedEmotes":bannedEmotes }


if __name__ =="__main__":

    pass 
