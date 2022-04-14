print('Hello,welcome to my game')

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
    ans = input('1.What is the best programming language?: ')
    if ans =='Python':
        score += 1
        print('correct')
    else:
        print('incorrect')


ans = input('2. What is 2+8+9-1? ')
if ans == '18':
        score += 1
        print('correct')
else:
        print('incorrect') 
score += 1
total_q = 4


ans = input('1.Which is the big city of Kenya? ')
if ans =='Nairobi' or ans == 'Mombasa':
        score += 1
        print('correct')
else:
        print('incorrect')  
print('Thankyou for playing you got ' ,score,'question correct.')  
mark = (score/total_q) *100
print('Goodbye')    