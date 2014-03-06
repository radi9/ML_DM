#include<iostream>
#include<fstream>

using namespace std;
 
#define SIZE 100
char line[SIZE];
 
int main(){
    fstream fin;
    fin.open("HappyMan.txt",ios::in);
    while(fin.getline(line,sizeof(line),'\n')){
        cout<<line<<endl;
    }
 
    system("pause");
    return 0;
}
