 # COMP9331_22T1
labs content


## Assignment Help session schedule
![image](https://user-images.githubusercontent.com/27357380/162346774-f2f01251-dfcc-4bbc-a9d4-efc36c25f986.png)

### Week 7 : How to get started
	- What should we do?
	- How to design the program?
	- How to start with the example code?
	- UDP vs TCP
	- Useful library
 
 Slides: (to be uploaded)  
 Recording: (to be uploaded)  

### Week 8: How to implement the Config. 2 ?
	- Program structure
	- Multi clients
	- TCP file transmission
  Slides: (to be uploaded)  
  Recording: (to be uploaded)  

### Week 9~10:  Debug/Testing/Submission
 - Demo code for some hard function
 - Testing  
 Slides: (to be uploaded)  
 Recording: (to be uploaded)  

![image](https://user-images.githubusercontent.com/27357380/160765808-fc2b6313-6d64-4497-9e96-05f42e7d2c63.png)












## Lab1：  
 - Lab 1 submission deadline: 10:00 Tue 1 March  
 - Slides: https://github.com/lrlrlrlr/COMP3331_9331_21T3/blob/main/COMP3331_w2%E2%80%94%E2%80%94demo.pdf 
-----------------------------


## Lab2
 - Lab 2 submission deadline: 10:00 Tue 8 March 

- **Q3 & Q4**
   - HTTP fundermentals: what is status code?
   - How to use wireshark

 - **Q5**
   - how to run the server
   - how to create a client (socket programming 101)
   - Example code (please checkout the recording video below 👇)

 - Recording clip(Short video): 
   - q3 https://youtu.be/eBnyq6_IQqE  
   - q4 https://youtu.be/Yg5IwiD2Ync   
   - q5 https://youtu.be/9ARKigLwJfM  


## Lab3

 - **Exercise3**
   - Q1: simply run the `dig www.eecs.berkeley.edu`
   - Q2: check the CNAME result in Q1 or run `dig www.eecs.berkeley.edu CNAME`
   - Q3: explain what we have in the response
   - Q4: in the bottom of the response
   - Q5: check the AUTHORITY SECTION/ADDITIONAL SECTION
   - Q6: reverse query `dig -x 129.94.242.33`
   - Q7: MX query `dig @129.94.242.33 yahoo.com MX`
   - Q8: ...
   - Q9: MX query `dig @ipaddr yahoo.com MX`, replace ipaddr with the IP addr of the Authoritative DNS.
   - Q10:
     - step1: run `dig . NS`, get the ip addr of root DNS
     - step2: run `dig @ipaddr lyre00.cse.unsw.edu.au NS`, you will get the Authoritative DNS IP addr in the response
     - step3~n: keep replacing the ipaddr until you find "aa" in the flags.

 - **Exercise4**
   - [Example code](https://github.com/lrlrlrlr/COMP9331_22T1/blob/main/WebServer_demo_0.py)


## Midterm
- [merged slides](https://github.com/lrlrlrlr/COMP3331_9331_21T3/blob/main/9331review/week1~week5_merged.pdf)

## Lab6
### Exercise 1. 
 - Create a simulator object: `set ns [new simulator]`
 - Open file: `set fx [open filename.tr w]`
 - Create nodes: `set n1 [$ns node]`
 - Create links between the nodes: `$ns duplex-link $n1 $n6 2.5Mb 40ms DropTail`
 - Set the correct orientation: `$ns duplex-link-op $n1 $n2 orient up`
 - Setup TCP and FTP:
 	```
	# Create TCP conn
 	set tcpX [new Agent/TCP]
	$ns attach-agent $nX $tcpX

	#Sink for traffic at Node nX
	set sinkX [new Agent/TCPSink]
	$ns attach-agent $nX $sinkX

	#Connect
	$ns connect $tcpX $sinkX
	$tcpX set fid_ X

	#Setup FTP over TCP connection
	set ftpX [new Application/FTP]
	$ftpX attach-agent $tcpX
	```

- the proc function
	```
	
	proc record {} {
	>>	**global ns sink1 sink2 f1 f2**
		
		#Get an instance of the simulator
		set ns [Simulator instance]
		#Set the time after which the procedure should be called again
		set time 0.1
		#How many bytes have been received by the traffic sinks at n5?
		set bw1 [$sink1 set bytes_]
	>>	set bw2 [$sink2 set bytes_]
		#Get the current time
		set now [$ns now]
		#Calculate the bandwidth (in MBit/s) and write it to the files
		puts $f1 "$now [expr $bw1/$time*8/1000000]"
		puts $f2 "$now [expr $bw2/$time*8/1000000]"
		#Reset the bytes_ values on the traffic sinks
	>>	$sink1 set bytes_ 0
	>>	$sink2 ...........

		#Re-schedule the procedure
		$ns at [expr $now+$time] "record"
	}
	```
 - start recording: `ns at 0.0 "record"`
 - start FTP sessions: `$ns at 0.5 "$ftp1 start"`
 - Stop FTP sessions:  `$ns at 8.5 "$ftp1 stop"`
 - Call the finish procedure after 10 seconds of simulation time: `$ns at 10.0 "finish"`
 - Run the simulation: `$ns run`
