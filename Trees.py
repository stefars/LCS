import pandas as pd
import time

st_p = time.process_time()
st_w = time.time()

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

symbols = ['<', '>', '=', '!', 'v', '^', '(', ')', '⇒', '∧', '¬', '∨', '⇔', "⊥", "⊤"]

symbols_for_use = ["⇔, ⇒, ∧, ∨, ¬, ⊥, ⊤"]


# skips steps

def stepsSkip(raw_proposition, list_of_steps):
    raw_proposition = list(raw_proposition)
    for index in range(len(raw_proposition)):
        if raw_proposition[index] == ')':
            for descending_index in range(index, -1, -1):
                if raw_proposition[descending_index] == '(':
                    raw_proposition[index] = ' '
                    raw_proposition[descending_index] = ' '
                    list_of_steps.append(index - descending_index + 1)
                    break


def initialize(abstract_tree, skips, var):
    print("You can use these symbols: {} \nAnd also: {}".format(symbols_for_use, "[=, >, ^, v, !]"))
    proposition = str(input("Enter string:"))

    # Remove extra spaces
    proposition = proposition.replace(" ", "")

    if len(proposition) == 1:
        if proposition in "⊥⊤" or proposition not in symbols:
            var[proposition[0]] = "?"
            abstract_tree = [proposition]
            return proposition
    stepsSkip(proposition, skips)

    strongParser(proposition, abstract_tree, -1, skips, 0, 0, var)
    return proposition


# Counts operations
def nr_operations(proposition):
    number_of_operations = 0
    proposition = list(proposition)
    for index in range(len(proposition)):
        if proposition[index] in symbols and proposition[index] not in "().,":
            number_of_operations += 1
    return number_of_operations


def auto_dic(binary_number, dictionary_of_variables):
    """Automatically adds values to var dictionary.
        Maps the binary value (bin) to it's corresponding variable in (var), considering order:
        (000) -> (ABC); All 0's, (001) -> (ABC); C = 1, A = B = 0 and so on."""
    binary_index = -1
    for index in dictionary_of_variables:
        if index in "⊥⊤":
            break
        binary_index += 1
        dictionary_of_variables[index] = binary_number[binary_index]


# Add var to dict
def var_add(symbol, dictionary_of_variables):
    if symbol not in dictionary_of_variables:
        dictionary_of_variables[symbol] = "?"


