import numpy as np
import matplotlib.pyplot as plt


def keyboard():
    """Draw Hinton diagram for visualizing a weight matrix."""
    ax = plt.gca()
    ax.patch.set_facecolor('gray')
    ax.set_aspect('equal', 'box')
    ax.xaxis.set_major_locator(plt.NullLocator())
    ax.yaxis.set_major_locator(plt.NullLocator())
    enlarge = 1.5
    bsizes = [(enlarge*v[0], enlarge*v[1]) for v in sizes]

    for lkey in locations:
        (x,y,t) = locations[lkey]
        color = 'blue'
        width, height = bsizes[t]
        rect = plt.Rectangle([enlarge*(x), enlarge*(y)],  width, height,
                             facecolor=color, edgecolor='black')
        ax.add_patch(rect)

    ax.autoscale_view()
    ax.invert_yaxis()

sizes = [(31,35), (65,35), (48, 35), (47, 35), (35,76), (59,35), (74,35),
         (85,35), (35, 76), (49, 35), (40, 35), (200, 35), (68, 35), (31, 35)]
locations = {
    "Escape": (13, 10, 0), "F1": (78, 10, 0), "F2": (116, 10, 0), 
    "F3": (154, 10, 0), "F4": (193, 10, 0), "F5": (253, 10, 0), 
    "F6": (291, 10, 0), "F7": (329, 10, 0), "F8": (367, 10, 0), 
    "F9": (428, 10, 0), "F10": (466, 10, 0), "F11": (504, 10, 0), 
    "F12": (542, 10, 0), "Snapshot": (601, 10, 0), "Scroll`": (639, 10, 0), 
    "Pause": (677, 10, 0), "Oem_3": (13, 82, 0), "1": (52, 83, 0), 
    "2": (89, 82, 0), "3": (127, 82, 0), "4": (165, 82, 0), "5": (203, 82, 0), 
    "6": (242, 82, 0), "7": (280, 82, 0), "8": (318, 82, 0), "9": (356, 82, 0), 
    "0": (394, 82, 0), "Oem_Minus": (432, 82, 0), "Oem_Plus": (470, 82, 0), 
    "Back": (508, 82, 1), "Insert": (603, 82, 0), "Home": (641, 82, 0), 
    "Prior": (679, 82, 0), "NumLock": (738, 82, 0), "Divide-": (776, 82, 0), 
    "Multiply*": (814, 82, 0), "Subtract": (852, 82, 0), "Tab": (13, 122, 2), 
    "Q": (69, 122, 0), "W": (107, 122, 0), "E": (146, 122, 0), "R": (184, 122, 0), 
    "T": (222, 122, 0), "Y": (260, 122, 0), "U": (297, 122, 0), "I": (336, 122, 0), 
    "O": (374, 122, 0), "P": (412, 122, 0), "Oem_4": (449, 122, 0), 
    "Oem_6": (487, 122, 0), "Oem_5": (526, 122, 3), "Delete": (602, 122, 0), 
    "End": (640, 122, 0), "Next": (678, 122, 0), "Numpad7": (737, 122, 0), 
    "Numpad8": (775, 122, 0), "Numpad9": (813, 122, 0), "Add": (852, 122, 4), 
    "Capital": (13, 161, 5), "A": (79, 161, 0), "S": (117, 161, 0), 
    "D": (156, 161, 0), "F": (194, 161, 0), "G": (232, 161, 0), "H": (270, 161, 0), 
    "J": (308, 161, 0), "K": (346, 161, 0), "L": (384, 161, 0), "Oem_1": (422, 161, 0), 
    "Oem_7": (461, 161, 0), "Return": (499, 161, 6), "Numpad4": (737, 161, 0), 
    "Numpad5": (776, 161, 0), "Numpad6": (814, 161, 0), "Lshift": (13, 200, 7), 
    "Z": (106, 200, 0), "X": (145, 200, 0), "C": (183, 200, 0), "V": (222, 200, 0), 
    "B": (260, 200, 0), "N": (298, 200, 0), "M": (336, 200, 0), 
    "Oem_Comma": (374, 200, 0), "Oem_Period": (413, 200, 0), "Oem_2": (451, 200, 0), 
    "Rshift": (489, 200, 6), "Up": (641, 200, 0), "Numpad1": (738, 201, 0), 
    "Numpad2": (775, 201, 0), "Numpad3": (814, 201, 0), "NumpadReturn": (851, 201, 9), 
    "Lcontrol": (13, 240, 10), "Lwin": (69, 240, 11), "Lmenu": (119, 240, 11), 
    "Space": (169, 240, 12), "Rmenu": (377, 240, 11), "Rwin": (427, 240, 11), 
    "Apps": (476, 240, 11), "Rcontrol": (525, 240, 10), "Left": (603, 240, 0), 
    "Down": (641, 240, 0), "Right": (679, 240, 0), "Numpad0": (738, 240, 13), 
    "Decimal": (814, 240, 0)
}

if __name__ == '__main__':
    keyboard()
    plt.show()
