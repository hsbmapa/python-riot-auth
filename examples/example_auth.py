import asyncio
import sys

import riot_auth

# region asyncio.run() bug workaround for Windows, remove below 3.8 or above 3.11 beta 1
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# endregion

CREDS = "USERNAME", "PASSWORD"

auth = riot_auth.RiotAuth()
asyncio.run(auth.authorize(*CREDS))

print(f"Access Token Type: {auth.token_type}\n")
print(f"Access Token: {auth.access_token}\n")
print(f"Entitlements Token: {auth.entitlements_token}\n")
print(f"User ID: {auth.user_id}")

# Reauth using cookies.
asyncio.run(auth.reauthorize())
