import pprint as pp
import numpy as np

def get_input_t():
    inp ='''.#.
..#
###'''
    overw = inp.split("\n")
    arr_len = len(overw)
    out = {0:{}}
    for x in range(arr_len):
        out[0][x] = {y:"#" for y,z in enumerate(overw[x]) if z == "#"}
    return out

def get_input():
    inp ='''######.#
##.###.#
#.###.##
..#..###
##.#.#.#
##...##.
#.#.##.#
.###.###'''
    overw = inp.split("\n")
    arr_len = len(overw)
    out = {0:{}}
    for x in range(arr_len):
        out[0][x] = {y:"#" for y,z in enumerate(overw[x]) if z == "#"}
    return out

def active_nearby(x1,y1,z1,check_dict):
    cnt = 0
    for z2 in range(-1,2):
        for x2 in range(-1,2):
            for y2 in range(-1,2):
                if (x2 | y2 | z2 ) != 0 and check_dict.get(z1+z2) is not None and check_dict[z1+z2].get(x1+x2) is not None and check_dict[z1+z2][x1+x2].get(y1+y2) is not None:
                    cnt +=1
    return cnt

def active_nearby_4d(x1,y1,z1,w1,check_dict):
    cnt = 0
    for w2 in range(-1,2):
        for z2 in range(-1,2):
            for x2 in range(-1,2):
                for y2 in range(-1,2):
                    if ((x2 | y2 | z2 | w2 ) != 0 
                    and check_dict.get(w1+w2) is not None 
                    and check_dict[w1+w2].get(z1+z2) is not None
                    and check_dict[w1+w2][z1+z2].get(x1+x2) is not None
                    and check_dict[w1+w2][z1+z2][x1+x2].get(y1+y2) is not None):
                        cnt +=1
    return cnt

def add_to_dict(x,y,z,add,val):
    if add.get(z) is None:
        add[z] = {}
    if add[z].get(x) is None:
        add[z][x] = {}
    add[z][x][y] = val
    return add

def add_to_dict_4d(x,y,z,w,add,val):
    if add.get(w) is None:
        add[w] = {}
    if add[w].get(z) is None:
        add[w][z] = {}
    if add[w][z].get(x) is None:
        add[w][z][x] = {}
    add[w][z][x][y] = val
    return add

def s1(inp, repeat):
    pre_run = inp.copy()
    for dummy in range(repeat):
        new_dict = {}
        for z in range(min(pre_run.keys()) - 1,max(pre_run.keys())+2):
            check_arr = [b for c in pre_run.keys() for b in pre_run[c].keys()]
            for x in range(min(check_arr) - 1,max(check_arr)+2):
                check_arr = [a for c in pre_run.keys() for b in pre_run[c].keys() for a in pre_run[c][b].keys()]
                for y in range(min(check_arr) - 1,max(check_arr)+2):
                    cnt = active_nearby(x,y,z,pre_run)
                    if cnt == 3:
                        new_dict = add_to_dict(x,y,z,new_dict,"#")
                    elif cnt == 2 and pre_run.get(z) is not None and pre_run[z].get(x) is not None and pre_run[z][x].get(y) is not None:
                        new_dict = add_to_dict(x,y,z,new_dict,"#")
        pre_run = new_dict.copy()
    pp.pprint(pre_run)

    print(len([a for c in pre_run.keys() for b in pre_run[c].keys() for a in pre_run[c][b].keys()]))

def s2(inp,repeat):
    pre_run = inp.copy()
    for dummy in range(repeat):
        new_dict = {}
        for w in range(min(pre_run.keys()) - 1,max(pre_run.keys())+2):
            check_arr = [b for c in pre_run.keys() for b in pre_run[c].keys()]
            for z in range(min(check_arr) - 1,max(check_arr)+2):
                check_arr = [a for c in pre_run.keys() for b in pre_run[c].keys() for a in pre_run[c][b].keys()]
                for x in range(min(check_arr) - 1,max(check_arr)+2):
                    check_arr = [aa for c in pre_run.keys() for b in pre_run[c].keys() for a in pre_run[c][b].keys() for aa in pre_run[c][b][a].keys()]
                    for y in range(min(check_arr) - 1,max(check_arr)+2):
                        cnt = active_nearby_4d(x,y,z,w,pre_run)
                        if cnt == 3:
                            new_dict = add_to_dict_4d(x,y,z,w,new_dict,"#")
                        elif (cnt == 2 
                        and pre_run.get(w) is not None
                        and pre_run[w].get(z) is not None 
                        and pre_run[w][z].get(x) is not None 
                        and pre_run[w][z][x].get(y) is not None):
                            new_dict = add_to_dict_4d(x,y,z,w,new_dict,"#")
        pre_run = new_dict.copy()
    # pp.pprint(pre_run)

    print(len([aa for c in pre_run.keys() for b in pre_run[c].keys() for a in pre_run[c][b].keys() for aa in pre_run[c][b][a].keys()]))
                    

s1(get_input(),6)
s2({0:get_input()},6)
