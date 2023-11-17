import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

symbols = ['<','>','=','!','v','^','(',')','⇒','∧','¬','∨','⇔',"⊥","⊤"]

symbols_for_use = ["⇔, ⇒, ∧, ∨, ¬, ⊥, ⊤"]

#skips steps
def steps_skip(s,v):
    s_ = list(s)
    for i in range(len(s_)):
            if s_[i] == ')':
                for j in range(i,-1,-1):
                    if s_[j] == '(':
                        s_[i] = ' '
                        s_[j] = ' '
                        v.append(i-j+1)
                        break





def initialize(z,skips,var):

    print("You can use these symbols: {} \nAnd also: {}".format(symbols_for_use,"[=, >, ^, v, !]"))
    print("Enter string:")
    x = str(input())

    # Remove extra spaces
    x = x.replace(" ", "")

    if len(x) == 1:
        if x in "⊥⊤" or x not in symbols:
            var[x[0]] = "?"
            z = [x]
            return x
    steps_skip(x, skips)

    rec(x, z, -1, skips, 0, 0, var)
    return x

# Counts operations
def nr_operations(s):
    v = 0
    s_ = list(s)
    for i in range(len(s_)):
        if s_[i] in symbols and s_[i] not in "().,":
            v += 1
    return v

# Automatically adds values to var dictionary
def auto_dic(bin,dic):
    o = -1
    for i in dic:
        if i in "⊥⊤":
            break
        o+=1
        dic[i] = bin[o]


#Add var to dict
def var_add(p,var):
    if p not in var:
        var[p] = "?"

# Main Parsing Method
def rec(prop,output,prop_pos,skips,i,l_r,var):

    #Takes in 7, arg1: String to be parsed, arg2: Empty list to return value, arg3: Start position for parsing, arg4: list containing skips


    global p
    p=i

    try:
        if prop[prop_pos + 1] in ".,":       # Only need to call prop_pos + 1
            print("I will never be printed")
    except:
        print("Missing closing parenthesis")
        exit()

    if prop[prop_pos] == ")" and prop[prop_pos + 1] in ".,":
        print("AM I EVEN CALLED?")
        return

    # VAR + )
    if (prop[prop_pos] in "⊥⊤" or prop[prop_pos] not in symbols) and prop[prop_pos + 1] == ")":
        if output[0] == 0:
            print("Too many parenthesis")
            exit()
        print("Move up")

        return

    # ) + )
    if prop[prop_pos] and prop[prop_pos+1] == ")":
        if output[0] == 0:
            print("Too many parenthesis")
            exit()
        print("Move up")
        return


    print("Step {}, Form: {}".format(l_r,output))
    # START
    if prop_pos == -1 and prop[prop_pos+1] == "(":
        output.append([0])
        rec(prop,output,prop_pos + 1,skips, p ,l_r+1,var)
        return

    # symbol + (
    elif prop[prop_pos] in symbols and prop[prop_pos] not in "()" and prop[prop_pos+1] == "(":
        if prop[prop_pos] in "!¬":
            output[1].append([0])
            print("Rec in pos [1]")
            rec(prop, output[1], prop_pos + 1, skips, i, l_r + 1,var)
            rec(prop, output, prop_pos + skips[p], skips, p + 1, l_r + 1,var)
            return
        else:
            output[2].append([0])
            print("Rec in pos [2]")
            rec(prop,output[2],prop_pos + 1,skips,i,l_r+1,var)
            rec(prop, output, prop_pos + skips[p], skips, p + 1, l_r + 1,var)
            return

    # ( + (
    if prop[prop_pos] == "(" and prop[prop_pos + 1] == "(":
        output.append([0])
        output[1].append([0])
        print("Rec in pos [1]")
        rec(prop, output[1], prop_pos + 1, skips, p, l_r+1,var)
        rec(prop,output,prop_pos + skips[p],skips, p+1,l_r+1,var)
        return

    # ( + !
    if prop[prop_pos] == "(" and prop[prop_pos + 1] in "!¬":
        output[0] = "¬"
        rec(prop,output,prop_pos + 1,skips,p,l_r+1,var)
        return

    # ( + VAR
    if prop[prop_pos] == "(" and (prop[prop_pos + 1] in "⊥⊤" or prop[prop_pos + 1] not in symbols):
        output.append([0])
        output[1] = [prop[prop_pos+1]]
        var_add(prop[prop_pos+1],var)
        rec(prop, output, prop_pos + 1, skips, p, l_r+1,var)
        return

    #VAR + symbol
    if (prop[prop_pos] in "⊥⊤" or prop[prop_pos] not in symbols) and prop[prop_pos + 1] in symbols and prop[prop_pos+1] not in "!()":
        output[0] = prop[prop_pos+1]
        rec(prop, output, prop_pos + 1, skips, p, l_r+1,var)
        return

    #symbol + VAR
    if prop[prop_pos] in symbols and ((prop[prop_pos + 1] in "⊥⊤" or prop[prop_pos + 1] not in symbols)) and prop[prop_pos+1] not in ".,":
        if prop[prop_pos] in "!¬":
            output[1] = [prop[prop_pos+1]]
            var_add(prop[prop_pos + 1], var)
            rec(prop, output, prop_pos + 1, skips, p, l_r + 1,var)
            return
        else:
            output[2] = [prop[prop_pos+1]]
            var_add(prop[prop_pos + 1], var)
            rec(prop, output, prop_pos + 1, skips, p, l_r+1,var)
            return

    # ) + symbol
    if prop[prop_pos] == ")" and prop[prop_pos+1] in symbols and prop[prop_pos+1] not in "!()":
        output[0] = prop[prop_pos+1]
        rec(prop,output,prop_pos+1,skips,p,l_r+1,var)
        return




    output = ["Wrong"]
    print(output)
    exit()


