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
        private Form myParent;
    
            
        public AddProductForm(Form myParent) {
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
	        	
	        	ManagerForm mngForm = new ManagerForm(this);
	        	mngForm.ProductName = ProdName;
        		mngForm.StartingAmount = StartAmount;
        		mngForm.CurrentPrice = Price;
        		mngForm.DateInput = Date;
        		mngForm.AddingProduct = true;
	        	myParent.Show();
	        	this.Hide();
        	}
        	catch
        	{
        		MessageBox.Show("Invalid Inputs");
        	}
	        	
        		
        }
    }
}
