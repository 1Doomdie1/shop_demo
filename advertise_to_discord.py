import requests
from sys import argv


PR_TITLE = argv[5]
PR_AUTHOR = argv[4]
PR_NUMBER = argv[3]
DISCORD_CHANEL = argv[2]
DISCORD_TOKEN = argv[1]

data = {"content": f"PR: {PR_TITLE}\nLINK: https://github.com/unifyai/ivy/pull/{PR_NUMBER}\nAUTHOR:{PR_AUTHOR}\nSTATUS: reviewed"}
header = {"authorization": DISCORD_TOKEN}
requests.post(DISCORD_CHANEL, data=data, headers=header)
