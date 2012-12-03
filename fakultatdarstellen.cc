//UNFERTIG

class fakultat
{
private:
	unsigned long int internezahl;
	fakultat *nachfolger;

public:
	fakultat (unsigned long int fakult)
	{
		internezahl=fakult;
		if (internezahl>1)
			nachfolger=new fakultat(internezahl-1);
	}
	unsigned long int zahlgesamt()
	{
		
	}
}
