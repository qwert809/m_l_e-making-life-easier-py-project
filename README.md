print("Powered BY CatBet123")
print("GitHub Community")
print("11.12.2024  \nnm<12>core\n")

# m_l_e-making-life-easier-py-project

#Function pri_
python
def pri_(pr = "",parameter = None ):
    if parameter == "$cl":
        print(pr,"                  |$ console log ")
    elif parameter == None:
        print(pr)
    else:
        print(pr,"                  |$",parameter )
        
#The pri_ function prints the pr string. If parameter equals "$cl", it adds " |$ console log " text. If parameter is not provided, it only prints pr. Otherwise, it adds " |$" and the value of parameter.


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
    
#The if_ function compares the values of a and c according to the operator b (<, >, =, !). It returns True if the condition is met, or False otherwise.


#Class do
#python
class do():
    global rm
    rm = {}
    def new(new, zn = None):
        rm[new] = zn
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
            
#The do class manages an associative array rm.
#new(new, zn = None): creates a new variable new in the rm array with the value zn.
#edit(what, zn): changes the value of the variable what to zn.
#get(what): returns the value of the variable what. If what is equal to "$all$", it returns the entire rm array.
#delit(what): deletes the variable what from the rm array.
#are_yes(what): returns True if the variable what exists in the rm array, or None if it does not.
