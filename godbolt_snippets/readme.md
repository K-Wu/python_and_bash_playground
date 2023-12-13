This directory stores all godbolt examples mentioned in the comment just in case shortened link won't work some time in future.

1. [3cGdneEKM.cpp](https://godbolt.org/z/3cGdneEKM) demonstrates conditional static assert. 
2. [3YfEK6W3f.cpp](https://godbolt.org/z/3YfEK6W3f) demonstrates templated structs.
3. [h66hP77qM.cpp](https://godbolt.org/z/3YfEK6W3f) demonstrates ND tensor related functions resolved at compile time.
4. [KaWzKPW8G.cpp](https://godbolt.org/z/KaWzKPW8G) demonstrates templated base class and templated derive class.
5. [3oaTddKxG.cpp](https://godbolt.org/z/3oaTddKxG) demonstrates only the base class object in the derived class object will be copied when passing derived class object to a function that takes base class object as parameter.
6. [7T4e3q5zT.cpp](https://godbolt.org/z/7T4e3q5zT) varies from 3oaTddKxG to show derived class virtual function won't be called when the derived class object is passed by-value to a function that takes base class object as parameter. However, if we pass the base class object by-reference instead in print_this(), the derived class virtual function will be called now.
7. [Yj86q3fEP.cpp](https://godbolt.org/z/Yj86q3fEP) demonstrates the use of shared_ptr.
8. [Ebf1qE1xa.cpp](https://godbolt.org/z/Ebf1qE1xa) demonstrates how to specify initial value for class members, e.g., a std::vector<int>, via initializer list.
9. [rGzeWxzqP.cpp](https://godbolt.org/z/rGzeWxzqP) is a variant from Ebf1qE1xa that demonstrates how to use new operator with constructor arguments to create a class object.
10. [Yodb91aMj.cpp](https://godbolt.org/z/Yodb91aMj) shows that virtual function preserves its virtual-ness in derived class.
11. [xrYhfTWMb.cpp](https://godbolt.org/z/xrYhfTWMb) extends from Yodb91aMj to show that virtual function will NOT call the non-virtual function of the class where the virtual function is defined.