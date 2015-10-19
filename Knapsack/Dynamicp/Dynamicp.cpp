//
// Created by Tadeze on 10/18/2015.
//

#include "Dynamicp.hpp"
#include "../util/utility.hpp"
//
// Created by Tadeze on 10/18/2015.
// Non-dynamic programming
int knapSack(int W,int wt[],int val[], int n)
{
    //Base case
    if (n==0 || W==0)
        return 0;
    //If wieight of the nth item is more than knapck  c

    if (wt[n-1]>W)
        return knapSack(W,wt,val,n-1);
    else return util::max(val[n-1] + knapSack(W-wt[n-1],wt,val,n-1),
                    knapSack(W,wt,val,n-1));



}
int knapSackDynamic(int W, int wt[],int val[],int n)
{

    int k[n+1][W+1];
    //Build the table k[][] in bottom up manner
    for (int i=0;i<=n;i++)
        for(int w=0;w<=W;w++)
        {
            if(i==0|| w==0)
                k[i][w] = 0;
            else if (wt[i-1]<=w)
                k[i][w]=util:: max(val[i-1]+k[i-1][w-wt[i-1]],
                             k[i-1][w]);
            else
                k[i][w] = k[i-1][w];

        }
    return k[n][W];
}
