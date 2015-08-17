# -*- coding: utf-8 -*-
from timeit import timeit
from programming_question_1 import SortCount as sorting_algorithm_1
from programming_question_2_problem_1 import QuickSort as sorting_algorithm_2
from programming_question_2_problem_2 import QuickSort as sorting_algorithm_3
from programming_question_2_problem_3 import QuickSort as sorting_algorithm_4

def readdata(filename):
    f=open(filename)
    data=map(int,f.readlines())
    f.close()
    return data
    
def test_correct(data,test_data):
    if test_data==sorted(data):
        return True
    else:
        return False
        
def printline(line):
    global f
    print line
    f.write(line+'\n')

iteration_num=1000
f=open('result.txt','w')
# Comparison Results
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_1(readdata("QuickSort.txt"))):
    printline("Algorithm 1 correct")
else:
    printline("Algorithm 1 wrong")
printline("Algorithm 1 costs:")
printline("    %.3fs/%d iterations"%(timeit('sorting_algorithm_1(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_1 import SortCount as sorting_algorithm_1;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num))
                        
printline("")
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_2(readdata("QuickSort.txt"))):
    printline("Algorithm 2 correct")
else:
    printline("Algorithm 2 wrong")
printline("Algorithm 2 costs:")
printline("    %.3fs/%d iterations"%(timeit('sorting_algorithm_2(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_2_problem_1 import QuickSort as sorting_algorithm_2;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num))
                        
printline("")
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_3(readdata("QuickSort.txt"))):
    printline("Algorithm 3 correct")
else:
    print "Algorithm 3 wrong"
printline("Algorithm 3 costs:")
printline("    %.3fs/%d iterations"%(timeit('sorting_algorithm_3(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_2_problem_2 import QuickSort as sorting_algorithm_3;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num))

printline("")
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_4(readdata("QuickSort.txt"))):
    printline("Algorithm 4 correct")
else:
    printline("Algorithm 4 wrong")
printline("Algorithm 4 costs:")
printline("    %.3fs/%d iterations"%(timeit('sorting_algorithm_4(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_2_problem_2 import QuickSort as sorting_algorithm_4;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num))

printline("")
printline("'sorted' function costs:")
printline("    %.3fs/%d iterations"%(timeit('sorted(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num))
                        
f.close()