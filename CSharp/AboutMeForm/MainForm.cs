/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/24/2025
 * Time: 2:35 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace AboutMeForm
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
            label1.Text = "Name: Gavin Schraedley\n\nFavorite Sport: Martial Arts\n\nFavorite Quote: Noting is impossible unless \nyou can't do it - George Washington";
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            label1.Text = "";
        }
        
        void Button3Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
