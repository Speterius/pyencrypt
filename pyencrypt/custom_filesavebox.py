import os
import tkinter as tk
import easygui.boxes.utils as ut
import easygui.boxes.fileboxsetup as fbs


def filesavebox(msg=None, title=None, default="", filetypes=None):
    """
    easygui.filesavebox custom fix to make sure it pops up

    :param str msg: the msg to be displayed.
    :param str title: the window title
    :param str default: default filename to return
    :param object filetypes: filemasks that a user can choose, e.g. " \*.txt"
    :return: the name of a file, or None if user chose to cancel
    """

    localRoot = tk.Tk()
    localRoot.lift()
    localRoot.attributes('-topmost', True)
    localRoot.after_idle(localRoot.attributes, '-topmost', False)

    initialbase, initialfile, initialdir, filetypes = fbs.fileboxSetup(
        default, filetypes)

    f = ut.tk_FileDialog.asksaveasfilename(
        parent=localRoot,
        title=ut.getFileDialogTitle(
            msg, title),
        initialfile=initialfile, initialdir=initialdir,
        filetypes=filetypes
    )
    localRoot.destroy()
    if not f:
        return None
    return os.path.normpath(f)
