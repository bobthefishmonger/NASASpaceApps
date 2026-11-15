#AI was used to generate
from Events import Environment
import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('APIKEY')

url = "https://ccmc.gsfc.nasa.gov/DONKI-API/get/FLR"

params = {
    "startDate": "2026-09-16",
    "endDate": "2026-11-15",
    "api_key": api_key
}

response = requests.get(url, params=params)


if response.status_code == 200:
    m_class = [f for f in response.json() if f.get("classType", "").upper().startswith("M")]
    
    print(f"found {len(m_class)} M-class flares.")
    probability = round(len(m_class) / 60, 2)
    print("probability =", probability)
    if m_class:
        print(json.dumps(m_class[0], indent=2))
else:
    print(f"error {response.status_code}: {response.text}")



#AI used to help with rng
class RandomHazards:
    def __init__(self, environment, buildings, storm_chance=0.01, flare_chance=probability):
        self.environment = environment
        self.buildings = buildings
        self.storm_chance = storm_chance  
        self.flare_chance = flare_chance
        self.rng = environment.rng 

    def tick(self):
        alerts = []
        if self.rng.random() < self.storm_chance:   
            alerts.append(self.environment.activate_sand_storm(self.buildings))
        if self.rng.random() < self.flare_chance:    
            alerts.append(self.environment.activate_solar_flare(self.buildings))
        return alerts
import numpy as np
import pygame

#AI used for class naming/understanding
class GameEvent:
    def __init__(
        self, event_id, target_module=None, severity="WARNING", flare_class=None
    ):
        self.event_id = event_id
        self.target_module = target_module
        self.severity = severity
        self.flare_class = flare_class
        self.is_resolved = False
#AI used for resolving damage
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

#AI used to help with rng building chooser
class Environment:
    def __init__(self):
        self.season = "spring"

        self.active_events = []
        self.rng = np.random.default_rng()

    def strike(self, event_id, buildings, count, flare_class=None):
        standing = [b for b in buildings if not b.is_damaged]
        # CHANGED: numpy's Generator has no .sample(); this is the equivalent
        targets = [standing[i] for i in self.rng.choice(len(standing), min(count, len(standing)), replace=False)] #AI used for rng
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

#
class Building:  # stand-in for your real building class, delete in your game
    def __init__(self, name, kind):
        self.name, self.kind = name, kind
        self.is_damaged = False

    def take_damage(self, amount):
        self.is_damaged = True

    def repair(self):
        self.is_damaged = False


pygame.init()
GRID_ROWS, GRID_COLS, CELL_SIZE = 8, 12, 60
WIDTH = GRID_COLS * CELL_SIZE
HEIGHT = GRID_ROWS * CELL_SIZE + (GRID_COLS - GRID_ROWS) * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont("consolas", 20)
FONT_BIG = pygame.font.SysFont("consolas", 28, bold=True)

PANEL_BG = (25, 30, 45)
BORDER = (200, 80, 80)
TEXT = (230, 230, 230)
BTN = (60, 110, 180)
BTN_HOVER = (90, 140, 210)
DONE = (90, 200, 120)



class Button:
    def __init__(self, rect, label):
        self.rect = pygame.Rect(rect)
        self.label = label

    def draw(self, surf):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(surf, BTN_HOVER if hover else BTN, self.rect, border_radius=8)
        txt = FONT.render(self.label, True, TEXT)
        surf.blit(txt, txt.get_rect(center=self.rect.center))

    def clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


class DisasterPopup:
    """Built from the GameEvents created by one strike."""

    def __init__(self, events):
        self.events = events
        first = events[0]
        self.event_id = first.event_id
        self.severity = first.severity
        self.flare_class = first.flare_class or "N/A"
        self.targets = [e.target_module.name for e in events]

        self.rect = pygame.Rect(0, 0, 520, 360)
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.todo_btn = Button(
            (self.rect.centerx - 110, self.rect.bottom - 70, 220, 45),
            "Open To-Do List",
        )
        self.visible = True

    def handle_event(self, e):
        """Returns True if the to-do button was pressed."""
        return self.visible and self.todo_btn.clicked(e)

    def draw(self, surf):
        if not self.visible:
            return
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        surf.blit(overlay, (0, 0))

        pygame.draw.rect(surf, PANEL_BG, self.rect, border_radius=12)
        pygame.draw.rect(surf, BORDER, self.rect, 3, border_radius=12)

        x, y = self.rect.x + 25, self.rect.y + 20
        surf.blit(FONT_BIG.render("DISASTER ALERT!", True, BORDER), (x, y))
        y += 55
        lines = [
            f"Event ID:    {self.event_id}",
            f"Severity:    {self.severity}",
            f"Flare class: {self.flare_class}",
            "Buildings hit:",
        ]
        for line in lines:
            surf.blit(FONT.render(line, True, TEXT), (x, y))
            y += 30
        for name in self.targets:
            surf.blit(FONT.render(f"  - {name}", True, (255, 170, 120)), (x, y))
            y += 26

        self.todo_btn.draw(surf)


