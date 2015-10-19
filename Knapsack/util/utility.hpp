//
// Created by Tadeze on 10/18/2015.
//

#ifndef UNTITLED_UTILITY_H
#define UNTITLED_UTILITY_H
#include<vector>
namespace util {
        template<class T>
        T max(T a, T b) { return (a > b ? a : b); }
        template<class T>
        T mean(std::vector<T> values)
        {       T sum =0.0;
                for(T el : values)
                        sum +=el;
                return sum/values.size();
        }
}

#endif //UNTITLED_UTILITY_H
