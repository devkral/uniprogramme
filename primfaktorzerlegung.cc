#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

class primfaktor
{
private:
//limit;
unsigned long int counter;


void teilerfinder(unsigned long int zahl)
{
	counter++;
	unsigned long int limit=ceil(sqrt(zahl));
	unsigned long int teilerneu=2;
	if (zahl&1)
	{
		teilerneu=3;
	}
	//	cout << "recursive: " << teilerneu << "  " << zahl << endl;
	while (zahl%teilerneu!=0 && teilerneu<=limit && counter<100000)
	{
		
		counter++;
		teilerneu+=2;
	}
	if(teilerneu<=limit && counter < 100000)
	{
		cout << teilerneu << "*";
		teilerfinder(zahl/teilerneu);
	}
	//else
	//	cout << "*1";
	if(teilerneu>limit)
		cout << zahl << "*1";
	
}
public:
primfaktor(long int input)
{
	//limit=ceil(sqrt(input));
	unsigned long int input2;
	counter=0;
	if (input < 0)
	{
		cout << "-1*";
		input2= input*(-1);
	}
	else
		input2= input;
	teilerfinder(input2);
	
	cout << "\nNach: " << counter << " Iterationen\n";
}


};

int main(int argc, char *argv[])
{
	//long int toll=11;
	//toll=atol(argv[1]);
	if (argc<2)
	{
		cout << "Error: no number.\n";
		return 1;
	}
	
	primfaktor(atol(argv[1]));
	return 0;
}
