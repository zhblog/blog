/*gcc server.c -o server -lzmq  
  ./server   
  接收客户消息，并回复随机数字  
  */ 
#include <zmq.h>  
#include <stdio.h>  
#include <unistd.h>  
#include <string.h>  
#include <stdlib.h>  
int main (void)  
{  
    void *context = zmq_init (1);  

    // Socket to talk to clients  
    void *responder = zmq_socket (context, ZMQ_REP);  
    //监听5555端口  
    zmq_bind (responder, "tcp://*:5555");  
    printf("binding on port 5555.\nwaiting client send message...\n");  
    while (1) {  
        // Wait for next request from client  
        zmq_msg_t request;  
        zmq_msg_init (&request);  
        //接收客户端消息  
        zmq_recv (responder, &request, 0);  
        int size = zmq_msg_size (&request);  

        //打印客户端消息  
        char *string = malloc (size + 1);  
        memset(string,0,size+1);  
        memcpy (string, zmq_msg_data (&request), size);  
        printf ("Received Hello string=[%s]\n",string);  
        free(string);  
        zmq_msg_close (&request);  

        // Do some 'work'  
        sleep (1);  

        // Send reply back to client  
        zmq_msg_t reply;  
        char res[128]={0};  

        //回复客户端  
        snprintf(res,127,"reply:%d",random());  
        zmq_msg_init_size (&reply, strlen(res));  
        memcpy (zmq_msg_data (&reply), res, strlen(res));  
        //发送  
        zmq_send (responder, &reply, 0);  
        zmq_msg_close (&reply);  
    }  
    // We never get here but if we did, this would be how we end  
    zmq_close (responder);  
    zmq_term (context);  
    return 0;  
} 