class TodoList:
    """One repair task per GameEvent. Clicking a task calls event.resolve()."""

    def __init__(self, events):
        self.events = events
        self.rect = pygame.Rect(0, 0, 520, 360)
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.close_btn = Button(
            (self.rect.centerx - 60, self.rect.bottom - 60, 120, 40), "Close"
        )
        self.visible = False

    def task_rect(self, i):
        return pygame.Rect(
            self.rect.x + 25, self.rect.y + 80 + i * 50, self.rect.width - 50, 40
        )

    def handle_event(self, e):
        if not self.visible:
            return
        if self.close_btn.clicked(e):
            self.visible = False
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            for i, ev in enumerate(self.events):
                if not ev.is_resolved and self.task_rect(i).collidepoint(e.pos):
                    ev.resolve()  # marks resolved + repairs the building

    def all_done(self):
        return all(ev.is_resolved for ev in self.events)

    def draw(self, surf):
        if not self.visible:
            return
        pygame.draw.rect(surf, PANEL_BG, self.rect, border_radius=12)
        pygame.draw.rect(surf, BTN, self.rect, 3, border_radius=12)
        surf.blit(
            FONT_BIG.render("REPAIR TO-DO LIST", True, TEXT),
            (self.rect.x + 25, self.rect.y + 20),
        )

        for i, ev in enumerate(self.events):
            r = self.task_rect(i)
            pygame.draw.rect(surf, (40, 48, 70), r, border_radius=6)
            box = pygame.Rect(r.x + 10, r.y + 10, 20, 20)
            pygame.draw.rect(surf, TEXT, box, 2)
            if ev.is_resolved:
                pygame.draw.line(surf, DONE, box.topleft, box.bottomright, 3)
                pygame.draw.line(surf, DONE, box.topright, box.bottomleft, 3)
            colour = DONE if ev.is_resolved else TEXT
            surf.blit(
                FONT.render(f"Repair {ev.target_module.name}", True, colour),
                (r.x + 45, r.y + 10),
            )

        if self.all_done():
            surf.blit(
                FONT.render("All repairs complete!", True, DONE),
                (self.rect.x + 25, self.rect.bottom - 100),
            )
        self.close_btn.draw(surf)
'''This function for drawing the grid is in another team-mate's code. 
I just used my version here so that i could test my code'''
def draw_grid(grid_rows,grid_cols,cell_size):

    screen.fill((20,20,20))

    hud_height=(grid_cols-grid_rows)*cell_size
    hud=pygame.Rect(0,0, grid_cols*cell_size, hud_height)
    pygame.draw.rect(screen, (255,255,255), hud, 1)

    grid_width=grid_rows*cell_size
    grid = []
    row = []
    for row_no in range(grid_rows):
        row = []
        for col_no in range (grid_cols):
           grid_square=pygame.Rect(cell_size*col_no,cell_size*row_no, cell_size, cell_size)
           pygame.draw.rect(screen,(100,100,100),grid_square,1)
           row.append(grid_square)
        grid.append(row)

    return grid


def draw_frame(popup=None, todo=None):
    # 1. grid function (fills the background, draws HUD + cells)
    grid = draw_grid(GRID_ROWS, GRID_COLS, CELL_SIZE)

    # 2. overlays, drawn on top of the grid
    if popup:
        popup.draw(screen)
    if todo:
        todo.draw(screen)

    # 3. a single flip per frame
    pygame.display.flip()

    return grid  # so main() can use the cell rects for clicks


# ======================= MAIN LOOP =======================
HAZARD_TICK = pygame.USEREVENT + 1
DAY_MS = 5000  # one hazard roll every 5 seconds


def main():
    clock = pygame.time.Clock()

    env = Environment()
    buildings = [
        Building("Farm 1", "farm"), Building("Farm 2", "farm"),
        Building("O2 Scrubber 1", "o2"), Building("O2 Scrubber 2", "o2"),
        Building("Solar Panel 1", "solar"), Building("Solar Panel 2", "solar"),
        Building("Water Recycler", "water"), Building("Habitat", "hab"),
    ]
    hazards = RandomHazards(env, buildings)
    pygame.time.set_timer(HAZARD_TICK, DAY_MS)

    popup = todo = None
    grid = []

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

            # random hazard roll (replaces the SPACE trigger)
            if e.type == HAZARD_TICK and popup is None:
                start = len(env.active_events)
                hazards.tick()
                new_events = env.active_events[start:]
                if new_events:
                    popup, todo = DisasterPopup(new_events), TodoList(new_events)

            if todo and todo.visible:
                todo.handle_event(e)
            elif popup and popup.handle_event(e):
                popup.visible = False
                todo.visible = True

        # discard the UI once the player closes a finished to-do list
        if todo and not todo.visible and not popup.visible and todo.all_done():
            popup = todo = None

        grid = draw_frame(popup, todo)
        clock.tick(60)/2

    pygame.quit()

if __name__ == "__main__":
    main()