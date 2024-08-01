using System;

class Program
{
    static void Main()
    {
        for (int i = 0; i < 3; i++)
        {
            Console.WriteLine("Húrá po {0}!", i);
        }

        // Pridanie ďalšieho výpisu
        Console.WriteLine("Cyklus for skončil.");

        Console.ReadKey();
    }
}
