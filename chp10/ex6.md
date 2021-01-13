quick sort:
choose the first element as pivot, copy file into two files, etc recursively, once there is a sufficient small number of lines in a file, we can sort it in memory


answer:
it might actually be better to split the file into chunks, sort all of them, once we have a lot of sort chunks, merge them. This is external sort

that way, we have a perfect split. where with quick sort, worst case is O(n*2)
