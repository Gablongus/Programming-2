
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class ConfrenceOptions(Form):
    def __init__(self, parent, total):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._checkedListBox1 = System.Windows.Forms.CheckedListBox()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLight
        self._groupBox1.Controls.Add(self._checkBox2)
        self._groupBox1.Controls.Add(self._checkBox1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(342, 129)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Confrence"
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(30, 39)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(266, 24)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Confrence Registration $895"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(30, 78)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(316, 24)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Opening Night Dinner and Keynote $30"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.SystemColors.ControlLight
        self._groupBox2.Controls.Add(self._checkedListBox1)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(365, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(269, 129)
        self._groupBox2.TabIndex = 2
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Preference Workshops"
        # 
        # checkedListBox1
        # 
        self._checkedListBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkedListBox1.FormattingEnabled = True
        self._checkedListBox1.Items.AddRange(System.Array[System.Object](
            ["Intro to E-Commerce",
            "The Future of the Web",
            "Advanced Visual Basic",
            "Network Security"]))
        self._checkedListBox1.Location = System.Drawing.Point(29, 25)
        self._checkedListBox1.Name = "checkedListBox1"
        self._checkedListBox1.Size = System.Drawing.Size(203, 88)
        self._checkedListBox1.TabIndex = 0
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(295, 148)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(162, 63)
        self._button2.TabIndex = 20
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(472, 148)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(162, 63)
        self._button1.TabIndex = 21
        self._button1.Text = "Close"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # ConfrenceOptions
        # 
        self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self.ClientSize = System.Drawing.Size(646, 221)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "ConfrenceOptions"
        self.Text = "ConfrenceOptions"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)


    

    

    def Button1Click(self, sender, e):
        error = False
        self.total = 0
        if self._checkBox1.Checked:
            self.total += 895
        if self._checkBox2.Checked:
            self.total += 30
        if self._checkedListBox1.GetItemChecked(0):
            if self._checkBox1.Checked:
                total += 295
                error = False
            else:
                MessageBox.Show("You Need to select Conference Registration first!")
                error = True
        if self._checkedListBox1.GetItemChecked(1):
            if self._checkBox1.Checked:
                total += 295
                error = False
            else:
                MessageBox.Show("You Need to select Conference Registration first!")
                error = True
        if self._checkedListBox1.GetItemChecked(2):
            if self._checkBox1.Checked:
                total += 395
                error = False
            else:
                MessageBox.Show("You Need to select Conference Registration first!")
                error = True
        if self._checkedListBox1.GetItemChecked(3):
            if self._checkBox1.Checked:
                total += 395
                error = False
            else:
                MessageBox.Show("You Need to select Conference Registration first!")
                error = True
        if error == False:
            self.myparent.Show()
            self.Close()
            
            