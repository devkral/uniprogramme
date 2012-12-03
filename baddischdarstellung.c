#include <stdio.h>
//#include <math.h>

void leeren()
{
while (getchar()!='\n');
}

int eingabezahl(char *muuh)
{
	printf(muuh);
	int temp;
	int status=scanf("%i",&temp);
	
	if(status==1 && getchar()=='\n' && temp>=0)
		return temp;
	else
	{
		if (temp<0)
			printf("Error: negative number\n");
		else
			leeren();
		return eingabezahl(muuh);
	}
}

long long int powi(long long int basis, long long int exp)
{
	if (exp>0)
		return powi(basis,exp-1)*basis;
	else
		return 1;
}

void badd(int b, int x)
{
	int m=0;
	//printf("%f", pow (t,d));
	
	while ( powi(b,m) <= x) //x<(int)pow(b,n+1))
	{
		m++;
		//printf("%i %li\n",m, powi(b,m));
	}
	int N=m-1;
	
	while (N>=0)
	{
		//printf("\nN=%i\n",N);
		if (powi(b,N)<=x)
		{
			int s=0;
			while ( s*powi(b,N) <= x) //x<(int)pow(b,n+1))
			{
				s++;
				//printf("%i %li\n",m, powi(b,m));
			}
			printf("%i", s-1);
			x=x-(s-1)*powi(b,N);
			N--;
		}
		else
		{
			printf("0");
			N--;
		
		}
	}
}




int main ()
{
	int b=eingabezahl("Bitte geben Sie die Basis ein: ");
	int zahl=eingabezahl("Bitte geben Sie die Dezimalzahl ein: ");
	//int n;
	//for (n=0;n<zahl;n++)
	//	printf("%lli\n",powi(b,n));
	badd(b,zahl);
	//printf("%i\n",badd(b,zahl));
	printf("\n");
	return 0;
}




