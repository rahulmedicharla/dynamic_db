## Evolate: the first ever multistructered dynamic data structure

The idea behind evolate is that data is always changing. When the average person uses a data structure in their program, they usually aren't
considering the implications that structure could have on your CPU, Memory, or Efficiency. Certain features of the data your storing, your use case, and the search algorithms you chose to use may cause your structure be inefficent. 
<br>
Evolate solves the problem using ML. Evolate keeps track of the features of the data you're storing and based on custom trained model, it will automatically switch between different data implementations, which use different search algorithms to maximize efficiency while minimizing stress on your PC. 

<h3>Data Structures Evolate uses and switches between:</h3>
<ul>
    <li>Singly Linked List</li>
    <ul>
        <li>Uses Iterative Search <i>Runtime: Θ(n)</i></li>
        <li>Uses Iterative Insertion & Deletion <i>Runtime: Θ(n)</i></li>
    </ul>
    <li>Sequence</li>
    <ul>
        <li>Uses Iterative Binary Search <i>Runtime: Θ(log(n))</i></li>
        <li>Uses Iterative Insertion & Deletion <i>Runtime: Θ(n)</i></li>
    </ul>
    <li>Tree Map</li>
    <ul>
        <li>Uses Recursive Binary Search <i>Runtime: Θ(log(n))</i></li>
        <li>Uses Iterative Insertion & Deletion <i>Runtime: Θ(log(n))</i></li>
    </ul>
    <li>Hash Map</li>
    <ul>
        <li>Uses Hashed Search <i>Runtime: Θ(1)</i></li>
        <li>Uses Hashed Insertion & Deletion <i>Runtime: Θ(1)</i></li>
    </ul>
</ul>
  
<br>
The runtimes provided are in the general case of the data set. However, certain data structures operate better based on specifications for the data.
<ul>
    <li>Singly Linked List</li>
    <ul>
        <li><i>Advantanges:</i> Efficient search at head of list & constant insertion/deletion</li>
        <li><i>Disadvantages:</i> Slow search at end of list</li>
    </ul>
    <li>Sequence</li>
    <ul>
       <li><i>Advantanges:</i> Efficient random search  & constant insertion/deletion</li>
       <li><i>Disadvantages:</i> Inefficient for search patterns</li>
    </ul>
    <li>Tree Map</li>
    <ul>
       <li><i>Advantanges:</i> Fast random search for smaller data sets (Memory Extensive)</li>
       <li><i>Disadvantages:</i> Slow insertion/deletion (need to maintain balanced tree)</li>
    </ul>
    <li>Hash Map</li>
    <ul>
         <li><i>Advantanges:</i> Fast insertion/deletion & search</li>
         <li><i>Disadvantages:</i> Not good for very large data sets</li>
    </ul>
</ul>

<h3>Machine Learning</h3>

From this, I realized that both iterative (Sequence) and recursive (Tree Map) binary search algorithms are good for when the search was random, but inefficient when there was a pattern in the search indexes. On the other hand Singly Linked Lists and Hash Maps are good for patterened search an inneficient for random searches. On top of this Tree Maps are inefficient when there is a lot of insertion and deletion since we have to maintain the balanced tree, and Hash Maps are inefficient for very large data sets. 

<b>Based on the specifications for the data, these were the features I chose to keep track of in real time</b>
<ul>
    <li>Total length of data set</li>
    <li>Insertion/Deletion frequency</li>
    <li>Search Randomness (normalized standard deviation of search pattern)</li>
</ul> 

Here is a visualization of a small piece of the data the ML model is trained on. A negative search randomness indicates patterned search while a positive one indicates random.
<div style="display: inline-flex; flex-direction: row;">
    <img src="https://github.com/rahulmedicharla/dynamic_db/assets/46610295/5bd4cf3b-43ac-44e5-8672-3df883cbbab6" width=500></img>
    <img src="https://github.com/rahulmedicharla/dynamic_db/assets/46610295/ea8b2263-08a1-4d26-a27e-d23ea114953f" width=500></img>    
</div>

