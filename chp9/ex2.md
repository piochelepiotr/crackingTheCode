Table of people
id Name description age etc

Table of relationships
id1 id2


because it's very large, we can't store this tables on a single node
How do we shard data?
we can shard by person id, or by a hash of the name. Maybe hash of the name is better because when we search for someone, we know it's name, not it's id

for the other table, we should store id1 -> id2 and id2 -> id1. then we can shard by id and get all the friends of someone

To get the shortest path from 1 person to the other, we start at the 2 ends at the same time, and we do a breadth first traversal, but it's going to quickly be huge

------------
just use an easy class first
go through IDs only if you need to scale
talk about reducing machine jumps. First batch jumps, but also cluster people that are more likely to be friends on the same machines
instead of marking nodes as visited, use a separate hashtable to mark that

