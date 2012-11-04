#include <iostream>
#include <sstream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
string result="", result2="";
int stellwert=atoi(argv[1]);
int zahldezi=atoi(argv[2]);
int zahlcalc=zahldezi;
int counter=0, rest=0;;
//  std::stringstream out;


while (zahlcalc>0) {
  counter++;
  rest=zahlcalc%stellwert;
  zahlcalc=(zahlcalc-rest)/stellwert;
  std::stringstream out;
  out << rest;
  std::stringstream out2;
  out2 << counter;
  result2=out.str()+" "+result2;
  result="Ziffer: "+out.str()+"; "+result;
  result="Position: "+out2.str()+", "+result;
  
}
result.erase(result.length()-2);
cout << "Sei arg1 der Stellenwert und argv2 eine beliebige Zahl so ist im arg1 Stellenwertsystem die Zahl:\n";
cout << result << endl;
cout << "kurz:" << endl;
cout << result2 << endl;
return 0;
}
