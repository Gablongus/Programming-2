/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/23/2025
 * Time: 3:10 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Lang54d_Console
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter Base:");
            double b = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter Height:");
            double h = double.Parse(Console.ReadLine());
            
            double hyp = Math.Round(Math.Sqrt((b * b) + (h * h)), 2);
            Console.WriteLine("Hypotenuse = "+ hyp);
            Console.ReadLine();
                
          
        }
    }
}