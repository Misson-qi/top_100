# 热题100 题解（Python）

题目顺序与 [力扣热题100 学习计划](https://leetcode.cn/studyplan/top-100-liked/) 一致。

## 运行

每题均为力扣标准接口（`Solution` 类 + 对应方法），可直接复制到力扣提交。本地可对单文件运行简单用例，例如：

```bash
cd solutions
python -c "from importlib.util import spec_from_file_location, module_from_spec; m=module_from_spec(spec_from_file_location('s', '001_two_sum.py')); m.loader.exec_module(m.module_from_spec(spec_from_file_location('s', '001_two_sum.py'))); exec(open('001_two_sum.py').read()); print(Solution().twoSum([2,7,11,15], 9))"
```

或直接打开对应 `.py` 在 IDE 中运行/调试。
