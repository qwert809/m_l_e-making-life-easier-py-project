print("Povered BY CatBet123")
print("GitHub Communiti")
print("11.12.2024  \nnm<12>core\n")
def pri_(pr = "",parameter = None ):
    if parameter == "$cl":
        print(pr,"                  |$ consol log ")
    elif parameter == None:
        print(pr)
    else:
        print(pr,"                  |$",parameter )

def if_(a, b, c):
    if b == "<": 
        if a <= c:
            msd = True 
        else:
            msd = False
    elif b == ">":
        if a >= c:
            msd = True
        else:
            msd = False
    elif b == "=":
        if a == c:
            msd = True
        else:
            msd = False
    elif b == "!":
        if a != c:
            msd = True
        else:
            msd = False
    else:
        msd = None
    return msd


class do():
        #zm ця зміна що є прив'язаним до ключа в асоціятивному масиві
        #what ця зміна означає ключ до значення в асоціятивному масиві
    global rm
    rm = {}
    def new(new, zn = None):    #функція створення зміної в середені асоціятивного масиву 'rm'.
        rm[new] = zn            #'new' це ім'я зміної а zn значення 
    def edit(what, zn):
        rm[what] = zn
    def get(what):
        if what == "$all$":
            return(rm)
        else:
            return(rm[what])
    def delit(what):
        rm.pop(what)
    def are_yes(what):
        if what in rm: 
            return(True)
        else: 
            return(None)

