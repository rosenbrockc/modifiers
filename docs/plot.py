# Using the magic encoding
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import re
import xml.etree.ElementTree as ET
import argparse
import matplotlib

matplotlib.rc('font', family='arial unicode ms')
sizes = [(35,35), (65,35), (48, 35), (47, 35), (35,76), (59,35), (74,35), (85,35),
         (85,35), (35, 76), (49, 35), (46, 35), (204, 35), (70, 35), (35, 35),
         (35,35)]
custmods = {
    "MODOPG": "VK_MODIFIER_MODOPG",
    "MODOPT": "VK_MODIFIER_MODOPT",
    "MODOPB": "VK_MODIFIER_MODOPB",
    "MODOPH": "VK_MODIFIER_MODOPH"
}
modifiers = ["MODOPG", "MODOPT", "MODOPB", "MODOPH", "CONTROL_L", "CONTROL_R",
             "OPTION_L", "OPTION_R", "COMMAND_L", "COMMAND_R", "SHIFT_L", "SHIFT_R",
             "CAPSLOCK", "VK_MODIFIER_MODOPG", "VK_MODIFIER_MODOPT", 
             "VK_MODIFIER_MODOPB", "VK_MODIFIER_MODOPH"]
locations = {
    "ESCAPE": (13, 10, 0, "Esc"), "F1": (78, 10, 0, 0), "F2": (116, 10, 0, 0), 
    "F3": (154, 10, 0, 0), "F4": (193, 10, 0, 0), "F5": (253, 10, 0, 0), 
    "F6": (291, 10, 0, 0), "F7": (329, 10, 0, 0), "F8": (367, 10, 0, 0), 
    "F9": (422, 10, 0, 0), "F10": (460, 10, 14, 0), "F11": (498, 10, 14, 0), 
    "F12": (536, 10, 14, 0), "VK_MODIFIER_MODOPT": (738, 10, 14, "M-T"), 
    "VK_MODIFIER_MODOPG": (776, 10, 14, "M-G"), 
    "VK_MODIFIER_MODOPB": (814, 10, 14, "M-B"), "VK_MODIFIER_MODOPH": (852, 10, 14, "M-H"),
    
    "F13": (601, 10, 14, "Prt Sc"), "Scroll`": (639, 10, 15, "Scroll"), 
    "Pause": (677, 10, 15, 0), 

    "BACKQUOTE": (13, 82, 0, "~"), "KEY_1": (51, 82, 0, "1"), 
    "KEY_2": (89, 82, 0, "2"), "KEY_3": (127, 82, 0, "3"), "KEY_4": (165, 82, 0, "4"), 
    "KEY_5": (203, 82, 0, "5"), 
    "KEY_6": (242, 82, 0, "6"), "KEY_7": (280, 82, 0, "7"), "KEY_8": (318, 82, 0, "8"), 
    "KEY_9": (356, 82, 0, "9"), 
    "KEY_0": (394, 82, 0, "0"), "MINUS": (432, 82, 0, "-"), "EQUAL": (470, 82, 0, "+"), 
    "DELETE": (508, 82, 1, "Backspace"), 

    "HELP": (603, 82, 15, "Insert"), "HOME": (641, 82, 15, "Home"), 
    "PAGEUP": (679, 82, 15, "PgUp"), "PC_KEYPAD_NUMLOCK": (738, 82, 15, "Num"), 
    "KEYPAD_SLASH": (776, 82, 0, "/"), 
    "KEYPAD_MULTIPLY": (814, 82, 0, "*"), "KEYPAD_MINUS": (852, 82, 0, "-"), 

    "TAB": (13, 122, 2, "Tab"), 
    "Q": (69, 122, 0, 0), "W": (107, 122, 0, 0), "E": (146, 122, 0, 0), "R": (184, 122, 0, 0), 
    "T": (222, 122, 0, 0), "Y": (260, 122, 0, 0), "U": (297, 122, 0, 0), "I": (336, 122, 0, 0),
    "O": (374, 122, 0, 0), "P": (412, 122, 0, 0), "BRACKET_LEFT": (449, 122, 0, "{"), 
    "BRACKET_RIGHT": (487, 122, 0, "}"), "BACKSLASH": (526, 122, 3, "\\"), 

    "FORWARD_DELETE": (602, 122, 14, "Del"), 
    "END": (640, 122, 14, "End"), "PAGEDOWN": (678, 122, 15, "PgDn"), "KEYPAD_7": (737, 122, 0, "7"), 
    "KEYPAD_8": (775, 122, 0, "8"), "KEYPAD_9": (813, 122, 0, "9"), 
    "KEYPAD_PLUS": (852, 122, 4, "+"), 
    
    "CAPSLOCK": (13, 161, 5, "Caps Lock"), "A": (79, 161, 0, 0), "S": (117, 161, 0, 0), 
    "D": (156, 161, 0, 0), "F": (194, 161, 0, 0), "G": (232, 161, 0, 0), "H": (270, 161, 0, 0), 
    "J": (308, 161, 0, 0), "K": (346, 161, 0, 0), "L": (384, 161, 0, 0), 
    "SEMICOLON": (422, 161, 0, ":"), 
    "QUOTE": (461, 161, 0, '"'), "RETURN": (499, 161, 6, "Enter"), 

    "KEYPAD_4": (737, 161, 0, "4"), 
    "KEYPAD_5": (776, 161, 0, "5"), "KEYPAD_6": (814, 161, 0, "6"), 

    "SHIFT_L": (13, 200, 7, "Shift"), 
    "Z": (106, 200, 0, 0), "X": (145, 200, 0, 0), "C": (183, 200, 0, 0), "V": (222, 200, 0, 0), 
    "B": (260, 200, 0, 0), "N": (298, 200, 0, 0), "M": (336, 200, 0, 0), 
    "COMMA": (374, 200, 0, ","), "DOT": (413, 200, 0, "."), "SLASH": (451, 200, 0, "?"), 
    "SHIFT_R": (489, 200, 8, "Shift"), 

    "CURSOR_UP": (641, 200, 0, u"↑"), "KEYPAD_1": (738, 201, 0, "1"), 
    "KEYPAD_2": (775, 201, 0, "2"), "KEYPAD_3": (814, 201, 0, "3"), 
    "ENTER": (852, 201, 9, "Enter"),

    "CONTROL_L": (13, 240, 10, "Ctrl"), "COMMAND_L": (69, 240, 11, "Cmd"), 
    "OPTION_L": (119, 240, 11, "Opt"), 
    "SPACE": (169, 240, 12, ""), "OPTION_R": (377, 240, 11, "Opt"), 
    "COMMAND_R": (427, 240, 11, "Cmd"), 
    "PC_APPLICATION": (476, 240, 11, "App"), "CONTROL_R": (525, 240, 10, "Ctrl"), 

    "CURSOR_LEFT": (603, 240, 0, u"←"), 
    "CURSOR_DOWN": (641, 240, 0, u"↓"), "CURSOR_RIGHT": (679, 240, 0, u"→"), 
    "KEYPAD_0": (738, 240, 13, "0"), 
    "KEYPAD_DOT": (814, 240, 0, "."),

    "VK_MOUSEKEY_DIAGONAL_NW": (907, 161, 0, u"\u2196"), "VK_MOUSEKEY_UP": (945, 161, 0, u"↑"),
    "VK_MOUSEKEY_DIAGONAL_NE": (983, 161, 0, u"\u2197"), 
    "VK_MOUSEKEY_LEFT": (907, 201, 0, u"←"),
    "VK_MOUSEKEY_RIGHT": (983, 201, 0, u"→"), 
    "VK_MOUSEKEY_DIAGONAL_SW": (907, 240, 0, u"\u2199"),
    "VK_MOUSEKEY_DIAGONAL_SE": (983, 240, 0, u"\u2198"), "VK_MOUSEKEY_DOWN": (945, 240, 0, u"↓"),

    "VK_MOUSEKEY_SCROLL_UP": (945, 82, 0, u"\u21c8"), 
    "VK_MOUSEKEY_SCROLL_DOWN": (945, 122, 0, u"\u21ca"),
    "VK_MOUSEKEY_SCROLL_LEFT": (907, 122, 0, u"\u21c7"),
    "VK_MOUSEKEY_SCROLL_RIGHT": (983, 122, 0, u"\u21c9"),

    "VK_MOUSEKEY_BUTTON_LEFT": (907, 10, 0, "LB"),
    "VK_MOUSEKEY_BUTTON_MIDDLE": (945, 10, 0, "CB"),
    "VK_MOUSEKEY_BUTTON_RIGHT": (983, 10, 0, "RB")
}
keylengths = {
    "SimultaneousKeyPresses": 2,
    "KeyToKey": 1,
    "HoldingKeyToKey": 2
}
special = ["VK_NONE"]

