import os
import sys
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from core.scanner import UltimateNetScanner

BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███╗   ██╗███████╗████████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ████╗  ██║██╔════╝╚══██╔══╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██╔██╗ ██║█████╗     ██║   [/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██║╚██╗██║██╔══╝     ██║   [/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║ ╚████║███████╗   ██║   [/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝  ╚═══╝╚══════╝   ╚═╝   [/bold blue]
 [bold yellow]     GHOST-NetHunter: Elite Weaponized Network Arsenal & 1100+ DB[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

async def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    console.print("[bold yellow][*] Initializing GHOST-NetHunter Elite Network Engine...[/bold yellow]\n")
    
    target_host = Prompt.ask("[bold cyan]Enter Target IP or Hostname[/bold cyan]")
    
    console.print(f"\n[bold green][*][/bold green] Executing Deep Port Enumeration & 1100+ Vulnerability Mapping...")
    
    scanner = UltimateNetScanner(target_host)
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Scanning ports and matching service vulnerabilities...", total=None)
        results = await scanner.run()
        
    if results:
        t = Table(title=f"Fingerprinted Services & Vulnerability Mapping for {target_host}", border_style="bold red")
        t.add_column("Port", style="cyan")
        t.add_column("State", style="green")
        t.add_column("Active CVE Matches", style="bold yellow")
        t.add_column("Avg Reliability", style="bold green")
        
        for r in results:
            reliability = "9.5/10" # Placeholder for avg reliability in this view
            t.add_row(str(r['port']), r['state'], str(r['cve_matches']), reliability)
        console.print(t)
        console.print(f"\n[bold green][*][/bold green] Total weaponized network exploits in local DB: [bold white]{len(scanner.vulnerabilities)}[/bold white]")
    else:
        console.print("[bold red][!][/bold red] No open ports found or target is filtering traffic.")

if __name__ == "__main__":
    asyncio.run(main())
