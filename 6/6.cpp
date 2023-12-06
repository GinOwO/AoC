#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

template<typename T>
T lb(const T&t, const T&x){
    T l=1, r=t-1, mid;
    while(l<=r){
        mid=l+r>>1;
        if(mid*(t-mid)<=x) l=mid+1;
        else r=mid-1;
    }
    return l;
}

template<typename T>
T ub(const T&t, const T&x){
    T l=1, r=t-1, mid;
    while(l<=r){
        mid=l+(r-l>>1);
        if(mid*(t-mid)>x) l=mid+1;
        else r = mid-1;
    }
    return l;
}

template<typename T>
T solve1(vector<vector<T>> arr){
    T ans=1;
    for(int i=0; i<arr[0].size(); i++){
        T  l=lb(arr[0][i], arr[1][i]), 
           u=ub(arr[0][i], arr[1][i]);
        ans*=u-l;
    }
    return ans;
}

ull solve2(vector<vector<int>>arr){
    vector<vector<ull>> a;
    for(auto&v:arr){
        string s;
        for(auto&c:v) s+=to_string(c);
        a.push_back({stoull(s)});
    }
    return solve1(a);
}

int main(){
    string s;
    vector<vector<int>> arr;
    while(getline(cin, s)){
        stringstream ss(s);
        arr.push_back({});
        while(getline(ss, s, ' ')){
            if(s.empty() || *s.rbegin()==':') continue;
            arr.back().push_back(stoi(s));
        }
    }
    // cout << solve1(arr) << '\n';
    cout << solve2(arr) << '\n';
}