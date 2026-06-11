import sys
import math
import random
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

TRANSLATIONS = {
    "en": {
        "title": "Minecraft Clone",
        "new_game": "New Game",
        "settings": "Settings",
        "exit": "Exit",
        "language": "Language",
        "theme": "Theme",
        "light": "Light",
        "dark": "Dark",
        "back": "Back",
        "blocks": "Blocks",
        "grass": "Grass",
        "dirt": "Dirt",
        "stone": "Stone",
        "wood": "Wood",
        "sand": "Sand",
        "water": "Water",
        "score": "Score",
        "position": "Position",
        "controls": "Controls",
        "wasd_move": "WASD: Move",
        "space_jump": "Space: Jump",
        "left_click": "Left Click: Break",
        "right_click": "Right Click: Place",
        "esc_menu": "ESC: Menu",
        "resume": "Resume",
        "save": "Save",
        "load": "Load",
        "inventory": "Inventory",
        "health": "Health",
        "hunger": "Hunger",
        "selected": "Selected",
        "game_paused": "Game Paused",
        "welcome": "Welcome to Minecraft Clone",
        "play": "Play",
        "options": "Options",
        "controls_title": "Controls",
        "mouse_look": "Mouse: Look Around",
        "scroll_select": "Scroll: Select Block",
        "fps": "FPS",
        "day_night": "Day/Night",
        "time": "Time",
        "seed": "World Seed",
        "generate": "Generate World",
        "world_size": "World Size",
        "small": "Small",
        "medium": "Medium",
        "large": "Large",
    },
    "zh": {
        "title": "我的世界克隆",
        "new_game": "新游戏",
        "settings": "设置",
        "exit": "退出",
        "language": "语言",
        "theme": "主题",
        "light": "浅色",
        "dark": "深色",
        "back": "返回",
        "blocks": "方块",
        "grass": "草地",
        "dirt": "泥土",
        "stone": "石头",
        "wood": "木头",
        "sand": "沙子",
        "water": "水",
        "score": "分数",
        "position": "位置",
        "controls": "控制",
        "wasd_move": "WASD: 移动",
        "space_jump": "空格: 跳跃",
        "left_click": "左键: 破坏",
        "right_click": "右键: 放置",
        "esc_menu": "ESC: 菜单",
        "resume": "继续",
        "save": "保存",
        "load": "加载",
        "inventory": "背包",
        "health": "生命值",
        "hunger": "饥饿值",
        "selected": "已选择",
        "game_paused": "游戏暂停",
        "welcome": "欢迎来到我的世界克隆",
        "play": "开始游戏",
        "options": "选项",
        "controls_title": "控制说明",
        "mouse_look": "鼠标: 环顾四周",
        "scroll_select": "滚轮: 选择方块",
        "fps": "帧率",
        "day_night": "昼夜",
        "time": "时间",
        "seed": "世界种子",
        "generate": "生成世界",
        "world_size": "世界大小",
        "small": "小",
        "medium": "中",
        "large": "大",
    },
    "fa": {
        "title": "کلون ماین‌کرافت",
        "new_game": "بازی جدید",
        "settings": "تنظیمات",
        "exit": "خروج",
        "language": "زبان",
        "theme": "تم",
        "light": "روشن",
        "dark": "تاریک",
        "back": "برگشت",
        "blocks": "بلوک‌ها",
        "grass": "چمن",
        "dirt": "خاک",
        "stone": "سنگ",
        "wood": "چوب",
        "sand": "شن",
        "water": "آب",
        "score": "امتیاز",
        "position": "موقعیت",
        "controls": "کنترل‌ها",
        "wasd_move": "WASD: حرکت",
        "space_jump": "فاصله: پرش",
        "left_click": "کلیک چپ: شکستن",
        "right_click": "کلیک راست: قرار دادن",
        "esc_menu": "ESC: منو",
        "resume": "ادامه",
        "save": "ذخیره",
        "load": "بارگذاری",
        "inventory": "کوله‌پشتی",
        "health": "سلامتی",
        "hunger": "گرسنگی",
        "selected": "انتخاب شده",
        "game_paused": "بازی متوقف شد",
        "welcome": "خوش آمدید به کلون ماین‌کرافت",
        "play": "بازی",
        "options": "گزینه‌ها",
        "controls_title": "کنترل‌ها",
        "mouse_look": "ماوس: نگاه کردن",
        "scroll_select": "اسکرول: انتخاب بلوک",
        "fps": "فریم",
        "day_night": "روز/شب",
        "time": "زمان",
        "seed": "دانه دنیا",
        "generate": "تولید دنیا",
        "world_size": "اندازه دنیا",
        "small": "کوچک",
        "medium": "متوسط",
        "large": "بزرگ",
    }
}

THEMES = {
    "dark": {
        "bg": "#1a1a2e",
        "bg2": "#16213e",
        "bg3": "#0f3460",
        "accent": "#e94560",
        "accent2": "#533483",
        "text": "#eaeaea",
        "text2": "#a8a8b3",
        "border": "#2d2d44",
        "button_bg": "#16213e",
        "button_hover": "#e94560",
        "button_text": "#eaeaea",
        "panel": "#0d0d1a",
        "panel2": "#1a1a2e",
        "sky_top": "#0a0a1a",
        "sky_bottom": "#1a1a3e",
        "ground": "#2d5a1b",
        "sidebar": "#0d0d1a",
        "card": "#1a1a2e",
        "card_border": "#2d2d44",
        "progress_bg": "#0d0d1a",
        "progress_fill": "#e94560",
        "hotbar": "#000000aa",
        "selected_slot": "#e94560",
    },
    "light": {
        "bg": "#e8f4f8",
        "bg2": "#d0e8f0",
        "bg3": "#b8d8e8",
        "accent": "#2196F3",
        "accent2": "#4CAF50",
        "text": "#1a1a2e",
        "text2": "#4a4a6e",
        "border": "#b0c4d8",
        "button_bg": "#ffffff",
        "button_hover": "#2196F3",
        "button_text": "#1a1a2e",
        "panel": "#f0f8ff",
        "panel2": "#e8f4f8",
        "sky_top": "#87CEEB",
        "sky_bottom": "#b0e0ff",
        "ground": "#4a8c2a",
        "sidebar": "#f0f8ff",
        "card": "#ffffff",
        "card_border": "#b0c4d8",
        "progress_bg": "#d0e8f0",
        "progress_fill": "#2196F3",
        "hotbar": "#ffffffaa",
        "selected_slot": "#2196F3",
    }
}

