/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/29/2025
 * Time: 3:17 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg347_Sum
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
            
            
            // Need to Right-click "References"
            // under Solution Explorer (under Properties) >
            // Add Reference... > check "Microsoft.VisualBasic" > click "OK"
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            int ognum = int.Parse(Interaction.InputBox("Enter a positive integer value:", "Input Needed"));
            int num = ognum;
            if (num < 0) {
                MessageBox.Show("Invalid Integer");
            }
           
            int tot = 0;
            while (num >= 0) {
                tot = tot + num;
                num = num - 1;
            }
            MessageBox.Show("The sum of numbers 1 through " + ognum.ToString() + " is: " + tot.ToString());
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
