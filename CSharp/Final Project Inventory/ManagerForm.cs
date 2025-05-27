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
using System.Collections.Generic;

namespace Final_Project_Inventory
{
    /// <summary>
    /// Description of ManagerForm.
    /// </summary>
    public class Product {
    	private string strName;
		private int intAmount;
		private double dblPrice;
		private string strDate;
		
		public Product(string Name, int Amount, double Price, string Date){
    		strName = Name;
    		intAmount = Amount;
    		dblPrice = Price;
    		strDate = Date;
			
    			
    	}
		
		public string GetName() {
			return strName;
		}
		public int GetAmount() {
			return intAmount;
		}
		public double GetPrice() {
			return dblPrice;
		}
		public string GetDate() {
			return strDate;
		}
		
		public void SetAmount(int Amount) {
			intAmount = Amount;
		}
		public void SetPrice(double Price) {
			dblPrice = Price;
		}
		public override string ToString(){
		    return string.Format(strName + "\t\t" + intAmount + "\t" + dblPrice + "\t" + strDate);
		}
		
		
    	
    }
    public partial class ManagerForm : Form {
        private Form myParent;
        public string CompanyName {get; set;}
        
        public string ProductName {get; set;}
        public int StartingAmount {get; set;}
        public double CurrentPrice {get; set;}
        public string DateInput {get; set;}
        public bool AddingProduct {get; set;}
    
        List<Product> products;
        public ManagerForm(Form myParent) {
            InitializeComponent();
            
            this.myParent = myParent;
            
             
            //Ask about how to reference this later. Also ask about how you can add stuff to list box.
        	products = new List<Product>();
        	
        	listBox1.Items.Add("Modification Type  " +"\t" + "Product Name"+ "\t" +"Amount"+ "\t" +"Price"+ "\t" +"Date");
        	listBox1.Items.Add("----------------------------------------------------------");
            
        }
        
        
        	
        public void ManagerFormLoad(object sender, EventArgs e)
        {
            label1.Text = CompanyName;
            if (AddingProduct == true) {
        	products.Add(new Product(ProductName, StartingAmount, CurrentPrice, DateInput));
        	listBox1.Items.Add("NewProduct\t" + products[products.Count-1].ToString());
            }
        	
        }
        
        
        void Button4Click(object sender, EventArgs e)
        {
            AddProductForm addPr = new AddProductForm(this);
            addPr.Show();
            this.Hide();
                
        }
        
        void TextBox1TextChanged(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            // Figure this out or just remove it
            foreach (string str in products.ToString()) {
                if (str.StartsWith(textBox1.Text, StringComparison.CurrentCultureIgnoreCase))
                {
                    listBox1.Items.Add(str);
                }
            }
        }
    }
}
