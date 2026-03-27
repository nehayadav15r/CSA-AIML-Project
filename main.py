import pygame
import sys
from collections import deque
import heapq

pygame.init()

WIDTH = 620
GRID_SIZE = 600
ROWS = 25
PANEL_HEIGHT = WIDTH - GRID_SIZE  # 20px bottom strip (unused, panel is top)

WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("🧭 Pathfinding Visualizer")

clock = pygame.time.Clock()

# ── Colors ──────────────────────────────────────────────────────────────────
WHITE      = (245, 245, 250)
BLACK      = (30,  30,  40)
GREY       = (180, 180, 195)
DARK_GREY  = (100, 100, 115)
GREEN      = (72,  199, 116)   # start
RED        = (255, 82,  82)    # end
BLUE       = (66,  133, 244)   # final path
ORANGE     = (255, 183, 77)    # visited / frontier
PURPLE     = (171, 71,  188)   # wall
BG         = (20,  20,  30)    # window background
PANEL_BG   = (35,  35,  50)
HIGHLIGHT  = (255, 220, 50)


# ── Node ─────────────────────────────────────────────────────────────────────
class Node:
    def __init__(self, row, col, gap):
        self.row = row
        self.col = col
        self.x = col * gap          # x = horizontal = col  ← FIX
        self.y = row * gap          # y = vertical   = row  ← FIX
        self.color = WHITE
        self.gap = gap
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_wall(self):   return self.color == PURPLE
    def is_start(self):  return self.color == GREEN
    def is_end(self):    return self.color == RED

    def make_start(self):   self.color = GREEN
    def make_end(self):     self.color = RED
    def make_wall(self):    self.color = PURPLE
    def make_visited(self): self.color = ORANGE
    def make_path(self):    self.color = BLUE
    def reset(self):        self.color = WHITE

    def draw(self, win):
        pygame.draw.rect(win, self.color,
                         (self.x + 1, self.y + 1, self.gap - 1, self.gap - 1),
                         border_radius=2)

    def update_neighbors(self, grid):
        self.neighbors = []
        rows = len(grid)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in dirs:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < rows and 0 <= c < rows and not grid[r][c].is_wall():
                self.neighbors.append(grid[r][c])


# ── Grid helpers ─────────────────────────────────────────────────────────────
def make_grid(rows, width):
    gap = width // rows
    return [[Node(i, j, gap) for j in range(rows)] for i in range(rows)]


def draw_grid_lines(win, rows, width):
    gap = width // rows
    for i in range(rows + 1):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    mx, my = pos                    # pygame gives (x, y)
    col = mx // gap                 # x → col
    row = my // gap                 # y → row
    row = max(0, min(row, rows - 1))
    col = max(0, min(col, rows - 1))
    return row, col


# ── HUD / panel ──────────────────────────────────────────────────────────────
FONT_SM = pygame.font.SysFont("consolas", 14)
FONT_MD = pygame.font.SysFont("consolas", 17, bold=True)
FONT_LG = pygame.font.SysFont("consolas", 20, bold=True)

ALGO_NAMES = {pygame.K_b: "BFS", pygame.K_d: "DFS", pygame.K_a: "A*"}
ALGO_COLORS = {"BFS": (66, 200, 230), "DFS": (230, 120, 66), "A*": (120, 230, 66)}

def draw_hud(win, width, algo, status, step_count):
    # top bar
    bar_h = 22
    pygame.draw.rect(win, PANEL_BG, (0, 0, width, bar_h))

    algo_color = ALGO_COLORS.get(algo, HIGHLIGHT)
    label = f" [{algo}] " if algo else " [No algo] "
    surf = FONT_MD.render(label, True, algo_color)
    win.blit(surf, (6, 3))

    keys_txt = "LClick=Draw  RClick=Erase  B=BFS  D=DFS  A=A*  R=Reset"
    surf2 = FONT_SM.render(keys_txt, True, DARK_GREY)
    win.blit(surf2, (surf.get_width() + 12, 5))

    # status bottom bar
    bot_y = width - bar_h
    pygame.draw.rect(win, PANEL_BG, (0, bot_y, width, bar_h))
    status_surf = FONT_SM.render(f"  {status}   steps: {step_count}", True, HIGHLIGHT)
    win.blit(status_surf, (4, bot_y + 4))


HUD_TOP    = 22   # pixels reserved at top for panel
HUD_BOTTOM = 22   # pixels reserved at bottom


def full_draw(win, grid, rows, width, algo, status, step_count):
    win.fill(BG)
    # offset grid drawing downward by HUD_TOP
    surf = pygame.Surface((width, width))
    surf.fill(BG)
    for row in grid:
        for node in row:
            node.draw(surf)
    draw_grid_lines(surf, rows, width)
    win.blit(surf, (0, HUD_TOP))
    draw_hud(win, width, algo, status, step_count)
    pygame.display.flip()


