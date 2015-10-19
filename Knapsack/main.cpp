#include <iostream>
#include "util/Timer.hpp"
#include "Dynamicp/Dynamicp.hpp"
int main() {

    int val[] = { 60,100,120};
    int wt[] = {10,20,30};
    int W = 50;
    int n = sizeof(val)/sizeof(val[0]);
     Timer tmr;
    std::cout<<knapSack(W,wt,val,n)<<std::endl;
    double t = tmr.elapsed();
    std::cout<<t<<std::endl;
    tmr.reset();
    std::cout<<knapSackDynamic(W,wt,val,n)<<"--from dynamic programming"<<std::endl;
    std::cout<<tmr.elapsed()<<" Time elapsed for dynamic";
    return 0;

}