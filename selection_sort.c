#include <stdio.h>
void main() {
    int i,arr[10],j,min,m,n=6,k,temp;
    for ( i = 0; i < n; i++)
    {
        printf("enter");
        scanf("%d",&arr[i]);
    }
    for ( j= 0; j <n-1; j++)
    {
        min=j;
        for ( k =j+1; k <n ; k++)
        {
            if(arr[k]<arr[min])
            {
                temp=arr[min];
                arr[min]=arr[k];
                arr[k]=temp;
            }
        }
        
    }
    
    for ( m = 0; m< n; m++)
    {
        printf("%d",arr[m]);
    }
    


}