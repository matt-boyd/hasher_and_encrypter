import hashlib
from easygui import *
import sys
import time
from pyDes import *
image   = "bitcoin.gif"
msg     = "Bitcoin Password Hasher - Please choose an option."
choices = ["Start","Donate","Quit"]
reply   = buttonbox(msg, image=image, choices=choices)
if(reply == "Start"):
    msg = "Please enter your password you would like hashed\n Just not special characters(at the moment anyways.)"
    title = "/u/matthew_boyd's hashing program."
    password = enterbox(msg, title)
    hash = hashlib.sha256(password).hexdigest()
    hash1 = hashlib.sha224(password).hexdigest()
    hash2 = hashlib.md5(password).hexdigest()
    hash3 = hashlib.sha1(password).hexdigest()
    hash4 = hashlib.sha384(password).hexdigest()
    hash5 = hashlib.sha512(password).hexdigest()
    textbox(msg='The hash of your password is written below. Press control + c to copy it. ', title=" Matthew's Hashing program", text="SHA256: " + hash + "\n" + "\n" + "SHA224: " + hash1 + "\n" + "\n" + "MD5: " + hash2 + "\n" + "\n" + "SHA1: " + hash3 + "\n" +  "\n" + "SHA384: " + hash4 + "\n"  + "\n" + "SHA512: " + hash5, codebox=0)
    msg = "please enter the hash you want encrypted"
    title = "/u/matthew_boyd's hashing program."
    encryption = enterbox(msg, title)
    var = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    var1 = var.encrypt(encryption)
    textbox(msg='The hash encrypted, make sure to Control + C to copy it.', title=" Matthew's Hashing program", text="Encrypted: %r" % var1 + "\n" + "\n" + "Decrypted: %r" % var.decrypt(var1) + "\n" + "\n")
	
elif(reply == "Donate"):
    textbox(msg="Donation Address", title="Matthew's Hashing Program", text="Bitcoin donation address: 169iA76RmnatFXmEthT6AEehxMQ9X1ro3L", codebox=0)
    
else:
    sys.exit()
    
