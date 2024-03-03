#include <iostream>

int main(int argc, char** argv) {
  
  std::cout << "Hello World!";

  std::cout << "Hello" << "World!";

  std::cout << "New Line!" << std::endl;

  std::cout << "Escape Character New Line!" << "\n";

  std::cout << "Combine" 
  << "\nSome" 
  << "\n" 
  << "Stuff\n"
  << 34
  << "\nis\n"
  << "my age\n";

  return 0;
}