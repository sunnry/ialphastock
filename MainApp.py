import wx
import gui

class MFrame(gui.MainFrame):
    def __init__(self,parent):
        gui.MainFrame.__init__(self,parent)

class MApp(wx.App):
    def OnInit(self):
        self.frame = MFrame(None)
        self.SetTopWindow(self.frame)
        self.frame.Show(True)
        return True

def main():
    application = MApp(redirect=False)
    application.MainLoop()

if __name__ == '__main__':
    main()
