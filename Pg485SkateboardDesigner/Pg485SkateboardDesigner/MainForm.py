import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.deckprice = 0
        self.truckprice = 0
        self.wheelprice = 0
        
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._radioButton7 = System.Windows.Forms.RadioButton()
        self._radioButton8 = System.Windows.Forms.RadioButton()
        self._radioButton9 = System.Windows.Forms.RadioButton()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._radioButton10 = System.Windows.Forms.RadioButton()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._checkBox4 = System.Windows.Forms.CheckBox()
        self._checkBox5 = System.Windows.Forms.CheckBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLight
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(254, 140)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Decks:"
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(22, 27)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(196, 24)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "The Master Thrasher"
        self._radioButton1.UseVisualStyleBackColor = True
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(22, 64)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(208, 24)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = """The Dictator of Grind
"""
        self._radioButton2.UseVisualStyleBackColor = True
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(22, 101)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(208, 24)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = """The Street King

"""
        self._radioButton3.UseVisualStyleBackColor = True
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.SystemColors.ControlLight
        self._groupBox3.Controls.Add(self._radioButton7)
        self._groupBox3.Controls.Add(self._radioButton8)
        self._groupBox3.Controls.Add(self._radioButton9)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(281, 12)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._groupBox3.Size = System.Drawing.Size(150, 140)
        self._groupBox3.TabIndex = 3
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Truck Assembelies:"
        # 
        # radioButton7
        # 
        self._radioButton7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton7.Location = System.Drawing.Point(22, 106)
        self._radioButton7.Name = "radioButton7"
        self._radioButton7.Size = System.Drawing.Size(208, 24)
        self._radioButton7.TabIndex = 2
        self._radioButton7.TabStop = True
        self._radioButton7.Text = "8.5 Axle"
        self._radioButton7.UseVisualStyleBackColor = True
        self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
        # 
        # radioButton8
        # 
        self._radioButton8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton8.Location = System.Drawing.Point(22, 73)
        self._radioButton8.Name = "radioButton8"
        self._radioButton8.Size = System.Drawing.Size(208, 24)
        self._radioButton8.TabIndex = 1
        self._radioButton8.TabStop = True
        self._radioButton8.Text = "8 Axle"
        self._radioButton8.UseVisualStyleBackColor = True
        self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
        # 
        # radioButton9
        # 
        self._radioButton9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton9.Location = System.Drawing.Point(22, 44)
        self._radioButton9.Name = "radioButton9"
        self._radioButton9.Size = System.Drawing.Size(196, 24)
        self._radioButton9.TabIndex = 0
        self._radioButton9.TabStop = True
        self._radioButton9.Text = "7.75 Axle"
        self._radioButton9.UseVisualStyleBackColor = True
        self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.SystemColors.ControlLight
        self._groupBox2.Controls.Add(self._radioButton10)
        self._groupBox2.Controls.Add(self._radioButton4)
        self._groupBox2.Controls.Add(self._radioButton5)
        self._groupBox2.Controls.Add(self._radioButton6)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(443, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._groupBox2.Size = System.Drawing.Size(150, 140)
        self._groupBox2.TabIndex = 4
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Wheel Sets:"
        # 
        # radioButton4
        # 
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(22, 73)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(208, 24)
        self._radioButton4.TabIndex = 2
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "58 mm"
        self._radioButton4.UseVisualStyleBackColor = True
        self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
        # 
        # radioButton5
        # 
        self._radioButton5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton5.Location = System.Drawing.Point(22, 48)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(208, 24)
        self._radioButton5.TabIndex = 1
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "55 mm"
        self._radioButton5.UseVisualStyleBackColor = True
        self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
        # 
        # radioButton6
        # 
        self._radioButton6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton6.Location = System.Drawing.Point(22, 23)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(196, 24)
        self._radioButton6.TabIndex = 0
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "51 mm"
        self._radioButton6.UseVisualStyleBackColor = True
        self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
        # 
        # radioButton10
        # 
        self._radioButton10.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton10.Location = System.Drawing.Point(22, 101)
        self._radioButton10.Name = "radioButton10"
        self._radioButton10.Size = System.Drawing.Size(208, 24)
        self._radioButton10.TabIndex = 3
        self._radioButton10.TabStop = True
        self._radioButton10.Text = "61 mm"
        self._radioButton10.UseVisualStyleBackColor = True
        self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
        # 
        # groupBox4
        # 
        self._groupBox4.BackColor = System.Drawing.SystemColors.Control
        self._groupBox4.Controls.Add(self._checkBox5)
        self._groupBox4.Controls.Add(self._checkBox4)
        self._groupBox4.Controls.Add(self._checkBox3)
        self._groupBox4.Controls.Add(self._checkBox2)
        self._groupBox4.Controls.Add(self._checkBox1)
        self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox4.Location = System.Drawing.Point(13, 159)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._groupBox4.Size = System.Drawing.Size(183, 165)
        self._groupBox4.TabIndex = 5
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Misc Store"
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(19, 28)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(133, 24)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Grip Tape"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(19, 54)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(133, 24)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Bearings"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(19, 81)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(133, 24)
        self._checkBox3.TabIndex = 2
        self._checkBox3.Text = "Riser Pads"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # checkBox4
        # 
        self._checkBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox4.Location = System.Drawing.Point(19, 106)
        self._checkBox4.Name = "checkBox4"
        self._checkBox4.Size = System.Drawing.Size(180, 24)
        self._checkBox4.TabIndex = 3
        self._checkBox4.Text = "Nuts And Bolts Kit"
        self._checkBox4.UseVisualStyleBackColor = True
        # 
        # checkBox5
        # 
        self._checkBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox5.Location = System.Drawing.Point(19, 131)
        self._checkBox5.Name = "checkBox5"
        self._checkBox5.Size = System.Drawing.Size(180, 24)
        self._checkBox5.TabIndex = 4
        self._checkBox5.Text = "Assembely"
        self._checkBox5.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Gainsboro
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(211, 161)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(158, 52)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate Price"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Gainsboro
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(375, 161)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(118, 52)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Gainsboro
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(499, 159)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(94, 52)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.WhiteSmoke
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(281, 230)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(66, 34)
        self._label1.TabIndex = 9
        self._label1.Text = "Cost:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.WhiteSmoke
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(281, 259)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(66, 34)
        self._label2.TabIndex = 10
        self._label2.Text = "Tax:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.WhiteSmoke
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(281, 293)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(66, 34)
        self._label3.TabIndex = 11
        self._label3.Text = "Total:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.WhiteSmoke
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(344, 230)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(117, 34)
        self._label4.TabIndex = 12
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.WhiteSmoke
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(344, 261)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(117, 34)
        self._label5.TabIndex = 13
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.WhiteSmoke
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(344, 293)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(117, 34)
        self._label6.TabIndex = 14
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkGray
        self.ClientSize = System.Drawing.Size(605, 340)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg485SkateboardDesigner"
        self._groupBox1.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox4.ResumeLayout(False)
        self.ResumeLayout(False)


    def RadioButton1CheckedChanged(self, sender, e):
        self.deckprice = 60

    def RadioButton2CheckedChanged(self, sender, e):
        self.deckprice = 45

    def RadioButton3CheckedChanged(self, sender, e):
        self.deckprice = 50

    def RadioButton9CheckedChanged(self, sender, e):
        self.truckprice = 35

    def RadioButton8CheckedChanged(self, sender, e):
        self.truckprice = 40

    def RadioButton7CheckedChanged(self, sender, e):
        self.truckprice = 45

    def RadioButton6CheckedChanged(self, sender, e):
        self.wheelprice = 20

    def RadioButton5CheckedChanged(self, sender, e):
        self.wheelprice = 22

    def RadioButton4CheckedChanged(self, sender, e):
        self.wheelprice = 24

    def RadioButton10CheckedChanged(self, sender, e):
        self.wheelprice = 28

    def Button1Click(self, sender, e):
        customtotal = self.deckprice + self.truckprice + self.wheelprice
        