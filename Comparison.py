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
    
def test_1():
    data=readdata("QuickSort.txt")
    sorted_array,count=sorting_algorithm_1(data)
    return count
    
def test_2():
    data=readdata("QuickSort.txt")
    count=0
    sorted_array,count=sorting_algorithm_2(data,count)
    return count
    
def test_3():
    data=readdata("QuickSort.txt")
    count=0
    sorted_array,count=sorting_algorithm_3(data,count)
    return count
    
def test_4():
    data=readdata("QuickSort.txt")
    count=0
    sorted_array,count=sorting_algorithm_4(data,count)
    return count

iteration_num=1000
print "Algorithm 1 costs:"
print "    comparison: %d/iteration"%(test_1())
print "    time: %.3fs/%d iterations"%(timeit('test_1()',\
                        setup='from __main__ import test_1',\
                        number=iteration_num),iteration_num)
print ""
print "Algorithm 2 costs:"
print "    comparison: %d/iteration"%(test_2())
print "    time: %.3fs/%d iterations"%(timeit('test_2()',\
                        setup='from __main__ import test_2',\
                        number=iteration_num),iteration_num)
print ""
print "Algorithm 3 costs:"
print "    comparison: %d/iteration"%(test_3())
print "    time: %.3fs/%d iterations"%(timeit('test_3()',\
                        setup='from __main__ import test_3',\
                        number=iteration_num),iteration_num)
print ""
print "Algorithm 4 costs:"
print "    comparison: %d/iteration"%(test_4())
print "    time: %.3fs/%d iterations"%(timeit('test_4()',\
                        setup='from __main__ import test_4',\
                        number=iteration_num),iteration_num)