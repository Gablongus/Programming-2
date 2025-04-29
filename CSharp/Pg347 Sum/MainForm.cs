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
            using Microsoft.VisualBasic;
            double num = Interaction.InputBox("Enter a positive integer value:", "Input Needed");
        }
    }
}
