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
        private ManagerForm myParent;
    
            
        public AddProductForm(ManagerForm myParent) {
            this.myParent = myParent;
            InitializeComponent();
        }
        
        void Button1Click(object sender, EventArgs e)
        {
        	try
        	{
	        	string ProdName = textBox1.Text;
	        	int StartAmount = int.Parse(textBox2.Text);
	        	double Price = double.Parse(textBox6.Text);
	        	string Date = (textBox3.Text + "/" + textBox4.Text + "/" + textBox5.Text);
	        	
	        	
	        	this.myParent.ProductName = ProdName;
        		this.myParent.Amount = StartAmount;
        		this.myParent.CurrentPrice = Price;
        		this.myParent.DateInput = Date;
        		this.myParent.ModType = "NewProduct:";
        		this.myParent.SellingProduct = false;
        		this.myParent.AddingProduct = true;
        		myParent.ManagerFormLoad(null, null);
	        	myParent.Show();
	        	this.Hide();
        	}
        	catch
        	{
        		MessageBox.Show("Invalid Inputs");
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
