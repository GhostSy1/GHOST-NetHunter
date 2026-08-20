import os
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from core.scanner import NetworkScanner
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███████╗██╗   ██╗ ██╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██╔════╝╚██╗ ██╔╝███║[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ███████╗ ╚████╔╝ ╚██║[/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ╚════██║  ╚██╔╝   ██║[/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ███████║   ██║    ██║[/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚══════╝   ╚═╝    ╚═╝[/bold blue]
 [bold yellow]             Professional Network Arsenal Suite[/bold yellow]
 [italic cyan]                    Developed by Ghost-SY1[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
async def run_network_scan():
    target = Prompt.ask("[bold yellow]Enter Target IP/Range[/bold yellow]")
    ports_input = Prompt.ask("[bold yellow]Enter Ports (comma separated)[/bold yellow]", default="21,22,23,25,53,80,110,135,139,443,445,3306,3389,8080")
    ports = [int(p.strip()) for p in ports_input.split(",")]
    scanner = NetworkScanner(target)
    console.print(f"\n[bold green][*][/bold green] Starting scan on [bold cyan]{target}[/bold cyan]...")
    open_ports = await scanner.scan_host(target, ports)
    table = Table(title=f"Scan Results for {target}", border_style="bold red")
    table.add_column("Port", style="cyan")
    table.add_column("Service", style="white")
    table.add_column("Status", style="bold green")
    services = {21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP", 8080: "HTTP-Proxy"}
    for port in open_ports:
        table.add_row(str(port), services.get(port, "Unknown"), "OPEN")
    console.print(table)
def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    asyncio.run(run_network_scan())
if __name__ == "__main__":
    main()
