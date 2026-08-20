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
 [bold yellow]     GHOST-NetHunter: Dedicated Network Infrastructure & Service Hunter[/bold yellow]
 [italic cyan]                               Ghost-SY1 Security[/italic cyan]
"""

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

async def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    console.print("[bold yellow][*] Initializing GHOST-NetHunter Network Specialist...[/bold yellow]\n")
    
    target_host = Prompt.ask("[bold cyan]Enter Target Network IP or Hostname[/bold cyan]")
    
    console.print(f"\n[bold green][*][/bold green] Executing Deep Port Enumeration & Service Fingerprinting on: {target_host}")
    scanner = UltimateNetScanner(target_host)
    
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Scanning ports and grabbing service banners...", total=None)
        results = await scanner.scan()
        
    if results:
        t = Table(title=f"Fingerprinted Services on {target_host}", border_style="bold red")
        t.add_column("Port", style="cyan")
        t.add_column("State", style="green")
        t.add_column("Service", style="yellow")
        t.add_column("Banner / Match", style="white")
        for r in results:
            t.add_row(str(r['port']), r['state'], r['service'], r['banner'][:40])
        console.print(t)
    else:
        console.print("[bold red][!][/bold red] No open ports found or target is filtering traffic.")
        
    console.print(f"\n[bold green][+][/bold green] Module Focus: [bold white]Network Infrastructure and Port Services Only[/bold white]")

if __name__ == "__main__":
    asyncio.run(main())
