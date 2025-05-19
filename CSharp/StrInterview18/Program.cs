/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/19/2025
 * Time: 3:06 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace StrInterview18
{
    class Program
    {
 
        
        public static void Main(string[] args)
        {
            Console.WriteLine("Enter A String");
            string ogstr = Console.ReadLine();
            string str = ogstr;
            Console.WriteLine("Enter Charecter to be removed");
            string cha = (Console.ReadLine());
            str = str.Replace(cha, "");
            Console.WriteLine(ogstr + " without cha " + cha + " is: " + str);
            
            
            Console.ReadLine();
        }
    }
}