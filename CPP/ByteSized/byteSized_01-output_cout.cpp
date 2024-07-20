#include <iostream>

int main(int argc, char** argv) {
  
  std::string myName = "";

  std::cout << "Type a name:";
  std::cin >> myName;

  std::cout << "My name is: " << myName << "\n";

  return 0;
}