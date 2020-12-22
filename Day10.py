
def get_input():
    inp ='''56
139
42
28
3
87
142
57
147
6
117
95
2
112
107
54
146
104
40
26
136
127
111
47
8
24
13
92
18
130
141
37
81
148
31
62
50
80
91
33
77
1
96
100
9
120
27
97
60
102
25
83
55
118
19
113
49
133
14
119
88
124
110
145
65
21
7
74
72
61
103
20
41
53
32
44
10
34
121
114
67
69
66
82
101
68
84
48
73
17
43
140'''
    return inp.split("\n")



inp = [int(x) for x in get_input()]
inp.append(int(max(inp) + 3))
inp = sorted(inp)

outlet = 0
joints = {1:0,2:0,3:0}
for x in inp:
    joints[x - outlet] += 1
    outlet = x
print(joints[1]*joints[3])


pos = {0:1}
for x in inp:
    pos[x] = 0
    if x - 1 in pos:
        pos[x]+=pos[x-1]
    if x - 2 in pos:
        pos[x]+=pos[x-2]
    if x - 3 in pos:
        pos[x]+=pos[x-3]        
print(pos[max(inp)])