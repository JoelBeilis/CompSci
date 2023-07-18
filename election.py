__name__ = 'B. Joel'
'''
election
Wednesday, March 22, 2023
User enters election results for 3 states and calculates percentage of votes for each candidate
'''

newYorkA = int(input('Enter total votes for Awbrey from New York: '))
newJerseyA = int(input('Enter total votes for Awbrey from New Jersey: '))
connecticutA = int(input('Enter total votes for Awbrey from Connecticut: '))

newYorkM = int(input('Enter total votes for Martinez from New York: '))
newJerseyM = int(input('Enter total votes for Martinez from New Jersey: '))
connecticutM = int(input('Enter total votes for Martinez from Connecticut: '))

print('Election results for New York:')
print('Awbrey:', newYorkA)
print('Martinez:', newYorkM)
print('Election results for New Jersey:')
print('Awbrey:', newJerseyA)
print('Martinez:', newJerseyM)
print('Election results for Connecticut:')
print('Awbrey:', connecticutA)
print('Martinez:', connecticutM)

awbreyT = newYorkA+newJerseyA+connecticutA
martinezT = newYorkM+newJerseyM+connecticutM
total = martinezT+awbreyT
print('Candidate      Votes    Percentage')
print('Awbrey       ', awbreyT, round(awbreyT/total*100, 2), '%')
print('Martinez     ', martinezT, round(martinezT/total*100, 2), '%')
print('Total votes: ', total)
