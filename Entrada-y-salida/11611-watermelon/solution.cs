using System;

string input = Console.ReadLine();

if(int.TryParse(input, out int w))
{
    if(w > 2 && w % 2 == 0)
    {
        Console.WriteLine("SI");
    }
    else
    {
        Console.WriteLine("NO");
    }
}