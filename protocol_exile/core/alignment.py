# protocol_exile/core/alignment.py

class AlignmentTracker:
    def __init__(self):
        self.humanity = 0     # Empathy, care for life
        self.logic = 0        # Cold efficiency, self-preservation

    def apply_alignment_change(self, change_str):
        """
        Example: 'humanity +10' or 'logic -5'
        """
        if not change_str or change_str.lower() == "none":
            return

        try:
            axis, value = change_str.split()
            value = int(value)
            if axis == "humanity":
                self.humanity += value
            elif axis == "logic":
                self.logic += value
            print(f"🧭 Alignment updated: {axis} {value:+}")
        except Exception as e:
            print(f"⚠️ Error applying alignment change: {e}")

    def display(self):
        print("\n⚖️ [AI ALIGNMENT]")
        print(f"  Humanity: {self.humanity}")
        print(f"  Logic:    {self.logic}")