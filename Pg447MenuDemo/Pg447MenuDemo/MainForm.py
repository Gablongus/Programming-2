import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._menuStrip1 = System.Windows.Forms.MenuStrip()
        self._mnuFile = System.Windows.Forms.ToolStripMenuItem()
        self._mnuFileExit = System.Windows.Forms.ToolStripMenuItem()
        self._mnuColor = System.Windows.Forms.ToolStripMenuItem()
        self._mnuColorRed = System.Windows.Forms.ToolStripMenuItem()
        self._menuStrip1.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(264, 337)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Hello, World!"
        # 
        # menuStrip1
        # 
        self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._mnuFile,
            self._mnuColor]))
        self._menuStrip1.Location = System.Drawing.Point(0, 0)
        self._menuStrip1.Name = "menuStrip1"
        self._menuStrip1.Size = System.Drawing.Size(599, 24)
        self._menuStrip1.TabIndex = 1
        self._menuStrip1.Text = "menuStrip1"
        # 
        # mnuFile
        # 
        self._mnuFile.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._mnuFileExit]))
        self._mnuFile.Name = "mnuFile"
        self._mnuFile.Size = System.Drawing.Size(37, 20)
        self._mnuFile.Text = "&File"
        # 
        # mnuFileExit
        # 
        self._mnuFileExit.Name = "mnuFileExit"
        self._mnuFileExit.Size = System.Drawing.Size(92, 22)
        self._mnuFileExit.Text = "&Exit"
        # 
        # mnuColor
        # 
        self._mnuColor.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._mnuColorRed]))
        self._mnuColor.Name = "mnuColor"
        self._mnuColor.Size = System.Drawing.Size(48, 20)
        self._mnuColor.Text = "&Color"
        # 
        # mnuColorRed
        # 
        self._mnuColorRed.Name = "mnuColorRed"
        self._mnuColorRed.Size = System.Drawing.Size(152, 22)
        self._mnuColorRed.Text = "&Red"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(599, 432)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._menuStrip1)
        self.MainMenuStrip = self._menuStrip1
        self.Name = "MainForm"
        self.Text = "Pg447MenuDemo"
        self._menuStrip1.ResumeLayout(False)
        self._menuStrip1.PerformLayout()
        self.ResumeLayout(False)
        self.PerformLayout()

