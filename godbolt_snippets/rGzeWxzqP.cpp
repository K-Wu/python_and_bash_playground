#include <iostream>
#include <vector>

// Type your code here, or load an example.
int square(int num) { return num * num; }

class ABC {
public:
  int aaa{3};
  std::vector<int> abc{1, 2, 3, 4, 5};
  ABC() {}
  ABC(int _aaa, std::vector<int> _abc) {
    aaa = _aaa;
    abc = _abc;
  }
};

int main() {
  ABC *ptr_abc = new ABC{4, {5, 5, 5, 5, 5, 5}};
  std::cout << ptr_abc->aaa << std::endl;
  std::cout << ptr_abc->abc.size() << std::endl;

  ABC abc;
  std::cout << square(15) << std::endl;
  std::cout << abc.abc.size() << std::endl;
  std::cout << abc.aaa << std::endl;
  return 0;
}