# 2.4
- 把david_lin模板移动到GitHub，今天LeetCode有一个kmp的模板题，也顺便记一下笔记。
- kmp计算模式串的最大匹配数表代码：
```Java
// 构造模式串 pattern 的最大匹配数表
int[] calculateMaxMatchLengths(String pattern) {
    int[] maxMatchLengths = new int[pattern.length()];
    int maxLength = 0;
    for (int i = 1; i < pattern.length(); i++) {
        while (maxLength > 0 && pattern.charAt(maxLength) != pattern.charAt(i)) {
            maxLength = maxMatchLengths[maxLength - 1]; // ①
        }
        if (pattern.charAt(maxLength) == pattern.charAt(i)) {
            maxLength++; // ②
        }
        maxMatchLengths[i] = maxLength;
    }
    return maxMatchLengths;
}
```