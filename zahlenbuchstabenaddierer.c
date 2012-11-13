#include <stdio.h>
#include <stdlib.h>

//enum zahlen{"0","1","2","3","4","5","6","7","8","9"};


int main(int argc, char *argv[])
{
	int i;
	int insg=0;
	for (i=1; i<argc; i++)
	{
		if (argv[i][0]=='0' || argv[i][0]=='1' || argv[i][0]=='2' || argv[i][0]=='3' || argv[i][0]=='4' || argv[i][0]=='5' ||
		argv[i][0]=='6' || argv[i][0]=='7' || argv[i][0]=='8' || argv[i][0]=='9')
			insg+=atoi(argv[i]);
		else
			insg+=argv[i][0];
	}
	printf("Als Zahl: %i, Als Zeichen: %c\n",insg,insg);
	return 0;
}
