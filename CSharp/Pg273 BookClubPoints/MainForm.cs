/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/29/2025
 * Time: 2:44 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Pg273_BookClubPoints
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
             int books = int.Parse(textBox1.Text);
             int points = 0;
             if (books == 0) {
                 points = 0;
             } else if (books == 1) {
                 points = 5;
             } else if (books == 2) {
                 points = 15;
             } else if (books == 3) {
                 points = 30;
             } else if (books >= 4) {
                 points = 60;
             }
             label3.Text = points.ToString();
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            label3.Text = "";
        }
    }
}
