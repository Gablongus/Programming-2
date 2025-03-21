﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Public(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
        self.PriceEachTicket = 0
        
        
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._label9 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(231, 302)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(99, 32)
        self._button2.TabIndex = 29
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(126, 302)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(99, 32)
        self._button1.TabIndex = 28
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(302, 239)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(149, 25)
        self._label9.TabIndex = 27
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(302, 194)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(149, 25)
        self._label8.TabIndex = 26
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(302, 149)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(149, 25)
        self._label7.TabIndex = 25
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(231, 241)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(65, 23)
        self._label6.TabIndex = 24
        self._label6.Text = "Total:"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(247, 192)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(49, 23)
        self._label5.TabIndex = 23
        self._label5.Text = "Tax:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(231, 148)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(65, 23)
        self._label4.TabIndex = 22
        self._label4.Text = "Tickets:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(229, 114)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(235, 174)
        self._label3.TabIndex = 21
        self._label3.Text = "Total Cost:"
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.SystemColors.ButtonFace
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(61, 241)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(134, 24)
        self._radioButton3.TabIndex = 20
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Section C"
        self._radioButton3.UseVisualStyleBackColor = False
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(61, 192)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(134, 24)
        self._radioButton2.TabIndex = 19
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Section B"
        self._radioButton2.UseVisualStyleBackColor = False
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(61, 149)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(134, 24)
        self._radioButton1.TabIndex = 18
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Section A"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(36, 114)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(173, 174)
        self._label2.TabIndex = 17
        self._label2.Text = "Section:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(266, 55)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(185, 26)
        self._textBox1.TabIndex = 16
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(36, 20)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(428, 80)
        self._label1.TabIndex = 15
        self._label1.Text = "Number of Tickets:"
        # 
        # Public
        # 
        self.BackColor = System.Drawing.SystemColors.Highlight
        self.ClientSize = System.Drawing.Size(500, 354)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "Public"
        self.Text = "Public"
        self.ResumeLayout(False)
        self.PerformLayout()
    
    
    def CalcTax(self, cost):
        decTAXRATE = 0.06
        return float(cost * decTAXRATE)
    
    def RadioButton1CheckedChanged(self, sender, e):
        self.PriceEachTicket = 20.0
        

    def RadioButton2CheckedChanged(self, sender, e):
        self.PriceEachTicket = 15.0
        
        
    def RadioButton3CheckedChanged(self, sender, e):
        self.PriceEachTicket = 10.0

    def Button1Click(self, sender, e):
        NumTickets = 0
        TicketCost = 0.0
        SalesTax = 0.0
        Total = 0.0
        
        
        
        NumTickets = float(self._textBox1.Text)
        TicketCost = NumTickets * self.PriceEachTicket
        SalesTax = self.CalcTax(TicketCost)
        Total = TicketCost + SalesTax
        
        self._label7.Text = str(round(TicketCost, 2))
        self._label8.Text = str(round(SalesTax, 2))
        self._label9.Text = str(round(Total, 2))

    

    def Button2Click(self, sender, e):
        self.myparent.Show()
        self.Hide()