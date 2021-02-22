question_list = [
    "How many continents are there?",
    "What is the capital of India?",         
    "who is president of india?" 
]
a=[["1.four", "2.nine", "3.seven", "4.eight","5.helpline-5050"], ["1.chandigarh", "2.bhopal", "3.chennai", "4.delhi","5.helpline-5050"], ["1.narendra modi", "2.jawaharlal nehru", "3.rahul gandhi", "4.gandhi","5.helpline-5050"]]
b=[3, 4, 1]
c=[["1.seven", "2.eight"], ["1.bhopal", "2.delhi"], ["1.rahul gandhi", "2.narendra modi"]]
d=[1, 2, 2]
p=[["1.four", "2.nine", "3.seven", "4.eight"], ["1.chandigarh", "2.bhopal", "3.chennai", "4.delhi"], ["1.narendra modi", "2.jawaharlal nehru", "3.rahul gandhi", "4.gandhi"]]
amount=0
count=1
i=0
while i<len(question_list):
    print(question_list[i])
    print(a[i])
    n=int(input("enter a value"))
    if n!=b[i] and n!=5:
        print("wrong answer")
        break
    elif n==5:
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
            print(p[i])
            n=int(input("enter a value"))
            if n!=b[i]:
                print("wrong answer")
    amount=amount+1000
    print("congratulation! you win $", amount)
    i=i+1
print("game finished! enjoy your day '-'")