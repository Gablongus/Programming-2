/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/15/2025
 * Time: 2:41 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg514SalesData { 
    public partial class MainForm : Form {
        private bool GetSalesData(ref decimal[] decSales) {
            int intNumDays = 0;
            int intCount;
            bool blnSuccess = false;
            string strNumDays = Interaction.InputBox("For how many days do you have sales?");
            
            if (!int.TryParse(strNumDays, out intNumDays)) {
                MessageBox.Show("You entered a non-numeric value", "Error");
                return false;
            }
            decimal[] decSalesData = new decimal [intNumDays];
            if (intNumDays > 0) {
                decSalesData = new decimal[intNumDays];
            
            for (intCount = 0; intCount < intNumDays; intCount++) {
                bool blnValid = false;
                while (blnValid != true) {
                    blnValid = decimal.TryParse(
                                    Interaction.InputBox("Enter the sales " +
                                    "for day " + (intCount + 1).ToString()),
                                    out decSalesData[intCount]);
                    if (blnValid != true) {
                        MessageBox.Show("Please enter a valid number");
                    }
                }
            }
                decSales = decSalesData;
                blnSuccess = true;
            } else {
                MessageBox.Show("You must enter at least "+
                                "one day of sales");
            }
            return blnSuccess;
        } //END
        
        private decimal GetTotal(decimal[] decValues) {
            decimal decTotal = 0;
            int intCount;
            
            for (intCount = 0; intCount < decValues.Length; intCount++) {
                decTotal += decValues[intCount];
            }
            return decTotal;
        } //End
        
        private decimal GetAverage(decimal[] decValues) {
            return GetTotal(decValues) / decValues.Length;
        } //End
        
        private decimal GetHighest(decimal[] decValues) {
            int intCount;
            decimal decHighest = decValues[0];
            
            for (intCount = 1; intCount < decValues.Length; intCount++) {
                if (decValues[intCount] > decHighest) {
                    decHighest = decValues[intCount];
                }
            }
            return decHighest;
        } //End
        
        private decimal GetLowest(decimal[] decValues) {
            int intCount;
            decimal decLowest = decValues[0];
            for (intCount = 1; intCount < decValues.Length; intCount++) {
                if (decValues[intCount] < decLowest) {
                    decLowest = decValues[intCount];
                }
            }
            return decLowest;
        } //End
            
            
            
        public MainForm() {
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
            decimal[] decSales = null;
            decimal decTotal;
            decimal decAverage;
            decimal decHighest;
            decimal decLowest;
            
            if (GetSalesData(ref decSales)) {
                    decTotal = GetTotal(decSales);
                    decAverage = GetAverage(decSales);
                    decHighest = GetHighest(decSales);
                    decLowest = GetLowest(decSales);
                    
                    label5.Text = decTotal.ToString("$.00");
                    label6.Text = decAverage.ToString("$.00");
                    label7.Text = decHighest.ToString("$.00");
                    label8.Text = decLowest.ToString("$.00");
                }
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
  }

