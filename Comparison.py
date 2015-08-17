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

iteration_num=1000
# Comparison Results
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_1(readdata("QuickSort.txt"))):
    print "Algorithm 1 correct"
else:
    print "Algorithm 1 wrong"
print "Algorithm 1 costs:"
print "    time: %.3fs/%d iterations"%(timeit('sorting_algorithm_1(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_1 import SortCount as sorting_algorithm_1;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num)
                        
print ""
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_2(readdata("QuickSort.txt"))):
    print "Algorithm 2 correct"
else:
    print "Algorithm 2 wrong"
print "Algorithm 2 costs:"
print "    time: %.3fs/%d iterations"%(timeit('sorting_algorithm_2(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_2_problem_1 import QuickSort as sorting_algorithm_2;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num)
                        
print ""
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_3(readdata("QuickSort.txt"))):
    print "Algorithm 3 correct"
else:
    print "Algorithm 3 wrong"
print "Algorithm 3 costs:"
print "    time: %.3fs/%d iterations"%(timeit('sorting_algorithm_3(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_2_problem_2 import QuickSort as sorting_algorithm_3;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num)

print ""
if test_correct(readdata("QuickSort.txt"),sorting_algorithm_4(readdata("QuickSort.txt"))):
    print "Algorithm 4 correct"
else:
    print "Algorithm 4 wrong"
print "Algorithm 4 costs:"
print "    time: %.3fs/%d iterations"%(timeit('sorting_algorithm_4(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;from programming_question_2_problem_2 import QuickSort as sorting_algorithm_4;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num)

print ""
print "'sorted' function costs:"
print "    time: %.3fs/%d iterations"%(timeit('sorted(deepcopy(data))',\
                        setup='''from copy import deepcopy;from __main__ import readdata;data=readdata("QuickSort.txt")''',\
                        number=iteration_num),iteration_num)