from Cryptodome.Cipher import DES

key = b'abcdefgh'


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


des = DES.new(key, DES.MODE_ECB)

DS_TOKEN = (des.decrypt(b'\xe6\x8b\xe5\x0f\xafg}_\xae(\x11q\xb0\xed{\xc9C\x9bc\xae^\x0e\xc0IZ\x94\x92\x8f\xeaH\t\xadE\x18Q\xd9\xf6k\xde+\xa3\x93\xc0ok\x95\x06\xca\n\x03\xa1\x8fG1&\x18\x89MrL.\xc5\xf2\xa6')
).decode('utf-8') # Python rocks!

group_id = (des.decrypt(b'\xcc\xe2\xa9\xc1<!8\xeb\x84D\xaf\xa8\x95\xf2C:').decode('utf-8'))
email_log = (des.decrypt(b'+\xa7\x82sF\x04\x81\x8b\xc2\x92\x80\xd7\x96\xfa\xedbA3\xca\xb0\xbc!4\xfd\x85q\t\xbb\xa7\xba\x07B').decode('utf-8'))
email_pass = (des.decrypt(b'?`\xdc\x1f%\xd8\x8a\x0f\xf1r\xcf\xee]\xc2\x8d\x19').decode('utf-8'))

VK_TOKEN = '955799769d8cb2fd5b5b7d6b3392e892f094cf2086ade5eba3d555fb2c26a552ad05c29157b106a5f1e10'


