import os
dirname = os.path.dirname(__file__)
profanityList = os.path.join(dirname, 'profanity.txt')
tweets=os.path.join(dirname, 'tweets.txt')
profanityWords=[]
degree={1:'Low',2:'High'} #dictionary to 

def checkProfanity(word): #function to check if a word from the tweet is in the list of racial words list
    if(word in profanityWords):
                return 1      

with open(profanityList,'r') as file:     #get words from the racial slurs list and store it in the list 'profanityList'
    for line in file:      
        for word in line.split():       
            profanityWords.append(word.lower()) 
with open(tweets,'r') as file:    #read the tweets file,assuming each tweet is in a single line
    count=0
    for line in file:      
        for word in line.split():
            if(checkProfanity(word)):   #check for word in the list "profanityWords"
                count+=1    
        if(count>2):  #check for degree of profanity
            print('Profanity Degree in the tweet:',line.strip(),'is severe')
        elif(count>0 and count<=2):
            print('Profanity Degree in the tweet:',line.strip(),'is',degree[count])
    
        count=0