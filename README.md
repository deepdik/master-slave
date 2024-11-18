# Master-Slave MySQL Experiment with ProxySQL

This experiment involves setting up MySQL in a master-slave replication architecture and testing the functionality using Python scripts. Two setups are provided:
1. **Simple One Master One Slave Configuration**
2. **One Master Two Slaves with ProxySQL Load Balancer**

---

## 1. Simple One Master One Slave Configuration

### Steps to Run:

1. **Start the Docker Containers**:
   - Navigate to the directory containing the `docker-compose.yml` file.
   - Run `docker-compose up -d` to start the MySQL master and slave containers.

2. **Verify the MySQL Setup**:
   - Connect to both the master and slave containers using a MySQL client or `docker exec`.
   - Check that replication is set up correctly.

3. **Run the Python Script**:
   - Ensure you have `mysql-connector-python` installed: `pip install mysql-connector-python`.
   - Execute `replication.py` using `python replication.py`.
   - Observe the output to confirm data writes to the master and reads from the slave.

4. **Shutdown**:
   - To stop the containers, use `docker-compose down`.

---

## 2. One Master Two Slaves with ProxySQL Load Balancer

### Steps to Run:

1. **Start the Docker Containers**:
   - Navigate to the directory containing the `docker-compose.yml` file for the multi-slave setup.
   - Run `docker-compose up -d` to start the MySQL master, two slaves, and ProxySQL containers.

2. **Configure ProxySQL**:
   - Connect to the ProxySQL admin interface:
     ```bash
     docker exec -it proxysql mysql -u admin -padmin -h 127.0.0.1 -P 6032
     ```
   - Run the commands from `setup_proxysql.txt` to add the master and slave servers to ProxySQL and configure query rules.

3. **Verify the ProxySQL Setup**:
   - Check that the configuration changes have been applied using the ProxySQL admin interface.
   - Ensure that SELECT queries are routed to the slaves and all other queries are routed to the master.

4. **Run the Python Script**:
   - Make sure `mysql-connector-python` is installed: `pip install mysql-connector-python`.
   - Execute `replication.py` using `python replication.py`.
   - Observe that ProxySQL manages the read and write operations appropriately.

5. **Monitor and Test**:
   - Use logs or MySQL clients to monitor query routing and replication status.
   - Check the health of all nodes and ensure ProxySQL is functioning as expected.

6. **Shutdown**:
   - Use `docker-compose down` to stop all containers.

---

## Notes:
- Ensure that you have Docker and Docker Compose installed and running on your machine.
- For real-world scenarios, consider setting up monitoring and failover mechanisms.
- ProxySQL requires proper configuration to handle load balancing and fault tolerance effectively.

---

