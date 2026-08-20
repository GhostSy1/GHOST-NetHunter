import os
import sys
import asyncio
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn
from core.scanner import AdvancedNetScanner
BANNER = """
 [bold red] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ███╗   ██╗███████╗████████╗[/bold red]
 [bold red]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ████╗  ██║██╔════╝╚══██╔══╝[/bold red]
 [bold white]██║  ███╗███████║██║   ██║███████╗   ██║        ██╔██╗ ██║█████╗     ██║   [/bold white]
 [bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██║╚██╗██║██╔══╝     ██║   [/bold white]
 [bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║ ╚████║███████╗   ██║   [/bold blue]
 [bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝  ╚═══╝╚══════╝   ╚═╝   [/bold blue]
 [bold yellow]         Advanced Network Recon & Banner Grabbing Suite[/bold yellow]
 [italic cyan]                         Ghost-SY1 Security 2026[/italic cyan]
"""
console = Console()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
async def main():
    clear_screen()
    console.print(Panel(BANNER, border_style="bold red", expand=False))
    target = Prompt.ask("[bold yellow]Enter Target IP or Hostname[/bold yellow]")
    console.print(f"[bold cyan][*][/bold cyan] Initializing High-Speed Port Enumeration & Banner Grabbing for: {target}")
    scanner = AdvancedNetScanner(target)
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task(description="Scanning ports and grabbing service banners...", total=None)
        results = await scanner.run()
    if results:
        t = Table(title=f"Active Services on {target}", border_style="bold red")
        t.add_column("Port", style="cyan")
        t.add_column("State", style="green")
        t.add_column("Service Banner", style="white")
        for r in results:
            t.add_row(str(r['port']), r['state'], r['banner'][:60])
        console.print(t)
    else:
        console.print("[bold red][!][/bold red] No open ports found or target is filtering traffic.")
if __name__ == "__main__":
    asyncio.run(main())
