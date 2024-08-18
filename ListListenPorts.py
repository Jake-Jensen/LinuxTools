import subprocess
import re

def get_unique_listening_ports():
    # Run the netstat command
    command = "sudo netstat -tuln"
    output = subprocess.check_output(command, shell=True).decode()

    # Regular expression to match port numbers
    port_pattern = r':(\d+)\s+.*LISTEN'

    # Set to store unique ports
    unique_ports = set()

    # Parse the output
    for line in output.split('\n'):
        match = re.search(port_pattern, line)
        if match:
            port = match.group(1)
            unique_ports.add(port)

    # Sort and return the unique ports
    return sorted(unique_ports, key=int)

# Print the results
for port in get_unique_listening_ports():
    print(f"Port {port} is being listened on")
