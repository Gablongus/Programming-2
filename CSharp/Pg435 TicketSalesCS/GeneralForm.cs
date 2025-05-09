/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/7/2025
 * Time: 3:01 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Pg435_TicketSalesCS
{
    /// <summary>
    /// Description of GeneralForm.
    /// </summary>
    public partial class GeneralForm : Form {
        private Form myParent;
        int PriceEachTicket = 0;
        decimal decTAXRATE = 0.06m;
        private decimal CalcTax(decimal cost) {
            return cost * decTAXRATE;
        }
        
        public GeneralForm(Form myParent) { // Constructor (__init__)
            InitializeComponent();
            this.myParent = myParent;
        }
        void RadioButton1CheckedChanged(object sender, EventArgs e)
        {
            PriceEachTicket = 20;
        }
        
        void RadioButton2CheckedChanged(object sender, EventArgs e)
        {
            PriceEachTicket = 15;
        }
        
        void RadioButton3CheckedChanged(object sender, EventArgs e)
        {
            PriceEachTicket = 7;
        }
        
        void Button1Click(object sender, EventArgs e) {
            this.myParent.Show();
            this.Close();
        }
        
        void GeneralFormFormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show(); 
        }
        
        // TODO: decimal taxrate/calctax
        
        void Button2Click(object sender, EventArgs e)
        {
            int intNumTickets = 0;
            decimal decTicketCost = 0.0m;
            decimal decSalesTax = 0.0m;
            decimal decTotal = 0.0m;
            
            intNumTickets = int.Parse(textBox1.Text);
            decTicketCost = intNumTickets * PriceEachTicket;
            decSalesTax = CalcTax(decTicketCost);
            decTotal = decTicketCost + decSalesTax;
            
            label4.Text = decTicketCost.ToString("$.00");
            label5.Text = decSalesTax.ToString("$.00");
            label6.Text = decTotal.ToString("$.00");
                
        }
        
        
    }
}
