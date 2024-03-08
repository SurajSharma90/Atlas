///*
//* Include the library that contains the functionality for input and output
//* iostream stands for input/output stream
//* Allows us to implement input and output in our application
//*/
//#include <iostream>
//#include <string>
//
//
////Namespace to define what part of the library we want to get the functionality from
//using namespace std;
//
////Main function
//int main(int argc, char** argv)
//{
//  int myAge = 0;
//  std::string myName = "";
//
//  std::cout << "Input your age please: ";
//  std::cin >> myAge;
//
//  std::cout << "\n";
//
//  std::cout << "Input your name please: ";
//  std::cin >> myName;
//
//  std::cout << "\n";
//
//  std::cout << "Your name is " << myName << " and you are " << myAge << " years old!";
//
//  std::cout << "\n";
//
//  //Only one part of the name is shown because the string is cut off because of the white space.
//  std::cout << "Input your name please 2: ";
//  std::getline(std::cin, myName);
//
//  std::cout << "\n";
//
//  std::cout << "Your name is " << myName << " and you are " << myAge << " years old!";
//
//  //Cin still had the newline character in the stream and instantly closes getline
//  //Flush the stream to use getline again
//  //Do this only if you need to do getline after cin
//  std::cin.clear();
//  std::cin.ignore(INT_MAX, '\n');
//  
//  std::cout << "\n";
//
//  std::cout << "Input your name please 3: ";
//  std::getline(std::cin, myName);
//
//  std::cout << "\n";
//
//  std::cout << "Your name is " << myName << " and you are " << myAge << " years old!";
//
//  return 0;
//}
