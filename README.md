# COMP9331_22T1
labs content


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
