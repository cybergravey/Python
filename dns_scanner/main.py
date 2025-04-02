import dns.resolver
import sys

record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
if len(sys.argv) > 1:
    domain = sys.argv[1]  # Get domain from command-line argument
else:
    domain = input("Enter the domain name: ").strip()  # Get domain from user input

for records in record_types:
    try:
        answer = dns.resolver.resolve(domain, records)  # Query DNS records
        print(f'\n{records} Records')  # Print record type
        print('-' * 30)  # Print separator
        for server in answer:
            print(server.to_text())  # Print each record found
    except dns.resolver.NoAnswer:
        pass   # Ignore if no answer is found
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist.')  # Print if domain does not exist
        quit()
    except KeyboardInterrupt:
        print('Quitting.')  # Handle keyboard interrupt
        quit()