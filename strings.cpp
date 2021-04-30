#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin>>a>>b;
    
    cout<<a.size()<<" "<<b.size()<<endl;
    cout<<a + b<<endl;
    
    char a_new = a[0];
    
    a[0] = b[0];
    b[0] = a_new;
    
    cout<<a<<" "<<b;
}
