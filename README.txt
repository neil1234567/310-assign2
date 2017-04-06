Programming language: python

Execution steps:
1. open terminal
2. change to working directory of assign2.py
3. add test-data file to this directory
4. enter command: python assign2.py ./data_file_name.txt 
   - (data_file_name.txt is the name of test data file)

Output: the color values with countries’ value in increasing order.(saved in a list)

Algorithm:
- basic backtracking search along with MRV
- degree and least constraining value heuristic

Input data:
1. read first line of data file which contains the number of countries and number of colors.
2. create a matrix (size is number_countires*number_countries) using lists to remaining lines. 
     - If two countries is connected, the corresponding position is 1, otherwise is 0.

Degree:
1. create a list to store degree of each country. 
2. update the degree list for color assignment of each country. 
     - Countries which are not assigned color and are connected to current assigned country will decrease one degree. 
     - The degree of current assigned country is set to 0.

MRV:
1. create a list to store remaining color of each country
2. update the color list for color assignment of each country. 
     - Countries which are not assigned color and are connected to current assigned country will decrease one remaining color value. 
     - The remaining color value of current assigned country is set to 0.

Select next country to assign color:
1. use MRV and degree heuristics. 
2. search the largest degree. 
     - If only one country has the largest degree, the country will be assigned color. 
     - If many countries with the largest degree, then choose the country with smallest remaining color value.

Least constraining value when assign color:
always choose color in one order ( increasing order ). 
     - If have no conflict, then use this color. 
     - if conflict, then color value + 1, then test again till no conflict. 
     - This method ensure the color assigned is always the least constraining value.
    
Backtracking search:
use traversed to ensure the assigned country will not be selected again. 
     - each time one country is assigned color, its traversed value is set. 
     - the degree and remaining color value of each country will be updated for each color assignment. 
     - ignore that variable assignments are commutative. 
