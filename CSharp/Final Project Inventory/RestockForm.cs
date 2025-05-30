/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/30/2025
 * Time: 2:40 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Final_Project_Inventory
{
    /// <summary>
    /// Description of RestockForm.
    /// </summary>
    public partial class RestockForm : Form {
        private ManagerForm myParent;
        
        
        public RestockForm(ManagerForm myParent) {
            this.myParent = myParent;
            InitializeComponent();
            
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            this.myParent.SellingProduct = false;
            this.myParent.AddingProduct = false;
            myParent.ManagerFormLoad(null, null);
        	myParent.Show();
        	this.Hide();
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            
        }
        
        void RestockFormLoad(object sender, EventArgs e)
        {
            foreach (Product P in Product.products){
                string Typestuff = P.GetType();
                if (string.Equals(Typestuff, "NewProduct:")){
                    checkedListBox1.Items.Add(P.GetName());
                }
                
            }
        }
    }
}
