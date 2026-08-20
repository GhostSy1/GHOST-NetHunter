import socket
import asyncio
import json
import os

class UltimateNetScanner:
    def __init__(self, target):
        self.target = target
        self.db_path = os.path.join(os.path.dirname(__file__), '../db/vulnerabilities.json')
        self.vulnerabilities = self.load_db()
        self.common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 3389]

    def load_db(self):
        if os.path.exists(self.db_path):
            with open(self.db_path, 'r') as f:
                return json.load(f)
        return []

    async def scan_port(self, port):
        try:
            reader, writer = await asyncio.wait_for(asyncio.open_connection(self.target, port), timeout=2)
            writer.close()
            await writer.wait_closed()
            
            # Match port to known vulnerabilities in our 1000+ DB
            matches = [v for v in self.vulnerabilities if str(port) in v['description']]
            return {"port": port, "state": "OPEN", "cve_matches": len(matches)}
        except:
            return None

    async def run(self):
        tasks = [self.scan_port(p) for p in self.common_ports]
        results = await asyncio.gather(*tasks)
        return [r for r in results if r]
