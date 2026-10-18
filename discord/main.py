import requests
import os

url = 'https://discord.com/api/v9/channels/1561489132054777876/messages'

info = {
    "content": "this is a test"
}

AUTH = os.getenv("DISCORD_AUTH")

header = {
    "authorization" : AUTH
}

res = requests.post(url, info ,headers = header)

# DO NOT DO THIS, THIS WILL GET YOU FLAG