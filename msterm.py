#!/usr/bin/env python3

"""My Simple Terminal"""

import os
import sys
import gi
gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")
gi.require_version("Pango", "1.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import Pango
from gi.repository import Vte

command = [os.environ.get("SHELL")]
SET_TITLE = False

i = 0

while i < len(sys.argv):
    arg = sys.argv[i]

    if arg in ("-h", "--help"):
        print("Usage:", os.path.basename(sys.argv[0]))
        sys.exit()

    elif arg in ("-e", "--command"):
        SYSTEM_COMMANDS = sys.argv[i + 1]
        command.append("-c")
        command.append(SYSTEM_COMMANDS)
        i += 1

    elif arg in ("-T", "-t", "--title"):
        SET_TITLE = True
        title = sys.argv[i + 1]
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

if SET_TITLE:
    window.set_title(title)
else:
    window.set_title("msterm")

window.connect("delete-event", Gtk.main_quit)    # Handles the close signal
terminal.connect("child-exited", Gtk.main_quit)  # Handles the exit signal
terminal.set_font(Pango.FontDescription("monospace 12"))
terminal.set_bold_is_bright(True)                # Make text bright
# Color of the foreground (r, g, b, a)
terminal.set_color_foreground(Gdk.RGBA(1.0, 1.0, 1.0, 1.0))
window.add(terminal)
window.resize(800, 1200)
window.show_all()

Gtk.main()
