
def get_input_t():
    inp = '''5764801
17807724'''
    return [int(x) for x in inp.split("\n")]

def get_input():
    inp = '''11349501
5107328'''
    return [int(x) for x in inp.split("\n")]

def get_loop_size(inp_num):
    start_num = 1
    loop_size = 0
    while start_num != inp_num:
        loop_size += 1
        start_num *= 7
        start_num = start_num % 20201227
    return loop_size

def calc_encrypt(inp,loop_size):
    start_num = 1
    for _ in range(loop_size):
        start_num *= inp
        start_num = start_num % 20201227
    return start_num

def s1(inp):
    print(calc_encrypt(inp[0],get_loop_size(inp[1])))

s1(get_input())