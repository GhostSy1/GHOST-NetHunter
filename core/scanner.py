import socket
import asyncio
class UltimateNetScanner:
    def __init__(self, target):
        self.target = target
        self.ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080, 8443]
    async def analyze_service(self, port):
        try:
            reader, writer = await asyncio.wait_for(asyncio.open_connection(self.target, port), timeout=2)
            writer.write(b"HEAD / HTTP/1.0\r\n\r\n")
            await writer.drain()
            banner = await reader.read(256)
            writer.close()
            await writer.wait_closed()
            b_str = banner.decode(errors="ignore").strip().replace("\n", " ")
            service = "Unknown"
            if port == 22: service = "OpenSSH / Secure Shell"
            elif port in [80, 443, 8080, 8443]: service = "HTTP/S Web Server"
            elif port == 3306: service = "MySQL Database"
            elif port == 445: service = "Microsoft-DS SMB"
            elif port == 3389: service = "Microsoft RDP"
            return {"port": port, "state": "OPEN", "service": service, "banner": b_str if b_str else "Active TCP Stream"}
        except Exception:
            return None
    async def scan(self):
        tasks = [self.analyze_service(p) for p in self.ports]
        results = await asyncio.gather(*tasks)
        return [r for r in results if r]
