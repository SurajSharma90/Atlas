/*
* Include the library that contains the functionality for input and output
* iostream stands for input/output stream
* Allows us to implement input and output in our application
*/
#include <iostream>
#include "DArray.h"

//Namespace to define what part of the library we want to get the functionality from
//using namespace std;

//Main function
int main(int argc, char** argv)
{
  DArray<int> myArr;
  std::cout << myArr.getNrOfItems() << "\n";

  return 0;
}
