#include<iostream>
#include <random>
#include <functional>
#include "ll_array.h"

using namespace std;

int main()
{
    default_random_engine generator;
    uniform_int_distribution<int> list_size_distribution(1, 10);
    uniform_int_distribution<int> data_element_distribution(0, 30);

    auto random_list_size = bind(list_size_distribution, generator);
    auto random_element = bind(data_element_distribution, generator);
    
    int k,i,j,z,y,lenght,element, element_count_on_list[50], element_count[50]={};



    cout<<"poses listes 8es?\n";
    cin>>k;
    cout<<"wraia file, twra ftiaxnonte " << k << " listes\n";



    Chain<Chain<int>*>main_list;
    Chain<int> *list;
        
    for(i=0;i<k;i++) //~~~Gemizoume tis listes~~~
    {
        list = new Chain<int>;
        z=random_list_size();
        for(j=0;j<z;j++)
        {
            y=random_element();
            (*list).Insert(j,y);
        }
        main_list.Insert(i,list);
    }

    Chain<int>output; //Dhmiourgia listas output

    for(i=1;i<=k;i++)
    {
        main_list.Find(i,list);
        lenght=(*list).Length();
        for(j=0;j<51;j++)
        {
            element_count_on_list[j]=0; //To element_count_on_list mhdenizete oloklhro gia ka8e lista
        }
        for(j=1;j<=lenght;j++)
        {
            (*list).Find(j,element);
            element_count_on_list[element]=element_count_on_list[element]+1; //Gia ka8e fora pou vriskei ena stoixeio, afksanei kata 1 to count gia to antistixo stoixeio
        }
        for(j=0;j<51;j++)
        {
            if(element_count_on_list[j]>=1)
            {
                element_count[j]=element_count[j]+1; //afksanete kata 1 to plh8os ka8e fora pou uparxei ston pinaka to stoixeio
            }
        }
    }

    for(i=0;i<51;i++)
    {
        if(element_count[i]>=(k/2))
        {
            output.Insert(output.Length(),i);
        }
    }

    cout<<output;

    return 0;
}
