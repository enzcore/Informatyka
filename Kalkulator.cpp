#include <iostream>
 
using namespace std;
 
int main()
{
    cout << "Tabliczka mnozenia" << endl;
    cout<<endl;
 
    for (int i=1; i<=10; i++)
    {
        for (int j=1; j<=10; j++)
        {
            cout<<i << "*" << j <<"=";
            cout<<i*j << "\t";
        }
        cout<<endl;
 
    }
 
    return 0;
}