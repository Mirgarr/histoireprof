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
    print(f"{BLUE}gg bg t'as le doxx de la prof d'histoire:{RESET}")
    print(f"{RED}{decode_message()}{RESET}")

if __name__ == "__main__":
    main()

# This script is for educational purposes only
# Any malicious use is prohibited
