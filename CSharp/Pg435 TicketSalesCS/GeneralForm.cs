/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/7/2025
 * Time: 3:01 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Pg435_TicketSalesCS
{
    /// <summary>
    /// Description of GeneralForm.
    /// </summary>
    public partial class GeneralForm : Form {
        private Form myParent;
        
        public GeneralForm(Form myParent) { // Constructor (__init__)
            InitializeComponent();
            this.myParent = myParent;
        }
        
        void Button1Click(object sender, EventArgs e) {
            this.myParent.Show();
            this.Close();
        }
        
        void GeneralFormFormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show(); 
        }
        
        // TODO: decimal taxrate/calctax
        
        void Button2Click(object sender, EventArgs e)
        {
            
        }
    }
}
