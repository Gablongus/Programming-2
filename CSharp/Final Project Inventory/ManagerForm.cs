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
            
             
            //Ask about how to reference this later. Also ask about how you can add stuff to list box
        	
        	listBox1.Items.Add("Modification Type  " +"\t" + "Product Name"+ "\t" +"Amount"+ "\t" +"Price"+ "\t" +"Date");
        	listBox1.Items.Add("----------------------------------------------------------");
            
        }
        
        
        	
        public void ManagerFormLoad(object sender, EventArgs e)
        {
            label1.Text = CompanyName;
            if (AddingProduct == true) {
        	Product.products.Add(new Product(ProductName, StartingAmount, CurrentPrice, DateInput));
        	listBox1.Items.Add("NewProduct\t" + Product.products[Product.products.Count-1].ToString());
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
//            listBox1.Items.Clear();
//            // ASK ABOUT
//            foreach (string str in products.ToString())
//        {
//            if (str.ToUpper().Contains(textBox1.Text.ToUpper()))
//            {
//                listBox1.Items.Add(str);
//            }
//        }
        }
        
        void Button3Click(object sender, EventArgs e)
        {
            AddSaleForm addSl = new AddSaleForm(this);
            addSl.Show();
            this.Hide();
        }
    }
}
