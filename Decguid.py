import base64
import hashlib
import uuid
from binascii import unhexlify, Error as BinasciiError

def pstr(encoded, mod, pad_char='='):
    padding = pad_char * ((mod - len(encoded) % mod) % mod)
    return encoded + padding

def decb64usafe(encoded):
    try:
        padded = pstr(encoded, 4)
        decoded_bytes = base64.urlsafe_b64decode(padded)
        hex_bytes = ' '.join(f'{byte:02x}' for byte in decoded_bytes)
        decoded_text = decoded_bytes.decode('utf-8', errors='replace')
        return hex_bytes, decoded_text
    except Exception as e:
        return f"Error: {str(e)}", ""

def decode_hex(hex_str):
    try:
        return unhexlify(hex_str.replace(" ", ""))
    except BinasciiError:
        return None

def decode_base64(encoded):
    try:
        padded = pstr(encoded, 4)
        return base64.b64decode(padded).decode('utf-8', errors='ignore')
    except Exception:
        return None

def decode_base32(encoded):
    try:
        padded = pstr(encoded, 8)
        return base64.b32decode(padded.upper()).decode('utf-8', errors='ignore')
    except Exception:
        return None

def check_md5(encoded):
    common_inputs = [encoded.lower(), encoded.upper(), "rubika", "chat", "user"]
    for test_input in common_inputs:
        if hashlib.md5(test_input.encode()).hexdigest() == encoded.lower():
            return f"MD5 hash of '{test_input}'"
    return None

def format_uuid(hex_str):
    try:
        hex_str = hex_str.replace(" ", "")
        uuid_str = f"{hex_str[:8]}-{hex_str[8:12]}-{hex_str[12:16]}-{hex_str[16:20]}-{hex_str[20:]}"
        uuid.UUID(uuid_str)
        return uuid_str
    except ValueError:
        return None

def analyze_string(encoded):
    print(f"\nAnalyzing string: {encoded} (Length: {len(encoded)} characters)")
    

    hex_bytes, decoded_text = decb64usafe(encoded)
    print(f"decoded (Hex): {hex_bytes}")
    print(f" decoded (Text): {decoded_text}")
    
    hex_result = decode_hex(encoded)
    if hex_result:
        print(f"Hex decoded: {hex_result} (Text: {hex_result.decode('utf-8', errors='ignore')})")
    
    base64_result = decode_base64(encoded)
    if base64_result:
        print(f"Base64 decoded: {base64_result}")
    
    base32_result = decode_base32(encoded)
    if base32_result:
        print(f"Base32 decoded: {base32_result}")
    
    md5_result = check_md5(encoded)
    if md5_result:
        print(f"MD5 match: {md5_result}")
    
    
    uuid_result = format_uuid(encoded)
    if uuid_result:
        print(f"UUID format: {uuid_result}")

if __name__ == "__main__":
    encoded_string = input("Enter a string (e.g., u0HWpsY0c437f37ad6312190d9bbe99d): ")
    analyze_string(encoded_string)
