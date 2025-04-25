/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/25/2025
 * Time: 2:38 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace LP4_1_Console
{
    class Program
    {
        public static void Main(string[] args)
        {
            ﻿Console.Write("Enter # of copies to print: ");
            int copies = int.Parse(Console.ReadLine());
            double price = 0;
            double cost = 0;
            // && AND, || OR, ! NOT
            if (copies > 0 && copies <= 99)         price = 0.30;
            else if (copies > 99 && copies <= 499)  price = 0.28;
            else if (copies > 499 && copies <= 749) price = 0.27;
            else if (copies > 750 && copies <= 1000) price = 0.26;
            else if (copies > 1000) price = 0.25;
           
            else Console.WriteLine("Invalid number of copies!");
            cost = price * copies;
            Console.WriteLine("Price per copy is: " + price);
            Console.WriteLine("Total cost is: " + cost);
            
            Console.ReadLine();
            
        }
    }
}