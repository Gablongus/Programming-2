/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/28/2025
 * Time: 2:51 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Final_Project_Inventory
{
    /// <summary>
    /// Description of AddSaleForm.
    /// </summary>
    public partial class AddSaleForm : Form {
        private ManagerForm myParent;
        
        public AddSaleForm(ManagerForm myParent) {
            this.myParent = myParent;
            InitializeComponent();
        }
        
        
        
        void AddSaleFormLoad(object sender, EventArgs e)
        {
            foreach (Product P in Product.products){
                checkedListBox1.Items.Add(P.GetName());
            }
            
        }
        
        void CheckedListBox1SelectedIndexChanged(object sender, EventArgs e)
        {
            int index = checkedListBox1.SelectedIndex;
            
            int count = checkedListBox1.Items.Count;
            // Makes listbox 1 select
            for(int x=0; x<count; x++)
            {
                if (index != x)
                {
                    checkedListBox1.SetItemChecked(x, false);
                }
            }
            
            
        }
        
        void Button1Click(object sender, EventArgs e)
        {
            int NumSold = int.Parse(textBox2.Text);
            string Date = (textBox3.Text + "/" + textBox4.Text + "/" + textBox5.Text);
            
            
        }
    }
}
