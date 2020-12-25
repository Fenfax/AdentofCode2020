import copy as cp

def get_input_t():
    inp ='''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''
    out = {}
    current_player = ""
    for x in inp.split("\n"):
        if x == "":
            continue
        elif x.startswith("Player"):
            current_player = x.split(" ")[1][:-1]
            out[current_player] = []
        else:
            out[current_player].append(int(x))
    return out

def get_input_t2():
    inp ='''Player 1:
43
19

Player 2:
2
29
14'''
    out = {}
    current_player = ""
    for x in inp.split("\n"):
        if x == "":
            continue
        elif x.startswith("Player"):
            current_player = x.split(" ")[1][:-1]
            out[current_player] = []
        else:
            out[current_player].append(int(x))
    return out

def get_input():
    inp ='''Player 1:
8
19
46
11
36
10
35
9
24
22
50
1
34
7
18
28
3
38
43
2
6
42
23
12
20

Player 2:
39
27
44
29
5
48
30
32
15
31
14
21
49
17
45
47
16
26
33
25
13
41
4
40
37'''
    out = {}
    current_player = ""
    for x in inp.split("\n"):
        if x == "":
            continue
        elif x.startswith("Player"):
            current_player = x.split(" ")[1][:-1]
            out[current_player] = []
        else:
            out[current_player].append(int(x))
    return out


def s1(inp):
    while len([key for key,val in inp.items() if len(val) > 0]) > 1:
        played_cards = {}
        for key in inp.keys():
            played_cards[key] = inp[key][0]
            del inp[key][0]
        winnerplayer = [x for x in played_cards if played_cards[x] == max([y for y in played_cards.values()])][0]
        for played in sorted(played_cards.values())[::-1]:
            inp[winnerplayer].append(played)
        print(inp,winnerplayer)

    sum_all =0
    for i,x in enumerate(inp[winnerplayer][::-1]):
        i += 1
        sum_all += x*i
    print(sum_all)

def play_game(new_inp,level):
    old_dects = {}
    inp = cp.deepcopy(new_inp)
    for x in inp:
        old_dects[x] = set()
    while len([key for key,val in inp.items() if len(val) > 0]) > 1:
        for x in inp:
            check = ",".join([str(y) for y in inp[x]])
            if check in old_dects[x]:
                return '1',inp
            else:
                old_dects[x].add(check)
        played_cards = {}
        for key in inp.keys():
            played_cards[key] = inp[key][0]
            del inp[key][0]
        to_recursive = 0
        rec_game = {}
        for key,val in played_cards.items():
            if val <= len(inp[key]):
                rec_game[key] = inp[key].copy()[:val]
                to_recursive += 1
        if to_recursive == len(played_cards.keys()):
            winnerplayer = play_game(rec_game,level + 1)[0]
        else:
            winnerplayer = [x for x in played_cards if played_cards[x] == max([y for y in played_cards.values()])][0]
        inp[winnerplayer].append(played_cards.get(winnerplayer))
        for played in [x for x in sorted(played_cards.values())[::-1] if x != played_cards.get(winnerplayer)]:
            inp[winnerplayer].append(played)
        # print(level,inp,winnerplayer)
    
    sum_all =0
    for i,x in enumerate(inp[winnerplayer][::-1]):
        i += 1
        sum_all += x*i
    print(sum_all,winnerplayer)
    
    return winnerplayer,inp
def s2(inp):
    
    winnerplayer,inp = play_game(inp,0)

    sum_all =0
    for i,x in enumerate(inp[winnerplayer][::-1]):
        i += 1
        sum_all += x*i
    print(sum_all,winnerplayer)

# s1(get_input())
s2(get_input())