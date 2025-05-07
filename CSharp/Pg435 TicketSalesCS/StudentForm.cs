/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/7/2025
 * Time: 3:02 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Pg435_TicketSalesCS
{
    /// <summary>
    /// Description of StudentForm.
    /// </summary>
    public partial class StudentForm : Form { 
        private Form myParent;
        
        public StudentForm(Form myParent) {
            InitializeComponent();
            this.myParent = myParent;
            
            
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }
    }
}
