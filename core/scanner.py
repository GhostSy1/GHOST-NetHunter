import socket
import asyncio
class AdvancedNetScanner:
    def __init__(self, target):
        self.target = target
        self.common_ports = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 8080]
    async def scan_port(self, port):
        try:
            reader, writer = await asyncio.wait_for(asyncio.open_connection(self.target, port), timeout=2)
            writer.write(b"HEAD / HTTP/1.0\r\n\r\n")
            await writer.drain()
            banner = await reader.read(512)
            writer.close()
            await writer.wait_closed()
            return {"port": port, "state": "OPEN", "banner": banner.decode(errors="ignore").strip().replace("\n", " ")}
        except Exception:
            return {"port": port, "state": "OPEN", "banner": "No Banner / Raw TCP"}
    async def run(self):
        open_ports = []
        for port in self.common_ports:
            try:
                _, _ = await asyncio.wait_for(asyncio.open_connection(self.target, port), timeout=1)
                banner_info = await self.scan_port(port)
                open_ports.append(banner_info)
            except Exception:
                continue
        return open_ports
