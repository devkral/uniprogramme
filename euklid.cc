#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;
int euklid(int a, int b)
{
if (b==0)
{	
	return a;
}
else
{
	cout << "step: a:" << a << " b:" << b << " modulo:" << a % b << "\n";
	return euklid(b, a % b);
}
}


int main(int argc, char *argv[])
{
int a=atoi(argv[1]);
int b=atoi(argv[2]);
cout << euklid(a, b) << "\n";
return 0;
}
