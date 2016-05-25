# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ialphastock", pos = wx.DefaultPosition, size = wx.Size( 1158,628 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_FileMenu = wx.Menu()
		self.m_OpenMenu = wx.Menu()
		self.m_FileMenu.AppendSubMenu( self.m_OpenMenu, u"Open" )
		
		self.m_ExitMenu = wx.Menu()
		self.m_FileMenu.AppendSubMenu( self.m_ExitMenu, u"Exit" )
		
		self.m_menubar.Append( self.m_FileMenu, u"File" ) 
		
		self.m_MacroMenu = wx.Menu()
		self.m_menubar.Append( self.m_MacroMenu, u"Macro" ) 
		
		self.m_CalendarMenu = wx.Menu()
		self.m_menubar.Append( self.m_CalendarMenu, u"Calendar" ) 
		
		self.m_SimulateMenu = wx.Menu()
		self.m_menubar.Append( self.m_SimulateMenu, u"Simulate" ) 
		
		self.m_OptionMenu = wx.Menu()
		self.m_menubar.Append( self.m_OptionMenu, u"Options" ) 
		
		self.m_WarningMenu = wx.Menu()
		self.m_menubar.Append( self.m_WarningMenu, u"Warning" ) 
		
		self.m_HelpMenu = wx.Menu()
		self.m_AboutMenu = wx.Menu()
		self.m_HelpMenu.AppendSubMenu( self.m_AboutMenu, u"About ..." )
		
		self.m_menubar.Append( self.m_HelpMenu, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		self.m_toolBar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolBar.Realize() 
		
		MainFrameBSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_MainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_MainPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		
		bSizerMP = wx.BoxSizer( wx.VERTICAL )
		
		comIndexbSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		dowGSizer = wx.GridSizer( 1, 3, 0, 0 )
		
		self.m_dowName = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"DOW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dowName.Wrap( -1 )
		self.m_dowName.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		dowGSizer.Add( self.m_dowName, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_dowValue = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"17521.02", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dowValue.Wrap( -1 )
		self.m_dowValue.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_dowValue.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		dowGSizer.Add( self.m_dowValue, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_dowPercent = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"1.2%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dowPercent.Wrap( -1 )
		self.m_dowPercent.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_dowPercent.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		dowGSizer.Add( self.m_dowPercent, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		comIndexbSizer.Add( dowGSizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 15 )
		
		naqGSizer = wx.GridSizer( 1, 3, 0, 0 )
		
		self.m_naqIndexName = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"NASDAQ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_naqIndexName.Wrap( -1 )
		self.m_naqIndexName.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_naqIndexName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_naqIndexName.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		naqGSizer.Add( self.m_naqIndexName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_naqIndexValue = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"2123", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_naqIndexValue.Wrap( -1 )
		self.m_naqIndexValue.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_naqIndexValue.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		naqGSizer.Add( self.m_naqIndexValue, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_naqIndexPercent = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"0.8%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_naqIndexPercent.Wrap( -1 )
		self.m_naqIndexPercent.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_naqIndexPercent.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		naqGSizer.Add( self.m_naqIndexPercent, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		comIndexbSizer.Add( naqGSizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
		
		spGSizer = wx.GridSizer( 1, 3, 0, 0 )
		
		self.m_spIndexName = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"SP500", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_spIndexName.Wrap( -1 )
		self.m_spIndexName.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		spGSizer.Add( self.m_spIndexName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spIndexValue = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"1743", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_spIndexValue.Wrap( -1 )
		self.m_spIndexValue.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_spIndexValue.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		
		spGSizer.Add( self.m_spIndexValue, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spIndexPercent = wx.StaticText( self.m_MainPanel, wx.ID_ANY, u"-0.6%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_spIndexPercent.Wrap( -1 )
		self.m_spIndexPercent.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		self.m_spIndexPercent.SetForegroundColour( wx.Colour( 0, 0, 255 ) )
		
		spGSizer.Add( self.m_spIndexPercent, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		comIndexbSizer.Add( spGSizer, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 5 )
		
		
		bSizerMP.Add( comIndexbSizer, 1, wx.EXPAND, 0 )
		
		mainContentbSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_portfolioTreeCtrl = wx.TreeCtrl( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		self.m_portfolioTreeCtrl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer17.Add( self.m_portfolioTreeCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		mainContentbSizer.Add( bSizer17, 3, wx.EXPAND, 0 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel7 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer18.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel8 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer18.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel9 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel9.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer18.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel10 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer18.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		mainContentbSizer.Add( bSizer18, 8, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel11 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer19.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel12 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel12.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer19.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel13 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer19.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel14 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel14.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer19.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		mainContentbSizer.Add( bSizer19, 8, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel15 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel15.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer20.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel16 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer20.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel17 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel17.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer20.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel18 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer20.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		mainContentbSizer.Add( bSizer20, 8, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel19 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer21.Add( self.m_panel19, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		mainContentbSizer.Add( bSizer21, 4, wx.EXPAND, 5 )
		
		
		bSizerMP.Add( mainContentbSizer, 10, wx.EXPAND, 0 )
		
		bottomBSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel20 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bottomBSizer.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel21 = wx.Panel( self.m_MainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bottomBSizer.Add( self.m_panel21, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizerMP.Add( bottomBSizer, 3, wx.EXPAND, 0 )
		
		
		self.m_MainPanel.SetSizer( bSizerMP )
		self.m_MainPanel.Layout()
		bSizerMP.Fit( self.m_MainPanel )
		MainFrameBSizer.Add( self.m_MainPanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( MainFrameBSizer )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_statusBar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

