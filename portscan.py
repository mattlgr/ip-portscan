import socket

class Pscan:
    def __init__(self, ip):
        self.ip = ip
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.response = f"Response for {self.ip}\n"
    
    def validate_ipv4(self):
        try:
            socket.inet_aton(self.ip)
            return True
        except socket.error:
            try:
                self.ip = socket.inet_aton(socket.gethostbyname(self.ip))
                return True
            except socket.error:
                return None
    
    def startScan(self):
        ports = [21, 22, 23, 25, 53, 80, 8080, 110, 143, 443, 1433, 3306, 3389, 5900] # Just a list of ports for the bot to scan through that have some significance to networking.
        port_descriptions = ["ftp", "ssh", "telnet", "smtp", "dns", "http", "localhost", "pop3", "imap", "https", "ms-sql-s", "mysql", "ms-wbt-server", "vnc"] # Just the port types for the module to display.
        
        i = 0
        for port in ports:
            i += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)

            result = sock.connect_ex((self.ip, port))
            if result == 0:
                self.response += f"Port {port} ({port_descriptions[i-1]}) open on {self.ip}!\n"
            else:
                self.response += f"Port {port} ({port_descriptions[i-1]}) is closed on {self.ip}!\n"

    def getResponse(self):
        return self.response
