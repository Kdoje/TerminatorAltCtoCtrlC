AVAILABLE=["AltCtoCtrlC"]

from os import terminal_size
from terminatorlib import plugin
from terminatorlib.terminator import Terminator
# We can use the type hints to get the data we need for 
from terminatorlib.terminal import Terminal
from terminatorlib.window import Window

from terminatorlib.util import get_config_dir, err, dbg, gerr
import gi
gi.require_version('Vte', '2.91')
from gi.repository import Gdk 

class AltCtoCtrlC(plugin.Plugin):

    capabilities = ['AltCtoCtrlC']

    def __init__(self):
        super(AltCtoCtrlC, self).__init__()
        err("Initializing")
        terms =  Terminator().terminals[0]
        err("in-direct get terminals: %s" % terms.terminator.terminals)
        err("The terminal stuff is %s" % type(terms.terminator.terminals[0]))
        self.windows : list[Window] = Terminator().get_windows()
        for window in self.windows:
            window.connect('key-press-event', self.on_keypress)


    def on_keypress(self, window: Window, event):
        alt_mask = Gdk.ModifierType.MOD1_MASK
    

        if event.type == Gdk.EventType.KEY_PRESS:
            keyval = event.keyval
            state = event.state
            err("handling a key press %s" % keyval)
            err("the c value is %s" % str(keyval == Gdk.KEY_c))
            err("the mod1 mask is %s" % str(keyval & Gdk.ModifierType.MOD1_MASK))

        if (state & alt_mask) and (keyval == Gdk.KEY_c):
            err("We got the alt+c thing")
            Terminator().last_focused_term.feed('\x03')
            return True
        return False


