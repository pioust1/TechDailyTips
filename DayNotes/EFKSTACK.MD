# Monitoring using EFK stack

## ELastic Search ; Fluentd and Kibana


Kubernetes expects all the applications to log the outputs as a stdout stream; use a simple logs command to fetch the log but k8s does not keep the log history and we would need a more scalablility as the entire application might have 100s of pods.

## Logging Stack 

* Log Aggregator  
		Responsible for collecting logs from various sources and then ( different pods running on different nodes) and route them to a central location 
	Fluentd is the popular log aggregator. small efficient and has lot of plugins
	
* Log Collector  
		Stores the log from the log aggregator and provides an interface to search for the logs efficently.( Elastic search is the component used here)
		easy to collect logs from fluentd;use inverted indexes on the structured log data and use multi master architecture for HA
* UI and Alerting  
		Visualization of the data collected and help us debug the issues better and we will explore how Kibana helps in the UI. Along with it we can set alarms to alert high priority issues 
	
