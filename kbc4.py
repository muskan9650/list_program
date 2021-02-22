question_list =[]
size=int(input("enter number"))
for i in range(size):
    n=(input("enter question"))
    question_list.append(n)
print(question_list)
options_list=[]
option_list=[]
for i in range(size):
    for j in range(4):
        t=input("enter option for first question")
        option_list.append(t)
        j=j+1
    i=i+1
    options_list.append(t)
    print(options_list)
answer_list=[]
for i in range(size):
    n=int(input("enter answer"))
    answer_list.append(n)
print(answer_list)
lifelines_list=[]
lifeline_list=[]
for i in range(size):
    for j in range(2):
        t=input("enter option for question")
        lifelines_list.append(t)
        j=j+1
    i=i+1
    lifeline_list.append(lifelines_list)
    print(options_list)
lifeline_answer_list=[]
for i in range(size):
    m=int(input("enter lifeline answer"))
    lifeline_answer_list.append(m)
print(lifeline_answer_list)
amount=0
count=1
i=0
print("LETS PLAY THE GAME")
while i<len(question_list):
    print(question_list[i])
    j=0
    while j < len(options_list[i]):
        print(options_list[i][j])
        j=j+1
    print("DO YOU WANT 5050 LIFELINE BUT YOU HAVE ONLY ONE LIFELINE")
    n=input("yes/no")
    print("OHK!")
    if n=="yes":
        if count==1:
            m=1
            while m<len(lifeline_list[i]):
                j=0
                while j<len(lifeline_list[i]):
                    print(lifeline_list[i][j])
                    j=j+1
                m=m+1
            n=int(input("choosen your answer"))
            if n!=lifeline_answer_list[i]:
                print("wrong answer")
                break
            count=count-1
        else:
            print("you already use lifeline")
            print(question_list[i])
            s=i
            while s==i:
                j=0
                while j<len(options_list[s]):
                    print(options_list[s][j])
                    j+=1
                s+=1
                n=int(input("choose your answer"))
                if n!=answer_list[i]:
                    print("wrong answer")
                    break
    else:
        n=int(input("enter a value"))
        if n!=answer_list[i]:
            print("wrong answer")
            break
    amount=amount+1000
    print("congratulation! you win $", amount)
    i=i+1
print("game finished! enjoy your day '-'")
