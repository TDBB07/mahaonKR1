def decorator(func):
    def wrapper():
        print()
        func()
        print(s)
    return wrapper
u1=int(input())
u2=int(input())
t=int(input())
a=u2-u1/t
s=u1*t+a*t*t/2
def mama():
    print(a)
mama=decorator(mama)
mama()
