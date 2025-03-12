import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.maintotal = 0
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightCyan
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(340, 212)
        self._label1.TabIndex = 0
        self._label1.Text = "Dormatories:"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.LightCyan
        self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(25, 46)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(316, 32)
        self._radioButton1.TabIndex = 1
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Allen Hall        $1,500 Per Semester"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.LightCyan
        self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(26, 84)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(316, 32)
        self._radioButton2.TabIndex = 2
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Pike Hall         $1,600 Per Semester"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.LightCyan
        self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(26, 122)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(326, 32)
        self._radioButton3.TabIndex = 3
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Farthing Hall   $1,200 Per Semester"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.LightCyan
        self._radioButton4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(27, 160)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(325, 32)
        self._radioButton4.TabIndex = 4
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "University Suites $1,800 Per Semester"
        self._radioButton4.UseVisualStyleBackColor = False
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.LightCyan
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 231)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(565, 91)
        self._label2.TabIndex = 5
        self._label2.Text = "Total Costs:"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleTurquoise
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(359, 9)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(218, 84)
        self._button1.TabIndex = 6
        self._button1.Text = "Meal Plans"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Azure
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(359, 102)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(218, 55)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Azure
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(359, 166)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(218, 55)
        self._button3.TabIndex = 8
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.LightCyan
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(67, 266)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(182, 34)
        self._label3.TabIndex = 9
        self._label3.Text = "Price Per Semester:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(218, 262)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(268, 32)
        self._label4.TabIndex = 10
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.DarkCyan
        self.ClientSize = System.Drawing.Size(589, 340)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg484DormAndMealPlans"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        from MealPlans import *
        mealplans = MealPlans(self)
        mealplans.Show()
        self.Hide()