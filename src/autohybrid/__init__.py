import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from xml.etree import cElementTree as ET

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "AutoHybrid"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

class App(tk.Tk):
    # The GUI Windows Elements
    from ._ui_elements import __init__

    # All clickable actions in the GUI
    from ._ui_actions import button_clicked
    # Handling of Inputs & Outputs
    from ._io_handling import select_openjob, save_openjob