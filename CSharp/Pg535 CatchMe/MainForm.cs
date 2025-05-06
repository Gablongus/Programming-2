using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Pg535_CatchMe
{
    /// <summary>
    /// Description of MainForm.
    /// </summary>
    public partial class MainForm : Form
    {
        private string[] strCaption  = {"Click here", "Try Harder!",
                                                "Try again", "Not even close",
                                                "Where are you?", "I'm over here!",
                                                "Slow, aren't you?"};
        private Random rand = new Random();
        
        public MainForm() 
        {
            InitializeComponent();
            //
            // TODO: Add constructor code after the InitializeComponent() call.
            //
        }
        
        
        
        void Button1Click(object sender, EventArgs e){
            MessageBox.Show("You got me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();
        }
        

        
        void Button1MouseEnter(object sender, EventArgs e) {
            // Randomly choose a caption
            int intIndex = rand.Next(strCaption.Length);
            button1.Text = strCaption[intIndex];
            button1.Left = rand.Next(this.Width - button1.Width);
            button1.Top  = rand.Next(this.Height - button1.Height - 30);
        }
    }
}