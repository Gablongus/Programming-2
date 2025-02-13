import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Azure
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(209, 53)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Azure
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(13, 72)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(107, 53)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Azure
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(126, 72)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(96, 53)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # listBox1
        # 
        self._listBox1.ForeColor = System.Drawing.SystemColors.MenuText
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(228, 13)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(256, 459)
        self._listBox1.TabIndex = 4
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.PaleTurquoise
        self.ClientSize = System.Drawing.Size(490, 538)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog122a"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._listBox1.Text += ("Number\tSquare\tSquare Root\n")
        number = 1
        line = ""
        square = 0
        sqrt = 0
        for num in range(1,50):
            square = number**2
            sqrt = math.sqrt(number)
            line = (str(number) + "     " + str(square) + "     " + str(sqrt))
            self._listBox1.Text += (str(line)+"\n")
            number += 1

   