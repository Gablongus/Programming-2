﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Pluto(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ControlLight
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(10, 339)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(183, 63)
        self._button1.TabIndex = 7
        self._button1.Text = "Return"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(278, 56)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(124, 239)
        self._label3.TabIndex = 6
        self._label3.Text = """Low density

39.44 AU

1.2 x 10^22 kg

-230C
"""
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(31, 56)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(352, 239)
        self._label2.TabIndex = 5
        self._label2.Text = """Type:

Average distance from the sun:

Mass:

Surface Temp:"""
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(10, 16)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(407, 319)
        self._label1.TabIndex = 4
        self._label1.Text = "Pluto"
        # 
        # Pluto
        # 
        self.BackColor = System.Drawing.SystemColors.AppWorkspace
        self.ClientSize = System.Drawing.Size(437, 413)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "Pluto"
        self.Text = "Pluto"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.Hide()
        self.myparent.Show()