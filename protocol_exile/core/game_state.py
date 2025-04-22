class ShipState:
    def __init__(self):
        self.morale = 100
        self.fuel = 100
        self.power = 100
        self.trace = 0

    def apply_effect(self, effect_str):
        if effect_str.lower() == "nothing":
            print("🧊 No effect.")
            return

        try:
            stat, value = effect_str.split()
            value = int(value)
            if stat == "morale":
                self.morale += value
            elif stat == "fuel":
                self.fuel += value
            elif stat == "power":
                self.power += value
            elif stat == "trace":
                self.trace += value
            print(f"✅ {stat.capitalize()} updated by {value}")
        except Exception as e:
            print(f"⚠ Could not apply effect: {effect_str} ({e})")

    def display(self):
        print("\n🧭 Ship Status")
        print(f"  Morale: {self.morale}")
        print(f"  Fuel:   {self.fuel}")
        print(f"  Power:  {self.power}")
        print(f"  Trace:  {self.trace}")