/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/12/2025
 * Time: 2:41 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg334_LoanCalculator
{
    /// <summary>
    /// Description of MainForm.
    /// </summary>
    public partial class MainForm : Form {
        const int intMIN_MONTHS = 6;
        const int intMAX_MONTHS = 48;
        const float sngMONTHS_YEAR = 12.0f; // Months per year
        
        
        const double dblNEW_RATE = 0.089;
        const double dblUSED_RATE = 0.095;
        
        double dblAnnualRate = dblNEW_RATE; // Annual Intrest rate
        public MainForm() {
      
            InitializeComponent();
            
            //
            // TODO: Add constructor code after the InitializeComponent() call.
            //
        }
        void Button1Click(object sender, System.EventArgs e)
        {
            int intCount = 0;
            int intMonths = 0;
            double dblLoan = 0.0;
            double dblPayment = 0.0;
            double dblInterest = 0.0;
            double dldPrincipal = 0.0;
           
            try{
                intMonths = int.Parse(textBox3.Text);
                dblLoan = double.Parse(textBox1.Text) - double.Parse(textBox2.Text);
            } catch (Exception ex) {
                MessageBox.Show("Please enter numeric values");
                return;
            }
                
                
 
                   
        }
        
    }
}
