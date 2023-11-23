// This example extends from Yodb91aMj.cpp
// Output Derived class
// Helper
// NonVirtualHelperDerived
// Display Base class
// Output Derived class
// Helper2
// NonVirtualHelperDerived
// Display Base class
// Output Derived class
// Helper2
// NonVirtualHelperDerived
// Display Derived class

#include <iostream>
using namespace std;
class Base {
 public:
  virtual void Output() { cout << "Output Base class" << endl; }
  virtual void OutputHelper() { cout << "Helper" << endl; }
  void OutputHelper2() { cout << "NonVirtualHelper" << endl; }
  void Display() { cout << "Display Base class" << endl; }
};

class Derived : public Base {
 public:
  void OutputHelper2() { cout << "NonVirtualHelperDerived" << endl; }
  void Output() override {
    cout << "Output Derived class" << endl;
    OutputHelper();
    OutputHelper2();
  }
  void Display() { cout << "Display Derived class" << endl; }
};

class DerivedAgain : public Derived {
 public:
  void OutputHelper2() { cout << "NonVirtualHelperDerivedAgain" << endl; }
  virtual void OutputHelper() { cout << "Helper2" << endl; }
  // void Output() override{
  // cout << "Output DerivedAgain class" << endl;
  // }
  void Display() { cout << "Display DerivedAgain class" << endl; }
};

int main() {
  Base* bpointr;
  Derived dpointr;
  bpointr = &dpointr;
  // virtual function binding
  bpointr->Output();
  // Non-virtual function binding
  bpointr->Display();

  Base* bpointr_;
  Derived* dpointr_;
  DerivedAgain ddpointr_;
  dpointr_ = &ddpointr_;
  bpointr_ = &ddpointr_;

  // virtual function binding
  bpointr_->Output();
  // Non-virtual function binding
  bpointr_->Display();

  // virtual function binding
  dpointr_->Output();
  // Non-virtual function binding
  dpointr_->Display();
}