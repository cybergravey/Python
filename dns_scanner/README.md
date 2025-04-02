<h1>DNS Scanner</h1>

<h2>Description</h2>
This Python script performs a DNS enumeration by querying different DNS record types for a given domain.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>dnspython</b>
- <b>sys</b>

<h2>Environments Used </h2>

- <b>macOS Sequoia Version 15.3.2</b> 

<h2>Program walk-through:</h2>

<p align="center">
</b><b>1. Import the Required Modules</b> <br/>
<img src="https://i.imgur.com/NA2CYwb.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
• dns.resolver from the dnspython library is used to send queries.
<br />
• sys is used to handle command-line arguments so the user provides a domain to scan.
<br />
<br />
<br />
</b><b>2. Define the Record Types to Query</b>  <br/>
<img src="https://i.imgur.com/AKjgPWC.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
These are the different DNS record types being queried:
<br />
  • A - IPv4 address of the domain
<br />
  • AAAA - IPv6 address of the domain
<br />
  • NS - Nameservers for the domain
<br />
  • CNAME - Canonical name (alias) for the domain
<br />
  • MX - Mail exchange records (email servers)
<br />
  • PTR - Reverse DNS lookup (IP to domain)
<br />
  • SOA - Start of Authority (domain info)
<br />
  • TXT - Miscellaneous text records (SPF, DKIM, etc.)
<br />
<br />
<br />
<b>3. Handling User Input (Domain Name)</b> <br/>
<img src="https://i.imgur.com/IJ0ecce.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
  • If yes, it assigns sys.argv[1] (the second argument) to domain.
<br />
  • If no, it prompts the user to manually enter a domain.
<br />
  • Running via command-line → python3 script.py example.com
<br />
  • Running without an argument → The script asks: "Enter a domain name:"
<br />
<br />
<br />
<b>4. Looping Through Each DNS Record Type</b>  <br/>
<img src="https://i.imgur.com/dtH6I10.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
  • The script loops through each record type and queries the DNS server.
<br />
  • Calls dns.resolver.resolve(domain, records) to fetch the requested DNS records.
<br />
  • If the records exists, it prints results.
<br />
<br />
<br />
<b>5. Printing the Results</b>  <br/>
<img src="https://i.imgur.com/6wNs9D9.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
  • If a record is found, it prints the results.
<br />
<br />
<br />
<b>6. Handling Errors Gracefully</b>  <br/>
<img src="https://i.imgur.com/8a4fIvZ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
  • dns.resolver.NoAnswer: No record found for this type, so the script moves on.
<br />
  • dns.resolver.NXDOMAIN: The domain does not exist, so the script exits.
<br />
  • KeyboardInterrupt: If the user presses a key, the script stops gracefully.
<br />
<br />
<br />
<b>7. How to Run the Script</b>  <br/>
<img src="https://i.imgur.com/WmPFEGj.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
  • Run the Python script.
<br />
  • Enter the domain name in the command-line. The domain name example for this project is "amazon.com."
<br />
<br />
<img src="https://i.imgur.com/qSK8aVu.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<b>Final Thoughts:</b>  <br/>
  • Works with command-line arguments OR manual input
<br />
  • Queries multiple record types
<br />
  • Handles missing records and valid domains
<br />
  • Allows users to exit safely
<br />
<br />
<br />

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
