import random
from core.data_loader import load_events, load_fragments

class EventEngine:
    def __init__(self):
        self.events = load_events()
        self.fragments = load_fragments()
        self.unlocked_fragments = []

    def get_random_event(self):
        return random.choice(self.events)

    def check_fragment_unlock(self, event_id, choice_text):
        for frag in self.fragments:
            if frag['trigger']['event_id'] == event_id and frag['trigger']['choice'] == choice_text:
                if frag['id'] not in self.unlocked_fragments:
                    self.unlocked_fragments.append(frag['id'])
                    return frag['content']
                
    def get_unlocked_fgragements(self):
        return [
            frag for frag in self.fragments 
            if frag['id'] in self.unlocked_fragments
        ]
        return None
    
    def get_unlocked_fragments(self):
        return [
            frag for frag in self.fragments
            if frag['id'] in self.unlocked_fragments
        ]
    
