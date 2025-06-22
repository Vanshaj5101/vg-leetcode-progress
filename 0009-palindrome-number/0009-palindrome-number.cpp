class Solution {
public:
    bool isPalindrome(int x) {
        string rev_str;
	    string str = to_string(x);
	    for(int i=str.size() - 1; i>=0; i--){
		    rev_str.push_back(str[i]);
	    }
	    if(rev_str == str){
		    return true;
	    }else{
		    return false;
	    }
    }
};