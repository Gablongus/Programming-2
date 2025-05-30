/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/28/2025
 * Time: 3:06 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System.Collections.Generic;

public class Product {
    public static List<Product> products = new List<Product>();
    	private string strName;
    	private string strModType;
		private int intAmount;
		private double dblPrice;
		private string strDate;
		
		public Product(string ModType, string Name, int Amount, double Price, string Date){
    		strName = Name;
    		strModType = ModType;
    		intAmount = Amount;
    		dblPrice = Price;
    		strDate = Date;
			
    			
    	}
		
		public string GetName() {
			return strName;
		}
		public string GetType() {
			return strModType;
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
		public void SetType(string ModType) {
			strModType = ModType;
		}
		public override string ToString(){
		    return string.Format(strModType + "\t" + strName + "\t\t" + intAmount + "\t" + dblPrice + "\t" + strDate);
		}
		
		
		
    	
    }