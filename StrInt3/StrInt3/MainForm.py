import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(37, 43)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(110, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Input String:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(153, 40)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 26)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 87)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(257, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "First Non Repeating Char:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(240, 87)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(146, 31)
        self._label3.TabIndex = 3
        self._label3.Text = "label3"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Azure
        self.ClientSize = System.Drawing.Size(499, 383)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrInt3"
        self.ResumeLayout(False)
        self.PerformLayout()

