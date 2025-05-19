/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/19/2025
 * Time: 2:35 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace StrInterview8
{
    class Program
    {
        static int Count(string stringaling, char find)
        {
            return stringaling.Split(find).Length - 1;
        }
        

        public static void Main(string[] args)
        {
            Console.WriteLine("Enter String");
            string str = Console.ReadLine();
            Console.WriteLine("Enter Charecter to be found");
            char cha = Convert.ToChar(Console.ReadLine());
            int num = Count(str, cha);
            Console.WriteLine(str + " contains " + cha + " " +num + " time(s).");
            
            
            Console.ReadLine();
            
        }
    }
}