if they were only a small amount of URLs, we would use a hash table, and add urls 1 by one, detect duplicates that way O(n)
because we have 10B, the hash table will be too big

--------------
we can do a first pass on the document, create files of 1Gb based on the hash of the URL.
Then detect collisions inside each file

or we could do the same but split on different machines


