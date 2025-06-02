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
            
            int NumGained = int.Parse(textBox2.Text);
            string Date = (textBox3.Text + "/" + textBox4.Text + "/" + textBox5.Text);
            label4.Text = indexName;
            label3.Text = indexNum.ToString();
            
            this.myParent.Index = index;
            this.myParent.AmountGained = NumGained;
            this.myParent.DateInput = Date;
            this.myParent.Amount = indexNum + NumGained;
            this.myParent.ModType = ("Restock(" + NumGained + ")     ");
//                Product.products[index].SetAmount(indexNum - NumSold);
            this.myParent.AddingProduct = false;
            this.myParent.SellingProduct = false;
            this.myParent.RestockingProduct = true;
            myParent.ManagerFormLoad(null,null);
            myParent.Show();
            this.Hide();
 
            }
            catch
            {
                MessageBox.Show("Please Enter Valid Inputs");
            }
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
