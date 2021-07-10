
def Encrpytingchar(char):
    if(char!=" "):
        return chr((((ord(char)+3)+65)%26)+65)
    return " "
    

def CaesorEncrypter(a):
    encrypted_msg=""
    for i in range(0,len(a)):
        encrypted_msg+=Encrpytingchar(a[i])
    return encrypted_msg

def Decrpytingchar(char):
    if(char!=" "):
        return chr((((ord(char)-3)+65)%26)+65)
    return " "
    

def CypherDycrypter(a):
    decrypted_msg=""
    for i in range(0,len(a)):
        decrypted_msg+=Decrpytingchar(a[i])
    return decrypted_msg


msg=input("Enter the Message").upper()
Encrpyted_msg=CaesorEncrypter(msg)
print(Encrpyted_msg)
Decrypted_msg=CypherDycrypter(Encrpyted_msg)
print(Decrypted_msg)
