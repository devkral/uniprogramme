#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

//Anwendungsbeispiel für flags / bzw binären vergleich


int main(int argc, char *argv[])
{
int a=atoi(argv[1]);
if (a & 1<<0)
	cout << a << " ist ungerade \n";
else
	cout << a << " ist gerade \n";
return 0;
}
