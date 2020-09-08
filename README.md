# SF Crime Statistics with Spark Streaming


1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

        - maxRatePerPartition  - maximum rate (in messages per second) at which each Kafka partition will be read 
        - trigger - For processingTime

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
        
        - spark.executor.memory sets the memory for the executor.
        - spark.driver.memory sets the memory for the driver.




