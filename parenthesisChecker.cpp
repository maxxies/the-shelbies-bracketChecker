#include<iostream>
#include<string>
#include<stack>
#include<vector>
using namespace std;

//Function prototype
void checker(vector<string> &entry);
int main(){

    // Local variable declaration
    vector<string>entry;
    string line;
    cout<<"Input string with delimiters. Enter 'x' on a newline to end text."<<endl;
    //Takes user input into variable
    getline(cin,line,'x');

    //gets string before delimiter
    string delimiter = "\n";
    size_t pos = 0;
    string token;
    while ((pos = line.find(delimiter)) != string::npos) {
        token = line.substr(0, pos);
        cout << token << std::endl;
        entry.push_back(token);
        line.erase(0, pos + delimiter.length());
    }


    //entry.push_back(line);
    checker(entry);
    return 0;
}
void checker(vector<string> &entry){
    //stack instantiation
    stack < char > S;
    int condition = 0;// checks for closing delimiter when stack is empty with input empty too
    int counter;
    int j ;
    //looping through input
    for(j = 0; j < entry.size();j++){
        counter = counter + 1;
        for(int i = 0; i < entry[j].length(); i++){
            //Selects each character of input for comparisons
            char character = entry[j][i];
            switch(character){
                //Adds opening delimiters to stack
                case '(':
                case '{':
                case '[':
                    S.push(character);
                    break;
                //When character is an closing delimiter
                case ')':
                case '}':
                case ']':
                    //Checks if its the first delimiter in the input
                    if(S.empty()){
                        cout<<"Error: starting with a closing parenthesis at column "<<i+1<<", line "<<j+1<<endl;
                        condition = 1;
                    }
                    else {
                        //If not, compares with the available ones in the stack
                        switch(character){
                            //Removes delimiter if a match is made else an error has occurred
                            case ')':
                                if (S.top()== '('){
                                    S.pop();
                                }else{
                                    cout<<"Mismatched parenthesis at column "<<i+1<<", line "<<j<<endl;
                                    condition = 1;
                                }
                                break;
                            case ']':
                                if (S.top()== '['){
                                    S.pop();
                                }else{
                                    cout<<"Mismatched parenthesis at column "<<i+1<<",line "<<j+1<<endl;
                                    condition = 1;
                                }
                                break;
                            case '}':
                                if (S.top()== '{'){
                                    S.pop();
                                }else{
                                    cout<<"Mismatched parenthesis at column "<<i+1<<", line "<<j+1<<endl;
                                    condition = 1;
                                }
                                break;
                            default:
                                break;
                        }
                    }
                    break;
                default:
                    break;
            }
        }
    }
    //When stack is not empty but input is empty and no closing delimiter whatsoever
    if(!S.empty() && condition == 0){
        cout<<"Missing closing delimiter(s) at column "<<entry[counter].size()+1<<", line "<<j+1<<endl;
    //When stack is empty, input is empty and no closing delimiter
    }else if(S.empty() && condition == 0){
        cout<<"All set."<<endl;
    }
}


