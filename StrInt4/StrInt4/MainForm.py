import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PaleGreen
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 34)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(136, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Put Something:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PaleGreen
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 71)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Reversed:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(171, 31)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(188, 26)
        self._textBox1.TabIndex = 2
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(120, 70)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(239, 23)
        self._label3.TabIndex = 3
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Honeydew
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(8, 120)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(122, 48)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Honeydew
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(136, 120)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(108, 48)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Honeydew
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(250, 120)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(122, 48)
        self._button3.TabIndex = 6
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Lime
        self.ClientSize = System.Drawing.Size(381, 183)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrInt4"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        text = str(self._textBox1.Text)
        reverse = text[::-1]
        self._label3.Text = reverse

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""
        

    def Button3Click(self, sender, e):
        Application.Exit()