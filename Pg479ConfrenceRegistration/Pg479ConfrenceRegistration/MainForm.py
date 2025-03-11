import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self, total):
        self.InitializeComponent()
        self.total = total 
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox8 = System.Windows.Forms.TextBox()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLight
        self._groupBox1.Controls.Add(self._textBox8)
        self._groupBox1.Controls.Add(self._textBox5)
        self._groupBox1.Controls.Add(self._label8)
        self._groupBox1.Controls.Add(self._label7)
        self._groupBox1.Controls.Add(self._textBox6)
        self._groupBox1.Controls.Add(self._textBox7)
        self._groupBox1.Controls.Add(self._label5)
        self._groupBox1.Controls.Add(self._label6)
        self._groupBox1.Controls.Add(self._textBox4)
        self._groupBox1.Controls.Add(self._textBox3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label4)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(634, 189)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Registrant"
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(24, 32)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Name:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(24, 70)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "Company:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(24, 108)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Adress:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(24, 147)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 3
        self._label4.Text = "City:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(130, 30)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(134, 26)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(130, 68)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(134, 26)
        self._textBox2.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(130, 108)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(134, 26)
        self._textBox3.TabIndex = 6
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(130, 147)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(134, 26)
        self._textBox4.TabIndex = 7
        # 
        # textBox6
        # 
        self._textBox6.Location = System.Drawing.Point(387, 67)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(134, 26)
        self._textBox6.TabIndex = 11
        # 
        # textBox7
        # 
        self._textBox7.Location = System.Drawing.Point(387, 29)
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(134, 26)
        self._textBox7.TabIndex = 10
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(281, 69)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 9
        self._label5.Text = "Email:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.Location = System.Drawing.Point(281, 31)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 8
        self._label6.Text = "Phone:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.Location = System.Drawing.Point(281, 147)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(67, 23)
        self._label7.TabIndex = 12
        self._label7.Text = "State:"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label8
        # 
        self._label8.Location = System.Drawing.Point(442, 147)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(52, 23)
        self._label8.TabIndex = 13
        self._label8.Text = "Zip:"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(346, 147)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(98, 26)
        self._textBox5.TabIndex = 14
        # 
        # textBox8
        # 
        self._textBox8.Location = System.Drawing.Point(500, 144)
        self._textBox8.Name = "textBox8"
        self._textBox8.Size = System.Drawing.Size(85, 26)
        self._textBox8.TabIndex = 15
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.Control
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(430, 215)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(217, 56)
        self._label9.TabIndex = 16
        self._label9.Text = "Total Price:"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(455, 238)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(169, 23)
        self._label10.TabIndex = 17
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 209)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(401, 62)
        self._button1.TabIndex = 18
        self._button1.Text = "Select Confrence Options"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(143, 277)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(162, 63)
        self._button2.TabIndex = 19
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(332, 277)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(162, 63)
        self._button3.TabIndex = 20
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self.ClientSize = System.Drawing.Size(659, 356)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg479ConfrenceRegistration"
        self.Load += self.MainFormLoad
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        from ConfrenceOptions import *
        confrence = ConfrenceOptions(self)
        confrence.Show()
        self.Hide()
        
        
    

    def MainFormLoad(self, sender, e):
        total = self.total
        self._label10.Text = str(self.total)