first, if it's a small eCommerce,

each article has it's number of sales

we can sort all products, then every time a category is full, ignore next items from that category
we can filter only articles that are from the correct category and order them

imagine it has 1M items, sorting a 1M element array sounds reasonable. So no need to do anything more complex
amazon has 100M items. If we store itemID and category and number of sales for each product, that means 300Mb array
that is huge, but 1 machine should be enough
sorting that array will take some time

first pass, put elements in blocks by category

each category, keep a min heap of n elements for each category and do a traversal

-----------

discuss what are the best saling products? best of this month, this day? exponential decay

use a circular array to store the sales from last week

build the whole pipeline to ingest data and store stats