# Main Parsing Method
def strongParser(proposition, abstract_tree, proposition_index, skips, skips_pos, step, variables):
    """ Takes in 7, arg1: String to be parsed, arg2: Empty list to return value, arg3: Start position for parsing,
     arg4: list containing skips"""

    global p
    p = skips_pos

    symbol_one = proposition[proposition_index]
    symbol_two = proposition[proposition_index + 1]

    try:
        if symbol_two in ".,":  # Only need to call prop_pos + 1
            print("I will never be printed")
    except:
        print("Missing closing parenthesis")
        exit()

    if symbol_one == ")" and symbol_two in ".,":
        print("AM I EVEN CALLED?")
        return

    # VAR + )
    if (symbol_one in "⊥⊤" or symbol_one not in symbols) and symbol_two == ")":
        if abstract_tree[0] == 0:
            print("Too many parenthesis")
            exit()
        print("Move up")

        return

    # ) + )
    if symbol_one == ")" and symbol_two == ")":
        if abstract_tree[0] == 0:
            print("Too many parenthesis")
            exit()
        print("Move up")
        return

    print("Step {}, Form: {}".format(step, abstract_tree))
    # START
    if proposition_index == -1 and symbol_two == "(":
        abstract_tree.append([0])
        strongParser(proposition, abstract_tree, proposition_index + 1, skips, p, step + 1, variables)
        return

    # symbol + (
    if symbol_one in symbols and symbol_one not in "()" and symbol_two == "(":
        if symbol_one in "!¬":
            abstract_tree[1].append([0])
            print("Rec in pos [1]")
            strongParser(proposition, abstract_tree[1], proposition_index + 1, skips, skips_pos, step + 1, variables)
            strongParser(proposition, abstract_tree, proposition_index + skips[p], skips, p + 1, step + 1, variables)
            return
        else:
            abstract_tree[2].append([0])
            print("Rec in pos [2]")
            strongParser(proposition, abstract_tree[2], proposition_index + 1, skips, skips_pos, step + 1, variables)
            strongParser(proposition, abstract_tree, proposition_index + skips[p], skips, p + 1, step + 1, variables)
            return

    # ( + (
    if symbol_one == "(" and symbol_two == "(":
        abstract_tree.append([0])
        abstract_tree[1].append([0])
        print("Rec in pos [1]")
        strongParser(proposition, abstract_tree[1], proposition_index + 1, skips, p, step + 1, variables)
        strongParser(proposition, abstract_tree, proposition_index + skips[p], skips, p + 1, step + 1, variables)
        return

    # ( + !
    if symbol_one == "(" and symbol_two in "!¬":
        abstract_tree[0] = "¬"
        strongParser(proposition, abstract_tree, proposition_index + 1, skips, p, step + 1, variables)
        return

    # ( + VAR
    if symbol_one == "(" and (symbol_two in "⊥⊤" or symbol_two not in symbols):
        abstract_tree.append([0])
        abstract_tree[1] = [proposition[proposition_index + 1]]
        var_add(proposition[proposition_index + 1], variables)
        strongParser(proposition, abstract_tree, proposition_index + 1, skips, p, step + 1, variables)
        return

    # VAR + symbol
    if (symbol_one in "⊥⊤" or symbol_one not in symbols) and symbol_two in symbols and symbol_two not in "!()":
        abstract_tree[0] = symbol_two
        strongParser(proposition, abstract_tree, proposition_index + 1, skips, p, step + 1, variables)
        return

    # symbol + VAR
    if symbol_one in symbols and (symbol_two in "⊥⊤" or symbol_two not in symbols) and symbol_two not in ".,":
        if symbol_one in "!¬":
            abstract_tree[1] = [symbol_two]
        else:
            abstract_tree[2] = [symbol_two]

        var_add(symbol_two, variables)
        strongParser(proposition, abstract_tree, proposition_index + 1, skips, p, step + 1, variables)
        return

    # ) + symbol
    if symbol_one == ")" and symbol_two in symbols and symbol_two not in "!()":
        abstract_tree[0] = symbol_two
        strongParser(proposition, abstract_tree, proposition_index + 1, skips, p, step + 1, variables)
        return

    abstract_tree = ["Wrong"]
    print(abstract_tree)
    exit()


# Value under interpretation
def interp(abstract_representation, interpretation, lest):
    if abstract_representation[0] in "⊤⊥" or abstract_representation[0] not in symbols:
        rez = interpretation[abstract_representation[0]]
        return rez

    if abstract_representation[0] in symbols:

        if abstract_representation[0] in "⇒>":
            rez1 = not interp(abstract_representation[1], interpretation, lest)
            rez2 = interp(abstract_representation[2], interpretation, lest)
            rez = (rez1 or rez2)
            lest.append(rez)
            return rez

        if abstract_representation[0] in "∧^":
            rez1 = interp(abstract_representation[1], interpretation, lest)
            rez2 = interp(abstract_representation[2], interpretation, lest)
            rez = rez1 and rez2
            lest.append(rez)
            return rez

        if abstract_representation[0] in "!¬":
            rez = (not interp(abstract_representation[1], interpretation, lest))
            lest.append(rez)
            return rez

        if abstract_representation[0] in "∨v":
            rez1 = interp(abstract_representation[1], interpretation, lest)
            rez2 = interp(abstract_representation[2], interpretation, lest)
            rez = rez1 or rez2
            lest.append(rez)
            return rez

        if abstract_representation[0] in "⇔=":
            rez = (interp(abstract_representation[1], interpretation, lest) == interp(abstract_representation[2],
                                                                                      interpretation, lest))
            lest.append(rez)
            return rez


