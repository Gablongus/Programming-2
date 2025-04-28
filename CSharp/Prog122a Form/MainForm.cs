/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/28/2025
 * Time: 2:43 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Prog122a_Form
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
        
        void MainFormLoad(object sender, EventArgs e)
        {
            
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("Number\t\tSquare\t\tSquare Root");
            int lcv = 1;
            while (lcv <= 50) {
                int sqr = (int)Math.Pow(lcv, 2);
                double sqrt = Math.Sqrt(lcv);
                listBox1.Items.Add(lcv + "\t\t" + sqr + "\t\t" + Math.Round(sqrt, 4));
                //listBox1.Items.Add($"{lcv}\t\t{sqr}\t\t{Math.Round(sqrt,4)}");
                lcv++;
            }
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}
