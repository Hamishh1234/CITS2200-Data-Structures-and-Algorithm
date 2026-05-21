# CITS2200 Exercise 3: Heaps and Heapsort

Before you start: Refresh your understanding of heap by using a visualization website https://www.algoanimator.com/. The website has two tabs you should explore:

Algorithms – for visualizing how arrays, lists, and other structures work.

Tutorials – for guided explanations and examples.
*************************************************************************************************************


Implement all the function stubs in `heaps.py`.

Complexity targets for methods are included in their doc comments.

Sample tests are provided in `test_heaps.py` and can be invoked with `python -m unittest` in this directory.
You are encouraged to write your own additional tests, and to compare your implementations with other students and attempt to break each other's implementations.


**Use ChatGPT to help you fill in the function**

Copy the function’s docstring (the comment inside """ quotes).

Paste it into ChatGPT and ask questions like:

“How can I implement this in Python?”

Take the explanation and write your own Python


Remember the objective is for you to understand the logic behind these algorithms.
It is not sufficient to simply end up with working code, or be able to explain the algorithms step by step.
Your understanding should be sufficient that you can apply these logical ideas to novel problems in the future.

You should be able to write a logical argument for the correctness and time complexity of each algorithm.
Practise doing so, and see if other students and lab facilitators find your arguments convincing.
You argument should be sufficient to convince a fellow student who has never seen this algorithm before of its correctness.

Consider the following questions.
You are encouraged to discuss them with other students:
1. How would you use your heap to implement the operations of a priority queue with explicit priorities for each element?
2. How could you implement the `decrease_key` method, which allows replacing the key of a priority queue element with a better key?
3. How might you implement a heap such that given two heaps you can merge them efficiently?