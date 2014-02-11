#!/usr/bin/python
# gtkardlib
# GUI Arduino Library Installer by Sebastian Plamauer

from gi.repository import Gtk
import ardlib

class GridWindow(Gtk.Window):

    def __init__(self):
        #init
        Gtk.Window.__init__(self, title='gtkardlib')
        #grid
        grid = Gtk.Grid()
        self.add(grid)

        label = Gtk.Label('GUI Arduino Library Installer')
        label.set_line_wrap(True)

        #button
        button = Gtk.Button('Install selected lib')
        button.connect("clicked", self.on_click_me_clicked)

        #liblist
        store = Gtk.ListStore(str, str, str)
        for lib in repo.liblist:
            treeiter = store.append(lib)
        tree = Gtk.TreeView(store)

        column = Gtk.TreeViewColumn('Libraries')
        name = Gtk.CellRendererText()
        #info = Gtk.CellRendererText()
        column.pack_start(name, True)
        #column.pack_start(info, True)

        column.add_attribute(name, "text", 0)
        #column.add_attribute(info, "text", 2)

        tree.append_column(column)

        select = tree.get_selection()
        select.connect("changed", self.on_tree_selection_changed)

        #grid.attach(name,pos_hor,pos_ver,size_hor,size_ver)
        grid.attach(label,0,1,1,2)
        grid.attach(tree,1,1,1,4)
        grid.attach(button,2,4,1,1)

    def on_tree_selection_changed(self,selection):
        self.model, self.treeiter = selection.get_selected()
        if self.treeiter != None:
            print "You selected", self.model[self.treeiter][0]

    def on_click_me_clicked(self, button):
        repo.installlib(self.model[self.treeiter][0])

if __name__ == '__main__':
    repo = ardlib.library()
    repo.getliblist()
    win = GridWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()