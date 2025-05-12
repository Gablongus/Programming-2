/*
 * Created by SharpDevelop.
 * User: schraedl.g
 * Date: 5/12/2025
 * Time: 2:57 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace StrInterview16 {
    class Program {
        static bool searchText(string text, string search) {
            int tLen = text.Length;
            int sLen = search.Length;
            
            if (sLen > tLen) return false;
            
            for (int i = 0;i <= tLen - sLen; i++)
                // if (text[i.ToString.(i + sLen)] == search) return true; // text[i:i+sLen]
                if (text.Substring(i, sLen) == search) return true;
            // Substring uses startIndex, length (not endIndex)
            return false;
        }
        public static void Main(string[] args) {
            Console.Write("Enter a string: ");
            string text = Console.ReadLine();
            Console.Write("Enter a substring to search for: ");
            string word = Console.ReadLine();
            bool result = searchText(text, word);
            Console.WriteLine("Does \"{0}\" contain \"{1}\"?: {2}", text, word, result);
            Console.ReadLine();
        }
    }
}