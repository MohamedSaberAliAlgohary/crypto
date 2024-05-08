import binascii

def calculate_crc32(data):
    #? Convert data to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    #? Handle if data is not string must be converted
    else:
        data=str(data).encode('utf-8')
    
    #? Compute CRC32 checksum
    CRC32_value = binascii.crc32(data) & 0xFFFFFFFF
    
    return CRC32_value

#! Define input strings that defined that have collision in crc32 value 
string1 = "plumless"
string2 = "buckeroo"

#! Calculate CRC32 checksums value for both inputs
crc32_checksum1 = calculate_crc32(string1)
crc32_checksum2 = calculate_crc32(string2)

#! Dispaly CRC32 checksums
print(f"CRC32 checksum for '{string1}' is: {crc32_checksum1}")
print(f"CRC32 checksum for '{string2}' is: {crc32_checksum2}")

#! Check if the checksums are the same or not to give conclusion for the collision
if crc32_checksum1 == crc32_checksum2:
    print("The CRC32 checksums are the same, indicating a hash collision exist.")
else:
    print("The CRC32 checksums are different, indicating no hash collision exist.")
