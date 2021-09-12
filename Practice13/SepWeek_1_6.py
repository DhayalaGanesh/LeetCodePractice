
from typing import List
def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    longestTimeIndex = 0
    longestTimeDiff = 0
    for i in range(1,len(releaseTimes)):
        currTimeDiff = releaseTimes[i]-releaseTimes[i-1]
        if(longestTimeIndex == 0):
            longestTimeDiff = releaseTimes[longestTimeIndex]
        else:
            longestTimeDiff = releaseTimes[longestTimeIndex]-releaseTimes[longestTimeIndex-1]
        if(longestTimeDiff<currTimeDiff):
            longestTimeIndex = i
        elif(longestTimeDiff==currTimeDiff and ord(keysPressed[longestTimeIndex])<ord(keysPressed[i])):
            longestTimeIndex = i
    return keysPressed[longestTimeIndex]

print(slowestKey([28,65,97], "gaf"))