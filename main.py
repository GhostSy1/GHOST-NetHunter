import os
import sys
import asyncio
import json
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
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║ ╚████║███████║   ██║   [/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝  ╚═══╝╚══════╝   ╚═╝   [/bold blue]
 [bold yellow]     GHOST-NetHunter: Elite Weaponized Network Arsenal & 1100+ DB[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_help():
    help_text = """
[bold yellow]GHOST-NetHunter Help Menu[/bold yellow]

[bold cyan]Description:[/bold cyan]
Professional network infrastructure and service auditing suite.

[bold cyan]Features:[/bold cyan]
1. [bold white]Port Scanning[/bold white]: High-speed asynchronous port discovery.
2. [bold white]Banner Grabbing[/bold white]: Real-time service version identification.
3. [bold white]CVE Mapping[/bold white]: Automatically links open services to 1100+ weaponized CVEs.

[bold cyan]Usage:[/bold cyan]
Run the script and enter the target IP or hostname when prompted.
"""
    console.print(Panel(help_text, title="Help & Documentation", border_style="blue"))

async def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        show_help()
        return

    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    
    # Explicit Database Check
    db_path = os.path.join(os.path.dirname(__file__), 'db/vulnerabilities.json')
    if os.path.exists(db_path):
        with open(db_path, 'r') as f:
            db_size = len(json.load(f))
        console.print(f"[bold green][*] Successfully loaded network vulnerability database with {db_size} entries.[/bold green]")
    else:
        console.print("[bold red][!] Warning: Network vulnerability database not found![/bold red]")

    console.print("[bold yellow][*] Initializing GHOST-NetHunter Elite Network Engine...[/bold yellow]\n")
    
    target_host = Prompt.ask("[bold cyan]Enter Target IP or Hostname[/bold cyan]")
    
    console.print(f"\n[bold green][*][/bold green] Executing Deep Port Enumeration & 1100+ Vulnerability Mapping...")
    
    scanner = UltimateNetScanner(target_host)
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Scanning ports and matching service vulnerabilities...", total=None)
        results = await scanner.run()
        
    if results:
        t = Table(title=f"Fingerprinted Services for {target_host}", border_style="bold red")
        t.add_column("Port", style="cyan")
        t.add_column("State", style="green")
        t.add_column("Active CVE Matches", style="bold yellow")
        for r in results:
            t.add_row(str(r['port']), r['state'], str(r['cve_matches']))
        console.print(t)
    else:
        console.print("[bold red][!][/bold red] No open ports found or target is filtering traffic.")

if __name__ == "__main__":
    asyncio.run(main())
