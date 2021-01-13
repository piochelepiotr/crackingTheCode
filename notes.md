# Chapter 4

- Binary tree
- Binary search tree
- Balanced tree
- Complete tree (perfect except last line)
- Full Binary tree (0 or 2 children)
- Perfect Binary tree

## Binary heaps

keep a complete tree
to insert, add at the end, swap with parent if smaller until the root
to delete, swap with smallest children until the end
=> O(n ln(n)) for all operations

## Tries (prefix trees)

used for autocompletion for instance

## Graphs

check Depth-first search and Breadth-first search
bidirectionnal search can be used to go quicker for shortest path

## Bits

n & (n -1) clears the least significant bit
so n & (n -1) == 0 tests if n is a power of 2

## Object oriented designs

Ask a lot of questions about:
six Ws: who, what, where, when, how, why

## Recursion and dynamic programming

if a problem looks like a recursive problem, keep in mind that 50% of the time, it's not
bottom up (works for 1, let's try 1)
top-down: divide a problem in sub problems (often f(n-1), but also divide by 2


## Chapter 9: System designs and scalability

- listen carefully to the interviewer, he will guide you
- communicate a lot
- drive the answerm propose solutions
- design step by step

### Design step by step

1. Scope the problem
make a list of features
2. make reasonable assumptions
- 1M clicks per day? How much memory do we have? Are we concerned about lag?
3. draw major components
you can ignore scalability issues first
go to the white board
4. identify key issues
- Maybe bottlnecks?
- maybe some weird data sometimes?
5. redesign based on the issues
- maybe major re-design
- maybe just adding a cache

### Algorithm step by step

1. Ask questions to understand the problem better
2. Pretend it all fits on 1 machine first
3. Get real, sharding

### Key concepts

1. Horizontal vs Vertical scaling
2. Load balancer
3. Database denormalization and NoSQL: remove joins because they are slow, duplicate data
a No SQL database doesn't support joins, it is designed for scale
4. Sharding
- vertical partitioning: by feature (1 server stores people, the other one tasks for eg)
- key-based (hash based)
- directory based: maintain a lookup table: data key -> on which server is it?
5. Caching
- in memory, shared key value cache. You can cache directly query and result, or cache indirect results
6. Async processing and queues

#### Networking 
- bandwidth: max data / s 
- throughput: avg data /s 
- latency: 

#### Map reduce

you write two functions
1. Map data -> <key, value>
2. Reduce: key, set(values) -> key, value

### Don't forget about
failures
availability (% of up time) and reliability (proba that it's up during x time)
read-heavy vs write-heavy
security
