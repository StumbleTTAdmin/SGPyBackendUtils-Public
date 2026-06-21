# Backend.py Documentation

`Backend.py` implements a Python wrapper for Stumble Guys API interactions. The module is designed around a single `Backend` class with class-level state and helper methods.

## Setup Requirements
- pip install StumbleUtils

## Core Classes

### `Console`
A simple logger with static methods:

- `Console.log(prefix, message, color=None)`
- `Console.warn(prefix, message)`
- `Console.error(prefix, message)`

### `Backend`
A full API client class with shared state and request helpers.
# Import
Import The Backend Class by using `from StumbleUtils import Backend`
## Important configuration values

- `Backend.baseUrl` - API base URL, defaults to `https://api.stumbleguys.com`
- `Backend.LogsDebug` - enable error logging for failed requests
- `Backend.proxy` - optional proxy string for network requests
- `Backend.Version` - loaded from `SG_VERSION` environment variable
- `Backend.SharedType` - LIVE, STAGE, BETA, TEST or undefined based on the current server

## Authentication & Request Helpers

- `Backend.login(StumbleId='', DeviceId='', version='0.99', DontLogs=False, ScopelyId='', SteamTicket='')`
- `Backend.getAuthHeader(url, body='')`
- `Backend.Get(Patch)`
- `Backend.Post(Patch, Body='')`
- `Backend.Put(Patch, Body='')`
- `Backend.Delete(Patch)`
- `Backend.GetV2(Patch)`
- `Backend.GetV3(endpoint)`

## Core utilities

- `Backend.wait(ms=1000)` - sleeps, converting values <= 60 to milliseconds
- `Backend.Timestamp()` / `Backend.getTimestamp()` - returns current POSIX time
- `Backend.GetLevel(xp)` - calculate player level from experience points
- `Backend._save_user_file()` - save the current `Backend.User` data to `Users/{username}#{SharedType}.json` (might not work haven't tested on latest version)

## Game data & shared updates

- `Backend.updateinfos()` - refreshes shared data and online checks
- `Backend.onlinecheck()` - waits until API returns `OK`
- `Backend.updateshared()` - fetches game config and shared data, updates event/ranked state

## Player management

- `Backend.search(username)` - search for a player by name
- `Backend.addplayer(PlayerUsername)` - send a friend request using search results
- `Backend.addplayerange(PlayerUsername, BaseUsername, GenCaracters)` - set a generated username, then send request

## Account actions

- `Backend.deleteaccount()` - delete the current account
- `Backend.LinkPlatform(platform, platformId)` - link Google/Apple/Facebook/Scopely account
- `Backend.UnlinkPlatform(Platform)` - unlink a supported platform

## Battle pass and missions

- `Backend.purchasebattlepass()` - buy a battle pass using gems if available
- `Backend.GetFreeBattlePass()` - attempt a free battle pass login flow
- `Backend.completebattlepass()` - claim all available battle pass slots
- `Backend.completemissions()` - claim completed mission and objective rewards

## Shop & cosmetics

- `Backend.purchase(item)` - purchase an item by ID
- `Backend.purchaseV2(item, log=True)` - make a purchase using the V2 endpoint
- `Backend.purchaseluckyspinwheel()` - use any free lucky spin wheel spins
- `Backend.updateusername(username)` - change the current account username
- `Backend.updatecosmetics(SkinID, Color, Animation, Footstep, Emote1, Emote2, Emote3, Emote4, ActionEmote1='', ActionEmote2='', ActionEmote3='', ActionEmote4='')`
- `Backend.HandleActionEmotesShop()` - CLI-driven action emote shop helper

## Farm & event helpers
# NOTE THESE DO NOT WORK ON OFFICIAL SERVERS ONLY USE ON YOUR OWN CUSTOM SERVER
- `Backend.finishRound(round_num)` - submit a regular round finish payload
- `Backend.FinishRoundV4(round_num, event=True)` - submit a round finish payload for V4 events
- `Backend.CreateRoundFinishPacth(type_name)` - build finish endpoint path
- `Backend.CreateRoundFinishBody(type_name)` - build finish request body
- `Backend.FarmCrowns(StumbleId, WebHook, Winrate=100, Flags=None)` - multi-step farming flow with optional webhook reporting

## Helper lookups

- `Backend.GetSkinInfo(SkinId)` - lookup skin metadata in loaded shared data
- `Backend.GetMissionsInfo(Id)` - lookup mission objective metadata
- `Backend.GetPurchasableItemsInfo(Id)` - lookup purchasable item metadata
- `Backend.getBalanceAmount(name)` - return currency balance for the current logged-in user
- `Backend.JoinClub(Id)` - join a clan/club by ID
- `Backend.GetRankedSeason(Season)` - export ranked season map pool and banned emote data to a text file

## Example usage

```python
from StumbleUtils import Backend

Backend.LogsDebug = True
Backend.login(version=0.99)
# Search for a user
Backend.search("ItsOmeyNS")
```

## Notes

- Many methods depend on authenticated `Backend.User` data.
- `Backend.set_proxy()` is available, but not all methods currently pass proxies through to every request.
- `Backend.py` is best used as a helper library inside another script rather than run as a standalone module.

