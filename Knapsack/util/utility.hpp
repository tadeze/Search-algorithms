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
        T min(T a, T b) {return (a<b?a:b);}
        template<class T>
        T mean(std::vector<T> values)
        {       double sum =0.0;
                for(T el : values)
                        sum +=el;
                return sum/(double)values.size();
        }
}

#endif //UNTITLED_UTILITY_H
