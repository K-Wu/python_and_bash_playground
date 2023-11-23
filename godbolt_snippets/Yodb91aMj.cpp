// This example shows the virtual function overriden in a subclass still works as a virtual function when the subclass is further inherited.
// The example is extended from https://www.simplilearn.com/tutorials/cpp-tutorial/virtual-function-in-cpp
// The output is:
// Output Derived class
// Display Base class
// Output DerivedAgain class
// Display Base class
// Output DerivedAgain class
// Display Derived class

#include <iostream>
using namespace std;
class Base{
public:
virtual void Output(){
cout << "Output Base class" << endl;
}
void Display(){
cout << "Display Base class" << endl;
}
};

class Derived : public Base{
public:
void Output(){
cout << "Output Derived class" << endl;
}
void Display()
{
cout << "Display Derived class" << endl;
}
};

class DerivedAgain : public Derived{
public:
void Output(){
cout << "Output DerivedAgain class" << endl;
}
void Display()
{
cout << "Display DerivedAgain class" << endl;
}
};

int main(){
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