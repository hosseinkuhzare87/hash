import hashlib
print("                    hello world")
print("------------------------------------------------------")
print("                  my name:hossein")
print("                my telegram id:@Hsnsjs")
print("------------------------------------------------------")
print("                      start!"                          )
j=str(input("enter the word:"))
f=j.encode()
print("-------------------------------------------------------------------------------------")
print("md5:",hashlib.md5(f).hexdigest())
print("sha1:",hashlib.sha1(f).hexdigest())
print("sha224:",hashlib.sha224(f).hexdigest())
print("sha256:",hashlib.sha256(f).hexdigest())
print("sha384:",hashlib.sha384(f).hexdigest())
print("sha512:",hashlib.sha512(f).hexdigest())
print("blake2b:",hashlib.blake2b(f).hexdigest())
print("blake2s:",hashlib.blake2s(f).hexdigest())
print("sha3_224:",hashlib.sha3_224(f).hexdigest())
print("----------------------------------------------------------------------------------------")
