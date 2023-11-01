// Program returned: 0
// Program stdout
// base class created
// base class created
// derived class created
// 4
// 8
// base class copied
// 4
#include <iostream>
#include <string>
#include <vector>

class BaseClass {
  int a;

public:
  BaseClass() { std::cout << "base class created" << std::endl; }
  BaseClass(BaseClass &base) {
    a = base.a;
    std::cout << "base class copied" << std::endl;
  }
};

class DerivedClass : public BaseClass {
  int b;

public:
  DerivedClass() { std::cout << "derived class created" << std::endl; }
  DerivedClass(DerivedClass &derived) {
    b = derived.b;
    std::cout << "derived class copied" << std::endl;
  }
};

void print_this(BaseClass base) {
  std::cout << sizeof(base) << std::endl;
  return;
}

int main(int argc, const char *argv[]) {
  BaseClass base;
  DerivedClass derived;
  std::cout << sizeof(base) << std::endl;
  std::cout << sizeof(derived) << std::endl;
  print_this(derived);
}
