#include <iostream>
#include <cstdlib>

using namespace std;



int main(int argc, char *argv[])
{
int a=atoi(argv[1]); //y
int b=atoi(argv[2]); 
int ggt,br;
	ggt=a;
	br=b; //b/rest
int x=0, y=1, xalt=1, xneu, yalt=0, yneu; // Koeffizienten von a, b x = u y= v
//1*a+0*b=a, 0*a+1*b=b
//y*a+yalt*b=a, x*a+xalt*b=b
int q=0,restb=0; //
int counter=0;
 cout << counter << " b:" << b << " xneu:" << "uninitialized" << " xalt:" << xalt << " x:" << x << endl; //Trick: da rest Teiler von T(a) ∩ T(b) ist
 cout << counter << " a:" << a << " yneu:" << "uninitialized" << " yalt:" << yalt << " y:" << y << endl; //Trick: da rest Teiler von T(a) ∩ T(b) ist


while (br!=0)
{
	counter++;
	restb=ggt%br;
	q=(ggt-restb)/br;
	
	ggt=br;//weise a altes br zu (alter rest)
	br=restb; //br wird aktualisiert
	cout << counter << " q:" << q << endl; 
	
	//verstehen
	xneu= xalt -(q * x);
	//cout << counter << " xneu:" << xneu << " xalt:" << xalt << " x:" << x << endl; //Trick: da rest Teiler von T(a) ∩ T(b) ist
	xalt=x; x=xneu; //verschiebe nach x
	cout << counter  << " br:" << br  << " xneu:" << xneu << " xalt:" << xalt << " x:" << x << endl; //Trick: da rest Teiler von T(a) ∩ T(b) ist

	//verstehen
	yneu=yalt-(q * y);
	//cout << counter << " yneu:" << yneu << " yalt:" << yalt << " y:" << y << endl; //Trick: da rest Teiler von T(a) ∩ T(b) ist
	yalt=y; y=yneu; //verschiebe nach y
	cout << counter << "ggt:" << ggt << " yneu:" << yneu << " yalt:" << yalt << " y:" << y << endl; //Trick: da rest Teiler von T(a) ∩ T(b) ist

}
//benutze nicht x und y sondern deren alten versionen weil sonst 0 (da letzte rechnung 0 ergibt) 
cout << "ggt=yalt*a+xalt*b" << "\n";
cout << "ggt = a * xalt(u) + b * yalt (v)\n";
cout << "ggt:" << ggt << " = " << a << "*" << xalt << "+" << b << "*" << yalt << "\n";

return 0;
}
