import java.util.Scanner;
import java.util.Arrays;
import java.util.Random;
public class Quicksort 
{
	static final int MAX = 10005; 
	static int[] a = new int[MAX]; 
public static void main(String[] args) 
{  
Scanner input = new Scanner(System.in); 
System.out.print("Enter Max array size: "); 
int n = input.nextInt(); 
Random random= new Random(); 
System.out.println("Enter the array elements: "); 
for(int i = 0; i <n; i++) 
a[i] = input.nextInt(); 
System.out.println("Input Array:"); 
for(int i = 0; i <n; i++) 
System.out.print(a[i] + " "); 
long startTime = System.nanoTime(); 
QuickSortAlgorithm(0, n - 1); 
long stopTime = System.nanoTime(); 
int elapsedTime = (int) (stopTime- startTime); 
System.out.println("\nSorted Array:"); 
for(int i = 0; i <n; i++) 
System.out.print(a[i] + " "); 
System.out.println(); 
System.out.println("Time Complexity in ms for n=" + n + " is: " + (double) 
elapsedTime/ 1000000); 
}
public static void QuickSortAlgorithm(int p, int r)
{
	int i,j,temp,pivot = 0;
	if(p<r)
	{
	  i=p;
	  j=r+1;
	  a[p]=pivot;
	  while(true)
	  {
		  i++;
		  while(a[i]<pivot && j<r)
		  {
			  i++;
			  j--;
			  while(a[i]>pivot)
			  {
				  j--;
				  if(i<j)
				  {
					  temp=a[i];
					  a[i]=a[j];
					  a[j]=temp;
				  }else
					  break;
			  }
			       a[p]=a[i];
			       a[j]=pivot;
			       QuickSortAlgorithm(p,j-1);
			       QuickSortAlgorithm(j+1,r);
		  }
	  }
	}
			
}
}
