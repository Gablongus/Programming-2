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
            Console.WriteLine("Enter package weight in kilograms: ");
            double weight = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter package length in centimeters: ");
            double length = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter package width in centimeters: ");
            double width = double.Parse(Console.ReadLine());
            Console.WriteLine("Enter package height in centimeters: ");
            double height = double.Parse(Console.ReadLine());
            double vol = length * width * height;
            string msg = "Package Accepted";
            if (vol > 100000)            {
                msg = ("Too large");
                if (weight > 27) {
                    msg = ("Too heavy and too large");
                }
            } else if (weight > 27) {
                msg = ("Too heavy");
            }
            Console.WriteLine(msg);
            Console.ReadLine();
                
        }
    }
}