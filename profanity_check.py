import os
dirname = os.path.dirname(__file__)
profanity_list = os.path.join(dirname, 'profanity.txt')
tweets=os.path.join(dirname, 'tweets.txt')
profanity_words=[]
degree={1:'Low',2:'High'} #dictionary to 

def check_profanity(word): #function to check if a word from the tweet is in the list of racial words list
    if(any(word in slur for slur in profanity_words) ):
                return 1      

with open(profanity_list,'r') as file:     #get words from the racial slurs list and store it in the list 'profanity_list'
    for line in file:      
        for word in line.split():       
            profanity_words.append(word.lower()) 
with open(tweets,'r') as file:    #read the tweets file,assuming each tweet is in a single line
    count=0
    for line in file:      
        for word in line.split():
            if(check_profanity(word)):   #check for word in the list "profanity_words"
                count+=1    
        if(count>2):  #check for degree of profanity
            print('Profanity Degree in the tweet:',line.strip(),'is Severe')
        elif(count>0 and count<=2):
            print('Profanity Degree in the tweet:',line.strip(),'is',degree[count])
        count=0 #reset count after every tweet