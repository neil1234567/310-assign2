this code is implemented by python

1. open terminal
2. change to the directory where the assign2.py is
3. add the test data file to this work directory
4. enter command: python assign2.py ./data_file_name.txt
   (data_file_name.txt is the name of test data file)

the output will be the color of each country with the increasing order of countries

Algorithm:
basic backtracking search along with MRV, degree and least constraining value heuristic
Input data:
I first read first line of data file, this line contains the number of countries and number of colors.
Then, according to number of countries, i create a matrix (size is number_countires*number_countries) using
lists. Read remaining line. If two countries is connected, the corresponding position is 1, otherwise is 0.
Degree:
I create a list to store degree of each country, each time one country finish its color assignment, i update the
degree list. Every countries which are not assigned color and are connected to current assigned country will
decrease one degree. The degree of current assigned country is set 0.
MRV:
I create a list to store remaining color of each country, each time one country finish its color assignment, i
update the color list. Every countries which are not assigned color and are connected to current assigned
country will decrease one remaining color value. The remaining color value of current assigned country is set
0.
Select next country to assign color:
I use MRV and degree heuristics. First search the largest degree. If only one country has the largest degree,
the country will be assigned color. If many countries with the largest degree, then choose the country with
smallest remaining color value.
Least constraining value when assign color:
When color one country, i always choose color in one order ( increasing order ). If have no conflict, then use
this color, if conflict then color value + 1, then test again till no conflict. This method ensure the color assigned
is always the least constraining value.
Backtracking search:
I use traversed to ensure the assigned country will not be selected again. Each time one country is assigned
color, its traversed value is set. Also each country is assigned, the degree and remaining color value of each
country will be updated. This make i ignore that variable assignments are commutative. I assign just assign
one country at one step. This make i just consider assignments to a single variable at each node.
Output:
I save the color value of each country in one list. After finish all countries’ color assignments, output the list.
The output is the color values with countries’ value in increasing order.
