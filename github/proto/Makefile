all = test 

objs = amessage.pb-c.o   

CFLAGS = -Wall 

$(all): zzh.c $(objs)
	gcc -I. -o $@ $^ -lprotobuf-c

clean:
	$(RM) lexer.c parser.c
	$(RM) *.o
	$(RM) $(all)
	$(RM) parser.out* 
	$(RM) parser.t*
	$(RM) *~ 
