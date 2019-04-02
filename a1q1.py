from asgn1 import SubCipher

# Put your testing code here
# This function will be executed when you run your program on VPL
# This function will not be graded

    
    

#Task 1.1
def analyse(text):
    length=len(text)
    text=text.upper()
    freq=[0]*26
    
    b=0;
    for a in range(65,91,1):
        
     for y in range (length):
         if(text[y]==chr(a)):
             freq[b]=freq[b]+1
             
     b=b+1
    return freq

#Task 1.2
def substitute(text, cipher):
    length=len(text)
    length_1=len(cipher)
    text=text.upper()
    text_list=list(text)
    finaltxt=""
    for x in range(length_1):
        c=cipher[x]
        if(c.isalpha()):
            d=chr(x+65)
            for y in range (length):
                if(text[y]==d):
                    text_list[y]=c
    for z in range (length):
        finaltxt=finaltxt+text_list[z]
    return finaltxt
#Task 1.3
def main():
    
    uno = 3035453610 # replace this with your student ID
    text = SubCipher.getChallenge(uno)
    print(text)
  