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
	unsigned long long int limit=ceil(sqrt(zahl));
	unsigned long long int teiler=2;
	if (zahl&1)
	{
		teiler=3;
	}
	//	cout << "recursive: " << teilerneu << "  " << zahl << endl;
	while (zahl%teiler!=0 && teiler<=limit && counter<10000000000000000)
	{
		
		counter++;
		teiler+=2;
	}
	if(teiler<=limit && counter < 10000000000000000)
	{
		cout << teiler << "*";
		teilerfinder(zahl/teiler);
	}
	//else
	//	cout << "*1";
	if(teiler>limit)
		cout << zahl << "*1";
	
}
public:
primfaktor(long long int input)
{
	//limit=ceil(sqrt(input));
	unsigned long long int input2;
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
	
	primfaktor(atoll(argv[1]));
	return 0;
}
