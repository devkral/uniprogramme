#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>

using namespace std;

//enum darstellung
//{a'

class zahlliste
{
	private:
		zahlliste *nachfolger;
		int reprasentant;
		int stelle;
		bool zugewiesen;  //NULL is not reliable
		int stellwert;
	public:
		zahlliste(int _stellwert, int _stelle)
		{
			stellwert=_stellwert;
			stelle=_stelle;
			zugewiesen=false;
		}
		
		~zahlliste()
		{
			nachfolger=0;
			delete nachfolger;
		}
		void weisezu(int zahl)
		{
			if (zugewiesen==false)
			{
				if (zahl>=stellwert)
					cerr << "Error: " << zahl << "is too high. ignore!!!!!\n";
				else
				{
					reprasentant=zahl;
					nachfolger=new zahlliste(stellwert,stelle+1);
					zugewiesen=true;
				}
			}
			else
			{
				nachfolger->weisezu(zahl);				
			}
			
		}
		
		int gibzahl(int sustelle)
		{
			if (stelle==sustelle)
				return reprasentant;
			else
			{
				if (zugewiesen==false)
				{
					return 0; //hat zur Folge: z.B. 000888 return neutrales Element
				
				}else
				{
					nachfolger->gibzahl(sustelle);
				}
			}
		}
		
	
};



int main(int argc, char *argv[])
{
int stellwert=atoi(argv[1]);
zahlliste operanten[2]={zahlliste(stellwert,0),zahlliste(stellwert,0)};
int curoperant=0;
char operation=0;

for (int counte=2; counte<argc; counte++)
{
	if(argv[counte]==(char*)"*" || argv[counte]==(char*)"/" || argv[counte]==(char*)"+" || argv[counte]==(char*)"-")
	{
		operation=argv[counte][0];
		curoperant=1;
		
	}else
		operanten[curoperant].weisezu(atoi(argv[counte]));
}
switch(operation)
{
	case 0: cout << "Error: missing operator";;;
	case '*':;;
	
}


	return 0;
}
