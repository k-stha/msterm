#!/usr/bin/python3

"""A Simple Terminal Emulator based on VTE using GTK."""

import os
import sys

import gi

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
gi.require_version("Vte", "2.91")

from gi.repository import Gdk, Gtk, Pango, Vte


def return_help(script_name):
    """Return help text."""
    return (
        "Usage: "
        + script_name
        + " [OPTION...]\n\nOptions:\n"
        + "  -h, --help            Display this help and exit\n"
        + "  -e, --command <COMMAND>\n"
        + "                        Run COMMAND inside the terminal\n"
        + "  -T, -t, --title <TITLE>\n"
        + "                        Set the title of the window as TITLE\n"
        + "  -f, --font-size <SIZE>\n"
        + "                        Set the font size as SIZE"
    )


script_name = os.path.basename(sys.argv[0])
command = [os.environ.get("SHELL")]
system_commands = []
title = "msterm"
font_size = 12
display_help = return_help(script_name)

i = 1

while i < len(sys.argv):
    arg = sys.argv[i]

    if arg in {"-h", "--help"}:
        print(display_help)
        sys.exit()

    elif arg in {"-e", "--command"}:
        system_commands = sys.argv[i + 1]
        command.append("-c")
        command.append(system_commands)
        i += 1

    elif arg in {"-T", "-t", "--title"}:
        title = sys.argv[i + 1]
        i += 1

    elif arg in {"-f", "--font-size"}:
        font_size = sys.argv[i + 1]
        i += 1

    i += 1

terminal = Vte.Terminal()  # Initializing the terminal

terminal.spawn_async(
    Vte.PtyFlags.DEFAULT,  # Default Pty Flags
    None,                  # Working Directory
    command,               # SHELL
    None,                  # Environment variables
    0,                     # Spawn Flags
    None, None,            # Child Setup
    -1,                    # timeout (Here, -1 is to never timeout)
    None,                  # Cancellable
    None,                  # Callback
    None,                  # User data
    )

window = Gtk.Window()

window.set_title(title)

window.connect("delete-event", Gtk.main_quit)    # Handles the close signal
terminal.connect("child-exited", Gtk.main_quit)  # Handles the exit signal
terminal.set_font(Pango.FontDescription("monospace " + str(FONT_SIZE)))
terminal.set_bold_is_bright(True)                # Make text bright

# Scroll options
terminal.set_scrollback_lines(0)
terminal.set_scroll_on_output(False)
terminal.set_scroll_on_keystroke(True)

# Color of the foreground (r, g, b, a)
terminal.set_color_foreground(Gdk.RGBA(1.0, 1.0, 1.0, 1.0))
terminal.set_color_background(Gdk.RGBA(0.0, 0.0, 0.0, 1.0))

window.add(terminal)
window.show_all()

if __name__ == "__main__":
    Gtk.main()
