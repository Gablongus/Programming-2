/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/1/2025
 * Time: 2:59 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Pg535_CatchMe
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
            private string[] label1 = ("Click here", "Try harder", "Try again", "Not even close",
                       "Where are you?", "I'm over here!", "Slow, arent you?");
            
            private Random rand = new Random();
        }
        
        
        void Button1MouseEnter(object sender, EventArgs e)
        {
            p
        }
    }
}
