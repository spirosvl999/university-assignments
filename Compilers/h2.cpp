using namespace std;

#include <iostream>
#include <list>

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
    list<string> Tree_List;
    string string_a;
    int length_array;
    int i,  counter_s = 0, counter_e = 0;
    bool empty = false;
    bool correct_string;

    cout <<  "\n Give me the string you want us to analyse \n";
    cin >> (string_a);

    char* char_array = new char[string_a.length() + 1];                             // We create a new array of chars for the string we got to be able to work with it.

    char_array[string_a.length()] = '\0';                                           // We put \0 at the end of the array to tell thats the end of the chars.

    for (int i = 0; i < string_a.length(); i++) 
    {
        char_array[i] = string_a[i];                                                // We get each letter of the the string to the character array.
    }


    if (string_a.length() == 1 && char_array[0] == 'e')
    {
        empty = true;
    }
    else
    {
        i = 0;
        correct_string = true;
        while (correct_string == true && i < string_a.length())                    // We are finding out if the string can be created from our rules.
        {
            if (char_array[i] == '(')                                              // We are going to check for every char that we are able to get
            {                                                                      // the next one
                if(char_array[i+1] != 'a' && char_array[i+1] != 'b' && char_array[i+1] !='(')               
                {                                                                  // to see if the the final string
                    correct_string = false;                                        // can come from our grammar.
                }
                else
                {
                    counter_s++;
                }
            }
            else if(char_array[i] == ')')
            {
                counter_e++;
            }
            else if(char_array[i] == 'a' || char_array[i] == 'b')
            {
                if(char_array[i+1] != '+' && char_array[i+1] != '-' && char_array[i+1] != '*' && char_array[i+1] != ')')
                {
                    correct_string = false;
                }
            }
            else if (char_array[i] == '+' || char_array[i] == '-' || char_array[i] == '*')
            {
                if(char_array[i+1] != 'a' && char_array[i+1] != 'b' && char_array[i+1] != '(')
                {
                    correct_string = false;
                }
            }
            else
            {
                correct_string = false;
            }

            //i++;
            //cout << i;
        }
    }

    if(counter_s != counter_e)                                                      // If theres  more ( than )
    {
        correct_string = false;
    }

    if(correct_string == false)
    {
        cout << "\n String cant be made from our rules \n";
    }
    else                                                                           // If the string has been made from our rules, we have to check how it has been created.
    {
        if(empty == true)
        {
            cout << "The string is empty";
        }
        else
        {
            for(i=0; i<string_a.length(); i++)
            {
                if(char_array[i] == '(')
                {
                    if(i == 0)
                    {
                        Tree_List.push_back("G");
                    }
                    else
                    {
                        Tree_List.push_back("M");
                        Tree_List.push_back("Y");
                        Tree_List.push_back("G");
                    }
                }
                else if(char_array[i] == 'a' || char_array[i] == 'b')
                {
                    Tree_List.push_back("M");
                    Tree_List.push_back("Y");
                }
                else if(char_array[i] == '+' || char_array[i] == '-' || char_array[i] == '*')
                {
                    Tree_List.push_back("Z");
                }
            }
        }
    }

    cout << "\n The tree from we created the final string: \n";
    showlist(Tree_List);

}
