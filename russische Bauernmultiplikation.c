
//#include <math.h>
#include <stdio.h>
//#include <stdlib.h>

unsigned int testgerade(unsigned int u)
{
if (1&u)
	return 0; //false
else
	return 1; //true
}
//russischerBauer(unsigned int a, unsigned int b);

//funktioniert da: bei geraden Zahlen/2 *2 funktiert, aber bei ungeraden nicht, da bleibt rest 1*x

void leeren()
{
while (getchar()!='\n');
//char c;
//while (c!='\n' && c!=EOF && c!=NULL)
//	c=getchar();
}


unsigned int eingabe()
{
	printf("Bitte geben Sie eine Zahl ein!\n");
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
		return eingabe();
	}
}
unsigned int eingabe2()
{
	printf("Bitte geben Sie eine zweite Zahl ein!\n");
	int temp;
	int status=scanf("%i",&temp);
	
	if(status==1 && temp>=0 && getchar()=='\n')
		return temp;
	else
	{
		if (temp<0)
			printf("Error: negative number\n");
		else
			leeren();
		return eingabe2();
	}
}

unsigned int russischerBauer(unsigned int a, unsigned int b)
{
printf("%u %u\n",a,b);

if (a==1)
{
	return b;
}
unsigned int tempb=russischerBauer(a>>1,b<<1); // /2 *2
if (testgerade(a))
	return tempb;
else
	return tempb+b;
}


int main(int argc, char* argv[])
{
	printf("Multipliziere mittels der russischen Bauernmethode\n");
	unsigned int z=eingabe();
	unsigned int z2=eingabe2();
	
	printf("Ergebnis ist: %u\n", russischerBauer(z,z2));
	return 0;

}
