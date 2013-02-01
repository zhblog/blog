/* gcc client.c -o client -lzmq -L/data/zeromq/lib -I/data/zeromq/include  
   ./client "I am jack"  
   向服务器发送消息，并打印回复消息  
   */ 
#include <zmq.h>  
#include <string.h>  
#include <stdio.h>  
#include <unistd.h>  
#include <stdlib.h>  
int main (int argc,char**argv)  
{  
    //参数1为要发送的消息  
    if(argc < 2){  
        printf("need send msg\n");  
        return 1;  
    }  
    void *context = zmq_init (1);  

    // Socket to talk to server  
    printf ("Connecting to hello world server...\n");  
    //连接server  
    void *requester = zmq_socket (context, ZMQ_REQ);  
    zmq_connect (requester, "tcp://localhost:5555");  

    int request_nbr=0;  
    for (request_nbr = 0; request_nbr != 10; request_nbr++) {  
        //构建发送消息  
        zmq_msg_t request={0};  
        //申请消息的空间  
        zmq_msg_init_size (&request, strlen(argv[1]));  
        //填充消息  
        memcpy (zmq_msg_data (&request), argv[1], strlen(argv[1]));  
        printf ("Sending Hello %d\n", request_nbr);  
        //发送消息  
        zmq_send (requester, &request, 0);  
        zmq_msg_close (&request);  

        //准备接收回复  
        zmq_msg_t reply={0};  
        zmq_msg_init (&reply);  
        //接收回复  
        zmq_recv (requester, &reply, 0);  

        //读取回复消息  
        int size = zmq_msg_size (&reply);  
        char *string = malloc (size + 1);  
        memset(string,0,size+1);  
        memcpy (string, zmq_msg_data (&reply), size);  
        printf ("recv from server string=[%s]\n",string);  
        free(string);  
        zmq_msg_close (&reply);  
    }  
    zmq_close (requester);  
    zmq_term (context);  
    return 0;  
} 