def table_heading(abstract_representation, operations):
    connective = abstract_representation[0]

    if connective in "⊤⊥" or connective not in symbols:
        return connective

    if connective in symbols:

        element_one = abstract_representation[1]
        element_two = abstract_representation[2]

        if connective in "⇒>":
            table_element = "({} ⇒ {})".format(table_heading(element_one, operations), table_heading(element_two, operations))
            operations.append(table_element)
            return table_element

        if connective in "∧^":
            table_element = "({} ∧ {})".format(table_heading(element_one, operations), table_heading(element_two, operations))
            operations.append(table_element)
            return table_element

        if connective in "!¬":
            table_element = "(¬{})".format(table_heading(element_one, operations))
            operations.append(table_element)
            return table_element

        if connective in "∨v":
            table_element = "({} ∨ {})".format(table_heading(element_one, operations), table_heading(element_two, operations))
            operations.append(table_element)
            return table_element

        if connective in "⇔=":
            table_element = "({} ⇔ {})".format(table_heading(element_one, operations), table_heading(element_two, operations))
            operations.append(table_element)
            return table_element


def da(variables, abstract_representation):
    table = [[]]
    proposition_result = []
    nr_var = 0
    for j in variables:
        if j in "⊤⊥":
            nr_var -= 1
        nr_var += 1
        table[0].append(j)

    table_heading(abstract_representation, table[0])

    # Make a binary number containing exactly nr_var elements.
    model = "0:0{}b".format(nr_var)
    model = "{" + model + "}"

    k = 0
    for i in range(2 ** int(nr_var)):
        k += 1
        table.append([])

        auto_dic(model.format(i), variables)
        for j in variables:


            if variables[j] == "1" or variables[j] == "T" or variables[j] == True:
                variables[j] = True
                table[k].append(variables[j])
            elif variables[j] == "0" or variables[j] == "F" or variables[j] == False:
                variables[j] = False
                table[k].append(variables[j])

        result = interp(abstract_representation, variables, table[k])
        proposition_result.append(result)
    return table, proposition_result


def main():
    while (True):

        print(
            "Choose operation:\n [1] Verify proposition \n [2] Compute given interpretation. \n [3] Compute table of all interpretations\n [4] Compute logical equivalence \n [5] Exit")
        print("Your operation: ")
        y = int(input())

        # Verify proposition
        if y == 1:
            z = [0]
            skips = []
            var = {}
            x = initialize(z, skips, var)
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

            result = interp(z, var, lest)

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
            x = initialize(z, skips, var)
            et_w = time.time()
            et_p = time.process_time()
            print("Process time:{}".format(et_p - st_p))
            print("Wall time:{}".format(et_w - st_w))
            if len(x) == 1:
                z = [x]
            table_ = da(var, z)
            table_values = table_[0][1:]
            table_columns = table_[0][0]

            # Panda Table
            df = pd.DataFrame(table_values)
            df.columns = table_columns
            print(df)

            j = table_[1][0]

            i = 0

            while i < len(table_[1]) - 1:
                if table_[1][i] == table_[1][i + 1]:
                    i += 1
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
            l_eq = [0, 0]
            print("Insert two propositions:")
            for i in range(2):
                print("Proposition {}:".format(i + 1))
                z = [0]
                skips = []
                var = {}
                x = initialize(z, skips, var)
                var = dict(sorted(var.items()))
                if len(x) == 1:
                    z = [x]

                l_eq[i] = da(var, z)[1]
            a = len(l_eq[0])
            b = len(l_eq[1])
            if b == 1:
                for i in range(a - 1):
                    l_eq[1].append(l_eq[1][0])
            if a == 1:
                for i in range(b - 1):
                    l_eq[0].append(l_eq[0][0])

            if l_eq[0] == l_eq[1]:
                print("The two propositions are logically equivalent")
            else:
                print("The propositions are not logically equivalent")

        elif y == 5:
            return ()


main()


"""
    (F v (F^G)) ~ F
"""
