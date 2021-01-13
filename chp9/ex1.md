1000 client applications
end of day stock price

from the numbers, I think it can be done by a single machine

Q: how many stocks? 100 000?
Q: how many queries per client? 1000 is a pretty small number
Q: queries always for the same timerange?
R: I'm designing the database, so I will shard it by stock id

Load balancer -> can shard based on stock id -> server with cache -> server with data sharded by stock id

some retries are done by the load balancer, so that if a server crashes, we still reply correctly to the client
if a client server crashes, it is restarted. It is stateless, the request can be made to a different server
If a data server crashes, it is restarted, data is copied from the replica.

To monitor, I use a Application performance product and I trace the calls

If we can use technologies: Postgres for recent data if we are concerned about latency, S3 for all old data


OK, that was overengineered a lot
so indeed, scale was really small
