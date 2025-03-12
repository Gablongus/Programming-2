
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Student(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
        
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label10 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(428, 80)
        self._label1.TabIndex = 0
        self._label1.Text = "Number of Tickets:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(243, 48)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(185, 26)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 107)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(173, 174)
        self._label2.TabIndex = 2
        self._label2.Text = "Section:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(206, 107)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(235, 174)
        self._label3.TabIndex = 6
        self._label3.Text = "Total Cost:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(208, 141)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(65, 23)
        self._label4.TabIndex = 7
        self._label4.Text = "Tickets:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(224, 185)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(49, 23)
        self._label5.TabIndex = 8
        self._label5.Text = "Tax:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(208, 234)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(65, 23)
        self._label6.TabIndex = 9
        self._label6.Text = "Total:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(279, 142)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(149, 25)
        self._label7.TabIndex = 10
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(279, 187)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(149, 25)
        self._label8.TabIndex = 11
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(279, 232)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(149, 25)
        self._label9.TabIndex = 12
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(103, 295)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(99, 32)
        self._button1.TabIndex = 13
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(208, 295)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(99, 32)
        self._button2.TabIndex = 14
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label10.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(25, 149)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(142, 108)
        self._label10.TabIndex = 15
        self._label10.Text = "All students are in student section."
        # 
        # Student
        # 
        self.BackColor = System.Drawing.SystemColors.GradientActiveCaption
        self.ClientSize = System.Drawing.Size(453, 334)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "Student"
        self.Text = "Student"
        self.ResumeLayout(False)
        self.PerformLayout()


    def CalcTax(self, cost):
        decTAXRATE = 0.06
        return float(cost * decTAXRATE)
    

    def Button1Click(self, sender, e):
        NumTickets = 0
        TicketCost = 0.0
        SalesTax = 0.0
        Total = 0.0
        PriceEachTicket = 7
        
        
        
        NumTickets = float(self._textBox1.Text)
        TicketCost = NumTickets * PriceEachTicket
        SalesTax = self.CalcTax(TicketCost)
        Total = TicketCost + SalesTax
        
        self._label7.Text = str(round(TicketCost, 2))
        self._label8.Text = str(round(SalesTax, 2))
        self._label9.Text = str(round(Total, 2))

    

    def Button2Click(self, sender, e):
        self.myparent.Show()
        self.Hide()

    

   