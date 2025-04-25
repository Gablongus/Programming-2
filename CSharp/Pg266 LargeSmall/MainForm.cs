/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/25/2025
 * Time: 3:02 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Pg266_LargeSmall
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
            double num1 = double.Parse(textBox1.Text);
            double num2 = double.Parse(textBox2.Text);
            if (num1 > num2) {
                label3.Text = ("The greater number is: " + num1);
            } else if (num2 > num1) {
                label3.Text = ("The greater number is: " + num2);
            } else {
                label3.Text = ("ERROR");
            }
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            label3.Text = "";
            textBox2.Text = "";
            textBox1.Text = "";
                
        }
        
        void Button3Click(object sender, EventArgs e)
        {
            Application.Exit()
        }
    }
}
