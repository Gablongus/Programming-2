/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/23/2025
 * Time: 3:01 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
namespace Final_Project_Inventory
{
    partial class AddProductForm
    {
        /// <summary>
        /// Designer variable used to keep track of non-visual components.
        /// </summary>
        private System.ComponentModel.IContainer components = null;
        
        /// <summary>
        /// Disposes resources used by the form.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing) {
                if (components != null) {
                    components.Dispose();
                }
            }
            base.Dispose(disposing);
        }
        
        /// <summary>
        /// This method is required for Windows Forms designer support.
        /// Do not change the method contents inside the source code editor. The Forms designer might
        /// not be able to load this method if it was changed manually.
        /// </summary>
        private void InitializeComponent()
        {
        	this.label1 = new System.Windows.Forms.Label();
        	this.label2 = new System.Windows.Forms.Label();
        	this.textBox1 = new System.Windows.Forms.TextBox();
        	this.label3 = new System.Windows.Forms.Label();
        	this.textBox2 = new System.Windows.Forms.TextBox();
        	this.button1 = new System.Windows.Forms.Button();
        	this.label4 = new System.Windows.Forms.Label();
        	this.textBox3 = new System.Windows.Forms.TextBox();
        	this.textBox4 = new System.Windows.Forms.TextBox();
        	this.textBox5 = new System.Windows.Forms.TextBox();
        	this.label5 = new System.Windows.Forms.Label();
        	this.label6 = new System.Windows.Forms.Label();
        	this.label7 = new System.Windows.Forms.Label();
        	this.label8 = new System.Windows.Forms.Label();
        	this.textBox6 = new System.Windows.Forms.TextBox();
        	this.button2 = new System.Windows.Forms.Button();
        	this.SuspendLayout();
        	// 
        	// label1
        	// 
        	this.label1.BackColor = System.Drawing.Color.AliceBlue;
        	this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label1.Location = new System.Drawing.Point(90, 9);
        	this.label1.Name = "label1";
        	this.label1.Size = new System.Drawing.Size(244, 45);
        	this.label1.TabIndex = 0;
        	this.label1.Text = "Add A Product";
        	this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
        	// 
        	// label2
        	// 
        	this.label2.BackColor = System.Drawing.Color.LightCyan;
        	this.label2.Font = new System.Drawing.Font("Microsoft YaHei", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label2.Location = new System.Drawing.Point(24, 78);
        	this.label2.Name = "label2";
        	this.label2.Size = new System.Drawing.Size(190, 91);
        	this.label2.TabIndex = 1;
        	this.label2.Text = "Enter Product Name:";
        	// 
        	// textBox1
        	// 
        	this.textBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.textBox1.Location = new System.Drawing.Point(42, 124);
        	this.textBox1.Name = "textBox1";
        	this.textBox1.Size = new System.Drawing.Size(153, 31);
        	this.textBox1.TabIndex = 2;
        	// 
        	// label3
        	// 
        	this.label3.BackColor = System.Drawing.Color.LightCyan;
        	this.label3.Font = new System.Drawing.Font("Microsoft YaHei", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label3.Location = new System.Drawing.Point(24, 187);
        	this.label3.Name = "label3";
        	this.label3.Size = new System.Drawing.Size(190, 91);
        	this.label3.TabIndex = 3;
        	this.label3.Text = "Enter Starting Amount of Product:";
        	// 
        	// textBox2
        	// 
        	this.textBox2.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.textBox2.Location = new System.Drawing.Point(42, 232);
        	this.textBox2.Name = "textBox2";
        	this.textBox2.Size = new System.Drawing.Size(153, 31);
        	this.textBox2.TabIndex = 4;
        	// 
        	// button1
        	// 
        	this.button1.BackColor = System.Drawing.Color.LightCyan;
        	this.button1.Font = new System.Drawing.Font("Microsoft YaHei", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.button1.Location = new System.Drawing.Point(325, 294);
        	this.button1.Name = "button1";
        	this.button1.Size = new System.Drawing.Size(95, 91);
        	this.button1.TabIndex = 5;
        	this.button1.Text = "Add";
        	this.button1.UseVisualStyleBackColor = false;
        	this.button1.Click += new System.EventHandler(this.Button1Click);
        	// 
        	// label4
        	// 
        	this.label4.BackColor = System.Drawing.Color.LightCyan;
        	this.label4.Font = new System.Drawing.Font("Microsoft YaHei", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label4.Location = new System.Drawing.Point(230, 78);
        	this.label4.Name = "label4";
        	this.label4.Size = new System.Drawing.Size(190, 200);
        	this.label4.TabIndex = 6;
        	this.label4.Text = "Date(in numbers):";
        	// 
        	// textBox3
        	// 
        	this.textBox3.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.textBox3.Location = new System.Drawing.Point(249, 119);
        	this.textBox3.Name = "textBox3";
        	this.textBox3.Size = new System.Drawing.Size(146, 31);
        	this.textBox3.TabIndex = 7;
        	// 
        	// textBox4
        	// 
        	this.textBox4.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.textBox4.Location = new System.Drawing.Point(249, 176);
        	this.textBox4.Name = "textBox4";
        	this.textBox4.Size = new System.Drawing.Size(146, 31);
        	this.textBox4.TabIndex = 8;
        	// 
        	// textBox5
        	// 
        	this.textBox5.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.textBox5.Location = new System.Drawing.Point(249, 232);
        	this.textBox5.Name = "textBox5";
        	this.textBox5.Size = new System.Drawing.Size(146, 31);
        	this.textBox5.TabIndex = 9;
        	// 
        	// label5
        	// 
        	this.label5.BackColor = System.Drawing.Color.LightCyan;
        	this.label5.Font = new System.Drawing.Font("Microsoft YaHei", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label5.Location = new System.Drawing.Point(293, 155);
        	this.label5.Name = "label5";
        	this.label5.Size = new System.Drawing.Size(59, 20);
        	this.label5.TabIndex = 10;
        	this.label5.Text = "Day:";
        	this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
        	// 
        	// label6
        	// 
        	this.label6.BackColor = System.Drawing.Color.LightCyan;
        	this.label6.Font = new System.Drawing.Font("Microsoft YaHei", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label6.Location = new System.Drawing.Point(294, 98);
        	this.label6.Name = "label6";
        	this.label6.Size = new System.Drawing.Size(59, 20);
        	this.label6.TabIndex = 11;
        	this.label6.Text = "Month:";
        	this.label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
        	// 
        	// label7
        	// 
        	this.label7.BackColor = System.Drawing.Color.LightCyan;
        	this.label7.Font = new System.Drawing.Font("Microsoft YaHei", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label7.Location = new System.Drawing.Point(294, 210);
        	this.label7.Name = "label7";
        	this.label7.Size = new System.Drawing.Size(59, 20);
        	this.label7.TabIndex = 12;
        	this.label7.Text = "Year:";
        	this.label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
        	// 
        	// label8
        	// 
        	this.label8.BackColor = System.Drawing.Color.LightCyan;
        	this.label8.Font = new System.Drawing.Font("Microsoft YaHei", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.label8.Location = new System.Drawing.Point(24, 294);
        	this.label8.Name = "label8";
        	this.label8.Size = new System.Drawing.Size(190, 91);
        	this.label8.TabIndex = 13;
        	this.label8.Text = "Enter Starting Price of Product:";
        	// 
        	// textBox6
        	// 
        	this.textBox6.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.textBox6.Location = new System.Drawing.Point(42, 342);
        	this.textBox6.Name = "textBox6";
        	this.textBox6.Size = new System.Drawing.Size(153, 31);
        	this.textBox6.TabIndex = 14;
        	// 
        	// button2
        	// 
        	this.button2.BackColor = System.Drawing.Color.LightPink;
        	this.button2.Font = new System.Drawing.Font("Microsoft YaHei", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
        	this.button2.Location = new System.Drawing.Point(224, 294);
        	this.button2.Name = "button2";
        	this.button2.Size = new System.Drawing.Size(95, 91);
        	this.button2.TabIndex = 15;
        	this.button2.Text = "Cancel";
        	this.button2.UseVisualStyleBackColor = false;
        	// 
        	// AddProductForm
        	// 
        	this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
        	this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        	this.BackColor = System.Drawing.Color.Azure;
        	this.ClientSize = new System.Drawing.Size(432, 397);
        	this.Controls.Add(this.button2);
        	this.Controls.Add(this.textBox6);
        	this.Controls.Add(this.label8);
        	this.Controls.Add(this.label7);
        	this.Controls.Add(this.label6);
        	this.Controls.Add(this.label5);
        	this.Controls.Add(this.textBox5);
        	this.Controls.Add(this.textBox4);
        	this.Controls.Add(this.textBox3);
        	this.Controls.Add(this.label4);
        	this.Controls.Add(this.button1);
        	this.Controls.Add(this.textBox2);
        	this.Controls.Add(this.label3);
        	this.Controls.Add(this.textBox1);
        	this.Controls.Add(this.label2);
        	this.Controls.Add(this.label1);
        	this.Name = "AddProductForm";
        	this.Text = "AddProductForm";
        	this.ResumeLayout(false);
        	this.PerformLayout();
        }
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.TextBox textBox6;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox textBox5;
        private System.Windows.Forms.TextBox textBox4;
        private System.Windows.Forms.TextBox textBox3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
    }
}
