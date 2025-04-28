/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/28/2025
 * Time: 2:56 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Prog310a_Form
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
            Random rand = new Random();
            
            // int lcv = 0; while (lcv < ...) {...; lcv++; }
            for (int lcv = 0; lcv < rand.Next(5, 11); lcv++) {
                double freq = rand.Next(0, 21) + rand.NextDouble();
                string msg = "";
                int stars = (int)Math.Round(freq);
                for (int i = 0; i < stars; i++)
                    msg += "*";
                msg += " " + Math.Round(freq, 2);
                listBox1.Items.Add(msg);
            }
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}
