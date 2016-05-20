# -*- coding: utf-8 -*-
#Boa:Frame:mainFrame

import wx

def create(parent):
    return mainFrame(parent)

[wxID_MAINFRAME, wxID_MAINFRAMEMAINFRAMEPANEL, 
 wxID_MAINFRAMEMAINFRAMESTATUSBAR, wxID_MAINFRAMEMAINFRAMETOOLBAR, 
] = [wx.NewId() for _init_ctrls in range(4)]

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

    def _init_coll_MainFrameStatusBar_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'Status:')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar = wx.MenuBar()

        self.File = wx.Menu(title='')

        self._init_coll_menuBar_Menus(self.menuBar)
        self._init_coll_File_Items(self.File)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_MAINFRAME, name=u'mainFrame',
              parent=prnt, pos=wx.Point(499, 133), size=wx.Size(1121, 607),
              style=wx.DEFAULT_FRAME_STYLE, title=u'ialphastock')
        self._init_utils()
        self.SetClientSize(wx.Size(1113, 580))
        self.SetMenuBar(self.menuBar)
        self.SetToolTipString(u'mainFrame')

        self.MainFrameStatusBar = wx.StatusBar(id=wxID_MAINFRAMEMAINFRAMESTATUSBAR,
              name=u'MainFrameStatusBar', parent=self, style=0)
        self._init_coll_MainFrameStatusBar_Fields(self.MainFrameStatusBar)
        self.SetStatusBar(self.MainFrameStatusBar)

        self.MainFrameToolBar = wx.ToolBar(id=wxID_MAINFRAMEMAINFRAMETOOLBAR,
              name=u'MainFrameToolBar', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1113, 28), style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.SetToolBar(self.MainFrameToolBar)

        self.MainFramePanel = wx.Panel(id=wxID_MAINFRAMEMAINFRAMEPANEL,
              name=u'MainFramePanel', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1113, 541), style=wx.TAB_TRAVERSAL)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnFileItems0Menu(self, event):
        event.Skip()
