using System.Text;
using System.Threading.Tasks;

namespace Lang52aConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter length: ");
            int len = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter width: ");
            int wid = int.Parse(Console.ReadLine());
            int area = len * wid;
            int perim = 2 * len + 2 * wid;
            Console.WriteLine("Area: " + area);
            Console.WriteLine("Perimeter: " + perim);
            Console.ReadKey();
        }
    }
}