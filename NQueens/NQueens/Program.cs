using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NQueens
{
    class Program
    {

        public static int n = 10;
        public static Dictionary<int, int[]> result = new Dictionary<int, int[]>();

        public static bool CheckRow(int[,] board, int x, int y)
        {
            Dictionary<int, bool> cont = new Dictionary<int, bool>();

            Parallel.For(0, n, i =>
            {
                if (y != i)
                {
                    if (board[x, i] == 1)
                    {
                        cont.Add(i, false);
                    }
                }
            });

            if (cont.Count() > 0)
            {
                return false;
            }
            /*
            for(int i = 0; i<n; i++) {
                if(y!=i) {
                    if(board[x,i] == 1) {
                        return false;
                    }
                }
            }
            */
            return true;
        }

        public static bool CheckCol(int[,] board, int x, int y)
        {
            Dictionary<int, bool> cont = new Dictionary<int, bool>();

            Parallel.For(0, n, i =>
            {
                if (x != i)
                {
                    if (board[i, y] == 1)
                    {
                        cont.Add(i, false);
                    }
                }
            });

            if (cont.Count() > 0)
            {
                return false;
            }

            /*
            for (int i = 0; i < n; i++)
            {
                if (x != i)
                {
                    if (board[i,y] == 1)
                    {
                        return false;
                    }
                }
            }*/
            return true;
        }

        public static bool CheckF(int[,] board, int x1, int x2, int y1, int y2)
        {
            if (x1 < n && y1 < n)
            {
                if (board[x1,y1] == 1)
                {
                    return false;
                }
            }
            if (x2 >= 0 && y1 < n)
            {
                if (board[x2,y1] == 1)
                {
                    return false;
                }
            }
            if (x1 < n && y2 >= 0)
            {
                if (board[x1,y2] == 1)
                {
                    return false;
                }
            }
            if (x2 >= 0 && y2 >= 0)
            {
                if (board[x2,y2] == 1)
                {
                    return false;
                }
            }
            return true;
        }

        public static bool CheckDiag(int[,] board, int x, int y)
        {
            /*
            Map<Integer, Boolean> cont = new HashMap<Integer, Boolean>();

            IntStream range = IntStream.range(0, n);
            range.parallel().forEach(i->{
                */
            Dictionary<int, bool> cont = new Dictionary<int, bool>();

            Parallel.For(0, n, i =>
             {
                 int x1 = x + (i + 1);
                 int x2 = x - (i + 1);
                 int y1 = y + (i + 1);
                 int y2 = y - (i + 1);

                 if (!CheckF(board, x1, x2, y1, y2))
                 {
                     cont.Add(i, false);
                 }
             });

            if(cont.Count()> 0)
            {
                return false;
            }
            return true;

            /*
                Boolean con = true;
                //System.out.println("Thread: " + Thread.currentThread().getName() + " " + i);
                int x1 = x + (i + 1);
                int x2 = x - (i + 1);
                int y1 = y + (i + 1);
                int y2 = y - (i + 1);

                if (!CheckF(board, x1, x2, y1, y2))
                {
                    con = false;
                }

                cont.put(i, con);
            });

            for (Map.Entry<Integer, Boolean> entries : cont.entrySet())
            {
                if (entries.getValue() == false)
                {
                    return false;
                }
            }
            return true;
            */
        }


        public static bool Solve(int[,] board, int col)
        {
            if (col == n)
            {
                int[] v = new int[n];
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        if (board[i,j] == 1)
                        {
                            v[i] = j + 1;
                        }
                    }
                }


                int size;
                try
                {
                    size = result.Count;
                }
                catch (Exception e)
                {
                    size = 0;
                }

                result.Add(size, v);
                return true;
            }
            bool res = false;


            for (int i = 0; i < n; i++)
            {
                //System.out.println(board.length  + " " + col);
                bool c1 = CheckRow(board, i, col);
                bool c2 = CheckCol(board, i, col);
                bool c3 = CheckDiag(board, i, col);

                if (c1 && c2 && c3)
                {
                    board[i,col] = 1;
                    res = Solve(board, col + 1) || res;
                    board[i,col] = 0;
                }
            }

            return res;
        }

        static void Main(string[] args)
        {
            int[,] board = new int[n,n];

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    board[i,j] = 0;
                }
            }

            Solve(board, 0);
            
            Console.WriteLine("Result:");
            foreach(var element in result)
            {
                Console.Write("[");
                for (int i = 0; i < element.Value.Count(); i++)
                {
                    Console.Write(element.Value[i]);
                    if (i != element.Value.Count() - 1)
                        Console.Write(",");
                }
                Console.Write("]\n");
            }

            Console.ReadLine();

        }
    }
}