class Autogen(object):
    def __init__(self, xmltag, parent):
        self.xml = xmltag
        self.keytype = None
        self.codes = []
        self.parent = parent
        self.shortcut = None
        self.multiple = None
        self.isources = 0

        self._parse_xml()

    @property
    def chr_shortcut(self):
        """Returns an adjusted shortcut value so that we don't have
        the symbols between upper and lower case alphabet in ASCII."""
        if self.shortcut is not None:
            if self.shortcut > 90:
                return "A" + chr(self.shortcut + 6).upper()
            else:
                return chr(self.shortcut)
        else:
            return ""

    @property
    def sources(self):
        """Returns the source key press codes."""
        if self.keytype is not None and self.isources is not None:
            return self.codes[0:self.isources]
        else:
            return []

    @property
    def targets(self):
        """Returns the targets of the mappings."""
        if self.keytype is not None and self.isources is not None:
            return self.codes[self.isources::]
        else:
            return []

    def _parse_xml(self):
        """Parses the contents of the autogen tag to determine which
        keys are being remapped.
        """
        contents = self.xml.text
        null, keytype, keymap = contents.split("__")
        if keytype in keylengths:
            self.keytype = keytype
        else:
            raise ValueError("Can't interpret remapping type {}".format(keytype))

        commakeys = re.split(",\s*", keymap)
        keys = []
        for ckey in commakeys:
            keys.extend(re.split("\s*|\s*", ckey))

        #We want to loop through all the mappings and extract the key code
        #for each one. The virtual modifiers (custmods) need to mapped to
        #their full virtual key name. Other virtual keys (special) shouldn't
        #raise an exception, but aren't included in the diagram.
        sources = keylengths[self.keytype]
        nonmods = 0
        for key in keys:
            #Modifiers don't count as keys when we are counting the source
            #and target key combinations. However, we still want them to
            #show up as sources because they are obviously required to make
            #the remapping work.
            ismod = "Modifier" in key
            if "KeyCode" in key or ismod:
                code = key.split("::")[1].strip()
                if code in locations or code in special:
                    self.codes.append(code)
                elif code in custmods:
                    self.codes.append(custmods[code])
                else:
                    raise ValueError("Can't interpret key code {}".format(code))

                #increase the counter for non-modifier keys, then check whether we
                #have already had as many non-modifiers as required by the key type.
                if not ismod:
                    nonmods += 1
                if nonmods <= sources:
                    self.isources += 1

