﻿/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/12/2025
 * Time: 2:43 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace StrInterview7 {
    class Program {
        public static void Main(string[] args) {
            Console.Write("Enter a string: ");
            string word = Console.ReadLine().ToLower();
            
            int v = 0;
            int c = 0;
            
            for (int i = 0; i < word.Length; i++) {
                char let = word[i];
                if (let == 'a' || let == 'e' || let == 'i' || let == 'o' || let == 'u' )
                    v++;
                else if (let >= 'a' && let <= 'z') c++; // Check ASCII range
            }
            
            Console.WriteLine("{0} contains {1} vowels and {2} consonants",
                              word, v, c);
            Console.ReadLine();
        }
    }
}