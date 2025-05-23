/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/23/2025
 * Time: 3:01 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Final_Project_Inventory
{
    /// <summary>
    /// Description of AddProductForm.
    /// </summary>
    public partial class AddProductForm : Form {
        private Form myParent;
    
            
        public AddProductForm(Form myParent) {
            this.myParent = myParent;
            InitializeComponent();
        }
    }
}
