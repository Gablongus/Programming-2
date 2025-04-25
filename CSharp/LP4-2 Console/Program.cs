/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/25/2025
 * Time: 3:19 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace LP4_2_Console
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter package weight: ");
            double weight = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter package length: ");
            double length = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter package width: ");
            double width = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter package height: ");
            double height = double.Parse(Console.ReadLine());
            Console.ReadLine();
        }
    }
}