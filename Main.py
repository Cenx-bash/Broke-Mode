#!/usr/bin/env python3
"""
I Wanna Be Yours — AM Style  |  Lyrics Player
Synced lyrics with smooth pre-typed animation — no visible delay.

Requirements:
    pip install pygame rich mutagen
"""

import os, sys, time, threading
import pygame
from mutagen.mp3 import MP3
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich.live import Live

# ── config ────────────────────────────────────────────────────────────
MUSIC_FILE    = "i_wanna_be_yours_style.mp3"
TYPING_SPEED  = 0.048
PRE_TYPE_SEC  = 1.5
REFRESH_HZ    = 30
CURSOR_BLINK  = 0.5

# ── colours ───────────────────────────────────────────────────────────
C_ACTIVE   = "bold #FFFFFF"
C_GLOW     = "bold #B8E8F5"
C_PAST     = "#3A6475"
C_FUTURE   = "#1C3340"
C_ACCENT   = "#7EC8E3"
C_DIM      = "#1A2E38"
C_SECTION  = f"bold {C_ACCENT}"
C_CURSOR   = "#7EC8E3"
C_BAR_FILL = "#7EC8E3"
C_BAR_EMPTY= "#1C3340"

console = Console()

# ── guards ────────────────────────────────────────────────────────────
if not os.path.exists(MUSIC_FILE):
    console.print(f"[red]Error:[/red] '{MUSIC_FILE}' not found.")
    sys.exit(1)

# ── pygame init ───────────────────────────────────────────────────────
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()
try:
    pygame.mixer.music.load(MUSIC_FILE)
except Exception as e:
    console.print(f"[red]Could not load {MUSIC_FILE}:[/red] {e}")
    sys.exit(1)

audio    = MP3(MUSIC_FILE)
duration = audio.info.length

# ── lyrics (AM-style vibe) ────────────────────────────────────────────
lyrics = [
    (10,  "✦ Verse 1"),
    (13,  "I wanna be your vacuum cleaner"),
    (17,  "Breathing in your dust, slow and quiet"),
    (22,  "I wanna be your morning coffee"),
    (26,  "Hot enough to keep you alive"),

    (32,  "✦ Verse 2"),
    (35,  "I wanna be your setting lotion"),
    (39,  "Hold your hair in deep devotion"),
    (44,  "At least as deep as the Pacific Ocean"),
    (49,  "I wanna be yours"),

    (55,  "✦ Chorus"),
    (58,  "Secrets I have held in my heart"),
    (63,  "Are harder to hide than I thought"),
    (68,  "Maybe I just wanna be yours"),
    (73,  "I wanna be yours"),

    (80,  "✦ Verse 3"),
    (83,  "Let me be your electric meter"),
    (87,  "I will never run out on you"),
    (92,  "Let me be your portable heater"),
    (96,  "You’ll get cold without me too"),

    (102, "✦ Outro"),
    (105, "Wanna be yours"),
    (109, "Wanna be yours"),
    (113, "Wanna be yours"),
]
lyrics.sort(key=lambda x: x[0])

# ── pre-typing engine ─────────────────────────────────────────────────
def chars_visible(idx: int, elapsed: float) -> int:
    ts, text = lyrics[idx]
    type_start = ts - PRE_TYPE_SEC
    if elapsed < type_start:
        return 0
    chars = int((elapsed - type_start) / TYPING_SPEED)
    return min(chars, len(text))

# ── progress bar ─────────────────────────────────────────────────────
def progress_bar(elapsed: float, width: int = 36) -> Text:
    pct   = min(elapsed / duration, 1.0)
    filled = int(pct * width)
    bar   = Text()
    bar.append("  ")
    bar.append("━" * filled,        style=C_BAR_FILL)
    bar.append("━" * (width-filled), style=C_BAR_EMPTY)
    bar.append(f"  {fmt_time(elapsed)} / {fmt_time(duration)}", style=f"dim {C_ACCENT}")
    return bar

def fmt_time(s: float) -> str:
    m   = int(s) // 60
    sec = int(s) % 60
    return f"{m}:{sec:02d}"

# ── blinking cursor ───────────────────────────────────────────────────
_cursor_visible = True
_cursor_lock    = threading.Lock()

def _blink_loop():
    global _cursor_visible
    while True:
        time.sleep(CURSOR_BLINK)
        with _cursor_lock:
            _cursor_visible = not _cursor_visible

threading.Thread(target=_blink_loop, daemon=True).start()

def get_cursor() -> str:
    with _cursor_lock:
        return "▌" if _cursor_visible else " "

# ── current lyric index ───────────────────────────────────────────────
def current_index(elapsed: float) -> int:
    idx = 0
    for i, (ts, _) in enumerate(lyrics):
        if elapsed >= ts - PRE_TYPE_SEC:
            idx = i
        else:
            break
    return idx

# ── render ────────────────────────────────────────────────────────────
def build_display(elapsed: float) -> Panel:
    active = current_index(elapsed)

    body = Text()
    body.append("\n")

    for i, (ts, text) in enumerate(lyrics):
        is_section = text.startswith("✦")
        n_vis      = chars_visible(i, elapsed)
        is_typing  = 0 < n_vis < len(text)
        is_done    = n_vis >= len(text)

        if i < active and is_done:
            if is_section:
                body.append(f"  {text}\n", style=f"dim {C_ACCENT}")
            else:
                body.append(f"  {text}\n", style=C_PAST)

        elif i == active or (i < active and not is_done):
            visible = text[:n_vis]
            cursor  = get_cursor() if is_typing else ""

            if is_section:
                body.append(f"\n  {visible}{cursor}\n", style=C_SECTION)
            else:
                body.append("\n  ❯ ", style=C_ACCENT)
                body.append(visible, style=C_GLOW)
                body.append(cursor,  style=C_CURSOR)
                body.append("\n")

        else:
            if is_section:
                body.append(f"\n  {text}\n", style=f"dim {C_DIM}")
            else:
                body.append(f"  {text}\n", style=C_FUTURE)

    body.append("\n")
    body.append(progress_bar(elapsed))
    body.append("\n")

    return Panel(
        body,
        title=f"[bold {C_ACCENT}]  I Wanna Be Yours  ·  AM-style  [/bold {C_ACCENT}]",
        border_style=C_ACCENT,
        padding=(0, 2),
    )

# ── main ──────────────────────────────────────────────────────────────
def run():
    console.clear()

    splash = Text()
    splash.append("\n\n  I Wanna Be Yours", style=f"bold {C_ACCENT}")
    splash.append("  ·  ", style="dim white")
    splash.append("AM Style\n\n", style="white")
    console.print(Align.center(splash))
    time.sleep(1.0)
    console.clear()

    pygame.mixer.music.play()
    start = time.time()

    try:
        with Live(
            console=console,
            refresh_per_second=REFRESH_HZ,
            screen=False,
            vertical_overflow="visible",
        ) as live:
            while pygame.mixer.music.get_busy():
                elapsed = time.time() - start
                live.update(build_display(elapsed))

    except KeyboardInterrupt:
        pass
    finally:
        pygame.mixer.music.stop()
        pygame.quit()

    console.print(f"\n  [bold {C_ACCENT}]♡  finished[/bold {C_ACCENT}]\n")

if __name__ == "__main__":
    run()