# Value under interpretation
def interp(s,itrp,lest):

    if s[0] in "⊤⊥" or s[0] not in symbols:
        rez = itrp[s[0]]
        return rez

    if s[0] in symbols:
        if s[0] in "⇒>":
            rez1 = interp(s[1],itrp,lest)
            rez2 = interp(s[2],itrp,lest)
            rez = (rez1 and rez2 ) or not interp(s[1],itrp,lest)
            lest.append(rez)
            return rez
        if s[0] in "∧^":
            rez1 = interp(s[1],itrp,lest)
            rez2 = interp(s[2],itrp,lest)
            rez = rez1 and rez2
            lest.append(rez)
            return rez
        if s[0] in "!¬":
            rez = (not interp(s[1],itrp,lest))
            lest.append(rez)
            return rez
        if s[0] in "∨v":
            rez1 = interp(s[1], itrp, lest)
            rez2 = interp(s[2], itrp, lest)
            rez = rez1 or rez2

            lest.append(rez)
            return rez
        if s[0] in "⇔=":
            rez = (interp(s[1],itrp,lest) == interp(s[2],itrp,lest))
            lest.append(rez)
            return rez


def table(s,itrp,z):
    if s[0] in "⊤⊥" or s[0] not in symbols:
        #rez = itrp[s[0]]
        return s[0]

    if s[0] in symbols:
        if s[0] in "⇒>":
            w = "({} ⇒ {})".format(table(s[1], itrp, z), table(s[2], itrp, z))
            z.append(w)
            return w
        if s[0] in "∧^":
            w = "({} ∧ {})".format(table(s[1], itrp, z), table(s[2], itrp, z))
            z.append(w)
            return w
        if s[0] in "!¬":
            w = "(¬{})".format(table(s[1],itrp,z))
            z.append(w)
            return w
        if s[0] in "∨v":
            w = "({} ∨ {})".format(table(s[1], itrp, z), table(s[2], itrp, z))
            z.append(w)
            return w
        if s[0] in "⇔=":
            w = "({} ⇔ {})".format(table(s[1],itrp,z),table(s[2],itrp,z))
            z.append(w)
            return w


