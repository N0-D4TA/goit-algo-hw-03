import re

# Option 1 (preferable)

def normalize_phone(num: str) -> str:
   
    # Cleaning string from any character except numbers and "+" symbol
    pattern = r'[^\d+]'
    replacement = ''
    
    normal_num = re.sub(pattern, replacement, num)
    if normal_num.startswith('+380'):
        return normal_num
    elif normal_num.startswith('380'):
        return '+' + normal_num
    elif normal_num.startswith('0'):
        return '+38' + normal_num


# Option 2 (messy)

def normalize_phone(num: str) -> str:
    # Cleaning string from any character except numbers and "+" symbol
    pattern = r'[^\d+]'
    replacement = ''
    
    normal_num = re.sub(pattern, replacement, num)

    # Key is previous prefix, value is code we have to add
    prefix_dict = {'+380': '', '380': '+', '0': '+38'}
    for prefix, code  in prefix_dict.items():
        if normal_num.startswith(prefix):
            return code + normal_num