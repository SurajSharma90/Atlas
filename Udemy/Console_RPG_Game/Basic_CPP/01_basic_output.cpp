/*
* Include the library that contains the functionality for input and output
* iostream stands for input/output stream
* Allows us to implement input and output in our application
*/
#include <iostream>

//Namespace to define what part of the library we want to get the functionality from
//using namespace std;

//Main function
int main(int argc, char** argv)
{
  //Hello World!
  std::cout << "Hello World!" << std::endl;

  //Stream of strings
  std::cout << "Hello" << " " << "World" << std::endl;

  //Stream of strings on different lines
  std::cout 
  << "Hello " 
  << "World" 
  << std::endl;

  //Stream of strings on actual different lines
  std::cout << "Hello\n" << " \n" << "World" << std::endl;

  //Numbers and other types of data in the stream
  std::cout << "My Number is: " << 25 << "\n";

  return 0;
}
