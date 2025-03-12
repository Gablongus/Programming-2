import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.shadetypeprice = 0
        self.sizeprice = 0
        self.colorprice = 0
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._radioButton7 = System.Windows.Forms.RadioButton()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._radioButton9 = System.Windows.Forms.RadioButton()
        self._radioButton10 = System.Windows.Forms.RadioButton()
        self._radioButton11 = System.Windows.Forms.RadioButton()
        self._radioButton12 = System.Windows.Forms.RadioButton()
        self._radioButton8 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Azure
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(224, 182)
        self._label1.TabIndex = 0
        self._label1.Text = "Styles:"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.Azure
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(35, 50)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(143, 40)
        self._radioButton1.TabIndex = 1
        self._radioButton1.Text = "Regular Shades"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.Azure
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(35, 96)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(143, 40)
        self._radioButton2.TabIndex = 2
        self._radioButton2.Text = "Folding Shades"
        self._radioButton2.UseVisualStyleBackColor = False
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.Azure
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(35, 142)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(143, 40)
        self._radioButton3.TabIndex = 3
        self._radioButton3.Text = "Roman Shades"
        self._radioButton3.UseVisualStyleBackColor = False
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.Azure
        self._groupBox1.Controls.Add(self._radioButton7)
        self._groupBox1.Controls.Add(self._radioButton6)
        self._groupBox1.Controls.Add(self._radioButton5)
        self._groupBox1.Controls.Add(self._radioButton4)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(263, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(145, 182)
        self._groupBox1.TabIndex = 9
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Sizes"
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.Azure
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(20, 23)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(143, 40)
        self._radioButton4.TabIndex = 10
        self._radioButton4.Text = "25 Inches"
        self._radioButton4.UseVisualStyleBackColor = False
        self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
        # 
        # radioButton5
        # 
        self._radioButton5.BackColor = System.Drawing.Color.Azure
        self._radioButton5.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton5.Location = System.Drawing.Point(20, 53)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(143, 40)
        self._radioButton5.TabIndex = 11
        self._radioButton5.Text = "27 Inches"
        self._radioButton5.UseVisualStyleBackColor = False
        self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
        # 
        # radioButton6
        # 
        self._radioButton6.BackColor = System.Drawing.Color.Azure
        self._radioButton6.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton6.Location = System.Drawing.Point(20, 90)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(143, 40)
        self._radioButton6.TabIndex = 12
        self._radioButton6.Text = "32 Inches"
        self._radioButton6.UseVisualStyleBackColor = False
        self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
        # 
        # radioButton7
        # 
        self._radioButton7.BackColor = System.Drawing.Color.Azure
        self._radioButton7.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton7.Location = System.Drawing.Point(20, 129)
        self._radioButton7.Name = "radioButton7"
        self._radioButton7.Size = System.Drawing.Size(143, 40)
        self._radioButton7.TabIndex = 13
        self._radioButton7.Text = "40 Inches"
        self._radioButton7.UseVisualStyleBackColor = False
        self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.Azure
        self._groupBox2.Controls.Add(self._radioButton8)
        self._groupBox2.Controls.Add(self._radioButton12)
        self._groupBox2.Controls.Add(self._radioButton9)
        self._groupBox2.Controls.Add(self._radioButton10)
        self._groupBox2.Controls.Add(self._radioButton11)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(432, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(145, 182)
        self._groupBox2.TabIndex = 14
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Colors"
        # 
        # radioButton9
        # 
        self._radioButton9.BackColor = System.Drawing.Color.Azure
        self._radioButton9.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton9.Location = System.Drawing.Point(20, 76)
        self._radioButton9.Name = "radioButton9"
        self._radioButton9.Size = System.Drawing.Size(143, 40)
        self._radioButton9.TabIndex = 12
        self._radioButton9.Text = "Blue"
        self._radioButton9.UseVisualStyleBackColor = False
        self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
        # 
        # radioButton10
        # 
        self._radioButton10.BackColor = System.Drawing.Color.Azure
        self._radioButton10.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton10.Location = System.Drawing.Point(20, 49)
        self._radioButton10.Name = "radioButton10"
        self._radioButton10.Size = System.Drawing.Size(143, 40)
        self._radioButton10.TabIndex = 11
        self._radioButton10.Text = "Teal"
        self._radioButton10.UseVisualStyleBackColor = False
        self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
        # 
        # radioButton11
        # 
        self._radioButton11.BackColor = System.Drawing.Color.Azure
        self._radioButton11.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton11.Location = System.Drawing.Point(20, 23)
        self._radioButton11.Name = "radioButton11"
        self._radioButton11.Size = System.Drawing.Size(143, 40)
        self._radioButton11.TabIndex = 10
        self._radioButton11.Text = "Natural"
        self._radioButton11.UseVisualStyleBackColor = False
        self._radioButton11.CheckedChanged += self.RadioButton11CheckedChanged
        # 
        # radioButton12
        # 
        self._radioButton12.BackColor = System.Drawing.Color.Azure
        self._radioButton12.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton12.Location = System.Drawing.Point(19, 111)
        self._radioButton12.Name = "radioButton12"
        self._radioButton12.Size = System.Drawing.Size(143, 24)
        self._radioButton12.TabIndex = 14
        self._radioButton12.Text = "Red"
        self._radioButton12.UseVisualStyleBackColor = False
        self._radioButton12.CheckedChanged += self.RadioButton12CheckedChanged
        # 
        # radioButton8
        # 
        self._radioButton8.BackColor = System.Drawing.Color.Azure
        self._radioButton8.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton8.Location = System.Drawing.Point(19, 137)
        self._radioButton8.Name = "radioButton8"
        self._radioButton8.Size = System.Drawing.Size(143, 24)
        self._radioButton8.TabIndex = 15
        self._radioButton8.Text = "Green"
        self._radioButton8.UseVisualStyleBackColor = False
        self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.AliceBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(88, 246)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(136, 41)
        self._button1.TabIndex = 15
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.AliceBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(230, 246)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(136, 41)
        self._button2.TabIndex = 16
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.AliceBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(372, 246)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(136, 41)
        self._button3.TabIndex = 17
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(159, 206)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(73, 29)
        self._label2.TabIndex = 18
        self._label2.Text = "Total:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(248, 206)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(165, 29)
        self._label3.TabIndex = 19
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LightCyan
        self.ClientSize = System.Drawing.Size(589, 316)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg485ShadeDesigner"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)



    def RadioButton1CheckedChanged(self, sender, e):
        self.shadetypeprice = 0
        pass

    def RadioButton2CheckedChanged(self, sender, e):
        self.shadetypeprice = 10
        pass

    def RadioButton3CheckedChanged(self, sender, e):
        self.shadetypeprice = 15
        pass

    def RadioButton4CheckedChanged(self, sender, e):
        self.sizeprice = 0

    def RadioButton5CheckedChanged(self, sender, e):
        self.sizeprice = 2

    def RadioButton6CheckedChanged(self, sender, e):
        self.sizeprice = 4

    def RadioButton7CheckedChanged(self, sender, e):
        self.sizeprice = 6

    def RadioButton11CheckedChanged(self, sender, e):
        self.colorprice = 5

    def RadioButton10CheckedChanged(self, sender, e):
        self.colorprice = 0

    def RadioButton9CheckedChanged(self, sender, e):
        self.colorprice = 0

    def RadioButton12CheckedChanged(self, sender, e):
        self.colorprice = 0

    def RadioButton8CheckedChanged(self, sender, e):
        self.colorprice = 0
        
        

    def Button1Click(self, sender, e):
        total = 50 + self.shadetypeprice + self.sizeprice + self.colorprice
        self._label3.Text = str(total)
        

    

    def Button2Click(self, sender, e):
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()