# ── Algorithms ───────────────────────────────────────────────────────────────
def reconstruct_path(parent, current, start, end, draw_fn):
    path = []
    while current in parent:
        current = parent[current]
        if current is not start:
            path.append(current)
    for node in reversed(path):
        node.make_path()
        draw_fn()
    end.make_end()
    start.make_start()


def bfs(draw_fn, grid, start, end):
    queue = deque([start])
    parent = {}
    visited = {start}
    steps = 0
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        current = queue.popleft()
        steps += 1
        if current is end:
            reconstruct_path(parent, current, start, end, draw_fn)
            return True, steps
        for nb in current.neighbors:
            if nb not in visited:
                visited.add(nb)
                parent[nb] = current
                queue.append(nb)
                if nb is not end:
                    nb.make_visited()
        if steps % 3 == 0:
            draw_fn()
    return False, steps


def dfs(draw_fn, grid, start, end):
    stack = [start]
    parent = {}
    visited = {start}
    steps = 0
    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        current = stack.pop()
        steps += 1
        if current is end:
            reconstruct_path(parent, current, start, end, draw_fn)
            return True, steps
        for nb in current.neighbors:
            if nb not in visited:
                visited.add(nb)
                parent[nb] = current
                stack.append(nb)
                if nb is not end:
                    nb.make_visited()
        if steps % 3 == 0:
            draw_fn()
    return False, steps


def heuristic(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def astar(draw_fn, grid, start, end):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))
    parent = {}
    g = {node: float("inf") for row in grid for node in row}
    g[start] = 0
    open_hash = {start}
    steps = 0
    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        current = heapq.heappop(open_set)[2]
        open_hash.discard(current)
        steps += 1
        if current is end:
            reconstruct_path(parent, current, start, end, draw_fn)
            return True, steps
        for nb in current.neighbors:
            tentative = g[current] + 1
            if tentative < g[nb]:
                parent[nb] = current
                g[nb] = tentative
                f = tentative + heuristic(nb.get_pos(), end.get_pos())
                if nb not in open_hash:
                    count += 1
                    heapq.heappush(open_set, (f, count, nb))
                    open_hash.add(nb)
                    if nb is not end:
                        nb.make_visited()
        if steps % 3 == 0:
            draw_fn()
    return False, steps


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    grid = make_grid(ROWS, GRID_SIZE)
    start = end = None
    algo = ""
    status = "Click to place START, then END, then draw walls!"
    step_count = 0

    def draw_fn():
        full_draw(WIN, grid, ROWS, GRID_SIZE, algo, status, step_count)
        clock.tick(120)

    run = True
    while run:
        draw_fn()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # ── Mouse ──
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
                mx, my = pygame.mouse.get_pos()
                # grid starts at y=HUD_TOP
                if HUD_TOP <= my < GRID_SIZE + HUD_TOP:
                    adj_pos = (mx, my - HUD_TOP)
                    row, col = get_clicked_pos(adj_pos, ROWS, GRID_SIZE)
                    node = grid[row][col]

                    left, _, right = pygame.mouse.get_pressed()

                    if left:
                        if not start and node is not end:
                            start = node
                            start.make_start()
                            status = "Start placed! Now click to place END."
                        elif not end and node is not start:
                            end = node
                            end.make_end()
                            status = "End placed! Draw walls, then press B / D / A to run."
                        elif node is not start and node is not end:
                            node.make_wall()

                    if right:
                        node.reset()
                        if node is start:
                            start = None
                            status = "Start removed."
                        elif node is end:
                            end = None
                            status = "End removed."

            # ── Keyboard ──
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid = make_grid(ROWS, GRID_SIZE)
                    start = end = None
                    algo = ""
                    step_count = 0
                    status = "Grid reset! Place START and END."

                run_algo = None
                if event.key == pygame.K_b and start and end:
                    algo = "BFS";  run_algo = bfs
                elif event.key == pygame.K_d and start and end:
                    algo = "DFS";  run_algo = dfs
                elif event.key == pygame.K_a and start and end:
                    algo = "A*";   run_algo = astar

                if run_algo:
                    # clear previous search marks
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                            if node.color in (ORANGE, BLUE):
                                node.reset()
                    start.make_start(); end.make_end()
                    status = f"Running {algo}…"
                    draw_fn()
                    found, step_count = run_algo(draw_fn, grid, start, end)
                    status = (f"{algo} found path in {step_count} steps! 🎉"
                              if found else
                              f"{algo}: No path found 😢 ({step_count} steps)")

    pygame.quit()
    sys.exit()


main()
