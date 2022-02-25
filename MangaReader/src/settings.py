

class Settings(object):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.objM = self.obj.objMainWindow
        self.objP = self.obj.objPref
        self.objR = self.obj.objReader

        self.themeIndex = 0
        self.compressionState = True
        self.updateChapter = True
        self.updateOther = True
        self.hideNav = True
        self.fsState = True

    def setStates(self):
        self.objP.compressionState = self.compressionState

        self.objP.updateChapter = self.updateChapter

        self.objP.updateOther = self.updateOther

        self.objP.hideNav = self.hideNav

        self.objP.fsState = self.fsState

        self.objP.compressArchiveToggleBtn.setChecked(self.objP.compressionState)

        self.objP.toggleOne.setChecked(self.objP.updateChapter)

        self.objP.toggleTwo.setChecked(self.objP.updateOther)

        self.objP.readerNavtoggle.setChecked(self.objP.hideNav)

        self.objP.readerFStoggle.setChecked(self.objP.fsState)
        