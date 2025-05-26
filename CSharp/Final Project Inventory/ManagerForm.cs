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
		
		
    	
    }
    public partial class ManagerForm : Form {
        private Form myParent;
        public string CompanyName {get; set;}
        
        public string ProductName {get; set;}
        public int StartingAmount {get; set;}
        public double CurrentPrice {get; set;}
        public string DateInput {get; set;}
        public bool AddingProduct {get; set;}
    
        
        public ManagerForm(Form myParent) {
            InitializeComponent();
            
            this.myParent = myParent;
            
            List<Product> products = new List<Product>(); #Ask about how to reference this later. Also ask about how you can add stuff to list box.
        	label1.Text = CompanyName;
            
        }
        
        
        	
        void ManagerFormLoad(object sender, EventArgs e)
        {
        	if (AddingProduct == true){
        	products.Add(new Product(ProductName, StartingAmount, CurrentPrice, DateInput));
        	}
        	
        }
        
        void Button4Click(object sender, EventArgs e)
        {
            AddProductForm addPr = new AddProductForm(this);
            addPr.Show();
            this.Hide();
                
        }
    }
}
