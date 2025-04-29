/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/29/2025
 * Time: 3:10 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Pg273_MassAndWeight
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
            double mass = double.Parse(textBox1.Text);
            double weight = mass * 9.8;
            if (weight > 1000) {
                label3.Text = "Too Heavy";
            } else if (weight < 10) {
                label3.Text = "Too light";
            } else label3.Text = weight.ToString();
            
                
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            label3.Text = "";
            textBox1.Text = "";
        }
    }
}
