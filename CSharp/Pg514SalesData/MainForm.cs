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
        private bool GetSalesData(ref decimal decSales) {
            decimal decSalesData;
            int intNumDays = 0;
            int intCount;
            bool blnSuccess;
            string strNumDays = Interaction.InputBox("For how many days do you have sales?");
            
            if (!int.TryParse(strNumDays, out intNumDays)) {
                MessageBox.Show("You entered a non-numeric value", "Error");
                return false;
            }
            if (intNumDays > 0) {
                decSalesData = new decimal(intNumDays);
            }
            for (intCount = 0; intCount < intNumDays; intCount++) {
                bool blnValid = false;
                while (blnValid != true) {
                    blnValid = decimal.TryParse(
                        Interaction.InputBox("Enter the sales for day " + (intCount + 1).ToString()),
                        out decSalesData(intCount));
                    if (blnValid != true) {
                        MessageBox.Show("Please enter a valid number");
                    }
                }
            }
            
        }
            
            
            
        public MainForm() {
            //
            // The InitializeComponent() call is required for Windows Forms designer support.
            //
            InitializeComponent();
            
            //
            // TODO: Add constructor code after the InitializeComponent() call.
            //
        }
    }
  }

