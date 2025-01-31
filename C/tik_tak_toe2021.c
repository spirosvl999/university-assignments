#include <stdio.h>
#include <stdlib.h>

void print_g(char table[3][3]);
int winable(char table[3][3]);

void main()
{
    int a,lul,i,y,player=1,w1,w2,check; 
    char table[3][3],mark;
    for (i=0;i<3;i++)
    {
        for (y=0;y<3;y++)
        {
         table[i][y] =' ';
        }
    }
    printf("1.Two players\n2.Player VS Computer?\n");
    scanf("%d", &lul);
    if (lul==1) //pevepe//
    {
        w1=0;
        w2=0;
        i=69;   
        do
        {
            do
            {
	            printf("Player %d, enter a number ( 1 - 9 ): ", player);
		        scanf("%d", &a);
	        }while (a <1 || a > 9); 
            if (player==0 || player==2)
		    {
                player=1;
            }
	        else
		    {
                player=2;
            } 
	        if (player==1)
            {
                mark='X';
            }
	        else 
            {
		        mark='O';
            }
            if (a==1){
                if (table[0][0]==' ')
                {
                    table[0][0]=mark;
                    check=0;
                }
                else
                {
                    printf("space already occupied,try again\n");
                    check=1;
                }
        
            }
                else if (a==2){
                    if (table[0][1]==' '){
                        table[0][1]=mark;
                        check=0;
                    }
                    else
                    {
                        printf("space already occupied,try again\n");
                        check=1;
                    }
                }
                else if (a==3){
                    if (table[0][2]==' '){
                        table[0][2]=mark;
                        check=0;
                    }
                    else
                    {
                        printf("space already occupied,try again\n");
                        check=1;
                    }
                }
                else if (a==4){
                    if (table[1][0]==' '){
                       table[1][0]=mark;
                       check=0;
                    }
                    else
                    {
                        printf("space already occupied,try again\n");
                        check=1;
                    }        
                }
                else if (a==5){
                    if (table[1][1]==' '){
                        table[1][1]=mark;
                        check=0;
                    }
                    else
                    {
                        printf("space already occupied,try again\n");
                        check=1;
                    }
                }
                else if (a==6){
                    if (table[1][2]==' '){
                        table[1][2]=mark;
                        check=0;
                    }
                    else
                    {
                        printf("space already occupied,try again\n");
                        check=1;
                    }
                }
                else if (a==7){
                    if (table[2][0]==' '){
                        table[2][0]=mark;
                        check=0;
                    }
                    else
                    {
                        printf("space already occupied,try again\n");
                        check=1;
                    }
                }
                else if (a==8){
                    if (table[2][1]==' '){
                       table[2][1]=mark;
                        check=0;
                    }
                    else
                    {
                        printf("space already occupied,try again\n");
                        check=1;
                    }
                }
                else if (a==9){
                    if (table[2][2]==' '){
                        table[2][2]=mark;
                        check=0;
                    }
                    else
                    {
                    printf("space already occupied,try again\n");
                    check=1;
                    }
            }
            if (check==0)
            {
                i=winable(table);
            }
            print_g(table);
        }while(i!=69);
            print_g(table);
            if (i==10)
            {
                w1=w1+1;      
            }
            else if (i==11)
            {
                w2=w2+1;
            }
            printf("score is %d - %d\n", w1, w2);
        }
        else
        {
        //den to exeis kanei akoma blaka int computer();
        }
}
   
/*-----------------------------------------------------------------------
||OLES OI SUNARTHSEIS APO EDW K KATW SKRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR||
 ------------------------------------------------------------------------*/

void print_g(char table[3][3])
{
    printf("     |     |     \n");
    printf("  %c  |  %c  |  %c \n", table[2][0],table[2][1],table[2][2]);

    printf("_____|_____|_____\n");
    printf("     |     |     \n");

    printf("  %c  |  %c  |  %c \n", table[1][0],table[1][1],table[1][2]);

    printf("_____|_____|_____\n");
    printf("     |     |     \n");

    printf("  %c  |  %c  |  %c \n", table[0][0],table[0][1],table[0][2]);

    printf("     |     |     \n\n");
}

int winable(char table[3][3])
{
    if (table[0][0] == table[0][1] && table[0][1] == table[0][2])
    {
        if (table[0][0] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[0][0] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    }   
    else if (table[0][0] == table[1][1] && table[1][1] == table[2][2])
    {
       if (table[0][0] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[0][0] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    }   
        
    else if (table[0][0] == table[1][0] && table[1][0] == table[2][0])
    {
        if (table[0][0] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[0][0] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    }   
        
     else if (table[0][1] == table[1][1] && table[1][1] == table[2][1])
    {
        if (table[0][1] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[0][1] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    }   
    else if (table[1][0] == table[1][1] && table[1][1] == table[1][02])
    {
        if (table[1][0] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[1][0] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    }   
     else if (table[2][0] == table[2][1] && table[2][1] == table[2][02])
    {
        if (table[2][0] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[2][0] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    } 
     else if (table[0][2] == table[1][2] && table[1][2] == table[2][2])
    {
        if (table[0][2] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[0][2] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    } 
    else if (table[2][0] == table[1][1] && table[1][1] == table[0][02])
    {
        if (table[2][0] == 'O')
        {
            printf("nikhse o defteros\n");
            return 11;
        }  
        else if (table[2][0] == 'X')
        { 
            printf("nikhse o prwtos\n");
            return 10;
        }     
            
    }
    else if (table[0][0] != ' ' && table[0][1] != ' ' && table[0][2] != ' ' && table[1][0] != ' ' && table[1][1] != ' ' && table[1][2] != ' ' && table[2][0] != ' ' && table[2][1] != ' ' && table[2][2] != ' ')
    {
        return 420;
    }
    else
    {
        return 69;
    }
   
}
