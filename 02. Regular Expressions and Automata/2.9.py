import re

no_states = 5
transition_table = [{} for i in range(no_states)]
transition_table[0]['b'] = 1
transition_table[1]['a']=2
transition_table[2]['a']=3
transition_table[3]['a']=3
transition_table[3]['!']=4
success = [False,False,False,False,True]

def d_recognize(strr):
    state = 0
    for char in strr:
        if success[state] is True:
            return True # we fixed the second deficiency.
        else:
            try:
                state = transition_table[state][char]
            except KeyError:
                return False
    return success[state]

def ngd(strr):
    for i in range(len(strr)):
        if d_recognize(strr[i:]) is True:
            return True
    return False

if __name__=="__main__":
    b = input("input: ")
    print(d_recognize(b)) # True if input starts with sheep-language.
    print(ngd(b)) # True if input contains sheep-language

