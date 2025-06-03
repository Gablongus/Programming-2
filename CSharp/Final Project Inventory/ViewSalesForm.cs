/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 6/3/2025
 * Time: 3:16 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Final_Project_Inventory
{
    /// <summary>
    /// Description of ViewSalesForm.
    /// </summary>
    public partial class ViewSalesForm : Form {
        private ManagerForm myParent
        
            public ViewSalesForm(ManagerForm myParent) {
            this.myParent = myParent;
            InitializeComponent();
        }
        
        void ViewSalesFormLoad(object sender, EventArgs e)
        {
            //Fin
            foreach (Product P in Product.products){
                string Typestuff = P.GetType();
                if (Typestuff.Contains("Sale")) {
                    checkedListBox1.Items.Add(P.GetName());
                }
                
            }
        }
    }
}
