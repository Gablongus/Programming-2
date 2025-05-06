/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/6/2025
 * Time: 2:33 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace CalcWithFunctions
{
    class Program
    {
        
        public static void Main(string[] args)
        {
            // <access level> <static or not> <return type> name(<args>) {}
            // In console apps, we'll make all functions "static"
            // Not static in Forms apps; always "public" though
            
            
            
            Console.WriteLine("Hello World!");
            
            
        }
        
        static int add(int x, int y) { 
            return x + y; 
        }
        static int sub(int x, int y) { return x - y; }
        static int mul(int x, int y) { return x * y; }
        static int div(int x, int y) { return x / y; }
        
        static void wait() { //Void means "returns nothing"
            
        }
    }
}