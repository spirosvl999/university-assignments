#include <stdio.h>

#define SIZE 100

int main()
{
	int arr[SIZE]={0};
	int i=0,j=0,count=0,selection=0,search_elem=0,opt_search=0,search_last=-1,swap,opt_del=0,del_last=-1,max=0,min=0,sum=0,key=0,temp=0,sort_opt=0,found=0,found2=0;
	float avr=0.000;

	printf("Enter your option:\n" //Menu epilogwn
			"1. Add element\n"
			"2. Search element\n"
			"3. Delete element\n"
			"4. Max\n"
			"5. Min\n"
			"6. Sum\n"
			"7. Average\n"
			"8. Sort array\n"
			"9. Show array\n"
			"0. Exit\n");

	scanf("%d",&selection);

	while (selection!=0) //Se periptwsh pou h epilogh einai 0, termatizei h epanalhpsh kai to programma
	{
		if (selection==1) //Epilogh 1
		{
			if (count<SIZE) //Otan o pinakas exei xwro
			{
				printf("Input element:\n");
				scanf("%d",&temp);
				arr[count]=temp;
				count++;

			}
			else //Otan o pinakas einai gematos
			{
				printf("Array is full\n");
			}
		}
		else if (selection==2) //Epilogh 2
		{
			printf("Enter element to search: ");
			scanf("%d",&search_elem); //Diavazoume to element pou 8elei o xrhsths na vroume
			printf("1.First\n"
					"2.Last\n"
					"3.Every occurrence?\n"); //Rwtame ton xristh an 8elei na emfanisoume thn prwth, teleftea h oles ths pi8anes 8eseis tou stixeiou
			scanf("%d",&opt_search);
			if (opt_search==1) //An 8elei thn prwth 8esh
			{
				for (i=0; i<count,found==0;i++)
				{
					if (search_elem==arr[i])
					{
						printf("Element found at %d index\n",i);
						found=1;
					}
				}
			}
			else if (opt_search==2) //An 8elei thn teleftea
			{
				for (i=0; i<count; i++)
				{
					if (arr[i]==search_elem)
					{
						search_last=i;
					}
					if (i+1==count && search_last!=-1)
					{
						printf("Last occurrence of %d is at index %d\n",search_elem,search_last);
					}
				}
			}
			else if (opt_search==3) //Ean 8elei oles tis pi8anes 8eseis
			{
				for (i=0; i<count; i++)
				{
					if (arr[i]==search_elem)
					{
						printf("Found element %d at index %d\n",search_elem,i);
					}
				}
			}
			else //Periptwsh plhktrologishs la8os ari8mou apo xrhsth
			{
				printf("Invalid option\n");
			}
		}	
		else if (selection==3) //Epilogh 3
		{
			swap=0;
      		printf ("Tell me the Key\n") ;
     		scanf("%d", &key); //Diavazoume to element pou 8a diagrapsoume
     		printf("1.First\n"
	  			  "2.Last\n"
	  		       "3.Every occurrence?\n"); //Rwtame ton xristh an 8elei na diagrapsoume thn prwth, teleftea h oles ths pi8anes 8eseis tou stixeiou
      		scanf("%d",&opt_del);

    		if (opt_del==1)
     		{
				found2=0;
				for (i=0; i<count&&found2==0; i++) //An 8elei thn prwth
				{
	  				if (key==arr[i])
	  				{
	    				int temp=arr[i];
	    				arr[i]=arr[count-1];
	    				arr[count-1]=temp;
	    				count--;
	    				found2=1;
	 				}
				}
     		}
      		else if (opt_del==2) //An 8elei thn teleftea
			{
				for (i=0; i<count; i++)
				{
	  				if (key==arr[i])
	  				{
	    				del_last=i;
	  				}
	  				if (i+1==count && del_last!=-1)
	  				{
	    				int temp=arr[del_last];
	    				arr[del_last]=arr[count-1];
	    				arr[count-1]=temp;
	   					count--;
	 				}
				}
			}
      		else if (opt_del==3)
      		{
				for (i=0; i<count; i++)
				{
					if (key==arr[i])
					{
	    				swap++;
						int temp=arr[i];
						arr[i]=arr[count-1];
						arr[count-1]=temp;
						count--;
	  				}
				}
				if (swap!=0)
				{
				count--;
				}
    		}
		}

		else if (selection==4) //Epilogh 4
		{
			max = arr[0]; //Arxhkopoihsh tou max me to prwto stoixeio tou pinaka
			for (i=0; i<=count; i++)
   			{
        		if (max<arr[i])
        			{
        				max = arr[i];
   	 				}   
			}
			printf("Max is %d\n", max);
		}

		else if (selection==5) //Epilogh 5
		{
			min=arr[0]; //Arxikopoihsh tou min me to prwto stoixeio tou pinaka
			for (i=0; i<=count; i++)
			{
				if (min>arr[i])
					{
						min = arr [i];
					}
			}
			printf("Min is %d\n", min);
		}
		
		else if (selection==6) //Epilogh 6
		{
    		for (i=0; i<count; i++)
    		{
       			sum=sum+arr[i];
			}
			printf("Sum is %d\n", sum);	
		}
		
		else if (selection==7) //Epilogh 7
		{
			avr=sum/count+1;
			printf("Average is %.3f\n", avr);

		}

		else if (selection==8) //Epilogh 8
		{
			printf("Which type of sort do you want?\n 1. Ascending\n 2. Descending\n");
			scanf ("%d",&sort_opt);

			if (sort_opt==1) // Afkousa taksinomish
			{
				for (i = 0 ; i < count - 1; i++)
  				{
    				for (j = 0 ; j < count - i - 1; j++)
    				{
    					if (arr[j] > arr[j+1])
     					{
        				temp       = arr[j];
        				arr[j]   = arr[j+1];
        				arr[j+1] = temp;
     					}
   					}
  				}
				printf("Sort has been finished\n"); //Munhma epitixous taksinomhshs
			}
			else if (sort_opt==2) //F8inousa taksinomish
			{
				for (i = 0 ; i < count - 1; i++)
  				{
    				for (j = 0 ; j < count - i - 1; j++)
    				{
    					if (arr[j] > arr[j+1])
     					{
        				temp       = arr[j];
        				arr[j]   = arr[j+1];
        				arr[j+1] = temp;
     					}
   					}
  				}
				printf("Sort has been finished\n"); //Munhma epitixous taksinomhshs
			}
		}

		else if (selection==9) //Epilogh 9
		{
			printf("Printing array\n");
			for (i=0; i<count; i++)
			{
				printf("%d ", arr[i]);
			}
			printf("\n");
		}
		printf("Enter Your Option:\n" //Emfanish menou Epilogwn
			"1. Add element\n"
			"2. Search element\n"
			"3. Delete element\n"
			"4. Max\n"
			"5. Min\n"
			"6. Sum\n"
			"7. Average\n"
			"8. Sort array\n"
			"9. Show array\n"
			"0. Exit\n");

		scanf("%d",&selection);
		
	}

	return 0;

}