BLOCK_COLORS = {
    "grass": {"top": "#4CAF50", "side": "#8B6914", "bottom": "#8B6914"},
    "dirt": {"top": "#8B6914", "side": "#8B6914", "bottom": "#8B6914"},
    "stone": {"top": "#9E9E9E", "side": "#757575", "bottom": "#757575"},
    "wood": {"top": "#6D4C41", "side": "#8D6E63", "bottom": "#6D4C41"},
    "sand": {"top": "#F4E04D", "side": "#E6C84A", "bottom": "#E6C84A"},
    "water": {"top": "#1565C0", "side": "#0D47A1", "bottom": "#0D47A1"},
    "leaves": {"top": "#2E7D32", "side": "#388E3C", "bottom": "#2E7D32"},
    "brick": {"top": "#B71C1C", "side": "#C62828", "bottom": "#B71C1C"},
    "snow": {"top": "#FFFFFF", "side": "#ECEFF1", "bottom": "#ECEFF1"},
    "coal": {"top": "#37474F", "side": "#263238", "bottom": "#263238"},
}


class Block:
    def __init__(self, x, y, z, block_type="grass"):
        self.x = x
        self.y = y
        self.z = z
        self.type = block_type

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z


class World:
    def __init__(self, seed=42, size=20):
        self.blocks = {}
        self.seed = seed
        self.size = size
        self.generate(seed, size)

    def generate(self, seed, size):
        self.blocks = {}
        random.seed(seed)
        for x in range(-size, size):
            for z in range(-size, size):
                height = int(3 + 4 * math.sin(x * 0.3 + seed * 0.1) * math.cos(z * 0.3 + seed * 0.1) +
                             2 * random.uniform(0, 1))
                for y in range(0, height):
                    if y == height - 1:
                        btype = "grass"
                    elif y > height - 4:
                        btype = "dirt"
                    else:
                        btype = "stone"
                    self.blocks[(x, y, z)] = Block(x, y, z, btype)
                # Trees
                if random.random() < 0.03:
                    for ty in range(height, height + 4):
                        self.blocks[(x, ty, z)] = Block(x, ty, z, "wood")
                    for lx in range(x - 2, x + 3):
                        for lz in range(z - 2, z + 3):
                            for ly in range(height + 3, height + 6):
                                if (lx, ly, lz) not in self.blocks:
                                    self.blocks[(lx, ly, lz)] = Block(lx, ly, lz, "leaves")

    def get_block(self, x, y, z):
        return self.blocks.get((x, y, z))

    def add_block(self, x, y, z, btype):
        self.blocks[(x, y, z)] = Block(x, y, z, btype)

    def remove_block(self, x, y, z):
        if (x, y, z) in self.blocks:
            del self.blocks[(x, y, z)]


class Camera:
    def __init__(self):
        self.x = 0.0
        self.y = 8.0
        self.z = 0.0
        self.yaw = 0.0
        self.pitch = 0.0
        self.speed = 0.15
        self.sensitivity = 0.3

    def get_direction(self):
        yr = math.radians(self.yaw)
        pr = math.radians(self.pitch)
        dx = math.cos(pr) * math.sin(yr)
        dy = math.sin(pr)
        dz = math.cos(pr) * math.cos(yr)
        return dx, dy, dz

    def get_right(self):
        yr = math.radians(self.yaw)
        return math.cos(yr), 0, -math.sin(yr)


