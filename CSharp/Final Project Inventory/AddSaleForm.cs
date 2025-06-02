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
                string Typestuff = P.GetType();
                if (string.Equals(Typestuff, "NewProduct:")){
                    checkedListBox1.Items.Add(P.GetName());
                }
                
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
            try{
    		int indexNum= 0 ;
            double indexPrice = 0.00;
            int index = checkedListBox1.SelectedIndex;
            string indexName = checkedListBox1.SelectedItem.ToString();
            int realindex;
            
            for(int i = Product.products.Count-1; i>=0; i--){
            	if (Product.products[i].GetName() == indexName){
            		indexNum = Product.products[i].GetAmount();
            		label2.Text = Product.products[i].GetName();
            		indexPrice = Product.products[i].GetPrice();
            		this.myParent.ProductName = Product.products[i].GetName();
            		this.myParent.CurrentPrice = indexPrice;
            		break;
            	}
            }
            
            int NumSold = int.Parse(textBox2.Text);
            string Date = (textBox3.Text + "/" + textBox4.Text + "/" + textBox5.Text);
            label4.Text = indexName;
            label3.Text = indexNum.ToString();
            if (NumSold > indexNum){
                MessageBox.Show("This sale is more than you have in stock!");
            }
            else{
                // Fix index
                this.myParent.Index = index;
                this.myParent.AmountSold = NumSold;
                this.myParent.DateInput = Date;
                this.myParent.Amount = indexNum - NumSold;
                this.myParent.ModType = ("Sale(" + NumSold + ")     ");
                this.myParent.MoneyGained = (NumSold * indexPrice);
//                Product.products[index].SetAmount(indexNum - NumSold);
                this.myParent.AddingProduct = false;
                this.myParent.SellingProduct = true;
                this.myParent.RestockingProduct = false;
                myParent.ManagerFormLoad(null,null);
                myParent.Show();
                this.Hide();
            }
            }
            catch
            {
                MessageBox.Show("Please Enter Valid Inputs");
            }
            
            
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            this.myParent.SellingProduct = false;
            this.myParent.AddingProduct = false;
            myParent.ManagerFormLoad(null, null);
        	myParent.Show();
        	this.Hide();
        }
    }
}
