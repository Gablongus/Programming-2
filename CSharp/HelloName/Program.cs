﻿using System.Text;
using System.Threading.Tasks;  

namespace HelloName
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name);

            Console.Write("Enter your age: ");
            int age = int.Parse(Console.ReadLine());
            Console.WriteLine("You are " + age + " years old!");

            Console.ReadKey();
        }
    }
}