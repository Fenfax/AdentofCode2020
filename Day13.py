
def get_input():
    inp = '''1001938
41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'''
    return int(inp.split("\n")[0]),[x for x in inp.split("\n")[1].split(",")]


def s1():
    start_time,bus_ids = get_input()
    bus_ids = [int(x) for x in bus_ids if x != "x"]
    time_cnt = start_time
    while True:
        possible_departs = [x for x in bus_ids if time_cnt % x == 0]
        if len(possible_departs) > 0:
            return (time_cnt - start_time) * possible_departs[0]
        time_cnt +=1

def get_val(cur_val,t_dict):
    return_arr = []
    for x,after in t_dict.items():
        if (cur_val + after) % x == 0:
            return_arr.append(x)
        else:
            return return_arr
    return return_arr

def s2():
    start_time,bus_ids = get_input()
    start_time = start_time
    bus_timing = {[int(x) for x in bus_ids if x != "x"][0]:0}
    bus_timing = {}
    for y,x in enumerate(bus_ids):
        if x != "x":
            bus_timing[int(x)] = y
    
    print(bus_timing)

    current_time = 100000000000000
    current_time = 100000586937155
    current_time = 100105832739903
    current_time = 556100168221130
    while True:
        tmp_arr = get_val(current_time,bus_timing)
        if len(tmp_arr) == len(bus_timing):
            return current_time
        if 41 in tmp_arr:
            current_time += 41
        else:
            current_time += 1

    

print(s1())
print(s2())