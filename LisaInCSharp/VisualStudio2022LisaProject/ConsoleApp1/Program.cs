using System;
using AIMLbot;

namespace Lisa 
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Bot AI = new Bot(); 
            AI.loadSettings();
            AI.loadAIMLFromFiles(); 
            AI.isAcceptingUserInput = false;
            User myUser = new User("User", AI); 
            AI.isAcceptingUserInput = true;
            while (true)
            { 
                Console.Write("User: ");
                string? inq = Console.ReadLine();
                Request r = new Request(inq, myUser, AI);                
                Result res = AI.Chat(r);
                Console.WriteLine("Lisa: "+ res.Output.ToUpper());
                Console.WriteLine("");
            } 
        }
    }
}