import base64
import hashlib
import uuid
from binascii import unhexlify, Error as BinasciiError

encoded_string = input("enter guid(ex:u0HWpsY0c437f37ad6312190d9bbe99d"): )



def deruid(encoded_str):
    try:
        padding = '=' * ((4 - len(encoded_str) % 4) % 4)
        padded_str = encoded_str + padding
        
        decoded_bytes = base64.urlsafe_b64decode(padded_str)
        
        hex_bytes = ' '.join(f'{byte:02x}' for byte in decoded_bytes)
        
        decoded_text = decoded_bytes.decode('utf-8', errors='replace')
        
        return hex_bytes, decoded_text
    except Exception as e:
        return f"Error: {str(e)}", ""


hex_bytes, decoded_text = deruid(encoded_string)

def htby(hex_str):
    try:
        return unhexlify(hex_str)
    except BinasciiError:
        return None

def base64dec(encoded):
    try:
        padded = encoded + '=' * (4 - len(encoded) % 4) if len(encoded) % 4 else encoded
        return base64.b64decode(padded).decode('utf-8', errors='ignore')
    except Exception:
        return None

def base32dec(encoded):
    try:
        padded = encoded + '=' * (8 - len(encoded) % 8) if len(encoded) % 8 else encoded
        return base64.b32decode(padded.upper()).decode('utf-8', errors='ignore')
    except Exception:
        return None

def chmd5(encoded_string):
    common_inputs = [encoded_string.lower(), encoded_string.upper(), "rubika", "chat", "user"]
    for test_input in common_inputs:
        if hashlib.md5(test_input.encode()).hexdigest() == encoded_string.lower():
            return f"MD5 hash of '{test_input}'"
    return None

def tuuid(hex_str):
    try:
        uuid_str = f"{hex_str[:8]}-{hex_str[8:12]}-{hex_str[12:16]}-{hex_str[16:20]}-{hex_str[20:]}"
        uuid.UUID(uuid_str)
        return uuid_str
    except ValueError:
        return None

def decode_string(encoded):
    print(f"Analyzing string: {encoded}")
    print(f"Length: {len(encoded)} characters")

    hex_result = htby(encoded)
    if hex_result:
        print(f"Hex to bytes: {hex_result}")
        print(f"Hex to string (UTF-8): {hex_result.decode('utf-8', errors='ignore')}")

    base64_result = base64dec(encoded)
    if base64_result:
        print(f"Base64 decoded: {base64_result}")

    base32_result = base32dec(encoded)
    if base32_result:
        print(f"Base32 decoded: {base32_result}")

    md5_result = chmd5(encoded)
    if md5_result:
        print(f"MD5 match: {md5_result}")

    uuid_result = tuuid(encoded)
    if uuid_result:
        print(f"UUID format: {uuid_result}")
        
print(f"Input: {encoded_string}\n")
print("Base64 Decoded Bytes (Hex):")
print(hex_bytes)
print("\nThis translates to:")
print(decoded_text, "(meaningless binary data)")

    if not any([hex_result, base64_result, base32_result, md5_result, uuid_result]):
        print(".")
        print("")

decode_string(encoded_string)
