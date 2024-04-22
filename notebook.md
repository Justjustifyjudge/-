# 2.4
- 把david_lin模板移动到GitHub，今天LeetCode有一个kmp的模板题，也顺便记一下笔记。
- 计算模式串的最大匹配数表代码：
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
- kmp搜索最大的匹配串：
```Java
// 在文本 text 中寻找模式串 pattern，返回所有匹配的位置开头
List<Integer> search(String text, String pattern) {
    List<Integer> positions = new ArrayList<>();
    int[] maxMatchLengths = calculateMaxMatchLengths(pattern);
    int count = 0;
    for (int i = 0; i < text.length(); i++) {
        while (count > 0 && pattern.charAt(count) != text.charAt(i)) {
            count = maxMatchLengths[count - 1];
        }
        if (pattern.charAt(count) == text.charAt(i)) {
            count++;
        }
        if (count == pattern.length()) {
            positions.add(i - pattern.length() + 1);
            count = maxMatchLengths[count - 1];
        }
    }
    return positions;
}
```

- 其实kmp就是用next表来跳过前面前缀和后缀相同的部分了。核心就在于主串的指针永远不往前回溯，而是刷新子串的匹配状态。

- next数组的关键是求解最长相等的前后缀
```Python
def kmp_search(string, patt):
    next = build_next(patt)
    i=0 # 主串
    j=0 # 子串
    while i < len(string):
        if string[i] == patt[j]:
            i+=1
            j+=1
        elif j>0:
            j=next[j-1]
        else:
            i+=1
        if j==len(patt):
            return i-j
```
- 所以kmp的核心就在于next表的求解，要通过已知的信息来求解后面各位的next值，感觉与动归颇有相似之处
- 求解next表的代码如下：
```Python
def build_next(patt):
    next_form=[0] # next表
    prefix_lex=0 # 当前共同前后缀的长度
    i=1
    while i<len(patt):
        if patt[prefix_lex]==patt[i]:
            prefix_lex=prefix_len+1
            next_form.append(prefix_len)
            i=i+1
        else:
            if prefix_len==0:
                next_form.append(0)
                i=i+1
            else:
                prefix_len=next_form[prefix_len-1]
    return next_form
```
- 哈希表的删除
```C++
unordered_map<int, int> cnt;
int key;
auto item = cnt.find(key);
cnt.earse(item);
```
- devCPP的修改语言方法：工具——编译器选项——new document encoding（翻译：新文档的编码）——改成UTF-8——确定
