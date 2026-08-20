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
 [bold yellow]         Ultimate Network Recon & Service Fingerprinting Engine (2026)[/bold yellow]
 [italic cyan]                         Ghost-SY1 Security[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
async def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    console.print("[bold yellow][*] Initializing Ghost-NetHunter Interactive Engine...[/bold yellow]\n")
    target = Prompt.ask("[bold cyan]Enter Target IP or Hostname[/bold cyan]")
    console.print(f"\n[bold green][*][/bold green] Executing Deep Port Enumeration & Service Fingerprinting on: {target}")
    scanner = UltimateNetScanner(target)
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Enumerating ports and grabbing service fingerprints...", total=None)
        results = await scanner.scan()
    if results:
        t = Table(title=f"Fingerprinted Services on {target}", border_style="bold red")
        t.add_column("Port", style="cyan")
        t.add_column("State", style="green")
        t.add_column("Service", style="yellow")
        t.add_column("Banner", style="white")
        for r in results:
            t.add_row(str(r['port']), r['state'], r['service'], r['banner'][:40])
        console.print(t)
    else:
        console.print("[bold red][!][/bold red] No open ports found or target is filtering traffic.")
if __name__ == "__main__":
    asyncio.run(main())
