/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 4/22/2025
 * Time: 3:22 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Lang54c_Console
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter Radius");
            double radius = double.Parse(Console.ReadLine());
            double Pi = 3.14159;
            double Diameter =  radius * 2;
            double Area = Math.Round(Pi * (radius * radius),3);
            double Circum = Math.Round(2 * Pi * radius, 3);
            Console.WriteLine("Diameter = " + Diameter);
            Console.WriteLine("Area = " + Area);
            Console.WriteLine("Circumference = " + Circum);
            
            Console.ReadLine();
            
        }
    }
}