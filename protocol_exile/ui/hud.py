# protocol_exile/ui/hud.py

# protocol_exile/ui/hud.py

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def display_ship_stats(ship, alignment=None):
    status = (
        f"[bold cyan]🧭 Ship Status[/bold cyan]\n"
        f"[green]Morale:[/] {ship.morale}   "
        f"[yellow]Fuel:[/] {ship.fuel}   "
        f"[blue]Power:[/] {ship.power}   "
        f"[red]Trace:[/] {ship.trace}"
    )

    if alignment:
        status += (
            f"\n\n[bold magenta]🤖 AI Alignment[/bold magenta]\n"
            f"[cyan]Humanity:[/] {alignment.humanity}   "
            f"[magenta]Logic:[/] {alignment.logic}"
        )

    console.print(Panel.fit(status, title="Status Core", border_style="cyan"))

def display_event(event, result=None):
    console.print("\n[bold magenta]📡 EVENT:[/bold magenta] " + event['description'])
    for i, choice in enumerate(event['choices']):
        console.print(f"  [bold cyan]{i+1}[/bold cyan]. {choice['option']}")

    if result:
        console.print(f"\n[bold green]🧬 RESULT:[/bold green] {result}")

def display_memory_archive(fragments):
    if not fragments:
        console.print("\n🧠 [bold cyan]Memory Archive is empty.[/bold cyan]\n")
        return

    console.print("\n[bold magenta]🧬 Memory Fragment Archive[/bold magenta]\n")
    for frag in fragments:
        panel = Panel.fit(
            Text(f"“{frag['content']}”", style="italic cyan"),
            title=f"[bold white]{frag['id'].replace('_', ' ').title()}",
            border_style="magenta"
        )
        console.print(panel)