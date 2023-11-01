// Program returned: 0
// Program stdout
// base class created
// base class created
// derived class created
// 16
// 16
// base class copied
// 16
// value a 5
#include <iostream>
#include <string>
#include <vector>

class BaseClass {
public:
  int a;
  BaseClass() { std::cout << "base class created" << std::endl; }
  BaseClass(BaseClass &base) {
    a = base.a;
    std::cout << "base class copied" << std::endl;
  }
  virtual void print_value() { std::cout << "value a " << a << std::endl; }
};

class DerivedClass : public BaseClass {
public:
  int b;
  DerivedClass() { std::cout << "derived class created" << std::endl; }
  DerivedClass(DerivedClass &derived) {
    b = derived.b;
    std::cout << "derived class copied" << std::endl;
  }
  void print_value() { std::cout << "value b " << b << std::endl; }
};

void print_this(BaseClass base) {
  std::cout << sizeof(base) << std::endl;
  base.print_value();
  return;
}

int main(int argc, const char *argv[]) {
  BaseClass base;
  base.a = 3;
  DerivedClass derived;
  derived.a = 5;
  derived.b = 7;
  std::cout << sizeof(base) << std::endl;
  std::cout << sizeof(derived) << std::endl;
  print_this(derived);
}
