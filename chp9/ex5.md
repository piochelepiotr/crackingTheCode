is it ok not to get the most recent data?

given that the queries are split randomly, implementing a shared cache would make sense
the key is the query, we cache the result
we evict data if it's too old.
We also use an LRU (least recently used) but if data is too old, it's evicted anyway.
but if we need to evict some data, let's evict data that isn't used

asumption: some queries are ran a lot, while a lot of queries are ran only once

--------------------------

design how the cache would work on a single machine

linked list (expire old data) + hash map (lookups)

Then, instead of using a separate shared cache, we could have machines that forward requests to one another based on a hash of the query % number of machines
we would need to implement some sort of TTL
