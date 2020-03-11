# Backend Research
### *1. What is the entire cycle of events that follows when you type in the url of a webpage? <br/> 2.How are urls mapped to website hosted on a server in Bangalore?*


__a__.  When you first type in the URL to address bar of your browser, it  checks the local browser cache for a DNS record to find the corresponding IP address.
DNS(Domain Name System) is a list of domain names and their corresponding IP addresses.<br /> __b__.  If the DNS record is not found on the local browser cache 
then a series of searches on other cached memories (like OS cache, Router cache etc.) take place one after the other. If it still remains unfounded then a DNS query is initiated.<br /> 
__c__.  Once the IP address is found, a connection is established using an internet protocol (eg. TCP), and now the browser can send an HTTP request to the webserver.<br />__d__.  The server handles the
request and sends out an HTTP response, which then the browser displays as HTML content. Requests for additional elements such as pictures, CSS and JavaScript
are sent later.<br/>
### *3. Read up in brief about TCP and UDP*
TCP and UDP are both intenet protocols.
