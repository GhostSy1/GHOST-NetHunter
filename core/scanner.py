import socket
import asyncio
class NetworkScanner:
    def __init__(self, target_range):
        self.target_range = target_range
    async def scan_port(self, ip, port):
        conn = asyncio.open_connection(ip, port)
        try:
            reader, writer = await asyncio.wait_for(conn, timeout=1)
            writer.close()
            await writer.wait_closed()
            return port
        except Exception:
            return None
    async def scan_host(self, ip, ports):
        open_ports = []
        tasks = [self.scan_port(ip, port) for port in ports]
        results = await asyncio.gather(*tasks)
        return [p for p in results if p is not None]
