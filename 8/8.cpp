#include<bits/stdc++.h>

using namespace std;

regex P(R"/((\w{3})\s*=\s*\((\w{3}),\s*(\w{3})\))/");

typedef unordered_map<string, vector<string>> map_t;

unsigned long long solve1(const string& __restrict seq, const map_t& __restrict mp, const int& __restrict i, const string& __restrict cur, const bool type=0){
    if((!type&&cur=="ZZZ")||(type&&cur[2]=='Z')) return 0;
    return 1ull+solve1(seq, mp, (i+1)%seq.size(), mp.at(cur)[seq[i]=='R'], type);
}

unsigned long long solve2(const string& __restrict seq, const map_t& __restrict mp, const vector<string>& __restrict ends){
    unsigned long long lcm = 1, q = 1;
    for(auto&c:ends){
        q = solve1(seq, mp, 0, c, 1);
        lcm = (lcm*q)/gcd(lcm,q);
    }
    return lcm;
}

int main(){
    string S, s; cin>>S; 
    map_t mp; vector<string> ends;
    getline(cin,s); 
    while(getline(cin,s)){
        smatch mt; 
        if(regex_search(s,mt,P)){
            mp[mt[1]] = {mt[2], mt[3]};
            if(string(mt[1])[2]=='A') ends.push_back(mt[1]);
        }
    }
    // cout << solve1(S, mp, 0, "AAA") << '\n';
    cout << solve2(S, mp, ends) << '\n';
    return 0;
}