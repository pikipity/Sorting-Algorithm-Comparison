# Sorting Algorithms' Comparison
Compare three different sorting algorithms introduced by ["Algorithms: Design and Analysis, Part 1"](https://www.coursera.org/course/algo) in ["Cousera"](https://www.coursera.org). The comparison includes

1. Merge Sorting Algorithm introduced in week 1 courses (sorting_algorithm_1)
2. QuickSort Algorithm by using first element as the pivot introduced in week 2 courses (sorting_algorithm_2)
3. QuickSort Algorithm by using last element as the pivot introduced in week 2 courses (sorting_algorithm_3)
4. QuickSort Algorithm by using "median-of-three" pivot rule introduced in week 2 courses (sorting_algorithm_4)
5. "sorted" build-in function of python which uses ["Timsort" algorithm](https://en.wikipedia.org/wiki/Timsort)

Comparison results are shown in "result.txt" as shown below.

```
Algorithm 1 correct
Algorithm 1 costs:
    113.557s/1000 iterations

Algorithm 2 correct
Algorithm 2 costs:
    93.443s/1000 iterations

Algorithm 3 correct
Algorithm 3 costs:
    95.201s/1000 iterations

Algorithm 4 correct
Algorithm 4 costs:
    94.088s/1000 iterations

'sorted' function costs:
    19.413s/1000 iterations
```

It can be seen that the build-in function "sorted" is fastest. Moreover, the Merge Sorting Algorithm is slowest. The three types of QuickSort Algorithms are almost same.