class GameRenderer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.world = None
        self.camera = Camera()
        self.theme = "dark"
        self.lang = "en"
        self.keys = set()
        self.mouse_captured = False
        self.last_mouse = QPoint()
        self.selected_block = 0
        self.block_types = list(BLOCK_COLORS.keys())
        self.health = 100
        self.hunger = 100
        self.score = 0
        self.fps = 60
        self.frame_count = 0
        self.day_time = 0.0
        self.paused = False
        self.inventory_open = False
        self.fps_timer = QElapsedTimer()
        self.fps_timer.start()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setMouseTracking(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(16)
        self.render_distance = 8
        self.vertical_velocity = 0.0
        self.on_ground = False
        self.highlighted_block = None
        self.setMinimumSize(400, 300)

    def set_world(self, world):
        self.world = world

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def update_game(self):
        if self.paused or not self.world:
            return
        self.day_time = (self.day_time + 0.002) % 1.0
        self.handle_movement()
        self.apply_gravity()
        self.frame_count += 1
        elapsed = self.fps_timer.elapsed()
        if elapsed >= 1000:
            self.fps = int(self.frame_count * 1000 / elapsed)
            self.frame_count = 0
            self.fps_timer.restart()
        self.update()

    def handle_movement(self):
        dx, _, dz = self.camera.get_direction()
        rx, _, rz = self.camera.get_right()
        move_x, move_z = 0, 0
        if Qt.Key.Key_W in self.keys:
            move_x += dx * self.camera.speed
            move_z += dz * self.camera.speed
        if Qt.Key.Key_S in self.keys:
            move_x -= dx * self.camera.speed
            move_z -= dz * self.camera.speed
        if Qt.Key.Key_A in self.keys:
            move_x -= rx * self.camera.speed
            move_z -= rz * self.camera.speed
        if Qt.Key.Key_D in self.keys:
            move_x += rx * self.camera.speed
            move_z += rz * self.camera.speed
        if Qt.Key.Key_Space in self.keys and self.on_ground:
            self.vertical_velocity = 0.25
            self.on_ground = False
        self.camera.x += move_x
        self.camera.z += move_z

    def apply_gravity(self):
        self.vertical_velocity -= 0.015
        self.camera.y += self.vertical_velocity
        gx = int(round(self.camera.x))
        gy = int(self.camera.y) - 1
        gz = int(round(self.camera.z))
        ground_y = 0
        for ty in range(12, -1, -1):
            if self.world.get_block(gx, ty, gz):
                ground_y = ty + 1
                break
        if self.camera.y <= ground_y + 1.8:
            self.camera.y = ground_y + 1.8
            self.vertical_velocity = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def project_point(self, x, y, z, w, h):
        cx, cy, cz = self.camera.x, self.camera.y, self.camera.z
        rx = x - cx
        ry = y - cy
        rz = z - cz
        yr = math.radians(self.camera.yaw)
        pr = math.radians(self.camera.pitch)
        cos_y = math.cos(-yr)
        sin_y = math.sin(-yr)
        tx = rx * cos_y - rz * sin_y
        tz = rx * sin_y + rz * cos_y
        cos_p = math.cos(-pr)
        sin_p = math.sin(-pr)
        ty = ry * cos_p - tz * sin_p
        tz2 = ry * sin_p + tz * cos_p
        if tz2 < 0.3:
            return None
        fov = 1.2
        sx = int(w / 2 + (tx / tz2) * fov * w / 2)
        sy = int(h / 2 - (ty / tz2) * fov * h / 2)
        return sx, sy, tz2

    def draw_block(self, painter, block, w, h, highlight=False):
        x, y, z = block.x, block.y, block.z
        colors = BLOCK_COLORS.get(block.type, BLOCK_COLORS["stone"])

        corners = [
            (x - 0.5, y - 0.5, z - 0.5),
            (x + 0.5, y - 0.5, z - 0.5),
            (x + 0.5, y + 0.5, z - 0.5),
            (x - 0.5, y + 0.5, z - 0.5),
            (x - 0.5, y - 0.5, z + 0.5),
            (x + 0.5, y - 0.5, z + 0.5),
            (x + 0.5, y + 0.5, z + 0.5),
            (x - 0.5, y + 0.5, z + 0.5),
        ]

        proj = []
        for cx, cy, cz in corners:
            p = self.project_point(cx, cy, cz, w, h)
            proj.append(p)

        if any(p is None for p in proj):
            return

        faces = [
            ([0, 1, 2, 3], colors["side"], 0.7),
            ([4, 5, 6, 7], colors["side"], 0.8),
            ([0, 4, 7, 3], colors["side"], 0.6),
            ([1, 5, 6, 2], colors["side"], 0.9),
            ([3, 2, 6, 7], colors["top"], 1.0),
            ([0, 1, 5, 4], colors["bottom"], 0.5),
        ]

        cx_cam = self.camera.x
        cy_cam = self.camera.y
        cz_cam = self.camera.z

        face_normals = [
            (0, 0, -1), (0, 0, 1),
            (-1, 0, 0), (1, 0, 0),
            (0, 1, 0), (0, -1, 0)
        ]

        day_brightness = 0.5 + 0.5 * math.sin(math.pi * self.day_time * 2 - math.pi / 2)

        for i, (indices, color_hex, brightness) in enumerate(faces):
            nx, ny, nz = face_normals[i]
            dot = (cx_cam - x) * nx + (cy_cam - y) * ny + (cz_cam - z) * nz
            if dot <= 0:
                continue

            face_proj = [proj[idx] for idx in indices]
            if any(p is None for p in face_proj):
                continue

            poly = QPolygon([QPoint(p[0], p[1]) for p in face_proj])

            base_color = QColor(color_hex)
            r = int(base_color.red() * brightness * day_brightness)
            g = int(base_color.green() * brightness * day_brightness)
            b = int(base_color.blue() * brightness * day_brightness)
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))

            if highlight:
                r = min(255, r + 60)
                g = min(255, g + 60)
                b = min(255, b + 60)

            painter.setBrush(QBrush(QColor(r, g, b)))
            if highlight:
                painter.setPen(QPen(QColor(255, 255, 0), 2))
            else:
                painter.setPen(QPen(QColor(max(0, r - 30), max(0, g - 30), max(0, b - 30)), 1))
            painter.drawPolygon(poly)

    def get_visible_blocks(self, w, h):
        if not self.world:
            return []
        visible = []
        cx = self.camera.x
        cy = self.camera.y
        cz = self.camera.z
        rd = self.render_distance

        dx_dir, _, dz_dir = self.camera.get_direction()

        for (bx, by, bz), block in self.world.blocks.items():
            dist = math.sqrt((bx - cx) ** 2 + (by - cy) ** 2 + (bz - cz) ** 2)
            if dist > rd:
                continue

            dot = (bx - cx) * dx_dir + (bz - cz) * dz_dir
            if dist > 2 and dot < -1:
                continue

            visible.append((dist, block))

        visible.sort(key=lambda x: x[0], reverse=True)
        return [b for _, b in visible]

    def get_highlighted_block(self):
        if not self.world:
            return None
        dx, dy, dz = self.camera.get_direction()
        cx, cy, cz = self.camera.x, self.camera.y, self.camera.z
        for step in range(1, 20):
            t = step * 0.25
            tx = int(round(cx + dx * t))
            ty = int(round(cy + dy * t))
            tz = int(round(cz + dz * t))
            block = self.world.get_block(tx, ty, tz)
            if block:
                return block
        return None

    def get_sky_color(self):
        t = self.theme
        day_val = 0.5 + 0.5 * math.sin(math.pi * self.day_time * 2 - math.pi / 2)
        if t == "dark":
            r = int(10 + 30 * day_val)
            g = int(10 + 20 * day_val)
            b = int(26 + 60 * day_val)
        else:
            r = int(100 + 135 * day_val)
            g = int(170 + 56 * day_val)
            b = int(200 + 55 * day_val)
        return QColor(r, g, b)

    def paintEvent(self, event):
        w = self.width()
        h = self.height()
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        sky_color = self.get_sky_color()
        painter.fillRect(0, 0, w, h, sky_color)

        grad = QLinearGradient(0, h // 2, 0, h)
        tc = THEMES[self.theme]
        grad.setColorAt(0, QColor(tc["ground"]))
        grad.setColorAt(1, QColor("#2d1a0a"))
        painter.fillRect(0, h // 2, w, h // 2, QBrush(grad))

        if self.world:
            visible = self.get_visible_blocks(w, h)
            self.highlighted_block = self.get_highlighted_block()
            for block in visible:
                is_highlight = (self.highlighted_block and
                                block.x == self.highlighted_block.x and
                                block.y == self.highlighted_block.y and
                                block.z == self.highlighted_block.z)
                self.draw_block(painter, block, w, h, is_highlight)

        self.draw_hud(painter, w, h)

        if self.paused:
            self.draw_pause_overlay(painter, w, h)

        if self.inventory_open:
            self.draw_inventory(painter, w, h)

        painter.end()

    def draw_hud(self, painter, w, h):
        tc = THEMES[self.theme]
        painter.setFont(QFont("Arial", max(10, w // 80)))

        # Crosshair
        cx, cy = w // 2, h // 2
        cs = max(8, w // 60)
        painter.setPen(QPen(QColor(255, 255, 255, 200), 2))
        painter.drawLine(cx - cs, cy, cx + cs, cy)
        painter.drawLine(cx, cy - cs, cx, cy + cs)

        # Hotbar
        slot_size = max(40, min(60, w // 14))
        num_slots = min(9, len(self.block_types))
        bar_w = num_slots * (slot_size + 4) + 4
        bar_x = (w - bar_w) // 2
        bar_y = h - slot_size - 16

        bar_bg = QColor(tc["hotbar"])
        painter.setBrush(QBrush(bar_bg))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(bar_x - 4, bar_y - 4, bar_w + 8, slot_size + 16, 8, 8)

        for i in range(num_slots):
            sx = bar_x + i * (slot_size + 4)
            sy = bar_y
            if i == self.selected_block:
                painter.setBrush(QBrush(QColor(tc["selected_slot"])))
                painter.setPen(QPen(QColor(255, 255, 255), 2))
            else:
                painter.setBrush(QBrush(QColor(0, 0, 0, 100)))
                painter.setPen(QPen(QColor(150, 150, 150), 1))
            painter.drawRoundedRect(sx, sy, slot_size, slot_size, 4, 4)

            btype = self.block_types[i]
            bc = BLOCK_COLORS.get(btype, BLOCK_COLORS["stone"])
            block_color = QColor(bc["top"])
            block_inner = slot_size - 12
            bi_x = sx + 6
            bi_y = sy + 6
            painter.setBrush(QBrush(block_color))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(bi_x, bi_y, block_inner, block_inner)

            # 3D effect
            side_color = QColor(bc["side"])
            offset = max(4, slot_size // 10)
            side_poly = QPolygon([
                QPoint(bi_x + block_inner, bi_y),
                QPoint(bi_x + block_inner + offset, bi_y - offset),
                QPoint(bi_x + block_inner + offset, bi_y + block_inner - offset),
                QPoint(bi_x + block_inner, bi_y + block_inner),
            ])
            painter.setBrush(QBrush(side_color))
            painter.drawPolygon(side_poly)
            top_poly = QPolygon([
                QPoint(bi_x, bi_y),
                QPoint(bi_x + offset, bi_y - offset),
                QPoint(bi_x + block_inner + offset, bi_y - offset),
                QPoint(bi_x + block_inner, bi_y),
            ])
            painter.setBrush(QBrush(block_color.lighter(120)))
            painter.drawPolygon(top_poly)

        # Info panel
        font_size = max(9, w // 90)
        painter.setFont(QFont("Arial", font_size))
        info_bg = QColor(0, 0, 0, 140)
        painter.setBrush(QBrush(info_bg))
        painter.setPen(Qt.PenStyle.NoPen)
        panel_w = max(160, w // 5)
        painter.drawRoundedRect(8, 8, panel_w, 100, 6, 6)

        painter.setPen(QPen(QColor(255, 255, 255)))
        painter.drawText(16, 26, f"{self.t('fps')}: {self.fps}")
        painter.drawText(16, 46, f"X:{self.camera.x:.1f} Y:{self.camera.y:.1f} Z:{self.camera.z:.1f}")
        painter.drawText(16, 66, f"{self.t('selected')}: {self.block_types[self.selected_block]}")

        day_pct = int(self.day_time * 100)
        painter.drawText(16, 86, f"{self.t('day_night')}: {day_pct}%")

        # Health & Hunger bars
        bar_panel_y = h - slot_size - 80
        bar_panel_w = max(160, w // 4)
        bar_panel_x = 10
        painter.setBrush(QBrush(QColor(0, 0, 0, 140)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(bar_panel_x, bar_panel_y, bar_panel_w, 60, 6, 6)

        bar_w_full = bar_panel_w - 20
        bh = max(10, h // 40)

        # Health bar
        painter.drawText(bar_panel_x + 10, bar_panel_y + 18,
                         f"{'❤' if self.health > 30 else '💔'} {self.t('health')}: {self.health}%")
        painter.setBrush(QBrush(QColor(50, 50, 50)))
        painter.drawRoundedRect(bar_panel_x + 10, bar_panel_y + 22, bar_w_full, bh, 3, 3)
        painter.setBrush(QBrush(QColor(220, 50, 50)))
        painter.drawRoundedRect(bar_panel_x + 10, bar_panel_y + 22,
                                int(bar_w_full * self.health / 100), bh, 3, 3)

        # Hunger bar
        painter.setPen(QPen(QColor(255, 255, 255)))
        painter.drawText(bar_panel_x + 10, bar_panel_y + 42,
                         f"🍖 {self.t('hunger')}: {self.hunger}%")
        painter.setBrush(QBrush(QColor(50, 50, 50)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(bar_panel_x + 10, bar_panel_y + 46, bar_w_full, bh, 3, 3)
        painter.setBrush(QBrush(QColor(220, 140, 30)))
        painter.drawRoundedRect(bar_panel_x + 10, bar_panel_y + 46,
                                int(bar_w_full * self.hunger / 100), bh, 3, 3)

        # Controls hint (bottom right)
        painter.setFont(QFont("Arial", max(8, w // 100)))
        painter.setPen(QPen(QColor(200, 200, 200, 180)))
        hints = [self.t("wasd_move"), self.t("space_jump"), self.t("left_click"),
                 self.t("right_click"), self.t("esc_menu")]
        hint_bg_w = max(120, w // 6)
        hint_bg_h = len(hints) * 16 + 10
        hint_x = w - hint_bg_w - 10
        hint_y = 8
        painter.setBrush(QBrush(QColor(0, 0, 0, 120)))
        painter.drawRoundedRect(hint_x, hint_y, hint_bg_w, hint_bg_h, 6, 6)
        for i, hint in enumerate(hints):
            painter.setPen(QPen(QColor(200, 200, 200)))
            painter.drawText(hint_x + 8, hint_y + 20 + i * 16, hint)

    def draw_pause_overlay(self, painter, w, h):
        tc = THEMES[self.theme]
        painter.setBrush(QBrush(QColor(0, 0, 0, 160)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(0, 0, w, h)
        font = QFont("Arial", max(16, w // 30), QFont.Weight.Bold)
        painter.setFont(font)
        painter.setPen(QPen(QColor(tc["accent"])))
        text = self.t("game_paused")
        fm = QFontMetrics(font)
        tw = fm.horizontalAdvance(text)
        painter.drawText((w - tw) // 2, h // 2 - 20, text)

    def draw_inventory(self, painter, w, h):
        tc = THEMES[self.theme]
        iw = min(400, w - 40)
        ih = min(300, h - 40)
        ix = (w - iw) // 2
        iy = (h - ih) // 2

        painter.setBrush(QBrush(QColor(tc["panel"])))
        painter.setPen(QPen(QColor(tc["border"]), 2))
        painter.drawRoundedRect(ix, iy, iw, ih, 12, 12)

        font = QFont("Arial", max(12, w // 60), QFont.Weight.Bold)
        painter.setFont(font)
        painter.setPen(QPen(QColor(tc["text"])))
        painter.drawText(ix + 20, iy + 35, self.t("inventory"))

        slot_size = min(50, (iw - 40) // 10)
        for i, btype in enumerate(self.block_types):
            col = i % 9
            row = i // 9
            sx = ix + 20 + col * (slot_size + 4)
            sy = iy + 60 + row * (slot_size + 4)
            if i == self.selected_block:
                painter.setBrush(QBrush(QColor(tc["accent"])))
            else:
                painter.setBrush(QBrush(QColor(tc["card"])))
            painter.setPen(QPen(QColor(tc["card_border"]), 1))
            painter.drawRoundedRect(sx, sy, slot_size, slot_size, 4, 4)
            bc = BLOCK_COLORS.get(btype, BLOCK_COLORS["stone"])
            painter.setBrush(QBrush(QColor(bc["top"])))
            painter.setPen(Qt.PenStyle.NoPen)
            inner = slot_size - 10
            painter.drawRect(sx + 5, sy + 5, inner, inner)

    def keyPressEvent(self, event):
        self.keys.add(event.key())
        if event.key() == Qt.Key.Key_Escape:
            self.paused = not self.paused
            if self.paused:
                self.mouse_captured = False
                self.setCursor(Qt.CursorShape.ArrowCursor)
        if event.key() == Qt.Key.Key_E:
            self.inventory_open = not self.inventory_open
        if event.key() == Qt.Key.Key_1:
            self.selected_block = 0
        if event.key() == Qt.Key.Key_2 and len(self.block_types) > 1:
            self.selected_block = 1
        if event.key() == Qt.Key.Key_3 and len(self.block_types) > 2:
            self.selected_block = 2
        if event.key() == Qt.Key.Key_4 and len(self.block_types) > 3:
            self.selected_block = 3

    def keyReleaseEvent(self, event):
        self.keys.discard(event.key())

    def mousePressEvent(self, event):
        if not self.paused and not self.inventory_open:
            if not self.mouse_captured:
                self.mouse_captured = True
                self.setCursor(Qt.CursorShape.BlankCursor)
                self.last_mouse = self.mapToGlobal(QPoint(self.width() // 2, self.height() // 2))
                QCursor.setPos(self.last_mouse)
                return

            if event.button() == Qt.MouseButton.LeftButton:
                if self.highlighted_block:
                    self.world.remove_block(
                        self.highlighted_block.x,
                        self.highlighted_block.y,
                        self.highlighted_block.z
                    )
                    self.score += 10

            elif event.button() == Qt.MouseButton.RightButton:
                if self.highlighted_block:
                    hb = self.highlighted_block
                    btype = self.block_types[self.selected_block]
                    dx, dy, dz = self.camera.get_direction()
                    nx = hb.x - int(round(dx))
                    ny = hb.y - int(round(dy))
                    nz = hb.z - int(round(dz))
                    if not self.world.get_block(nx, ny, nz):
                        self.world.add_block(nx, ny, nz, btype)
                        self.score += 5

    def mouseMoveEvent(self, event):
        if self.mouse_captured and not self.paused:
            global_pos = self.mapToGlobal(event.pos())
            center = self.mapToGlobal(QPoint(self.width() // 2, self.height() // 2))
            dx = global_pos.x() - center.x()
            dy = global_pos.y() - center.y()
            self.camera.yaw += dx * self.camera.sensitivity
            self.camera.pitch -= dy * self.camera.sensitivity
            self.camera.pitch = max(-89, min(89, self.camera.pitch))
            QCursor.setPos(center)

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        if delta > 0:
            self.selected_block = (self.selected_block - 1) % len(self.block_types)
        else:
            self.selected_block = (self.selected_block + 1) % len(self.block_types)


class MainMenuWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.lang = "en"
        self.anim_offset = 0.0
        self.anim_timer = QTimer(self)
        self.anim_timer.timeout.connect(self.animate)
        self.anim_timer.start(30)
        self.on_new_game = None
        self.on_settings = None
        self.on_exit = None
        self.setup_ui()

    def animate(self):
        self.anim_offset += 0.02
        self.update()

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def setup_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

    def create_button(self, text):
        btn = QPushButton(text)
        btn.setMinimumHeight(50)
        btn.setMinimumWidth(220)
        btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        btn.setMaximumWidth(350)
        self.apply_button_style(btn)
        return btn

    def apply_button_style(self, btn):
        tc = THEMES[self.theme]
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {tc['button_bg']};
                color: {tc['button_text']};
                border: 2px solid {tc['accent']};
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
            }}
            QPushButton:hover {{
                background-color: {tc['button_hover']};
                color: white;
                border: 2px solid {tc['accent2']};
            }}
            QPushButton:pressed {{
                background-color: {tc['accent2']};
            }}
        """)

    def refresh_buttons(self):
        tc = THEMES[self.theme]
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.spacerItem():
                pass

        self.main_layout.addStretch(2)

        title_label = QLabel(self.t("welcome"))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(f"""
            color: {tc['accent']};
            font-size: clamp(18px, 3vw, 32px);
            font-weight: bold;
            padding: 10px;
            background: transparent;
        """)
        title_label.setFont(QFont("Arial", 26, QFont.Weight.Bold))
        self.main_layout.addWidget(title_label)
        self.main_layout.addSpacing(30)

        btn_play = self.create_button(self.t("play"))
        btn_settings = self.create_button(self.t("settings"))
        btn_exit = self.create_button(self.t("exit"))

        for btn in [btn_play, btn_settings, btn_exit]:
            wrapper = QHBoxLayout()
            wrapper.addStretch()
            wrapper.addWidget(btn)
            wrapper.addStretch()
            self.main_layout.addLayout(wrapper)
            self.main_layout.addSpacing(12)

        self.main_layout.addStretch(2)

        if self.on_new_game:
            btn_play.clicked.connect(self.on_new_game)
        if self.on_settings:
            btn_settings.clicked.connect(self.on_settings)
        if self.on_exit:
            btn_exit.clicked.connect(self.on_exit)

    def paintEvent(self, event):
        w = self.width()
        h = self.height()
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        tc = THEMES[self.theme]

        grad = QLinearGradient(0, 0, 0, h)
        grad.setColorAt(0, QColor(tc["bg"]))
        grad.setColorAt(1, QColor(tc["bg2"]))
        painter.fillRect(0, 0, w, h, QBrush(grad))

        # Animated background blocks
        for i in range(20):
            bx = (i * 80 + int(self.anim_offset * 30) % w) % w
            by = int(h * 0.6 + 20 * math.sin(i * 0.5 + self.anim_offset))
            bs = int(30 + 10 * math.sin(i * 0.3 + self.anim_offset * 0.5))
            alpha = int(80 + 60 * math.sin(i * 0.4 + self.anim_offset))
            btypes = list(BLOCK_COLORS.keys())
            btype = btypes[i % len(btypes)]
            bc = BLOCK_COLORS[btype]
            c = QColor(bc["top"])
            c.setAlpha(alpha)
            painter.setBrush(QBrush(c))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(bx, by, bs, bs)

        painter.end()

    def apply_theme(self):
        tc = THEMES[self.theme]
        self.setStyleSheet(f"background: transparent;")
        self.refresh_buttons()


class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.lang = "en"
        self.on_back = None
        self.on_theme_change = None
        self.on_lang_change = None
        self.setup_ui()

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def setup_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().setSpacing(0)
        self.layout().setContentsMargins(20, 20, 20, 20)
        self.refresh_ui()

    def refresh_ui(self):
        tc = THEMES[self.theme]
        while self.layout().count():
            item = self.layout().takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.setStyleSheet(f"""
            QWidget {{ background-color: {tc['bg']}; }}
            QLabel {{ color: {tc['text']}; background: transparent; }}
            QComboBox {{
                background-color: {tc['button_bg']};
                color: {tc['text']};
                border: 2px solid {tc['accent']};
                border-radius: 8px;
                padding: 8px 15px;
                font-size: 14px;
                min-width: 150px;
            }}
            QComboBox::drop-down {{
                border: none;
            }}
            QComboBox QAbstractItemView {{
                background-color: {tc['panel']};
                color: {tc['text']};
                border: 1px solid {tc['border']};
                selection-background-color: {tc['accent']};
            }}
        """)

        main_widget = QWidget()
        main_widget.setMaximumWidth(500)
        main_widget.setStyleSheet("background: transparent;")
        vbox = QVBoxLayout(main_widget)
        vbox.setSpacing(20)

        title = QLabel(self.t("settings"))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {tc['accent']}; background: transparent;")
        vbox.addWidget(title)
        vbox.addSpacing(20)

        # Card style settings
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {tc['card']};
                border: 1px solid {tc['card_border']};
                border-radius: 12px;
                padding: 10px;
            }}
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(15)

        # Theme
        theme_row = QHBoxLayout()
        theme_label = QLabel(self.t("theme"))
        theme_label.setFont(QFont("Arial", 14))
        theme_label.setStyleSheet(f"color: {tc['text']}; background: transparent;")
        self.theme_combo = QComboBox()
        self.theme_combo.addItem(self.t("dark"), "dark")
        self.theme_combo.addItem(self.t("light"), "light")
        self.theme_combo.setCurrentIndex(0 if self.theme == "dark" else 1)
        self.theme_combo.currentIndexChanged.connect(self.theme_changed)
        theme_row.addWidget(theme_label)
        theme_row.addStretch()
        theme_row.addWidget(self.theme_combo)
        card_layout.addLayout(theme_row)

        # Language
        lang_row = QHBoxLayout()
        lang_label = QLabel(self.t("language"))
        lang_label.setFont(QFont("Arial", 14))
        lang_label.setStyleSheet(f"color: {tc['text']}; background: transparent;")
        self.lang_combo = QComboBox()
        self.lang_combo.addItem("English", "en")
        self.lang_combo.addItem("中文", "zh")
        self.lang_combo.addItem("فارسی", "fa")
        langs = ["en", "zh", "fa"]
        self.lang_combo.setCurrentIndex(langs.index(self.lang) if self.lang in langs else 0)
        self.lang_combo.currentIndexChanged.connect(self.lang_changed)
        lang_row.addWidget(lang_label)
        lang_row.addStretch()
        lang_row.addWidget(self.lang_combo)
        card_layout.addLayout(lang_row)

        vbox.addWidget(card)

        # Controls info card
        ctrl_card = QFrame()
        ctrl_card.setStyleSheet(f"""
            QFrame {{
                background-color: {tc['card']};
                border: 1px solid {tc['card_border']};
                border-radius: 12px;
                padding: 10px;
            }}
        """)
        ctrl_layout = QVBoxLayout(ctrl_card)
        ctrl_title = QLabel(self.t("controls_title"))
        ctrl_title.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        ctrl_title.setStyleSheet(f"color: {tc['accent2']}; background: transparent;")
        ctrl_layout.addWidget(ctrl_title)

        ctrl_texts = [
            self.t("wasd_move"),
            self.t("space_jump"),
            self.t("mouse_look"),
            self.t("left_click"),
            self.t("right_click"),
            self.t("scroll_select"),
            self.t("esc_menu"),
        ]
        for ct in ctrl_texts:
            cl = QLabel(ct)
            cl.setFont(QFont("Arial", 12))
            cl.setStyleSheet(f"color: {tc['text2']}; background: transparent;")
            ctrl_layout.addWidget(cl)

        vbox.addWidget(ctrl_card)

        # Back button
        back_btn = QPushButton(self.t("back"))
        back_btn.setMinimumHeight(45)
        back_btn.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        back_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {tc['button_bg']};
                color: {tc['button_text']};
                border: 2px solid {tc['accent']};
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                padding: 8px 20px;
            }}
            QPushButton:hover {{
                background-color: {tc['button_hover']};
                color: white;
            }}
        """)
        if self.on_back:
            back_btn.clicked.connect(self.on_back)
        vbox.addWidget(back_btn)

        wrapper = QHBoxLayout()
        wrapper.addStretch()
        wrapper.addWidget(main_widget)
        wrapper.addStretch()
        self.layout().addStretch()
        self.layout().addLayout(wrapper)
        self.layout().addStretch()

    def theme_changed(self, index):
        new_theme = self.theme_combo.itemData(index)
        if self.on_theme_change:
            self.on_theme_change(new_theme)

    def lang_changed(self, index):
        new_lang = self.lang_combo.itemData(index)
        if self.on_lang_change:
            self.on_lang_change(new_lang)

    def paintEvent(self, event):
        tc = THEMES[self.theme]
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        grad = QLinearGradient(0, 0, self.width(), self.height())
        grad.setColorAt(0, QColor(tc["bg"]))
        grad.setColorAt(1, QColor(tc["bg2"]))
        painter.fillRect(0, 0, self.width(), self.height(), QBrush(grad))
        painter.end()


class PauseMenuWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.lang = "en"
        self.on_resume = None
        self.on_menu = None
        self.on_exit = None
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setup_ui()

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def setup_ui(self):
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.refresh_ui()

    def refresh_ui(self):
        tc = THEMES[self.theme]
        while self.layout().count():
            item = self.layout().takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.setStyleSheet("background: transparent;")

        panel = QFrame()
        panel.setMaximumWidth(300)
        panel.setStyleSheet(f"""
            QFrame {{
                background-color: {tc['panel']};
                border: 2px solid {tc['accent']};
                border-radius: 16px;
            }}
        """)
        pvbox = QVBoxLayout(panel)
        pvbox.setSpacing(12)
        pvbox.setContentsMargins(20, 20, 20, 20)

        title = QLabel(self.t("game_paused"))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {tc['accent']}; background: transparent; border: none;")
        pvbox.addWidget(title)

        btn_style = f"""
            QPushButton {{
                background-color: {tc['button_bg']};
                color: {tc['button_text']};
                border: 2px solid {tc['accent']};
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                padding: 8px;
                min-height: 40px;
            }}
            QPushButton:hover {{
                background-color: {tc['button_hover']};
                color: white;
            }}
        """

        resume_btn = QPushButton(self.t("resume"))
        resume_btn.setStyleSheet(btn_style)
        menu_btn = QPushButton("Main Menu")
        menu_btn.setStyleSheet(btn_style)
        exit_btn = QPushButton(self.t("exit"))
        exit_btn.setStyleSheet(btn_style)

        if self.on_resume:
            resume_btn.clicked.connect(self.on_resume)
        if self.on_menu:
            menu_btn.clicked.connect(self.on_menu)
        if self.on_exit:
            exit_btn.clicked.connect(self.on_exit)

        pvbox.addWidget(resume_btn)
        pvbox.addWidget(menu_btn)
        pvbox.addWidget(exit_btn)

        wrapper = QHBoxLayout()
        wrapper.addStretch()
        wrapper.addWidget(panel)
        wrapper.addStretch()

        self.layout().addStretch()
        self.layout().addLayout(wrapper)
        self.layout().addStretch()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(0, 0, 0, 140)))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(0, 0, self.width(), self.height())
        painter.end()


class WorldGenDialog(QDialog):
    def __init__(self, parent=None, theme="dark", lang="en"):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self.world_seed = 42
        self.world_size = 15
        self.setModal(True)
        self.setMinimumWidth(350)
        self.setup_ui()

    def t(self, key):
        return TRANSLATIONS[self.lang].get(key, key)

    def setup_ui(self):
        tc = THEMES[self.theme]
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {tc['bg']};
                border: 2px solid {tc['accent']};
                border-radius: 12px;
            }}
            QLabel {{
                color: {tc['text']};
                background: transparent;
            }}
            QLineEdit, QSpinBox, QComboBox {{
                background-color: {tc['button_bg']};
                color: {tc['text']};
                border: 2px solid {tc['accent']};
                border-radius: 6px;
                padding: 6px;
                font-size: 13px;
            }}
            QPushButton {{
                background-color: {tc['button_bg']};
                color: {tc['button_text']};
                border: 2px solid {tc['accent']};
                border-radius: 8px;
                font-size: 14px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {tc['button_hover']};
                color: white;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel(self.t("generate"))
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        seed_row = QHBoxLayout()
        seed_label = QLabel(self.t("seed"))
        self.seed_input = QSpinBox()
        self.seed_input.setRange(0, 99999)
        self.seed_input.setValue(42)
        seed_row.addWidget(seed_label)
        seed_row.addWidget(self.seed_input)
        layout.addLayout(seed_row)

        size_row = QHBoxLayout()
        size_label = QLabel(self.t("world_size"))
        self.size_combo = QComboBox()
        self.size_combo.addItem(self.t("small"), 10)
        self.size_combo.addItem(self.t("medium"), 15)
        self.size_combo.addItem(self.t("large"), 22)
        self.size_combo.setCurrentIndex(1)
        size_row.addWidget(size_label)
        size_row.addWidget(self.size_combo)
        layout.addLayout(size_row)

        btn_row = QHBoxLayout()
        ok_btn = QPushButton(self.t("generate"))
        cancel_btn = QPushButton(self.t("back"))
        ok_btn.clicked.connect(self.accept_gen)
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(ok_btn)
        btn_row.addWidget(cancel_btn)
        layout.addLayout(btn_row)

    def accept_gen(self):
        self.world_seed = self.seed_input.value()
        self.world_size = self.size_combo.currentData()
        self.accept()


class MinecraftApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme = "dark"
        self.lang = "en"
        self.world = None
        self.setWindowTitle("Minecraft Clone")
        self.setMinimumSize(640, 480)
        self.resize(1100, 700)

        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)

        self.main_menu = MainMenuWidget()
        self.settings_widget = SettingsWidget()

        self.game_container = QWidget()
        self.game_layout = QStackedLayout(self.game_container)
        self.game_renderer = GameRenderer()
        self.pause_menu = PauseMenuWidget()

        self.game_layout.addWidget(self.game_renderer)
        self.game_layout.addWidget(self.pause_menu)
        self.game_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self.pause_menu.hide()

        self.stacked.addWidget(self.main_menu)
        self.stacked.addWidget(self.settings_widget)
        self.stacked.addWidget(self.game_container)

        self.connect_signals()
        self.apply_theme()
        self.apply_lang()

        self.stacked.setCurrentWidget(self.main_menu)

        self.pause_check_timer = QTimer(self)
        self.pause_check_timer.timeout.connect(self.check_pause)
        self.pause_check_timer.start(50)

    def connect_signals(self):
        self.main_menu.on_new_game = self.start_game
        self.main_menu.on_settings = self.show_settings
        self.main_menu.on_exit = self.close

        self.settings_widget.on_back = self.show_main_menu
        self.settings_widget.on_theme_change = self.change_theme
        self.settings_widget.on_lang_change = self.change_lang

        self.pause_menu.on_resume = self.resume_game
        self.pause_menu.on_menu = self.show_main_menu
        self.pause_menu.on_exit = self.close

    def check_pause(self):
        if self.stacked.currentWidget() == self.game_container:
            if self.game_renderer.paused:
                self.pause_menu.show()
                self.pause_menu.raise_()
            else:
                self.pause_menu.hide()

    def start_game(self):
        dialog = WorldGenDialog(self, self.theme, self.lang)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            seed = dialog.world_seed
            size = dialog.world_size
            progress = QProgressDialog("Generating world...", None, 0, 0, self)
            progress.setWindowModality(Qt.WindowModality.WindowModal)
            progress.setMinimumDuration(0)
            progress.setValue(0)
            QApplication.processEvents()

            self.world = World(seed=seed, size=size)
            self.game_renderer.set_world(self.world)
            self.game_renderer.camera = Camera()
            self.game_renderer.paused = False
            self.game_renderer.score = 0
            self.game_renderer.health = 100
            self.game_renderer.hunger = 100
            self.game_renderer.mouse_captured = False
            progress.close()
            self.stacked.setCurrentWidget(self.game_container)
            self.game_renderer.setFocus()

    def show_settings(self):
        self.stacked.setCurrentWidget(self.settings_widget)

    def show_main_menu(self):
        if self.stacked.currentWidget() == self.game_container:
            self.game_renderer.paused = False
            self.game_renderer.mouse_captured = False
            self.game_renderer.setCursor(Qt.CursorShape.ArrowCursor)
        self.stacked.setCurrentWidget(self.main_menu)

    def resume_game(self):
        self.game_renderer.paused = False
        self.game_renderer.setFocus()

    def change_theme(self, theme):
        self.theme = theme
        self.game_renderer.theme = theme
        self.settings_widget.theme = theme
        self.pause_menu.theme = theme
        self.main_menu.theme = theme
        self.apply_theme()

    def change_lang(self, lang):
        self.lang = lang
        self.game_renderer.lang = lang
        self.settings_widget.lang = lang
        self.pause_menu.lang = lang
        self.main_menu.lang = lang
        self.apply_lang()

    def apply_theme(self):
        tc = THEMES[self.theme]
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {tc['bg']};
            }}
            QStackedWidget {{
                background-color: {tc['bg']};
            }}
        """)
        self.main_menu.theme = self.theme
        self.main_menu.apply_theme()
        self.settings_widget.theme = self.theme
        self.settings_widget.refresh_ui()
        self.pause_menu.theme = self.theme
        self.pause_menu.refresh_ui()

    def apply_lang(self):
        self.main_menu.lang = self.lang
        self.main_menu.refresh_buttons()
        self.settings_widget.lang = self.lang
        self.settings_widget.refresh_ui()
        self.pause_menu.lang = self.lang
        self.pause_menu.refresh_ui()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'pause_menu') and self.pause_menu:
            self.pause_menu.setGeometry(self.game_container.rect())

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Exit",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Minecraft Clone")
    app.setOrganizationName("GameStudio")

    font = QFont("Arial", 10)
    app.setFont(font)

    window = MinecraftApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
