/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/21/2025
 * Time: 3:13 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Final_Project_Inventory
{
    /// <summary>
    /// Description of ManagerForm.
    /// </summary>
    public partial class ManagerForm : Form {
        private Form myParent;
        
        public ManagerForm(Form myParent) {
            InitializeComponent();
            this.myParent = myParent;
            
        }
    }
}
