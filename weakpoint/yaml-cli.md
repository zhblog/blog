# 由来

## 为什么要cli

* cli符合unix，linux用户使用配置习惯 
* 思科，华为等板卡的设置提供比较规范的cli设置
* 在一些系统上，cli是唯一的配置平台，不提供X和web 
* CLI的设置占用资源少，输入规范明了



## cli实现的方式

* 据说思科华为的实现方式是C的if，else，及其庞大，形成模板，我汗
* parser+lexer实现词法语法解析
* 其他实现方式,自己实现模板方法
* 我的实现方式  
* ![](/blog/img/w/test.png)




## 为什么是yaml-cli

* **yaml**的表达能力牛逼的要死 
* **json**可以方便的支持web的扩展
* readline提供了强有力的扩展API 
* C 提供了快速的，占用资源少的实现方式.
* LUA插件也许是未来的最好是先方式.  



# 解读

## 1. 代码结构


    ├── check.c
    ├── dispatcher.c
    ├── file
    │   ├── CMD3.yaml
    │   ├── regex
    │   ├── root.yaml
    ├── main.c
    ├── re2val.c
    ├── readline.c
    └── script
        └── write_web.py


## 2. 增加模块 

* 在file中新增一个yaml文件，那文件名字定义为你的模块名
* 在root.yaml中增加信的模块的部分 
* 在新的模块yaml中编写你的命令
* 编译执行测试
	


## 3. 编写模块的命令规则 

    - cmd: debug <int:integer>
      help: debug no help
      web: yes
      file: yes
      debug: no
      rpc: cli_set_debug_flag
	
	

## 4. 命令解读 

    cmd:命令过规则
    help：提示的字符串
    web：是否支持web
    file：是否支持配置导入
    debug：是不是内部命令
    rpc：此命令的解析函数名称

## 5. 命令规则解读


    <>:必选项，可包含其他形式
    []:可选项，可包含其他方式
    {}:可重复选项，多选多
    |：多选一


# 完善

## 加法和减法 
    
* 删除部分规则
* 增加新的规则

# 接下来


## json的不爽

1. 对树形结构的支持不好 
2. 命令多的时候很不好处理命名问题
3. rpc的解析很是不好玩



## LUA

* 快速，胶水
* 解释起小，可以移植
* 编写快速
