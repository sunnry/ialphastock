# -*- coding: utf-8 -*-
#Boa:Frame:mainFrame

import wx

def create(parent):
    return mainFrame(parent)

[wxID_MAINFRAME] = [wx.NewId() for _init_ctrls in range(1)]

[wxID_MAINFRAMEFILEITEMS0, wxID_MAINFRAMEFILEITEMS1, 
] = [wx.NewId() for _init_coll_File_Items in range(2)]

class mainFrame(wx.Frame):
    def _init_coll_menuBar_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.File, title=u'File')

    def _init_coll_File_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_MAINFRAMEFILEITEMS0, kind=wx.ITEM_NORMAL,
              text=u'Open')
        parent.Append(help='', id=wxID_MAINFRAMEFILEITEMS1, kind=wx.ITEM_NORMAL,
              text=u'Exit')
        self.Bind(wx.EVT_MENU, self.OnFileItems0Menu,
              id=wxID_MAINFRAMEFILEITEMS0)

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar = wx.MenuBar()

        self.File = wx.Menu(title='')

        self._init_coll_menuBar_Menus(self.menuBar)
        self._init_coll_File_Items(self.File)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name=u'mainFrame',
              parent=prnt, pos=wx.Point(578, 225), size=wx.Size(757, 489),
              style=wx.DEFAULT_FRAME_STYLE, title=u'ialphastock')
        self._init_utils()
        self.SetClientSize(wx.Size(749, 462))
        self.SetMenuBar(self.menuBar)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnFileItems0Menu(self, event):
        event.Skip()
