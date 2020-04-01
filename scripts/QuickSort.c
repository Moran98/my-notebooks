#include<stdio.h>

int main(){
   printf("==============QuickSortAlgorithm==============");
   printf("===============AaronMoran===============");

   // Initialise variables
   int i;
   int count;
   int number[15];

   printf("How many elements are u going to enter ? : ");
   scanf("%d",&count);

   printf("Enter %d elements : ", count);

   // for
   for(i=0;i<count;i++)
      scanf("%d",&number[i]);

   // call method Quicksort and pass variables
   quicksort(number,0,count-1);

   // for
   printf("Order of Sorted elements: ");
   for(i=0;i<count;i++)
      printf(" %d",number[i]);

   return 0;
}

// Quick Sort method - receives 
void quicksort(int number[25],int first,int last){

   // Initialise variables
   int i, j;
   int pivot, temp;


   if(first<last){
      pivot=first;
      i=first;
      j=last;

      // start while
      while(i<j){
         // nested while goes brrrr
         while(number[i]<=number[pivot]&&i<last)
            //increment
            i++;
         // nested while goes brrrr
         while(number[j]>number[pivot])
            // de-increment?lul
            j--;
         if(i<j){
            //adding to the queues
            temp=number[i];
            number[i]=number[j];
            number[j]=temp;
         }
      }

      temp=number[pivot];
      number[pivot]=number[j];
      number[j]=temp;
      quicksort(number,first,j-1);
      quicksort(number,j+1,last);
   }
}