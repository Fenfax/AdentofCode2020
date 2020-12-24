import re

def get_input_t():
    inp = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''
    rule_dict = {}
    do_sol = False
    sol = []
    inp = inp.replace('"',"")
    for x in inp.split("\n"):
        if x == "":
            do_sol = True
        elif do_sol:
            sol.append(x)
        else:
            split = x.split(": ")
            rule_dict[int(split[0])] = [y.split(" ") for y in split[1].split(" | ")]
    return rule_dict,sol

def get_input_t2():
    inp = '''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''
    rule_dict = {}
    do_sol = False
    sol = []
    inp = inp.replace('"',"")
    for x in inp.split("\n"):
        if x == "":
            do_sol = True
        elif do_sol:
            sol.append(x)
        else:
            split = x.split(": ")
            rule_dict[int(split[0])] = [y.split(" ") for y in split[1].split(" | ")]
    return rule_dict,sol

def get_input():
    inp = '''65: 35 126 | 43 104
35: "b"
28: 43 93 | 35 109
81: 35 16 | 43 126
100: 95 35 | 67 43
4: 113 35 | 61 43
93: 43 94 | 35 38
60: 35 108 | 43 102
19: 43 131 | 35 40
110: 43 92 | 35 126
116: 35 43 | 43 63
48: 35 35
82: 68 43 | 49 35
26: 35 58 | 43 24
89: 35 6 | 43 50
47: 90 35 | 65 43
56: 14 35 | 104 43
90: 43 92 | 35 18
43: "a"
94: 39 43 | 75 35
70: 55 43 | 12 35
55: 43 119 | 35 71
84: 7 35 | 76 43
128: 34 35 | 23 43
34: 63 63
105: 35 126 | 43 23
126: 35 43 | 43 43
107: 35 70 | 43 132
63: 35 | 43
27: 35 34 | 43 112
106: 33 43 | 77 35
132: 35 66 | 43 84
5: 92 43 | 48 35
91: 35 118 | 43 1
52: 115 63
37: 35 112 | 43 104
30: 35 59 | 43 14
73: 35 97 | 43 119
130: 35 74 | 43 75
129: 35 18 | 43 48
85: 43 43 | 43 35
29: 34 35
96: 35 127 | 43 3
75: 35 18 | 43 85
58: 101 35 | 36 43
11: 42 31
7: 126 43 | 14 35
59: 35 43
118: 35 126 | 43 18
33: 96 43 | 20 35
16: 43 43
92: 35 43 | 35 35
61: 16 35 | 34 43
111: 114 43 | 123 35
88: 43 26 | 35 19
114: 43 18 | 35 14
103: 65 43 | 128 35
38: 35 56 | 43 50
44: 88 43 | 83 35
76: 43 16 | 35 115
68: 43 13 | 35 69
22: 85 43 | 16 35
8: 42
113: 35 23 | 43 85
124: 15 43 | 47 35
104: 35 43 | 63 35
20: 4 35 | 78 43
49: 35 17 | 43 39
21: 43 48 | 35 104
109: 43 60 | 35 98
1: 43 48 | 35 126
121: 43 79 | 35 28
99: 73 35 | 103 43
42: 43 106 | 35 121
64: 35 118 | 43 81
102: 34 35 | 59 43
62: 35 91 | 43 64
50: 43 23 | 35 48
67: 35 105 | 43 2
83: 99 35 | 82 43
25: 35 41 | 43 117
97: 43 34 | 35 104
46: 43 57 | 35 128
15: 43 27 | 35 32
108: 85 43 | 126 35
10: 43 13 | 35 9
95: 86 43 | 30 35
127: 43 110 | 35 87
77: 43 100 | 35 62
69: 43 59 | 35 126
23: 35 63 | 43 43
54: 35 16 | 43 59
6: 35 104 | 43 112
13: 85 43 | 112 35
78: 29 43 | 128 35
125: 23 35 | 126 43
87: 23 43 | 48 35
40: 37 43 | 86 35
57: 112 43 | 59 35
36: 116 43 | 14 35
3: 43 133 | 35 129
32: 43 59 | 35 92
133: 35 59 | 43 92
39: 43 115 | 35 23
86: 43 16 | 35 112
9: 116 35 | 126 43
74: 115 35 | 126 43
18: 35 43 | 43 35
98: 5 35 | 54 43
66: 122 43 | 53 35
101: 35 115 | 43 23
120: 111 43 | 89 35
71: 59 35 | 59 43
119: 23 35 | 18 43
41: 130 43 | 46 35
24: 125 43 | 45 35
0: 8 11
80: 43 30 | 35 51
14: 35 35 | 43 43
72: 25 43 | 107 35
131: 35 52 | 43 22
122: 104 43 | 18 35
12: 21 43 | 75 35
112: 43 35
31: 43 44 | 35 72
45: 43 16
51: 18 43 | 92 35
2: 112 43 | 126 35
115: 35 35 | 43 35
79: 35 120 | 43 124
53: 85 43 | 59 35
123: 43 23 | 35 85
117: 35 80 | 43 10
17: 43 112 | 35 16

