#Practical 9 using MAC (Message Authentication Code)
import hashlib

print("===============================Sender side===============================\n")
message = "helloworld" 
secretkey = "ahmedabad" 
print("Message : ",message) 
print("Secret Key : ",secretkey) 
print("./\.")

actualmessage = message+secretkey

result = hashlib.sha512(actualmessage.encode()) 
hashval = result.hexdigest()
print("Hash value : ",hashval) 
print("./\.")
finalmessage = message+'xx'+hashval 
print("Final message : ",finalmessage) 
print("./\.")
print("\n..........................SENDING THE MESSAGE	\n")
print("===============================Receiver side===============================") 
print("\n..........................RECEIVING THE MESSAGE.	\n")

rm = finalmessage 
print("Received message : ",rm) 
secretkey = "ahmedabad" 
print("Secret Key : ",secretkey) 
print("./\.")

rm2 = rm.split('xx') 
message = rm2[0] 
hashval = rm2[1]
actualmessage=message+secretkey
result = hashlib.sha512(actualmessage.encode()) 
temp = result.hexdigest()
print("Received message : ",message) 
print("./\.")
print("Hash value of received message (By Receiver) : ",temp) 
print("./\.")
print("Received hash value : ",hashval) 
print("./\.")
print("\n................Checking If message is altered or not.	\n")
if temp == hashval:
    print("MAC got matched. Integrity Achieved. The message is not altered") 
else:
    print("MAC not matched. Integrity Not Achieved. The message is altered")