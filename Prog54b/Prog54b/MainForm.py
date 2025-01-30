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
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(307, 132)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(51, 29)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(138, 33)
        self._label2.TabIndex = 1
        self._label2.Text = "First Number:"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(21, 62)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(157, 33)
        self._label3.TabIndex = 2
        self._label3.Text = "Second Number:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(44, 95)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(157, 33)
        self._label4.TabIndex = 3
        self._label4.Text = "Third Number:"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(34, 128)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(157, 33)
        self._label5.TabIndex = 4
        self._label5.Text = "Fourth Number:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(180, 29)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(119, 26)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(180, 63)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(119, 26)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(180, 96)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(119, 26)
        self._textBox3.TabIndex = 7
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(180, 128)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(119, 26)
        self._textBox4.TabIndex = 8
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(116, 205)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(61, 33)
        self._label6.TabIndex = 9
        self._label6.Text = "Sum:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Plum
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(174, 205)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(125, 26)
        self._label7.TabIndex = 10
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(84, 238)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(93, 33)
        self._label8.TabIndex = 11
        self._label8.Text = "Average:"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.Plum
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(174, 237)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(125, 26)
        self._label9.TabIndex = 12
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Violet
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(21, 305)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(88, 50)
        self._button1.TabIndex = 13
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Violet
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(116, 305)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(92, 50)
        self._button2.TabIndex = 14
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Violet
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(214, 305)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(85, 50)
        self._button3.TabIndex = 15
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Thistle
        self.ClientSize = System.Drawing.Size(324, 383)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        num1 = int(self._textBox1.Text)
        num2 = int(self._textBox2.Text)
        num3 = int(self._textBox3.Text)
        num4 = int(self._textBox4.Text)
        sum = num1 + num2 + num3 + num4
        avg = sum/4
        self._label7.Text = str(sum)
        self._label9.Text = str(avg)
        
        

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._label7.Text = ""
        self._label9.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()