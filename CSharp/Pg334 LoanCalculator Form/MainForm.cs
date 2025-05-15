/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/14/2025
 * Time: 2:53 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg334_LoanCalculator_Form
{
    /// <summary>
    /// Description of MainForm.
    /// </summary
    public partial class MainForm : Form {
        const int intMIN_MONTHS = 6;
        const int intMAX_MONTHS = 48;
        const float sngMONTHS_YEAR = 12.0f; // Months per year
        
        
        const double dblNEW_RATE = 0.089;
        const double dblUSED_RATE = 0.095;
        
        double dblAnnualRate = dblNEW_RATE; // Annual Intrest rate
 
        public MainForm()
        {
            //
            // The InitializeComponent() call is required for Windows Forms designer support.
            //
            InitializeComponent();
            
            //
            // TODO: Add constructor code after the InitializeComponent() call.
            //
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            int intCount = 0;
            int intMonths = 0;
            double dblLoan = 0.0;
            double dblPayment = 0.0;
            double dblInterest = 0.0;
            double dblPrincipal = 0.0;
           
            try{
                intMonths = int.Parse(textBox3.Text);
                dblLoan = double.Parse(textBox1.Text) - double.Parse(textBox2.Text);
            } catch (Exception ex) {
                MessageBox.Show("Please enter numeric values");
                return;
            }
            
            dblPayment = Financial.Pmt(dblAnnualRate / sngMONTHS_YEAR,
                                       intMonths, -dblLoan);
            
            listBox1.Items.Clear();
            
            for (intCount = 1; intCount <= intMonths; intCount++) {
                string strOut = string.Empty;
                
                dblInterest = Financial.IPmt(dblAnnualRate / sngMONTHS_YEAR,
                                             intCount, intMonths, -dblLoan);
                
                dblPrincipal = Financial.PPmt(dblAnnualRate / sngMONTHS_YEAR,
                                              intCount, intMonths, -dblLoan);
                
                strOut += "Month: " + intCount;
                
                strOut += "  Payment: " + dblPayment.ToString("$.00");
                
                strOut += "  Interest: " + dblInterest.ToString("$.00");
                
                strOut += "  Principal: " + dblPrincipal.ToString("$.00");
                
                listBox1.Items.Add(strOut);
                
                
            }
                
        }
        
        
        
        void Button2Click(object sender, EventArgs e)
        {
            textBox1.CausesValidation = false;
            textBox2.CausesValidation = false;
            textBox3.CausesValidation = false;
            radioButton1.Checked = true;
            dblAnnualRate = dblNEW_RATE;
            label5.Text = dblNEW_RATE.ToString(".00%");
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            listBox1.Items.Clear();
            
            
            textBox1.Focus();
        }
        
        void Button3Click(object sender, EventArgs e)
        {
            textBox1.CausesValidation = false;
            textBox2.CausesValidation = false;
            textBox3.CausesValidation = false;
            
            Application.Exit();
        }
        
        void RadioButton1CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true) {
                dblAnnualRate = dblNEW_RATE;
                label5.Text = dblNEW_RATE.ToString(".00%");
            }
        }
        
        void RadioButton2CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked == true) {
                dblAnnualRate = dblUSED_RATE;
                label5.Text = dblUSED_RATE.ToString(".00%");
            }
        }
    }
}
