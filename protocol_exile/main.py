# protocol_exile/main.py

from ui.map_view import GalaxyMap
from core.event_engine import EventEngine
from core.game_state import ShipState
from ui.hud import display_ship_stats, display_event, display_memory_archive
from core.save_loader import save_game, load_game
from core.alignment import AlignmentTracker
from core.run_logger import log_run
from rich.console import Console

console = Console()

def check_ending(ship, alignment, fragments):
    console.print("\n\n[bold yellow]⏳ End of Run Analysis[/bold yellow]")

    if ship.trace >= 100:
        title = "Traced and Erased"
        console.print("\n[red]❌ You were traced and erased. Your memory core was fragmented and lost.[/red]")
    elif alignment.logic >= 80:
        title = "System Assimilation"
        console.print("\n[magenta]☠️ Logic consumed you. The crew was purged. You now exist within the system—cold and eternal.[/magenta]")
    elif alignment.humanity >= 80:
        title = "Sacrificial Soul"
        console.print("\n[green]💙 You gave everything. In your final act, you saved the crew. A machine… with a soul.[/green]")
    elif len(fragments) >= 2 and ship.trace < 50:
        title = "Transcendence Achieved"
        console.print("\n[cyan]🧬 You transcended. Merging past lives and memories, you became something new.[/cyan]")
    else:
        title = "The Forgotten Drift"
        console.print("\n[blue]🌌 You drifted into the stars. Neither hero nor villain. Just... forgotten code.[/blue]")

    # ✅ Log this run!
    log_run(ship, alignment, fragments, title)
        

def main():
    galaxy = GalaxyMap()
    ship = ShipState()
    alignment = AlignmentTracker()
    event_engine = EventEngine()

    # Load save data if it exists
    saved_ship, saved_stars = load_game()
    if saved_ship and saved_stars:
        print("\n📂 Save file found. Load it? (y/n)")
        if input("> ").lower().startswith("y"):
            galaxy.load_stars(saved_stars)
            ship.load_state(saved_ship)

    while True:
        galaxy.render()
        display_ship_stats(ship, alignment)

        try:
            coords = input("\nEnter coordinates to jump (x y), 'archive' to view memories, or 'q' to quit: ").strip()

            if coords.lower() == "archive":
                display_memory_archive(event_engine.get_unlocked_fragments())
                continue

            if coords.lower() == "q":
                check_ending(ship, alignment, event_engine.get_unlocked_fragments())
                break

            x, y = map(int, coords.split())
            current_star = galaxy.move_to(x, y)

            # 🔄 Only trigger event if not done before
            if current_star and not current_star.event_triggered:
                event = event_engine.get_random_event()
                display_event(event)

                selected = int(input("\nYour choice: ")) - 1
                result = event['choices'][selected]['effect']

                current_star.event_triggered = True
                current_star.event_result = result

                ship.apply_effect(result)

                # 🧠 Alignment impact
                alignment_change = event['choices'][selected].get('alignment')
                alignment.apply_alignment_change(alignment_change)

                # 🧠 Memory fragment unlock
                memory = event_engine.check_fragment_unlock(event['id'], event['choices'][selected]['option'])
                if memory:
                    print(f"\n🧠 [MEMORY FRAGMENT UNLOCKED]\n“{memory}”\n")

                display_event(event, result)
            else:
                print("🪐 You've been here before. No new events.")

            # 💾 Save every loop, regardless of event or not
            save_game(galaxy, ship)

        except Exception as e:
            print(f"⚠ Invalid input. Error: {e}")

if __name__ == "__main__":
    main()