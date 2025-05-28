/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/21/2025
 * Time: 3:12 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Final_Project_Inventory
{
    /// <summary>
    /// Description of MainForm.
    /// </summary>
    public partial class MainForm : Form {
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
            if (string.IsNullOrEmpty(textBox1.Text))
            {
                MessageBox.Show("Please Enter A Name");
            }
            else
            {
                string Name = textBox1.Text;
                ManagerForm mngForm = new ManagerForm(this);
                mngForm.CompanyName = Name;
                mngForm.AddingProduct = false;
                mngForm.Show();
                this.Hide();
            }
        }
        
        void MainFormLoad(object sender, EventArgs e)
        {
            
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
