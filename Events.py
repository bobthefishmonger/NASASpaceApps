import time


class GameEvent:
    def __init__(
        self, event_id, target_module=None, severity="WARNING", flare_class=None
    ):
        self.event_id = event_id
        self.target_module = target_module
        self.severity = severity
        self.flare_class = flare_class
        self.is_resolved = False

    def resolve(self):
        self.is_resolved = True
        if self.target_module:
            self.target_module.repair()

    def get_state(self):
        return {
            "event_id": self.event_id,
            "target": self.target_module.name if self.target_module else None,
            "severity": self.severity,
            "flare_class": self.flare_class,
            "is_resolved": self.is_resolved,
        }

#class InfrastructureModule:
#    def __init__(self, name, max_health=100.0):
#        self.name = name
#        self.max_health = max_health
#        self.health = max_health
#        self.is_damaged = False

#    def take_damage(self, amount):
#        self.health = max(0.0, self.health - amount)
#        if self.health <= 0.0:
#            self.is_damaged = True
#        return self.is_damaged
#
#    def repair(self):
#        self.health = self.max_health
#        self.is_damaged = False

class Environment:
    def __init__(self):
        self.season = "spring"
        self.active_events = []

    def strike(self, event_id, buildings, count, flare_class=None):
        standing = [b for b in buildings if not b.is_damaged]
        targets = self.rng.sample(standing, min(count, len(standing)))
        for building in targets:
            building.take_damage(100.0)
            self.active_events.append(GameEvent(event_id, target_module=building, severity="CRITICAL", flare_class=flare_class))
        return [b.name for b in targets]

    def activate_sand_storm(self, buildings, count=3):
        panels = [b for b in buildings if b.kind == "solar"]
        destroyed = self.strike("sand_storm_damage", panels, count)
        return {"code": "sand_storm", "destroyed": destroyed}

    def activate_solar_flare(self, buildings, flare_class="M", count=3):
        destroyed = self.strike("solar_flare_damage", buildings, count, flare_class)
        return {"code": "solar_flare", "flare_class": flare_class, "destroyed": destroyed}



#class MarsClock:
#    HOURS_PER_SOL = 24

#    def __init__(self, hours_per_tick=1):
#        self.hours_per_tick = hours_per_tick
#        self.total_hours = 0
#        self.sol = 1
#        self.hour = 0

#    def advance(self):
#        self.total_hours += self.hours_per_tick
#        self.sol = self.total_hours // self.HOURS_PER_SOL + 1
#        self.hour = self.total_hours % self.HOURS_PER_SOL

#    def get_state(self):
#        return {"sol": self.sol, "hour": self.hour, "total_hours": self.total_hours}


# clock = MarsClock()
# TICK_SECONDS = 15

# while True:
#     clock.advance()
#     print(clock.get_state())
#     time.sleep(TICK_SECONDS)



