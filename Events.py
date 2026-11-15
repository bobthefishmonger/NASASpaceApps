import numpy as np


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


class Environment:
    def __init__(self):
        self.season = "spring"

        self.active_events = []
        self.rng = np.random.default_rng()

    def strike(self, event_id, buildings, count, flare_class=None):
        standing = [b for b in buildings if not b.is_damaged]
        targets = self.rng.sample(standing, min(count, len(standing)))
        for building in targets:
            building.take_damage(100.0)
            self.active_events.append(
                GameEvent(
                    event_id,
                    target_module=building,
                    severity="CRITICAL",
                    flare_class=flare_class,
                )
            )
        return [b.name for b in targets]

    def activate_sand_storm(self, buildings, count=3):
        panels = [b for b in buildings if b.kind == "solar"]
        destroyed = self.strike("sand_storm_damage", panels, count)
        return {"code": "sand_storm", "destroyed": destroyed}

    def activate_solar_flare(self, buildings, flare_class="M", count=3):
        destroyed = self.strike("solar_flare_damage", buildings, count, flare_class)
        return {
            "code": "solar_flare",
            "flare_class": flare_class,
            "destroyed": destroyed,
        }
