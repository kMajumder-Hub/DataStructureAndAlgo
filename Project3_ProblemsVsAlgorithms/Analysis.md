# Project Explanation
Explanation of the different project submodules

## Problem 1
The principle of this algorithm is to implement a _variance of the binary search_, due to the required __time 
complexity__. This time, though, instead of counting with an already sorted array, we use the _natural consecution_ to
use as our __imaginary array__; the implementation relies on dividing the search space in two parts and checking at 
each time if the __mid point power of 2__ is bigger or smaller than the given number (as in a dictionary, is the found 
word, bigger or smaller than our goal). Additionally, there is the inclusion of a little _optimization trick_, this is
the fact that the __square root__ of a natural number (starting from 2) is _half or less_, thus giving us a __speed 
boost_ by starting with `end = number // 2`.

### Time and Space complexity:
In this case time complexity is __O(log(n))__, as we transverse the _hypothetically ordered natural's number list_ by 
using a __binary search approach__. As for the space complexity, it is __independent of the input__, requiring solely 
pointers to different array locations; __O(1)__.

## Problem 2
The principle employed in this algorithms is based directly in the _binary search_ algorithms, differently, to this 
implementations, in its structure, it has been decided to be employed a __more divide approach__, rather than
computationally expensive on previous levels to _spare_ some division; e.g. when the lists are of size 2, both values
could have been checked (though this would have increased our __time complexity__). 

### Time and Space complexity
The time complexity being an algorithm based on binary search is __O(log(n))__.  The number of iterations we perform,
i.e. recursive depth, follows the rule of _recursive_depth^2 = n_. Thus if we isolate the number of iterations in
relation to the __input space__ (n), we obtain __log(n) = recursive_depth__. As for the space complexity, it is 
__independent of the input__, requiring solely pointers to different array locations; __O(1)__.

## Problem 3
This problem, as stated to be solved in _time complexity_ of __O(n*log(n))__, has given the clue to be tackled by a 
variation of the __merge sort__ algorithm. Indeed, it is a _merge sort_ algorithm, except for the particular treatment 
if gives to the comparison of results coming from the previous recursion, if we are on the _first level_ of the
recursion. In this case, it does the _comparison_, as usual, but then starts saving the results on 
__alternative lists__, which are then returned as the results. 

The usage of this _alternative list saving_ is due to the fact that having the list perfectly sorted, if we start from
the index[0] and give alternatively a value to each list, occupying this value an increasing digit position, we 
__always__ obtain a combination that satisfies the condition of having a __maximum sum of two numbers__ and __maximum a
digit of difference between them__.  

### Time and Space complexity 
As the base of the algorithm is the __merge sort__, having a time complexity of __O(n*log(n))__, and there have been no
substantial modifications to the algorithm; just the addition of __O(1)__ operations, the time complexity remains 
_equal_. As for the space complexity, if we hold the assumption that python gets automatically rid of each previous 
step auxiliary created arrays, then the space complexity is of __O(n)__ (we have always arrays tat amount to the 
length of the input array).

## Problem 4
This problem is tackler as the construction of a output list, issue form a single transverse of the elements. By using,
several pointers, it is possible on a __single transverse__ to properly order the provided array.

### Time and Space complexity
In this case the _time complexity_ is precisely, __O(n)__. Analyzing the _space complexity_, due to the non usage of 
__auxiliary tables__ (only a few pointers), it is of order __O(1)__ (excluding the input space).

## Problem 5
This problem is focused on the development of the of a __trie__ a data structure derived from a _tree_, suited for a
 good ratio between _time and space_ complexity.

### Time and Space complexity
 Trie.insert() : The time complexity ofthis is O(n) and the space complexity is O(a\*n) where a is the length of the word and n is the total number of words
 
 Trie.find() : The time complexity ofthis is O(n) and the space complexity is O(a\*n) where a is the length of the word and n is the total number of words
 
 TrieNode.suffixes() : Each node is only inspected once, but extending the list as opposed to appending to it is relatively expensive. Therefore, its time complexity ends up O(k). The space complexity for the data structure is O(n\*m), where n is the number of words stored in the trie, and m the longest word length (worst case).
 
 TrieNode.insert() : Since checking a dictionary is considered a fixed time operation, the time complexitty is O(1). Same is the case with space complexity.

## Problem 6
This problem focuses on __finding max and min values__ from an unsorted array, we are not required to nothing extra 
and here _lies the key_, not being required to sort anything, we can solve the problem with a single transversal and
 two placeholders, as reference for _min_ and _max_ values.

### Time and Space complexity
In this case, we perform a __single transverse__ of the whole input, being the time complexity of __O(n)__. In respect 
to the _space complexity_, we have just a pair of pointers, hence, it is independent from _input size_; __O(1)__.

## Problem 7 
It is similar to __problem 5__, except for the _edge cases_, like "root handler", and working with a __hierarchy of 
web pages__ instead of strings. This problem is focused on the development of the of a __trie__ a data structure 
derived from a _tree_, suited for a good ratio between _time and space_ complexity.

### Time and Space complexity
 RouteTrie.insert() : The time complexity ofthis is O(n) and the space complexity is O(a\*n) where a is the length of the word and n is the total number of words
 
 RouteTrie.find() : The time complexity ofthis is O(n) and the space complexity is O(a\*n) where a is the length of the word and n is the total number of words.
 
 RouteTrieNode.insert() : Since checking a dictionary is considered a fixed time operation, the time complexitty is O(1). Same is the case with space complexity.
 
 Router.lookup() : The most interesting algorithm is lookup. Path stripping is O(n), and the find algorithm is something like O(nm), where n is the longest path and k the average number of branches: It has to iterate through the trie nodes (worst case the longest path), and at each level find the next path element out of all branches. So the overall time complexity is O(n + n * k) = O(nk). The space complexity is O(n\*m), where n is the number of paths stored in the trie, and m the longest path length (worst case).
 
 Router.add_handler() : The method calls split_path() and insert(). It does not contribute any extra complexities.
 
 Router.split_path() : The time complexity depends on the length of the raw path (technicall, the number of '/' within the raw path). Thus, it can be assumed to be O(k), where k is the length of raw path. The space complexity is also O(k) since the length of the splitted list depends in the input.
 