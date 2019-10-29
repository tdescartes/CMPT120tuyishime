# CMPT 120 Intro to Programming
# Lab #7 – Artificial Personality
# Created: 2019-10-29


#printing the emotion of current state of emotion
def printEmotion(currEmotion):
    emotionList= ["I am Freakin' angry", "Shit!! I am digusted", "Ohh My God! I am afraid", "I am over the moon!", "I am Really, really sad!", "Woow! I am so surprised"]
    print(emotionList[currEmotion])
    
    pass

# prompting the user of to enter their action toward the computer emotion

def getInteraction():
    print (" Choose Action: 0 for reward, 1 for punish, 2 for threaten, 3 for joke")
    userAction= eval(input ("Enter your choice: "))
    
    return userAction
    pass

# looking up the emotion using the action taken by the user and the current state of emotion

def lookupEmotion(currEmotion, userAction):
    emotion= [[3,1,2,1],
              [1,0,4,0],
              [5,2,0,3],
              [3,4,5,3],
              [3,0,1,1],
              [5,1,0,1]]
    currEmotion= emotion[currEmotion][userAction]
    
    return currEmotion  
    pass


def main():
#initialization of current Emotion.
    currEmotion=2
    emotionList= ["I am Freakin' angry", "Shit!! I am digusted", "Ohh My God! I am afraid", "I am over the moon!", "I am Really, really sad!", "Woow! I am so surprised"]
    print(emotionList[currEmotion])
    
 #Indefinite loop that is going to help us repeat the same block of codes in order to easy the access.    
    while True:
        userAction= getInteraction()
        currEmotion= lookupEmotion(currEmotion, userAction)
        printEmotion(currEmotion)
    

main()


