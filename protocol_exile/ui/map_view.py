# protocol_exile/ui/map_view.py

import random

# In ui/map_view.py (update StarSystem class)
class StarSystem:
    def __init__(self, name, x, y, visited=False, dangerous=False):
        self.name = name
        self.x = x
        self.y = y
        self.visited = visited
        self.dangerous = dangerous
        self.event_triggered = False
        self.event_result = None  # Can hold the result of the event

    def __str__(self):
        if self.visited:
            return "●" if not self.dangerous else "⚠"
        return "○"

class GalaxyMap:
    def __init__(self, width=10, height=6, num_stars=12):
        self.width = width
        self.height = height
        self.stars = []
        self.generate_stars(num_stars)
        self.current_x = 0
        self.current_y = 0

    def generate_stars(self, num_stars):
        taken = set()
        for _ in range(num_stars):
            while True:
                x = random.randint(0, self.width - 1)
                y = random.randint(0, self.height - 1)
                if (x, y) not in taken:
                    taken.add((x, y))
                    break
            name = f"S-{x}{y}"
            danger = random.choice([False, False, True])  # 1/3 chance
            self.stars.append(StarSystem(name, x, y, False, danger))

    def render(self):
        print("\n🗺️  Star Map\n")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if x == self.current_x and y == self.current_y:
                    row += "[X] "
                elif any(s.x == x and s.y == y for s in self.stars):
                    star = next(s for s in self.stars if s.x == x and s.y == y)
                    row += f" {str(star)}  "
                else:
                    row += " .  "
            print(row)

    def move_to(self, x, y):
        if any(s.x == x and s.y == y for s in self.stars):
            self.current_x = x
            self.current_y = y
            for s in self.stars:
                if s.x == x and s.y == y:
                    s.visited = True
                    return s
            else:
                print("\n⚠ Invalid star system.")
                return None