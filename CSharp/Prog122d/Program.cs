/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/12/2025
 * Time: 2:34 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Prog122d
{
    class Program
    {
        public static void Main(string[] args)
        {
            for (int x = -12; x <= 16; x++){
                double y = (Math.Pow(x, 6)-3*Math.Pow(x, 5)-93*Math.Pow(x, 4)+87*Math.Pow(x,3)+1596*Math.Pow(x,2)-1380*x-2800);
                Console.WriteLine(x + "\t" + y);
            }
            Console.ReadLine();
        }
    }
}