baaaabaababaaabbbbabbbabbabaabba
abaaababbaabbbbabbbabbaa
bababbbbaaabbbbaabbaaaaabbaababbabaaaaba
bbbabaabbbabbbbaabbabbbabaabbbbabaabbbbb
baaabaaaaaaaaabbaabaabaa
abbbaabbaaaaabbbbbaaabbabbbbabbb
bbabbaababbbaaabaaababaaaaaaaaba
abaabaababaabaabbbbabbba
bbbabbbaaabbabbababaaabbaaaaaabababaaaaa
abbbbababbbaaaabaababbaaabbbabbaaabbbbab
abaaabbaababaaaabbabbbab
bbbabababbbbbaaabaababbbbaaaababbbababaaaabbbbba
aaabbabaaaaabaabbbbbaaab
abbbbbaaaaabbbabbbbbbbaa
bbbabbaabaaaaababaaabbbabbbaabbbbbababbbaababbabaabaabbbbabbbaaa
baabaaabbababbbaaaaaabbaaabbbaaa
abbaabbbaaaaaabbbaaabbabaabbbabaabbaabab
bbbaaaabbaababaababaaaabbabaabaabaaabaababbaaaabaababaaaaaabbabbbbababab
bbbbbaaaabbbaabbbabbbabaaaaaaabbabaaaabababaabbbaabbbbbbbaabbbbabaaabbba
abbbaaaabbaababbbababaaabbbaabaabaaabbbabababaabaaabaaab
aaabbaaaaaabbaaaabbbaaab
abbbaaaabaaababbabaaaabb
baaabaaabbbaabbbbaaabaabbbabbbbaaaabbabb
baaabbbaabbabbabbbbaaabbaaabbbab
abbbbaaababbbbaabbaabbbb
abaabaabbbabbabbbaaabaabbbbbaabbbababbbbaaaaaabbabaabbabbbababab
ababbababababbbabbabbabb
baaababbbbbbbaabbbabbaabbbabaababaabbbbb
abaaaaabbbabaabbababbaaaaabbaabbabbababb
bbbbaabbbbaaabbbabaabbabababbbaabbabaabaaaaaaabbbabbababbbaabbbbaabaaaaabbbababaabbabbabbaaaabaa
bbbbabaaaaaaababaaabababbabbbaaa
bbbaaaabbabbbbababaabaab
babaabababbbbabaababaaab
abbababaaaaabaababbaabbbaabbaaaa
aaababbaaabaaabbbbbbbbaabaaabbbbabbaabaababbbbabbaabaaba
abaaaaabababaaaabaaaababaabaabbabaaababbbbbbbabbaaabaabbbbbbabab
bababbbaabbabbbaaaaaabaa
abbaaaaaaabbbaababaaabaa
bbababbaaaabbabbbabbbbaababbbaaa
aaabaabababbaababbabbbab
abaabababababbbaaaaaabbbbabbaabaaaaaaaaa
bababbbbaabbbaaaabaaaaabaaaabbab
aaababbabaaaaabaaaaaabbbababbbbaaaababaa
abaaababaaaabbaaaaaababaabbabbabbaaabaaaabbbabbaababbbaa
baabbbaababbaaaaabbaabaa
abaabbbaaababaabaabbbaabbababbbabbabaabababaabba
aabbbabababbaabbbaaaabba
baabbaababbbabbabbbbaaba
babbbaabbabbbbbabaabbbbababaaaaa
baabbabbbbbbaaaaaabaaaba
aaaaababbbabbaabbbbababababbabbabbabbaabaaaabbab
abbbaabaaaabaabaaaaababb
baaabaaabaabbabbaaababbaababbbbaababbbaa
abbabaababbbbbbaaaabababbababbbbabbbabbabbaaabbb
ababbaabbbbaabbbabbbbbabbaaaababbbbaaabb
aababbbbbbbaaabbbababbaaaaaaaababaababaabbabbabababaaaaaababbaab
baaabaabbaabaaabbbabbbaaababbbbb
ababbababbbbbaaabaabbaabaababaaa
bbbbbaaaabbaabbbabaaaaababaabbbaaaabbbbbbbbbaabb
abbbaabababaabaabaabbbaaabbbabba
baaababaaaaabaaababbabbb
bbabbabaaaaaabbbbbbbabbb
bababababbbaaabbabbaabbb
aabbbaababaabbaaabbbbabaabaabaabaababbbb
bbaabbabababaabbaabaaabb
aaabbbababaabbbabbabbbaabaabbbbbaabaababbabbabbabaabbabbbbbaaaab
bbabaabaabbabbababbbaaab
aaaaababbbaabaaaabaabaababaababb
baabaaabaabaaaabbbbabaababaababababababb
bbbaabbbbabbbbabaabbbaaababbabab
babaaabaabbbbbaaaababbaabbaababbbabababb
bbaabbaaaaaabbbbbbbbbbababbbabbb
babbaabaabaabaaaabaabbbabbbaaaabbbabbbaaaaaabbabaababbbabbbbaaababbaaaabbabbabab
abbbaababbaabbabaaabbbbbbabbaababbbaababaaaabbaaaabbbbab
aaaabaabbbbbbaabaababbaabaabaaababbaabbaabababaa
abbaaaaababaababaabbbbbb
babaababaaaaababbaabbaaa
ababaabaaabbabbbbbbaaaabaaababbb
abbababababbabbababbaaaaaabbbbaa
abbbababaaaaababbaababba
bbbaababbbabbbbabbbbabab
ababababaaaabbaabbbaaaba
aababbabbaabbbbbbbabaabaabbbbbabbabbbbaabaababab
aaaabaabababababaabbabbbabbbbbbbabbabaaa
abbabbbaaaabaababaaaabba
bbaaaabaaababbabaaaabbaabaaaabbb
abbbbbbabbaababbbaabaaaa
bbbaababbbabbabaababababbaaaabaabaaaabbaaabaabaa
abaabbaababaababbbabbaabbaaaabba
aaabbbbabaababaaabbababababbbbbbabababbb
abaabbabaaabbbabbbababaabaaaaaaa
aabaabbabbabaaaabaabaaaabaabaaba
babaabaaabbababbbabbaaabaaaababaabaabbaababbbabb
baabbbbabbaabbabaababaaa
aabbaababbbaabbabaabbbbbaababbbabbababaababbabaa
bbabaabaaabbbabababbaabbaaaabaabbababbababbaaaabbaabbaba
bbbaababbbbaaaabbbaabaaabbabbbaaaaabbabaabbababbbaabaabbbabbabbb
bbbaababbaaabaaabaaabbaababbaaaabaabaaba
bbbabaaaaaabbaaababbabababbaaaabbbbbabbabbbabbbaaabaabaa
aabababbbbabbbbbbbbbaabb
bababbbbababbaabaaababaa
aaababbaabbbbbaaababbaabbabbabbb
baaaaababbabaaaaabbbbabaaabababa
babbbbaabaaaababbaaaabba
baababbbbbbabaabbabbbbba
abbbbbaabbaaabbabbaaaaabbbabbaaabbbbbbba
bbabaaaaabaabaaaaaaabababbaaabbb
bbbabaaababaabaaaaaaababaaaabbbbabababbb
bbbaaabbaaabbbbabbbbabba
bbbaabbbaaababbabaaabbbabbbbbabaaabbbbaa
abbaaaaaababababaaabaabaababaaaabaabbbaabbbababaaaaaaaab
aabbabaaabbbbaaaababbbababbbbabb
bbbbbaabaaaaabbabaababaaabbaabbbbaabbaabbbbabbbb
bbaababbababbababbbaaabbababaaaabbabbbbabbaabbba
baaaababababbbabbbaababbaaaababaabbaabbabbaaaaaabbbaaababbaaaaaa
baabbbbaabaabbbabbbabbba
bbbabbabaababbabbbbbaaaa
babaabbbbabaaaababaabbab
abbaababbbbabbbabaabababaaaaabaaaabaaabbbbbababb
aabbbabaabaabaabbabbaaaaabbabbaa
abaaababbbabbababbaaaabbbbaabbbb
bbbaabbbbbabbaabbabaabba
abbaabbabbbaabbbababaabbbbbbbbba
abababbbbbbbaaabbbaaabaaaababbabaaaaaabaabaaabaaaaabaaaa
aababaababaabaaababbbabbbaabbababbaabaaaaabbaaaabababbab
bbbaabbaabbabbbbabbaabaaabbaaaba
bababbbbbbaaaaabbbbbaaaaaababbbb
aabababbabbaaaaabbbaaaabbbbabbabbaaaaaab
aaaaababbbabaaaabaaaabbb
abababbbaaabaaaabbabbabbbbbbbbbbabbbbbaabababbababbbaabaaaabbbabbbabbbbbbbbaaaabbaaaaaab
abbaabbabbabaabbaabbabab
aabaabbaabbbbaaabaababbbbaaaabbb
babaaaabaaaabbaaabbaabbaaaaaababbababbbaabaaaaabaaababaabaabbbbb
abaabbaaaabaabbaabbabbbb
aabbbaaababbbbabaaaaaaab
abbaabbabaabbbbabbbababb
bbbaaaaaabaabaabaababaabaabababbaaaabbabbababaab
baabbbaaababbababbbababaaaabbabaabbabbabbbaabaaabaabbaaa
abbbbbababbaabbbbbaaaaababbababb
abbbbbabbbaabbbaababaaab
ababaabbbabaaabaabaaaaaa
abbbaababaaababbbabbabbaaaaaaabbabbabbaaaabaabaaabbababb
bbaaaaababbbabbbbbbaaaaabbaaaaabbbbaaababbbababbbabbabababaababbaaabbbabbbbaaaabbaabbaba
aabaababbaabbabbababaabbabaabaaa
bbbbaaaaaabbbbbaabbbbbbb
ababaabababbaabbabbaabbabbbbaabaabbaaaab
aababbaaaabbaaabbabbabaa
aaababbbaabaabbaaaabaabababaaaabbabbaababbaaaaaaabaaaababbababbbababbaab
bababbbbbabbbbbbaabbabbbbaabbbab
babbaabbabaaababaabaaabbababbbaababaaaaabbbababb
bbbbbbbbaaaaabbabbaabbaaababbaabbbaaaaabbabbaabaabbabaaa
bbaababbbbbaabbaaabbbaaa
baabbaabaabaabaaaaabbabbaabaaababbbabbbb
bbbaaabbbaabbaabbaaabbbaababbaaaaababaabbaabbabbaabbbabbaaababbbabababaa
abaababaabbaabbbbaabbaba
aaaabaabbbbabaabbbbbbaabaabbaaabaaabbaabbbabbaaaababbbaa
aababbababbbababbabaabbbbabaabbbabaaaaabbaaaabba
baabbabbbabbaabbabababbbbbbbbbba
aabaababbbaaaabbbaabaabababbbababbbbbbabaabbbbbaabaabaab
babbbabbbabaabaabbbabbbbaaabbabbbbaaabbb
abbbbbbaaaabaabaaaaaaaaa
aabaabbabbbaabaabbbbbbbaabababbbabbbabba
aababbabaababbababaaababbbbabaababbababbbbbabbba
babababbbaababbaabaaaaabaababaaabbbbbbaa
bbabaaaabbbbbbababbbbbabbbbabbabaaaabababababaaaaabababa
babbabbababbbbaaaabbabab
abbbbababbaaaabaabbbaabbababbbaa
bbbaabbbbabaabaaaababaaa
abbabaabbbbaabbbabababba
abaabababbabbaabbbbababababababaaabababa
bbbabbbabaaaabbbababbbba
bbabbababbbabbabbababbbaaabbbaaabbabbbaababaaaabaabbaabb
abaaaaabaaabbabaaaababbabaababab
baabbbbbbbbbbbabaaabbbbbaabaaaababbbabbbbabaaaaaabbbbbbabbabbababbabbabaaabbaaabbaaaaaaa
aaabaabaababaabaabbaaaab
abbabbbabaababbbaaabbbbbabbaabaabaabbbab
baababaaaaaaababaaaaabaa
abbbbbbabaabbaababbbabbabaaabbabbbababababbaababbbaaabbbbbaaabaa
bbbbbbbbbbaabaaaaabbabbababbaaabbbaabbabbbbbbabbabbbbbbababaaabbbbbababa
aaabbabbaabbbbbbbbbbabbaabbbbabaaabbbbaabaabbbbbbbaabbbbaaabbbbbabaaaababbbababbabababbb
abbbbbabbabbbbabbbbababb
bbaaababaababaaaaaabbbabbbababba
babababaabbbbaaaababbbba
bbbbabaaaaaabbababbaaaabbbbbabbb
abbbbbbabababaaaabaababb
aaaaaabbbabaaaaaabbaaabb
ababaaaabaabbaababbaabaa
babbaabbbbaabbbabbbbaabb
bababbabbabaaaaaabbbabba
ababbbababbbabababbbabba
baaaaababbabbbaabbaaaaabaaabaaaa
abaabbaabaaababaabbbaaab
babbaabaabbbbbbaabbabaaa
bbaaaabbbbababbbaabbbbabaaaaaabaabbaabbbbbbbbaabbabbbbaaabbbbaaa
aaabbaaabbaaaaabbbabbbbaabaaabaaabbaababbbaabaabababbbaa
abbbbbbaababbaaaaababbbb
bbbaababbbbabababbababbbbbbbbaaaabbaabbaaabaabaa
bbaabbaaabbbbabaaaababbababaaababaaabaabaababbbb
aaaaabbaaaaaabaabbbababb
babababaaababbaabbaabbbbabaaaabb
baabbbaababbbbaababbbaaa
bbbabbaababaabababaaaaaa
abbababaaababbaababbabbababbaaab
abbabaabbbbaababbaaaaabababbaabbbabaabaabbabababaabbbbba
baaabbbaaabaabbaaabbbbaa
bbaabbaaaaaabbababbabaaabababaabaaabaaaabbabbabb
bbaaaaabbbbabaabbaaaaaaa
baaabaabbbbbbbabbbbaababbaabaababaabbbab
aaabaabaaabbabaabbbbbabb
aaaaaabaaabbbbbabaabaaba
abbbababbbabbbbbaaabbaab
aaaabaaaaaabbabaababbaabbbbbbbbbbbabaabaaaaabbaabbbbabbbabaaaaaaabbbbbbbbbababaa
bbbbbbbbaaaaabbbbaaaaaaa
ababaabbbaaababbbababbab
aaaaabbababbaabbabbbbbbb
aabbabaabbbaaabbabaabbbb
bbbaaaababbaabbababbabaa
abbbbbaababababaaaaabbaababbababaabbbbbb
bbbaabaaaabbaababbabaababbabbbab
bbaabbabbbbbabbbaabbabaaaabbbbbabbbbbabaabaababa
bbbaaaabbabbbabbaaabababbbaabaabbaaaabbb
babbbbabbbbaaabbbbabaaaaabbbbbaabbaaabbb
abbabaabbbaaabbaaaabaaaabbbabbbaabbbabaababbbaaabbbabbaa
baaaaaabbabbbbaaabbababaabbbaaababbbaaaabbaaabaa
aaabababaabaabbabbababab
aaaabaabbaaabbbababbbbaabaaabbabbbaabaab
bbaaaabaababababaaabababbaabaaaaabaaabaa
abaaaaabababbaabababaabbbabbaabbaabaaaaaaabbaaaabbaaaabaaaaababa
baaabaabaaaaaabaaabbbabbaaaaabba
baaaaababaabbbaabababbaababbbabbabbbbabaaaaabababbaaaabaaababaab
aaababbaabaabbbaabbbbabaaaabbbbaabaaaaaaaaaaaaaaababbbba
bababaaabaaaababaaaabbab
abaaaaabbbbaaaabbbbbbaababbaaaaabababbababaaaaaabbaaabaa
aabbaabababaabaaaaaaababbbbaabbbbbbbbbba
baababbaaaaabbabaaaabaaabbababbabbabaaababbabbaababbbbaabbabbbaabaaaabbbbbbbbaabbaabaaba
bbbaabbbbababababbbbbabb
aabababbbbbaaabbaaabababaabbbbaa
babbaabababbbabbababbaaaaaabaaaababbabab
baabbbbaabaababaabaaaaba
aaabbbbbabbbbbabbaaabbbababbbabbbbababbbbbbaaababbabbaaaabbaaabb
abaaababbbaabbabbbbabaaabaaabababaaaabbbbabbababbbababab
abaabaaaabbaaaaababbabaaabbabbbabaaabbbbabaaabaababbaaba
bababaabbbbaaaaabbbbaabaabbaababbaababba
aabbbabaabbbbbbaaabababa
aaabbbbaaabaabbaaaaaaaabaaabbbabbabbaaab
baababbbbaaabaaabbbaaaaa
aabbbaabaabaabaaaabbbbbb
bbbbaaabbbabbbabbbaabbbbbbbbbbbabaababab
bbbbbaaaaababbaababaaaabbaabbbabbbbbabab
bbbabaabbbababababbbabbbbaababbabaaabaaabbaabbbabaabababbaababaaabbbbbba
abbbbbbaabbabbbabbabaababbaabbaabbababbbaabbbbaaabbaabab
bbaabbbaabbaabbaaaabbbab
baaabaaabaabbabbaaabbbbbbaabbbaaaabaaabb
aaabaaabbbbabbabaaaabbbabbababaabbabbbabaaabaaab
abbabaabaabbbaabbaaababaababababaaabbaaabaabaabbbabbbbba
abbbaaaababaabababaabbabbabaabbbbaaaabbbbaababaabbbaabbababbabab
baaabbabbabaaababbbbbaaaaabbaaababbbaabbaaaaaaba
babaababaabaabbabaabbabbbbabaaaaaaabababaabbaabb
bbabbaaabbbaabbbbaaaaabbbbbbbbaaabbababbababbabbaaaabbaaaaaaabababbbabaaaababbab
ababaaaabbbabababababbbaabaaabbbaaabbbab
bbaaaaaaababbbaababbbbabaabbbabababbaabbbaaaabbababaabaabaaaaabbaaaaabab
ababbabaaaabababbbbaababbaaabbaaabbaaabaaabbabba
aabbaaabaababbabaabbaaabababbbbbaaaaaaababaabbbb
aabbabaabaaababbaabbbaaaababaaababbabbaa
aaaaababbaabbbbabaaabbbabbbbbbaababbabaa
bababbaaabbaabbaabbabaababaabaaaaababbabbababbbabbababaaaabaabbaaabbbbba
aabaabbaaabbbbbbbaabbbbabbbbbaabbabbaabbaaabbaaaabbbabbabbbbaaaabbaaabaaabaababb
babbaabbaabbababbbaaababbaaaaaabbbbbaaaa
bbbbbbbbaabbbaababbabaabaaabbbab
bbaabbabbbbbaabbaaabbbababbbabbababaaaaa
baabbaabaaabababaaabaaab
bababbbabbabbbaababbaaaabbaaabbbbabbbbaabaaabbbaabbbbbbbbbbababbbbabbbab
baaabbbbbabbbbbbbbabaabaabbbbbbb
ababaaaabbbaaabbaababbabababbaaabbbabbbb
aaabbaaabaaabaababbaaaab
babaaaabbaaabbbbaaaabbaaaaaabaaababbabbb
baaaaabbaaaaaaaaabbaaaabbababbab
aaababbaabbaabbbabbabababbabbbab
bbbbbaaaaaaaabbaabaabbaabbabbababaabbbababbababbbbbbabba
baaaabaaaaabaaaaabbbaaab
abaabaabaaabaaabaaaaaaab
aaaababaaaabbbbbabababbaaaabbbababaaaabbbaabbabaabaaabaaababaaaaabbaaaabaaaaaaaa
babaabababbbababaababaabababbbbbbbbbaaba
aababbababbbababbbbbabaabaabbbab
bababbbabaaababbbbabbbbbaabbbabababbaaababaaaabbbaaaaabb
bbbbbbbbabbabbbaabaabbaa
abbaaaaabaaabababbabaaab
babbaabababbbbaaaaabababaabbaaabbaabbaaaaaaaaaba
ababbaaabbababbbababbaabababaabbbabaaabbababbabb
abbbbbaaabbabaabbaabaaaaabaaabaa
bbaaaabbabaabbaabbbabababababaaabaababbbbababaab
bbbbbaaaabaababaabbbbabababbbaababbabbbb
abaaabbababaabbbaabaabbabbbbbbabbaaaabba
babaaabaaaaaabbbaababaaa
abbbababbaaabababbbbbbbbbabbbabaabbaabaa
abaabbaabababaaabbababba
babaabbbbaaabbabababababbbbbabaabaababab
abababababbaaaaaaaaabaabbabbaaaababbaabbaaabbaabbbbbabaabaaabbaa
aabaaaabababaabbbaababab
aaabbbbaabbbbaaabbaaabab
baabaaabbbabbbbbaabaaabbaabbabaabbbabbbbbaaaaabbabbabaaa
ababaababababbaaabaaabaabaabbbbb
baaabaaaabbbbbbaaabbbbaaaababaaababbababbbaabaabaaaabaaaaabaabba
aaabbbbbabaabbbabaabbbbb
abaabaabbbaaaabbbabbabaa
aaabbabaaaabbbbaabbbbaababbbaaab
bbbaaaababbaabbbbababbbbbaabbaababaaaaaabaaaaaab
abbaabbabaaaaababbababbbbbbbbbab
aaaaabbabbbbaaaabaaaabbaaaabaabbabbbaaab
baaaabbaaaababbabbbaaabbabaaababaabbbaabaabaaaaababbbabbbbaaabaababbbababbabbabaaaabaaabbbaaabaa
aaababbabbaababbababababbbbabbabbaabaaba
baaabbaabaaabbabbbbabbaa
babaabbbbbbabbabaaaaabaa
aababbababbbaabaaaaababb
bbaabbbaaabbaababaabaaababbbbabaabbabbbbababbbba
abbabaabbabbabbaabbabaababbabaaaaaabbbab
baabbbbbbbbaabbaababaaab
baaababaaaabababbabbaaaa
abbbbabaabbaabbaaaaaaaba
abbbababbbabaabbaabbbbbb
bababbbbbbbaabbbbabaaabaaabaaabb
baabbbaababababaabbaaaba
aababaabbababbbaaabaaaabababaaabaabbbbab
abbaaaaabababbbabbbabbba
baaabbbabbbaaabbbbaabaab
abbbaaaaabbbbbabababaaab
bbaabaaaaabbbabaaaaababb
aabbabbbbabbbbbbabbbaabbbbaaaabbbaabababbbbbaaaa
bbaaabaabbbbbbbbababbabb
bbbaabbbbabababaaaaabbbaaabababa
baaabaaaabaaababaabbbabb
bbabaabbbaababbbabbbabbb
abaaaaabbbabaabaabbababaabbaabbabbaabaaabbbbaaaa
bbbaaabbbabbaaaabaabbbab
aaaabbbabaaabbaabbbbbaabababbbabaaaabbbbaababaaa
abaaaaababbbbbabaabbabbbaaaaabbbbaaabaabbaabaabaabbaabab
baaaababbbbaaabbbbaabbababbaaabb
baaabaabaabbabbbbbaaaaabaabaabbb
baabaababbabbababaaabaaabbbbaaabbaabbbab
baaabbabaaabbabaaaaaaaba
aaaabababbaaaabbaababbaaaabaaaababaabbbabaabbaba
bababaaaabbaabbbabbaaabb
aaaaababbbaabaaaabbbabba
aaaabaabbbaabaaababbaabb
abaabbaabbaabbabababbabbaaaaaaaa
aabbaaabbbaabbababaaababaababbaaaababbabaabbbbabbbbbaabb
babababaabaaabbaabbbbababbbaababbaabbbaabaaaabba
baabbbbaababbaaaaabbbbabbababbabbaaabbbabababaaa
abbabbbabaababbbaaabbabbabbbbabb
abbaabbabbbbbaaaaabaaaaa
abaabaaaaabbbaababbaaaba
bbbaaabbbabbaabaaabbabaaaabbbbaa
aaababababaabaababbbbababbababab
babbaabbbbaabbaaababaaaaaabbbbababbbbabb
aabbabbbbbaababbbaaaaaaa
baaababbaaabbaabbbbababbbbbabbba
babbaaaabbabbaabbbbaaaba
bbbaababbabbabbabaaabbbaaababbba
aababbabaabaabbabbaabaaaabbbabaa
abbbbbaaaababaabbababaaaabaaabbb
aaabbbbbaaaabbbabbbaababbbbabaaabbbbabbbbabaaaaaabababbb
abbbaabbaababbaabbaaaaaa
babaababbbbaabaabbbbaaaa
abbabbabbaabbaabbbabbbbbaaabaaab
babbaaaaaabaabbaababbbabbaaaabbb
bababbbabbbbbaaabbaabaaabbaaabbabbabbabb
baababaabaaabbbaaaabaabb
abaabaaabbabbaabbbbbaabb
abaabbbaaaaabaababababbb
aaaaaaababbabbbababbbabbbaaaabbabaaaaaaaabbabaaabbabbbbababbbbbbbbabaabbbbbbbaabababbbaa
babaaabaabbbbababbaabbabbbbaabaaaababbbb
abbaabbbbaabbbbaaababbaabaababba
aaaababaaaaabaaaababaabaaabaaaabaabababbbbbabbba
bbaaabbababaabbbbbabaabbabbbbbbbaaaaaaba
bbaaaababbbaaaabbbaaaababbbbababbbbbabab
aaaababaabbbbababbbaabba
abbaaababbbaabaabaabababbbaabbaabbabababbaaabbbb
baabaabaaabbababbbbabbbabaaabaabbaaabbaabbaaabbabaabbbbb
aaabbabaaabaabbaaaaabaabbbabaaabbbaaaaaa
ababaaabbaaaaaabbabbabbb
baaabbbbabaabbaabbbbaaaa
babaaababbabaaaaabbbbababbbaaabb
bbabbbbbaaaababaaabbbabb
abbaabbbbaaabbaababbaabbbbaabaaaaaabbaaababbabbb
babaaabaaabababbbaaababaaabbbbbb
bbaabbbabbabbbbaabbbaaaabaaaaabb
bbabbbbaabaaabbabbabaabbbbaabbbbbabbaaab
baababaabbaaaabaabaabaaabbbabbaa
baaaabbababbbbbaababaababbbaaaaaabbbabab
abbbbbaababbaabbabbaabaa
aababaabbaaabbbbbaaaabaa
aaabbbbabaaabbaabaabbbbbbbaaaaababbbbabaababbabbbbaabbab
abaaababbbbbabaabaaaabbb
ababbbabbbabbaabaaaabbbabbbbaaabbbbabbbb
ababaaaaaabaaaabaabbabba
bbbababaababbaaabbaaaabaaaabbbbbaaaaaaaaabaababbaabbaaaa
baababaabbaabbbaaabaabbb
baaabbbaababaabaaabaaaabababbaaaabaababb
ababababbbbabbaabbbaaaaaaabaaabbaabbabab
bbabbbbabbaababbbabbbbaaabbababb
aaaaabbbababbababbabaaaabaaaaabb
bbaaabbaabbbbabaaaabbaab
bbabbaaaaabbaaaaaabbbbba
babaaaabbbbbbaaaaabbaaab
aaaabbbaaabaabbababaaabaababbbbb
bbbaaabbbbabbbaababbabab'''
    rule_dict = {}
    do_sol = False
    sol = []
    inp = inp.replace('"',"")
    for x in inp.split("\n"):
        if x == "":
            do_sol = True
        elif do_sol:
            sol.append(x)
        else:
            split = x.split(": ")
            rule_dict[int(split[0])] = [y.split(" ") for y in split[1].split(" | ")]
    return rule_dict,sol

def get_rule(rule_dict,rule_number):
    rule_str = ""
    if rule_dict.get(rule_number) is None:
        return ""
    elif not rule_dict[rule_number][0][0].isnumeric():
        return rule_dict[rule_number][0][0]
    else:
        rule_str += "("
        for rules in rule_dict[rule_number]:
            for rule in rules:
                rule_str += get_rule(rule_dict,int(rule))
            rule_str += "|"
        rule_str = rule_str[:-1]
        rule_str += ")"

    return rule_str

def s1():
    rule_dict,solutions = get_input()
    return len([ x for x in solutions if re.match(f"^{get_rule(rule_dict,0)}$",x)])

def s2():
    rule_dict,solutions = get_input()
    rule_dict[8] = [['42'],['42','8']]
    rule_dict[8] = [[f"({get_rule(rule_dict,42)})+"]]
    rule_dict[11] = [['42','31'],['42','11','31']]
    sum_match = 0
    #cheat to have rule 11 count for the same amount
    for i in range(1,20):
        ins = "{"+str(i)+"}"
        rule_dict[11] = [[f"({get_rule(rule_dict,42)}%s{get_rule(rule_dict,31)}%s)" % (ins,ins)]]
        sum_match += len([ x for x in solutions if re.match(f"^{get_rule(rule_dict,0)}$",x)])

    return sum_match


print(s1())
print(s2())