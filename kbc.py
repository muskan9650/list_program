question_list = [
    "How many continents are there?",
    "What is the capital of India?",         
    "who is prime minister of india?" 
]
options_list=[["1.four", "2.nine", "3.seven", "4.eight"], ["1.chandigarh", "2.bhopal", "3.chennai", "4.delhi",], ["1.narendra modi", "2.jawaharlal nehru", "3.rahul gandhi", "4.gandhi",]]
answer_list=[3, 4, 1]
lifeline_list=[["1.seven", "2.eight"], ["1.bhopal", "2.delhi"], ["1.rahul gandhi", "2.narendra modi"]]
lifeline_answer_list=[1, 2, 2]
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
