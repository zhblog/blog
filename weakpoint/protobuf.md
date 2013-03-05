# Protobug简介

## WHAT 

* google的
* 开源序的
* 平台无关、语言无关的
* 结构化数据的序列化与反序列化 



## WHERE

* [官方网站](blog.itpub.net/post/42700/527047) 
* [C语言支持](http://code.google.com/p/protobuf-c/)
* [其他语言列表](http://code.google.com/p/protobuf/wiki/ThirdPartyAddOns)
* [简介教程](https://developers.google.com/protocol-buffers/)  



## WHY

* 语言中立，平台中立，可扩展性好 
* 性能可靠
* 使用简单,API相对统一 
* 相较JSON，XML定义简单，接口统一



# Protobuf简单使用

## 1. protobuf文件

	message Person {
    required string name = 1;
    required int32 id = 2;
    optional string email = 3;

    enum PhoneType {
        MOBILE = 0;
        HOME = 1;
        WORK = 2;
		}

    message PhoneNumber {
        required string number = 1;
        optional PhoneType type = 2 [default = HOME];
		}

    repeated PhoneNumber phone = 4;
	}


## 2. 增加模块 

* message： 消息定义
* Person： 消息名称
* enum：枚举类型
* required：可选项
* optional：必选项
* repeated：数组选项
	


## 3. 测试用proto 

	message AMessage
	{
		required int32 a=1; 
		optional int32 b=2;
	}
	

## 4. 编译proto 

	#!/usr/bin/bash
	file="../file/person.proto"
	if [ $# -eq 1 ];
	then
		file="../file/$1.proto"
	fi
	echo $file
	protoc --python_out=../python/ --proto_path=../file/ $file
	protoc-c --c_out=../c/ --proto_path=../file $file


## 5. C语言打包程序


    static void* packbuf()
	{
		AMessage msg = AMESSAGE__INIT; // AMessage
		void *buf;                     // Buffer to store serialized data
		unsigned len;                  // Length of serialized data
		msg.a = 1;
		//msg.has_b = 1; 
		msg.b = 2;
		len = amessage__get_packed_size(&msg);

		buf = malloc(len);
		amessage__pack(&msg,buf);
		return buf;
	}


## 6. 编译C的makefile


    all = client 
	CC=clang
	objs = amessage.pb-c.o   
	CFLAGS = -Wall 
	$(all): test.c $(objs)
		clang -I. -o $@ $^ -lprotobuf-c -lzmq
	clean:
		$(RM) *.o
		$(RM) $(all)
		$(RM) *~ 


## 7. Python解包


	print "Received request: ", len(buf)
    print repr(buf)
    APB.AMessage.ParseFromString(am, buf)
    print am.a
    print am.b
