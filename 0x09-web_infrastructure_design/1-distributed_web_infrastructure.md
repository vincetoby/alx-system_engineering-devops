# Distributed Web Infrastructure

![Image of a distributed web infrastructure](1-distributed_web_infrastructure.PNG)


## Description

This is a distributed three server web infrastructure that hosts the website www.foobar.com and atttempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica).

## Specifics About This Infrastructure

+ The distribution algorithm the load balancer is configured with and how it works.<br/>The HAProxy load balancer is configured with the *Round Robin* distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, *Round Robin* allows server weights to be adjusted on the go.
+ The setup enabled by the load-balancer.<br/>The HAProxy load-balancer is enabling an *Active-Passive* setup rather than an *Active-Active* setup. In an *Active-Active* setup, the load balancer distributes workloads across all nodes in order to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an *Active-Passive* setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.
+ How a database *Primary-Replica* (*Master-Slave*) cluster works.<br/>A *Primary-Replica* setup configures one server to act as the *Primary* server and the other server to act as a *Replica* of the *Primary* server. However, the *Primary* server is capable of performing read/write requests whilst the *Replica* server is only capable of performing read requests. Data is synchronized between the *Primary* and *Replica* servers whenever the *Primary* server executes a write operation.
+ The difference between the *Primary* node and the *Replica* node in regard to the application.<br/>The *Primary* node is responsible for all the write operations the site needs whilst the *Replica* node is capable of processing read operations, which decreases the read traffic to the *Primary* node.

## Issues With This Infrastructure
1. Single Point of Failure (SPOF):
    + The load balancer can be a potential single point of failure. If it goes down, traffic distribution stops. Consider implementing a redundant load balancer for high availability.

2. Security Issues:
    + No firewall is mentioned in the design. It's crucial to implement firewalls to control incoming and outgoing traffic, adding an extra layer of security.
    + HTTPS is not mentioned. It's important to secure communication between users and the server. Implementing HTTPS using TLS certificates is recommended.

3. No Monitoring:
    + The infrastructure lacks a monitoring system. Implementing monitoring tools is essential for identifying and addressing issues proactively, ensuring optimal performance and availability.

