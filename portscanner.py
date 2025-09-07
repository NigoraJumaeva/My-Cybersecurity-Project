import socket

def scan_ports(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            print(f"Port {port}: OPEN")
        except Exception:
            print(f"Port {port}: CLOSED")
        finally:
            s.close()

if __name__ == "__main__":
    target = "127.0.0.1"  # localhost
    common_ports = [21, 22, 80, 443]
    scan_ports(target, common_ports)