class Remap(object):
    def __init__(self, xmltag):
        self.xml = xmltag
        self.name = None
        self.identifier = None
        self.autogens = []
    
        self._parse_xml()

    def _parse_xml(self):
        """Parses the XML tag for this instance and compiles a list
        of autogen specifiers.
        """
        for child in self.xml:
            if child.tag == "autogen":
                self.autogens.append(Autogen(child, self))
            elif child.tag == "name":
                self.name = child.text
            elif child.tag == "identifier":
                self.identifier = child.text

class RemapFile(object):
    """Represents one of the include files from the Kabiner remapping
    program.
    """
    def __init__(self, filepath):
        """Parses the XML file at the given file path and looks for
        key remappings.
        """
        self.filepath = filepath
        self.remaps = []
        self.xml = None
        self.sources = {}
        self.targets = {}

        self._parse_xml()

    def _parse_xml(self):
        """Loads the XML file if it exists and looks for remappings."""
        from os import path as ppath
        if ppath.isfile(self.filepath):
            self.xml = ET.parse(self.filepath).getroot()
            for child in self.xml:
                if child.tag == "item":
                    self.remaps.append(Remap(child))

        self._cache_colors()

    def _cache_colors(self):
        """Analyzes all the remaps in the file by source or target to
        decide what color to return for them.
        """
        for remap in self.remaps:
            for autogen in remap.autogens:
                self._add_source(autogen)
                self._add_target(autogen)

        #Examine all the sources for multiple combinations on keys
        #that get used more than once.
        ichar = self._process_autogen_color(True)
        self._process_autogen_color(False, ichar)

    def _add_target(self, autogen):
        """Adds any targets from the specified autogen instance."""
        for key in autogen.targets:
            if key in self.targets:
                #We only want to add this target in if its autogen instance is
                #not already in the list.
                sameinst = [a for a in self.targets[key] if a is autogen]
                if len(sameinst) == 0:
                    self.targets[key].append(autogen)
            else:
                self.targets[key] = [autogen]
            
    def _add_source(self, autogen):
        """Adds any sources from the specified autogen instance."""
        for key in autogen.sources:
            if key in self.sources:
                #We only want to add this source in if its autogen instance is
                #not already in the list.
                sameinst = [a for a in self.sources[key] if a is autogen]
                if len(sameinst) == 0:
                    self.sources[key].append(autogen)
            else:
                self.sources[key] = [autogen]

    def _get_color_type(self, keytype, source):
        """Returns the color based on the key remapping action."""
        dcolor = {
            "SimultaneousKeyPresses": "red",
            "KeyToKey": "green",
            "HoldingKeyToKey": "blue"
        }
        if keytype in dcolor:
            if source:
                return dcolor[keytype]
            else:
                return "green"
        else:
            return "white"

    def _get_shortcut_text(self, autogens):
        """Determines how best to display the list of shortcuts for
        a key that is used in multiple remappings.
        """
        #if there is only one in the list, we just return it.
        if len(autogens) == 1:
            return autogens[0].chr_shortcut

        #Before we begin, we should sort by shortcut value
        sautogens = sorted(autogens, key=(lambda v: v.shortcut))

        #We just need to determine if they are consecutive in the
        #alphabet and partition them up into consecutive sets.
        result = []
        previous = sautogens[0].shortcut
        running = [sautogens[0].chr_shortcut]
        
        def _process_shortcut(running, result):
            """Appends the text key for the current set of consecutive keys."""
            if len(running) > 1:
                result.append(running[0] + "-" + running[-1])
            else:
                result.append(running[0])

        for i in range(1, len(sautogens)):
            agen = sautogens[i]
            if abs(agen.shortcut - previous) != 1 or i == len(autogens)-1:
                #This one does NOT follow the other one immediately in the alphabet.
                #or we are at the end of the list of autogens.
                if i == len(autogens) - 1: 
                    if agen.shortcut - previous == 1:
                        running.append(agen.chr_shortcut)
                    else:
                        result.append(agen.chr_shortcut)
                _process_shortcut(running, result)
                running = []

            #Even if we have found a break in the list and added that text, the
            #current entry (which wasn't consecutive to the previous ones) is the
            #start of the new entry.
            if i != len(autogens) - 1:
                running.append(agen.chr_shortcut)
                previous = agen.shortcut

        return ','.join(result)

    def _get_key_color(self, autogens, source, key):
        """Determines the key color based on the number of unique key types
        in the remapping list for a single key.
        """
        if key in modifiers:
            return "brown"

        if len(autogens) > 1:
            if len(set([a.keytype for a in autogens])) == 1:
                return "purple"
            else:
                #We have a different color for composite mappings.
                return "orange"
        else:
            return self._get_color_type(autogens[0].keytype, source)

    def get_color(self, key, source=True):
        """Returns the color to use when plotting the key."""
        #We check the dictionary of remaps for the given XML file
        #and grab the key color based the type of key press required
        #to activate the mapping.
        if source:
            keydict = self.sources
        else:
            keydict = self.targets

        if key in keydict:
            return (self._get_key_color(keydict[key], source, key),
                    self._get_shortcut_text(keydict[key]))
        elif "MOUSE" in key:
            return ("white", "")
        else:
            return ("gray", "")

    def _get_other_key(self, autogen, key, source=True):
        """Gets the other key used in a hold/simultaneous keypress
        from an Autogen instance.
        """
        if keylengths[autogen.keytype] > 1:
            if source:
                complement = [k for k in autogen.sources if k != key]
            elif len(autogen.targets) > 0:
                complement = [k for k in autogen.targets if k != key]

            if len(complement) > 0:
                return complement[0]
            else:
                return None
        else:
            return None

    def _process_autogen_color(self, source=True, startchar=None):
        """Processes the list of autogens that are mapped to the same key
        within a single remap.
        """
        #The main reason to have this method is that if the key is used
        #in multiple places, we need to keep track of all of them when
        #we assign the identifiers for the operations. For example, the
        #control remappings use the same key with about 20 other keys;
        #in that case we want to use the first A-T letters so that it 
        #is easy to print the text for that key.

        #Find a list of all the keys that have multiple maps to them
        from operator import itemgetter
        if source:
            keydict = self.sources
        else:
            keydict = self.targets
        multiple = []
        single = []

        #Get a list of all the key codes that have multiple remaps
        for key in keydict:
            autogens = keydict[key]
            if len(autogens) > 1:
                multiple.append((key, len(autogens), autogens))
            else:
                single.append((key, autogens[0]))
        multiple = sorted(multiple, key=itemgetter(1), reverse=True)
        multikeys = [m[0] for m in multiple]

        if startchar is not None:
            ichar = startchar 
        else:
            ichar = ord("A")
        for mkey, mlen, mset in multiple:
            #Now we assign an identifier to each of the remaps that will
            #be printed with its color. if any of the other multiple key
            #remaps are in the list, we try and put them at the end so
            #that they will have as consecutive a set of chars as possible.
            rchar = 0
            startchar = ichar
            for i in range(mlen):
                #don't assign a shortcut if it has already been processed.
                if mset[i].shortcut is not None:
                    continue

                okey = self._get_other_key(mset[i], mkey, source)
                if okey is None or okey not in multikeys:
                    mset[i].shortcut = ichar
                    ichar += 1
                elif okey is not None and okey in multikeys:
                    #Use a character from the end of the set instead. Adjust for the number
                    #of characters already assigned after this one.
                    preassigned = len([k for k in mset[0:i] 
                                       if k.multiple is not None and k.shortcut > startchar])
                    remaining = ichar + mlen - i - 1
                    mset[i].shortcut = remaining + rchar - preassigned
                    mset[i].multiple = True
                    rchar += 1
                else:
                    mset[i].shortcut = ichar
                    ichar += 1

            #At the end of all the keys, add on the extra amount for keys we 
            #were assigning from the end of the list so that the next list can
            #start with the right keys
            ichar += rchar

        #The rest of the mappings are all simple, just go through
        #them one at a time and assign a shortcut.
        for skey, agen in single:
            if agen.shortcut is None:
                agen.shortcut = ichar
                ichar += 1
        
        return ichar

