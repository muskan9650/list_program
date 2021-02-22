question_list = [
    "How many continents are there?",
    "What is the capital of India?",         
    "who is prime minister of india?" 
]
a=[["1.four", "2.nine", "3.seven", "4.eight"], ["1.chandigarh", "2.bhopal", "3.chennai", "4.delhi",], ["1.narendra modi", "2.jawaharlal nehru", "3.rahul gandhi", "4.gandhi",]]
b=[3, 4, 1]
c=[["1.seven", "2.eight"], ["1.bhopal", "2.delhi"], ["1.rahul gandhi", "2.narendra modi"]]
d=[1, 2, 2]
amount=0
count=1
i=0
print("LETS PLAY THE GAME")
print("YOU HAVE ONLY ONE LIFELINE")
while i<len(question_list):
    print(question_list[i])
    print(a[i])
    print("DO YOU WANT 5050 LIFELINE",)
    n=input("yes/no")
    print("OHK!")
    if n=="yes":
        if count==1:
            print(c[i])
            n=int(input("enter a value"))
            if n!=d[i]:
                print("wrong answer")
                break
            count=count-1
        else:
            print("you already use lifeline")
            print(question_list[i])
            print(a[i])
            n=int(input("enter a value"))
            if n!=b[i]:
                print("wrong answer")
                break
    else:
        n=int(input("enter a value"))
        if n!=b[i]:
            print("wrong answer")
            break
    amount=amount+1000
    print("congratulation! you win $", amount)
    i=i+1
print("game finished! enjoy your day '-'")
