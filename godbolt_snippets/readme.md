This directory stores all godbolt examples mentioned in the comment just in case shortened link won't work some time in future.

1. [3cGdneEKM.cpp](https://godbolt.org/z/3cGdneEKM) demonstrates conditional static assert. 
2. [3YfEK6W3f.cpp](https://godbolt.org/z/3YfEK6W3f) demonstrates templated structs.
3. [h66hP77qM.cpp](https://godbolt.org/z/3YfEK6W3f) demonstrates ND tensor related functions resolved at compile time.
4. [KaWzKPW8G.cpp](https://godbolt.org/z/KaWzKPW8G) demonstrates templated base class and templated derive class.
5. [3oaTddKxG.cpp](https://godbolt.org/z/3oaTddKxG) demonstrates only the base class object in the derived class object will be copied when passing derived class object to a function that takes base class object as parameter.
6. [7T4e3q5zT.cpp](https://godbolt.org/z/7T4e3q5zT) varies from 3oaTddKxG to show virtual function during which a member in the derived class is accessed still works when the derived class object is passed by-value to a function that takes base class object as parameter.
7. [Yj86q3fEP.cpp](https://godbolt.org/z/Yj86q3fEP) demonstrates the use of shared_ptr.
