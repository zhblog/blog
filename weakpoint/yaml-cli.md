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
├── cJSON.c
├── dispatcher.c
├── file
│   ├── CMD1.yaml
│   ├── CMD2.yaml
│   ├── CMD3.yaml
│   ├── regex
│   ├── root.yaml
├── include
│   ├── cJSON.h
│   ├── cli_def.h
│   └── cli.h
├── main.c
├── Makefile
├── re2val.c
├── readline.c
└── script
    ├── write_cli_rpc.c.py
        ├── write_json.py
            ├── write_rpc.h.py
                └── write_web.py




## 2. 增加模块 

* 在file中新增一个yaml文件，那文件名字定义为你的模块名
* 在root.yaml中增加信的模块的部分 
* 在新的模块yaml中编写你的命令
* 编译执行测试
	


## 3. 编写模块的命令规则 

	# Chapter 1
	
	## It is a headline
	* first
	* second
	* third
	
	## Yet another headline
	It is a lovely day.
	
[markdown of this slideshow](weakpoint.md)

## 4. Build slides by typing 'python bootstrap.py'

    $ python bootstrap.py
 

## 5. Deploy them to Github Pages


    $ git checkout -- orphan gh-pages
    $ git add .
    $ git commit -m 'First page commit for my slides'
    $ git push origin gh-pages



# 完善

## $ \LaTeX $

*This is inline:* $ e^{ix} = \cos x + i\;\sin x $

And what's more:


$$
P_k= \frac{np(np-p)\dots(np-kp+p)}{k!}      \frac  {  {(1-p)^{-\frac{1}{p}} }^{-np}}   {(1-p)^{k}}
$$


# 接下来


## Libraries

1. [PyYAML](http://pyyaml.org/)
2. [Markdown in Python](http://freewisdom.org/projects/python-markdown/)
3. [bxslider](http://bxslider.com/)



## More Reading

* [用Markdown写幻灯片，用浏览器展示](http://blog.chengyichao.info/2012/06/17/slideshow-in-markdown/)
* [WeakPoint v1.0](http://blog.chengyichao.info/2012/07/07/weakpoint-v1)
