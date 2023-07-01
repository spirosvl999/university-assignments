using namespace std;

#include <iostream>
#include <list>
#include <random>                                                                   // Random and ctime are included to make sure our
#include <ctime>                                                                    // final string is totally randomized.

void showlist(list<string> a)
{                                                                                   // Creating a function to print the list.

    while (a.empty() != 1)
    {
        cout << a.front();
        a.pop_front();
    }
    cout << "\n";
}

int main()
{
    list<string> Output_List;
    bool Flag  {false};
    int count_Z = 0;                                                                // Z-Counter is used to fill the end of the list with the amount of ) needed.
    int path_G, path_M,i;
    int M_Needed = 0;
    string path = "Z";                                                              // The path starts from Z.
    
    while(Flag == false)
    {
        if(path == "Z")
        {
            Output_List.push_back("(");                                             // Because we Z starts with ( before all.
            path = "K";
            count_Z+=1;                                                             // I Use count Z to make sure we don't miss any ) at the end.
        }
        if(path == "K")
        {
            path = "G";
        }
        if(path == "G")
        {
            srand((unsigned) time(0));                                              // G has 2 options, using random fanction to make sure it's complitely random.
            path_G = rand() % 2;
            if(path_G == 0)
            {
                Output_List.push_back("v");
                path = "M";
            }
            else
            {
                path = "Z";
                M_Needed+=1;                                                        // Using M_Needed to make sure that none M's are missing.
            }
        }
        if(path == "M")
        {
            srand((unsigned) time(0));                                              // At the M, we have 3 options. Selecting a path complitely randomly.
            path_M = rand() % 3;
            if(path_M == 0)
            {
                Output_List.push_back("-");
                path = "K";
                M_Needed+=1;                                                        // Using again M_Needed.
            }
            else if(path_M == 1)
            {
                Output_List.push_back("+");
                path = "K";
                M_Needed+=1;                                                        // Using again M_Needed.
            }
            else
            {
                if(M_Needed>=1)
                {
                    path = "M";
                    M_Needed-=1;                                                    // In this case, we still have to go back at an other part of the program.
                }
                else
                {
                    Flag = true;                                                    // When M_Needed is finally 0, loop is finieshed and the output is almost ready.
                }
            }
        }
    }
    for(i=1; i<= count_Z; ++i)                                                      // Using the count_Z, Im putting the ) inside the output list.
    {
        Output_List.push_back(")");
    }

    cout << "\n The output of the program is\n";                                    // Printing the output.
    showlist(Output_List);

}