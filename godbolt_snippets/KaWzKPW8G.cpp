#include <iostream>
#include <string>
#include <vector>

template <typename T> class BaseClass {
public:
  virtual void print(T t) = 0;
};

class DerivedClass0 : BaseClass<int> {
public:
  void print(int a) override { std::cout << a << std::endl; }
};

template <typename T> class DerivedClassVariable : BaseClass<T> {
public:
  void print(T a) override { std::cout << a << std::endl; }
};

typedef DerivedClassVariable<float> DerivedClass1;

int main(int argc, const char *argv[]) {
  std::vector<std::string> args(argv, argv + argc);
  for (int idx = 0; idx < args.size(); idx++) {
    std::cout << args[idx] << std::endl;
  }

  DerivedClass1 dd;
  dd.print(3.5);
}