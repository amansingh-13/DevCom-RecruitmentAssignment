# Backend Research

### *1. What is the entire cycle of events that follows when you type in the url of a webpage? <br/> 2.How are urls mapped to website hosted on a server in Bangalore?*


__a__.  When you first type in the URL to address bar of your browser, it  checks the local browser cache for a DNS record to find the corresponding IP address.
DNS(Domain Name System) is a list of domain names and their corresponding IP addresses. <br /> 
__b__.  If the DNS record is not found on the local browser cache 
then a series of searches on other cached memories (like OS cache, Router cache etc.) take place one after the other. If it still remains unfounded then a DNS query is initiated.<br /> 
__c__.  Once the IP address is found, a connection is established using an internet protocol (eg. TCP), and now the browser can send an HTTP request to the webserver.<br />
__d__.  The server handles the
request and sends out an HTTP response, which then the browser displays as HTML content. Requests for additional elements such as pictures, CSS and JavaScript
are sent later.<br/>

### *3. Read up in brief about TCP and UDP*
TCP and UDP are both intenet protocols. Internet protocols relay data packets between IP addresses. <br />
For a TCP/IP protocol, it defines a "IP Packet" which contains the addresses, data and checksum scheme (checksum scheme is used to verify data integrity). This "IP Packet " hops around from one router to other, eventually getting closer to the destination. It does so in this fashion:<br />
- Suppose the destination address is 314.15.19.265<br />
- The routers look at the left part of the IP address (314.15.---) to get the packet to the right neighborhood<br />
- As the neighborhood has the same left part as the destination, the packet hops to routers close to right part of the IP 
address (---.19.265) untill it reaches the destination<br />

UDP is similar except it does not follow the checksum scheme for faster transfer speeds.

### *4. What does setting up a server even mean?* <br /> *5. How a server resolves a request?*
A Server is anything that serves to the clients (often multiple clients) requests. A Server can store, query and retrieve data. <br />
To understand it more clearly lets seperate Physical Servers and Web Servers. <br />
WEB SERVERS's job is to act as a middleman between the physical servers and multiple clients, at the same time. When a request is sent by the client, they often have to work with multiple programming languages like PHP, Python etc and convert them to HTML files with CSS, Javascript etc. These programs ensure setting up proper client-server structure.<br />
Google Apache and NginX are examples of Web Servers.<br />

### *6. How would you show your friend the html file you made if you are not allowed to share your code with him or upload your website?*
One way to do this would be to install XAMPP (WAMP for windows) on your device. WAMP is a web sever 'package' which includes Apache as the Web Server, MySQL, PHP, and your PC as the physical Server.<br />
Another similar way would be to use Microsoft IIS. Here is what I found: <br />

- Go to Control Panel > Programs and Features and use 'Turn Windows feature on or off' to activate Internet Information Services option
- After this, download Microsoft IIS by going to 127.0.0.1 or otherwise
- Use Microsoft IIS to setup your html page and specify which port number on the router you want to use (eg 314.15.19.265:**75** for port number 75)
- A few more ISP's settings need to be changed and then you are done (see video in README.md)
- Anyone can view your page by writing 314.15.19.265:75 in the URL bar

I couldn't find the use for 127.0.0.1 for setting up a server on your PC but figured out that it is a Special IP Address (localhost) used to establish an IP connection to the same PC. It is used to ensure the correct working of all Internet Protocols.<br />
PS: I am not sure, but the method described above will work only if your IP address is static and if your ISP allows you to host a server.<br />
PPS: Another thing I found out was that you can make personal webpages using Github (and Jekyll for additional features. This can't be used as an answer to **6.** but I made a basic one which helped me learn some html: https://feyn-aman.github.io/
