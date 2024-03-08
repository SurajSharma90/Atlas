/*
* Include the library that contains the functionality for input and output
* iostream stands for input/output stream
* Allows us to implement input and output in our application
*/
#include <iostream>

//Namespace to define what part of the library we want to get the functionality from
using namespace std;

//Main function
int main(int argc, char** argv)
{
  //Add
  int a = 0;
  int b = 0;

  std::cout << "Addition!" << "\n";
  //std::cout << "Input a: ";
  //std::cin >> a;
  //std::cout << "Input b: ";
  //std::cin >> b;
  std::cout << "Answer: " << a + b;
  int answer = a + b;
  std::cout << "\nAnswer: " << answer;

  //Subtract
  a = 5;
  b = 87;
  int c = 32;

  std::cout << "\n\nSubtraction!" << "\n";
  std::cout << "\nAnswer: " << a - b;
  answer = a - b - c;
  std::cout << "\nAnswer: " << answer;

  //Multiply
  a = 5;
  b = 3;

  std::cout << "\n\Multiplication!" << "\n";
  answer = a * b;
  std::cout << "'Answer: " << answer;

  //Divide
  //Even
  double t = 24;
  double n = 3;
  std::cout << "\n\Division!" << "\n";
  answer = t / n;
  std::cout << "Answer: " << answer;

  //Uneven
  t = 45;
  n = 3;
  answer = t / n;
  std::cout << "\nAnswer: " << answer;

  //Combine
  a = 3;
  b = 2;
  c = 2;
  t = 4;
  n = 5;

  answer = a + b * t / n - c;
  std::cout << "\nAnswer: " << answer;

  //Parentheses to focus
  answer = t / n - (a + b + c);
  std::cout << "\nAnswer: " << answer;

  //Integer division
  std::cout << "\n\Integer Division!" << "\n";
  a = 5;
  b = 2;
  answer = a / b;
  std::cout << "Answer: " << answer;

  //Modulo
  std::cout << "\n\Remainder (Modulo)!" << "\n";
  a = 5;
  b = 2;
  answer = a % b;
  std::cout << "Answer: " << answer;

  //Increment operators
  std::cout << "\n\Increment +!" << "\n";
  a = 2;
  a += 4;
  std::cout << "a: " << a;


  return 0;
}

