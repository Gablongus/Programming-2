
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MealPlans(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.LightCyan
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(373, 155)
        self._label1.TabIndex = 1
        self._label1.Text = "Meal Plans:"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.LightCyan
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(25, 43)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(339, 30)
        self._radioButton1.TabIndex = 2
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "7 meals per week       $560 per semester"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.LightCyan
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(25, 79)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(339, 30)
        self._radioButton2.TabIndex = 3
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "14 meals per week     $1,095 per semester"
        self._radioButton2.UseVisualStyleBackColor = False
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.LightCyan
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(25, 115)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(339, 30)
        self._radioButton3.TabIndex = 4
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Unlimited meals          $1,500 per semester"
        self._radioButton3.UseVisualStyleBackColor = False
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.PaleTurquoise
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(391, 9)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(247, 60)
        self._button1.TabIndex = 5
        self._button1.Text = "Close and Save"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # MealPlans
        # 
        self.BackColor = System.Drawing.Color.DarkCyan
        self.ClientSize = System.Drawing.Size(650, 183)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Name = "MealPlans"
        self.Text = "MealPlans"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.Hide()
        self.myparent.Show()

    def RadioButton1CheckedChanged(self, sender, e):
        self.myparent.mealtotal = 560

    def RadioButton2CheckedChanged(self, sender, e):
        self.myparent.mealtotal = 1096

    def RadioButton3CheckedChanged(self, sender, e):
        self.myparent.mealtotal = 1500