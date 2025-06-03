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
        
        public int StartingAmount {get; set;}
        public string ProductName {get; set;}
        public int Amount {get; set;}
        public double CurrentPrice {get; set;}
        public string DateInput {get; set;}
        public string ModType {get; set;}
        
        public int Index {get; set;}
        public int AmountSold {get; set;}
        public double MoneyGained {get; set;}
        
        public int AmountGained {get; set;}
        
        public bool AddingProduct {get; set;}
        public bool SellingProduct {get; set;}
        public bool RestockingProduct {get; set;}
        public bool AdjustingPrice {get; set;}
        
        
    
        
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
        	Product.products.Add(new Product(ModType, ProductName, StartingAmount, CurrentPrice, DateInput));
        	listBox1.Items.Add(Product.products[Product.products.Count-1].ToString());
            }
            if (SellingProduct == true) {
                Product.products.Add(new Product(ModType, ProductName, Amount, CurrentPrice, DateInput));
                listBox1.Items.Add(Product.products[Product.products.Count-1].ToString());
                //listBox1.Items.Add(ModType + "(" + AmountSold + ")\t" + Product.products[Index].ToString());
            }
            if (RestockingProduct == true) {
                Product.products.Add(new Product(ModType, ProductName, Amount, CurrentPrice, DateInput));
                listBox1.Items.Add(Product.products[Product.products.Count-1].ToString());
                //listBox1.Items.Add(ModType + "(" + AmountSold + ")\t" + Product.products[Index].ToString());
            }
            if (AdjustingPrice == true) {
               Product.products.Add(new Product(ModType, ProductName, Amount, CurrentPrice, DateInput));
               listBox1.Items.Add(Product.products[Product.products.Count-1].ToString());
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
            listBox1.Items.Add("Modification Type  " +"\t" + "Product Name"+ "\t" +"Amount"+ "\t" +"Price"+ "\t" +"Date");
            listBox1.Items.Add("----------------------------------------------------------");
            
            // ASK ABOUT
            foreach (Product P in Product.products)
                if (P.GetName().StartsWith(textBox1.Text, StringComparison.CurrentCultureIgnoreCase)){

                listBox1.Items.Add(P);
            }
                
        }
        
        void Button3Click(object sender, EventArgs e)
        {
            AddSaleForm addSl = new AddSaleForm(this);
            addSl.Show();
            this.Hide();
        }
        
        void Button6Click(object sender, EventArgs e)
        {
            RestockForm Res = new RestockForm(this);
            Res.Show();
            this.Hide();
        }
        
        void Button5Click(object sender, EventArgs e)
        {
            AdjustPriceForm Adj = new AdjustPriceForm(this);
            Adj.Show();
            this.Hide();
        }
        
        void Button2Click(object sender, EventArgs e)
        {
            ViewSalesForm VSF = new ViewSalesForm(this);
            VSF.Show();
            this.Hide();
        }
    }
}
