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
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(50, 33)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(181, 37)
        self._label1.TabIndex = 0
        self._label1.Text = "Diameter:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(172, 36)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(148, 29)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.DarkGreen
        self._label2.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(79, 96)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(98, 37)
        self._label2.TabIndex = 2
        self._label2.Text = "Radius:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.DarkGreen
        self._label3.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(101, 140)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(76, 37)
        self._label3.TabIndex = 3
        self._label3.Text = "Area:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.DarkGreen
        self._label4.Font = System.Drawing.Font("Palatino Linotype", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(12, 182)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(165, 37)
        self._label4.TabIndex = 4
        self._label4.Text = "Circumfrence:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.ForestGreen
        self._label5.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label5.Location = System.Drawing.Point(172, 99)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(148, 30)
        self._label5.TabIndex = 5
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.ForestGreen
        self._label6.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label6.Location = System.Drawing.Point(172, 143)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(148, 30)
        self._label6.TabIndex = 6
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.ForestGreen
        self._label7.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label7.Location = System.Drawing.Point(172, 187)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(148, 30)
        self._label7.TabIndex = 7
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.YellowGreen
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button1.Location = System.Drawing.Point(12, 244)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(97, 46)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.YellowGreen
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button2.Location = System.Drawing.Point(115, 244)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(94, 46)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.YellowGreen
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._button3.Location = System.Drawing.Point(215, 244)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(105, 46)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkGreen
        self.ClientSize = System.Drawing.Size(337, 318)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        Diameter = float(self._textBox1.Text)
        Radius   = Diameter/2
        Pi = 3.14159
        Circumfrence = 2 * Pi * Radius
        Area = Pi * Radius ** 2
        self._label5.Text = str(round(Radius,3))
        self._label6.Text = str(round(Area,3))
        self._label7.Text = str(round(Circumfrence,3))
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._label5.Text = ""
        self._label6.Text = ""
        self._label7.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()