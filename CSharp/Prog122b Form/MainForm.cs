/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/29/2025
 * Time: 3:01 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Prog122b_Form
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
            listBox1.Items.Clear();
            listBox1.Items.Add("Hours\t\tPay");
            int hour = 1;
            while (hour <= 40) {
                int pay = (int)4*(hour);
                listBox1.Items.Add(hour + "\t\t" + pay);
                //listBox1.Items.Add($"{lcv}\t\t{sqr}\t\t{Math.Round(sqrt,4)}");
                hour++;
            }
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}
