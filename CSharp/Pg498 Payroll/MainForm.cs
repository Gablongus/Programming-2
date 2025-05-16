/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/8/2025
 * Time: 2:49 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg498_Payroll
{
    /// <summary>
    /// Description of MainForm.
    /// </summary>
    public partial class MainForm : Form
    {
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
        const int intMAX_EMPLOYEES = 6;
        const decimal decHOURLY_PAY_RATE = 6.0m;
        void Button1Click(object sender, EventArgs e) {
            // Calc & Display Gross Pay Earned by Employees
            int[] intHours = new int[intMAX_EMPLOYEES]; // An array
            // <type>[] varName = new <type>[capacity];
            int Count = 0;
            int EmpHours = 0;
            decimal EmpPay = 0.0m;
            
            for (Count = 0; Count < intMAX_EMPLOYEES; Count ++) {
                while (int.TryParse(
                    Interaction.InputBox("Enter # of hours worked by employee #" +
                    (Count+1).ToString(), "Need Hours Worked"), 
                    out EmpHours) == false) {
                           MessageBox.Show("Please enter an interger for hours worked");
                           
                           
                   }
                       intHours[Count] = EmpHours;
            }
            
            //TODO: the rest
            listBox1.Items.Clear();
            for (Count = 0; Count < intMAX_EMPLOYEES; Count ++) {
                EmpPay = intHours[Count] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Employee " + (Count+1).ToString() +
                                   " earned " + EmpPay.ToString("$.00"));
            }
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
