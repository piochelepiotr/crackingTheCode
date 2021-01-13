web crawler

use a hash table of visited urls. If we already visited one, don't visit it again.
but a URL can sometimes have a date in it, and it's going to always change.
To avoid getting stuck in that, we can compute a degree of similitude with the page that has been crawled last time
if it's to high, crawl it maybe later

