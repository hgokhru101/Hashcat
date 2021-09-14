from flask import Flask,render_template,request
from urllib.request import urlopen, hashlib
import sys
app=Flask(__name__)

def sha256crack(hashcode): 
    ans=""   
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha256(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hashcode:
        	return guess
    return "False"    	
			
def sha1crack(hashcode): 
    ans=""   
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hashcode:
        	return guess
    return "False" 

def sha512crack(hashcode): 
    ans=""   
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha512(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hashcode:
        	return guess
    return "False" 


def sha384crack(hashcode): 
    ans=""   
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha384(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hashcode:
        	return guess
    return "False" 

def sha224crack(hashcode): 
    ans=""   
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha224(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hashcode:
        	return guess
    return "False" 

def md4crack(hashcode): 
    ans=""   
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.new('md4',bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hashcode:
        	return guess
    return "False" 

def md5crack(hashcode): 
    ans=""   
    LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hashcode:
        	return guess
    return "False" 


@app.route("/")
def return_home():
    return render_template("HashCat.html")



@app.route("/decrypt_hash",methods=["POST"])
def decrypt_hash():
    
    algo=request.form["algo"]
    code=request.form["code"]
    
    if algo=="1":
        return 	sha1crack(code.lower())
    elif algo=="2":
        return sha256crack(code.lower())
    elif algo=="3":
        return sha512crack(code.lower())
    elif algo=="4":
        return sha384crack(code.lower())
    elif algo=="5":
        return sha224crack(code.lower())
    elif algo=="6":
        return md5crack(code.lower())
    else:
        return md4crack(code.lower())
                        

 
if __name__ == '__main__':
        app.run(debug=True)    
