#include <stdio.h>
#include <stdlib.h>
#include "user.pb-c.h"

int main (int argc, const char * argv[]) 
{
    User user = USER__INIT; // user 
    void *buf;                     // Buffer to store serialized data
    unsigned len;                  // Length of serialized data
        
    if (argc != 2 && argc != 3)
    {   // Allow one or two integers
        fprintf(stderr,"usage: amessage a [b]\n");
        return 1;
    }
        
    user.username = argv[1];
    //if (argc == 3) { msg.has_b = 1; msg.b = atoi(argv[2]); }
    len = amessage__get_packed_size(&user);
        
    buf = malloc(len);
    user__pack(&user,buf);
        
    fprintf(stderr,"Writing %d serialized bytes\n",len); // See the length of message
    fwrite(buf,len,1,stdout); // Write to stdout to allow direct command line piping
        
    free(buf); // Free the allocated serialized buffer
    return 0;
}
