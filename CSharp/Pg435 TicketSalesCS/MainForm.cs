/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/7/2025
 * Time: 3:00 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Pg435_TicketSalesCS
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
            GeneralForm frm = new GeneralForm(this);
            // Python: frm = GeneralGorm()
            frm.Show();
            this.Hide();
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            Form frm = new StudentForm(this);
            frm.Show();
            this.Hide();
        }
        
        void Button3Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
