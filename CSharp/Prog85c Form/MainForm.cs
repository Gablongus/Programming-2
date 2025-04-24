/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/24/2025
 * Time: 3:11 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Prog85c_Form
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
        
        void Button1Click(object sender, EventArgs e)
        {
            double num = double.Parse(textBox1.Text);
            double step1 = num - 165;
            double step2 = step1/100;
            double month = Math.Round(step2);
            double day = (step2 - month) * 100;
            
            label4.Text = month.ToString() + "/" + day.ToString();
        }
    }
}