def da(var,x,z):
    for i in var.copy():
        if i in "⊤⊥":
            var.pop(i)
            if i == "⊥":
                var[i] = "F"
            else:
                var[i] = "T"
    lest = [[]]
    result_val = []
    o = len(var) + nr_operations(x)
    #for i in range(o):
        #lest[0].append(i)
    #lest.append([])
    l=0
    nr_var = 0
    for i in var:
        if i in "⊤⊥":
            l+=1
        nr_var += 1
        lest[0].append(i)


    table(z, var, lest[0])

    model = "0:0{}b".format(nr_var-l)
    model = "{" + model + "}"

    k = 0
    for i in range(2 ** int(nr_var-l)):
        k += 1
        lest.append([])

        auto_dic(model.format(i), var)
        for i in var:
            if var[i] == "1" or var[i] == "T" or var[i] == True:
                var[i] = True
                lest[k].append(var[i])
            elif var[i] == "0" or var[i] == "F" or var[i] == False:
                var[i] = False
                lest[k].append(var[i])

        result = interp(z, var, lest[k])
        result_val.append(result)
    return lest, result_val



while(True):


    print("Choose operation:\n [1] Verify proposition \n [2] Compute given interpretation. \n [3] Compute table of all interpretations\n [4] Compute logical equivalence \n [5] Exit")
    print("Your operation: ")
    y = int(input())

    # Verify proposition
    if y == 1:
        z = [0]
        skips = []
        var = {}
        x = initialize(z,skips,var)
        if len(x) == 1:
            z = [x]

        print()
        print("{} is a WFF.\n".format(x))
        print("It's abstract representation is: \n {} \n".format(z))
    # Compute one interpretation
    if y == 2:
        z = [0]
        skips = []
        var = {}
        lest = []
        x = initialize(z, skips, var)
        if len(x) == 1:
            z = [x]

        print("Enter Interpretation (T or F):")

        for i in var:
            if i == "⊤":
                var[i] = "T"
                continue
            elif i == "⊥":
                var[i] = "F"
                continue
            print("Truth value of {}".format(i))
            var[i] = str(input())
            if var[i] not in "TF":
                print("Wrong input, restart")
                exit()

        print(var)

        for i in var:
            if var[i] == "T":
                var[i] = True
            else:
                var[i] = False

        result = interp(z, var,lest)

        for i in var:
            if var[i] == 1:
                var[i] = "T"
            else:
                var[i] = "F"

        print("The truth value of {} under the interpretation {} is {}\n".format(x, var, result))
        print("Start over?(Y/N)")
        if input() == "Y":
            continue
        else:
            exit()
    # Compute table
    elif y == 3:
        z = [0]
        skips = []
        var = {}
        lest = []
        x = initialize(z,skips,var)
        if len(x) == 1:
            z = [x]

        temp = da(var,x,z)

        print(pd.DataFrame(temp[0]))
        #for i in temp[0]:
            #print(i)
        print()
        j = temp[1][0]

        i=0
        while i < len(temp[1])-1:
            if temp[1][i] == temp[1][i+1]:
                i+=1
                continue
            else:
                print("The proposition is satisfiable\n")
                break
        else:
            if j:
                print("The proposition is valid\n")
            else:
                print("The proposition is unsatisfiable\n")
    # Logical Equivalence
    elif y == 4:
        l_eq = [0,0]
        print("Insert two propositions:")
        for i in range(2):
            print("Proposition {}:".format(i+1))
            z = [0]
            skips = []
            var = {}
            x = initialize(z,skips,var)
            if len(x) == 1:
                z = [x]
            l_eq[i] = da(var, x, z)[1]
        if l_eq[0] == l_eq[1]:
            print("The two propositions are logically equivalent")
        else:
            print("The propositions are not logically equivalent")


    elif y == 5:
        exit()









