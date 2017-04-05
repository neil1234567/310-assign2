
# input name of data file
import sys

# use MRV and degree heuristice to determine next country to be assigned colour
def ponit_select(degree,traversed):
    j = -1
    i = 0
    selected_point = len(degree)
    while i < len(degree):
        if degree[i] >j and not i in traversed:
            selected_point = i
            j = degree[i]
        elif degree[i] == j and not i in traversed and remain_color[i] < remain_color[j]:
            selected_point = i
            j = degree[i]
        i += 1
    return selected_point

# after color assignment of one country, update the degree of every country
def update_dagree(degree, selected_point,traversed):
    degree[selected_point] = 0
    for i in range(0, len(nodes_map)):
        if nodes_map[selected_point][i] == 1 and not i in traversed:
            degree[i] -= 1

# after color assignment of one country, update the remaining values of each country
def update_remain_color(remain_color, selected_point,traversed):
    remain_color[selected_point] = 0
    for i in range(0, len(nodes_map)):
        if nodes_map[selected_point][i] == 1 and not i in traversed:
            remain_color[i] -= 1

# backtracking search
def ColorLabel(n_color, nodes_map, degree):
    traversed = set()
    Num=len(nodes_map)
    Color=[-1 for i in range(Num)]
    l=i=n=1

    while i<=Num:
        m = ponit_select(degree,traversed)
        while n<=n_color and l <=Num:
            flag=True
            for k in range(l):
                if nodes_map[m][k] == 1 and Color[k] == n:
                    flag=False
                    n += 1
                    break
            if flag:
                Color[m]=n
                traversed.add(m)
                update_dagree(degree,m,traversed)
                update_remain_color(remain_color,m,traversed)
                m = ponit_select(degree,traversed)
                i += 1
                l +=1
                n=1
        if n > n_color:
            m -= 1
            n=Color[m-1]+1
    return Color

# read file, input data as a matrix
file_name = sys.argv[1]
file_data = open(file_name, 'r')
data = file_data.readline()
data2 = data[1: ].split()
num_vertices = int(data2[0])
num_color = int(data2[1])

nodes_map = [[] for x in range(num_vertices)]
for i in range(0, num_vertices):
    data = file_data.readline().strip()
    data2 = data[1:-1].split(" ")
    for j in range(0, num_vertices):
        x = 0
        for k in range(0, len(data2)):
            if j + 1 == int(data2[k]) and i!= j:
                nodes_map[i].append(1)
                x = 1
        if x == 0:
            nodes_map[i].append(0)

file_data.close()

# initialize the degree of each country
degree = [0 for i in range(len(nodes_map))]
for i in range(0,len(nodes_map)):
    for j in range(len(nodes_map[i])):
        if nodes_map[i][j] == 1:
            degree[i] += 1

# initialize the remaining values of each country
remain_color = [0 for i in range(len(nodes_map))]
for i in range(0,len(nodes_map)):
    remain_color[i]= num_color

# output the one solution of coloring assignment
print"the outcome show color of each country with the country in increasing order"
for i in ColorLabel(num_color,nodes_map,degree):
    print i
