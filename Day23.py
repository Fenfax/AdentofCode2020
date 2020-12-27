

def get_input_t():
    inp = '''389125467'''
    return [int(x) for x in inp]

def get_input():
    inp = '''364297581'''
    return [int(x) for x in inp]

def s2_input(inp):
    for x in range(max(inp)+1,1000001):
        inp.append(x)
    return inp

def s1(inp,move_cnt):
    cur_pos = 0
    for z in range(move_cnt):
        num_to_find = inp[cur_pos] - 1
        pickup = []
        for _ in range(3):
            pickup.append(inp.pop(c if (c:= cur_pos + 1) < len(inp) else 0))
        next_cup = inp[c if (c:= cur_pos + 1) < len(inp) else 0]
        while num_to_find not in inp:
            num_to_find -= 1
            if num_to_find < 0:
                num_to_find = max(inp)
        cur_pos = inp.index(num_to_find)
        inp = inp[:cur_pos+1] + pickup + inp[cur_pos+1:]
        cur_pos = inp.index(next_cup)
    
    while inp[0] != 1:
        inp.append(inp.pop(0))

    if move_cnt <= 100:
        print("".join([str(x) for x in inp if x != 1]))
    else:
        print(inp[1],inp[2],inp[1]*inp[2])


def s2(inp,move_cnt):
    work_dict = {x: y for x, y in zip(inp, inp[1:] + [inp[0]])}
    current_num = inp[0]

    for z in range(move_cnt):
        tmp_num = current_num
        picklist = []
        picklist = [tmp_num := work_dict[tmp_num]  for _ in range(3) ]
        # for _ in range(3):
        #     picklist.append(work_dict[tmp_num])
        #     tmp_num = work_dict[tmp_num]
        work_dict[current_num] = work_dict[tmp_num]       
        num_to_find = current_num - 1
        while num_to_find in picklist or num_to_find not in work_dict.keys():
            num_to_find -= 1
            if num_to_find <= 0:
                num_to_find = max(work_dict.keys())
        
        work_dict[picklist[-1]],work_dict[num_to_find] = work_dict[num_to_find],picklist[0]

        current_num = work_dict[current_num]



    current_num = 1
    out = []
    while work_dict[current_num] != 1:
        out.append(work_dict[current_num])
        current_num = work_dict[current_num]

    if move_cnt <= 100:
        print("".join([str(x) for x in out]))
    else:
        print(out[0],out[1],out[0]*out[1])
        
    

    


s1(get_input(),100)
s2(s2_input(get_input()),10000000)
# s2(get_input(),100)