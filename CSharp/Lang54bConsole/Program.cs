namespace Lang52aConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter num1: ");
            int num1 = int.Parse(Console.ReadLine());
            Console.Write("Enter num2: ");
            int num2 = int.Parse(Console.ReadLine());
            Console.Write("Enter num3: ");
            int num3 = int.Parse(Console.ReadLine());
            Console.Write("Enter num4: ");
            int num4 = int.Parse(Console.ReadLine());
            
            int sum = num1 + num2 + num3 + num4;
            double average = sum / 4;
            Console.WriteLine("Sum: " + sum);
            Console.WriteLine("Average: " + average);
            Console.ReadLine();

        }
    }
}