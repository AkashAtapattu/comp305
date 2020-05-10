"""
Date: 5/8/20
Author: Tatiana Barbone
"""
def dayFreq(curDate):
    """
    Gets emotions felt throughout the day along with their respective frequencies

    Args:
        string: curDate: day to get emotions from
    Returns:
        list of ints: emotionsList
    """
    # get array for specified day
    dayInfo = curDate.info()
    dayFreq = []
    # loop through all emotions felt in the day
    for i in range(len(dayInfo):
        #append each frequency to the list
        dayFreq.extend(dayInfo[i][1][0]) #get emotion from each day
    
    emotionsList = [0,0,0,0,0,0,0] #index 1 = sad, index 2 = happy, etc.
    # loop through all emotions in the day, adding frequency of each emotion to its respective index
    for emotion in dayFreq: 
        if emotion == 'Sad': 
            emotionsList[0] += 1
        else if emotion == 'Happy':
            emotionsList[1] += 1
        else if emotion == 'Stressed':
            emotionsList[2] += 1
        else if emotion == 'Angry':
            emotionsList[3] += 1
        else if emotion == 'Confused':
            emotionsList[4] += 1
        else if emotion == 'Tired':
            emotionsList[5] += 1
        else if emotion == 'Excited':
            emotionsList[6] += 1

    return emotionsList

def weekFreq(curWeek):
    """
    Gets emotions felt throughout the week along with their respective frequencies
    
    Args:
        list: curWeek: Week array
    Returns:
        list of lists of ints: week_freq

    """
    week_freq = []
    for i in range(len(curWeek)): #Day = [7]
        week_freq.extend(dayFreq[i]) # append each Day frequency

    return week_freq


def weekVolatility():
    """
    Informs the user whether their week was volatile or not
    
    """
    count = 0
    weekInfo = week.getInfo()
    for day in weekInfo: # access each day in 
        # get VybeScore for each day
        for i in range(1, len(weekInfo[day]):
            if weekInfo[i][1][1] > 5: # access the VybeScore for each day
                # If the VybeScore for a certain day is greater than 5, you had a 
                # volatile day. 
                count += 1

    # If you had at least 4/7 volatile days, your week is considered volatile.
    if count => 4:
        print("You had a volatile week.\n")
    else: 
        print("Your week was not volatile.\n")