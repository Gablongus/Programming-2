/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/24/2025
 * Time: 2:49 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Prog54b_Form
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
            double number1 = double.Parse(textBox1.Text);
            double number2 = double.Parse(textBox2.Text);
            double number3 = double.Parse(textBox3.Text);
            double number4 = double.Parse(textBox4.Text);
            
            double sum = number1 + number2 + number3 + number4;
            label6.Text = sum.ToString();
            
            double avg = sum/4;
            label7.Text = avg.ToString();
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            label6.Text = "";
            label7.Text = "";
        }
        
        void Button3Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