def _plot_legend(ax, enlarge, yshift):
    """Plots the meanings of the colors for the remappings."""
    legend = [("red", 13, 300, "Simultaneous"),
              ("green", 183, 300, "Key to Key"),
              ("blue", 333, 300, "Hold Key"),
              ("purple", 463, 300, "Multiple Remaps"),
              ("orange", 653, 300, "Multiple Remap Types")]

    width, height = (35*enlarge, 35*enlarge)
    for color, x, y, text in legend:
        rect = plt.Rectangle([enlarge*(x), enlarge*(y + yshift)],  width, height,
                             facecolor=color, edgecolor='black', lw=0.1,
                             alpha=0.5)
        ax.add_patch(rect)
        ax.text(enlarge*(x + width/2 + 10), enlarge*(y + 2 + yshift), text, fontsize=8,
                color='black', ha='left', va='top', alpha=1)

def keyboard(remappings, source=True):
    from operator import itemgetter
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    enlarge = 2
    bsizes = [(enlarge*v[0], enlarge*v[1]) for v in sizes]
    yshift = 50 if source else 450

    for lkey in locations:
        (x,y,t,s) = locations[lkey]
        color, shortcut = remappings.get_color(lkey, source)
        width, height = bsizes[t]
        rect = plt.Rectangle([enlarge*(x), enlarge*(y + yshift)],  width, height,
                             facecolor=color, edgecolor='black', lw=0.1,
                             alpha=0.5)
        ax.add_patch(rect)

        if "," in shortcut or "-" in shortcut:
            fsize = 5
        else:
            fsize = 7

        scuts = shortcut.split(",")
        if len(scuts) > 1:
            scuts = sorted(scuts, key=itemgetter(0))

        for ishort in range(len(scuts)):
            ystart = (len(scuts) - 1)* 10
            ax.text(enlarge*(x + width/4), 
                    enlarge*(y + height/2 - 2 + 10*ishort - ystart + yshift), 
                    scuts[ishort], fontsize=fsize, weight="bold",
                    color='black', ha='center', va='bottom', alpha=1)

    ax.autoscale_view()
    plt.axis("off")
    if source:
        title = "Source Keyboard"
    else:
        title = "Target Keyboard"
    ax.text(enlarge*500, enlarge*yshift - 25, title, fontsize=14, 
            weight="bold", ha="center")
    ax.text(enlarge*920, enlarge*yshift, "Mouse", fontsize=10)

    for lkey in locations:
        (x,y,t,s) = locations[lkey]
        width, height = bsizes[t]
        if s == 0:
            s = lkey
        ax.text(enlarge*(x + 2), enlarge*(y + 2 + yshift), s, fontsize=5,
                color='black', ha='left', va='top', alpha=1)
    #We only need a legend for the source because it sits between both keyboards
    if source:
        _plot_legend(ax, enlarge, yshift)

def run():
    """Creates the plots of the keyboard remappings for the file(s)
    specified in the command-line arguments.
    """
    from os import path as ppath
    xpaths = [ppath.abspath(p) for p in args["sources"]]
    for xpath in xpaths:
        remappings = RemapFile(xpath)
        xfile = xpath.split("/")[-1]
        keyboard(remappings, True)
        keyboard(remappings, False)
        plt.gca().invert_yaxis()
        plt.savefig(xfile.replace(".xml", ".pdf"))

        #Get the plot ready for the next keyboard mapping set.
        plt.cla()
        plt.gca().invert_yaxis()

parser = argparse.ArgumentParser(description="MODIFIERS Key Remapping Plotter")
parser.add_argument("sources",  nargs="+", 
                    help="Specify the path(s) to the source XML remapping files.")

#Parse the args from the commandline that ran the script, call initialize
args = vars(parser.parse_args())
run()
