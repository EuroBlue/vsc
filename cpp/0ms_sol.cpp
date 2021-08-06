#include <unordered_map>
class Solution {
    std::unordered_map<int, int> dict
    {
        {0,0},{1,1}
    };
public:
    int fib(int n) {
        if(dict.find(n) != dict.end())
        {
            return dict[n];
        }
        else
        {
            std::pair<int,int> x={n,(fib(n-1)+fib(n-2))};
            dict.insert(x);
            return dict[n];
        }
    }
};