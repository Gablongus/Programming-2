/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/7/2025
 * Time: 3:02 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Pg435_TicketSalesCS
{
    /// <summary>
    /// Description of StudentForm.
    /// </summary>
    public partial class StudentForm : Form { 
        private Form myParent;
        decimal decTAXRATE = 0.06m;
        private decimal CalcTax(decimal cost) {
            return cost * decTAXRATE;
        }
        
        public StudentForm(Form myParent) {
            InitializeComponent();
            this.myParent = myParent;
            
            
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }
        
        void StudentFormFormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            int intNumTickets = 0;
            decimal decTicketCost = 0.0m;
            decimal decSalesTax = 0.0m;
            decimal decTotal = 0.0m;
            
            intNumTickets = int.Parse(textBox1.Text);
            decTicketCost = intNumTickets * 7;
            decSalesTax = CalcTax(decTicketCost);
            decTotal = decTicketCost + decSalesTax;
            
            label4.Text = decTicketCost.ToString("$.00");
            label5.Text = decSalesTax.ToString("$.00");
            label6.Text = decTotal.ToString("$.00");
        }
    }
}
