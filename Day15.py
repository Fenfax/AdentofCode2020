

def get_input():
    inp = '''15,5,1,4,7,0'''
    return {int(y):[x,x] for x,y in enumerate(inp.split(","))}


def s1(inp,turns):
    last_turn = [last_val for last_val,turn in inp.items() if turn[0] == len(inp.keys()) -1][0]
    allready_called = False
    for turn in range(len(inp.keys()),turns):
        if last_turn in inp.keys() and allready_called == True:
            new_number = (turn - 1) - inp[last_turn][0] 
            inp[last_turn][0] = inp[last_turn][1]
        else:
            new_number = 0
        if new_number in inp.keys():
            allready_called = True
            inp[new_number][1] = turn
        else:
            allready_called = False
            inp[new_number] = [turn,turn]       

        last_turn = new_number
    return new_number
      
      
print(s1(get_input(),2020))
print(s1(get_input(),30000000))