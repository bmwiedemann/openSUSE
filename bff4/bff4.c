/*
 Optimizing brainfuck implementation of dialect based on 
 Daniel's dbfi (see "A very short self-interpreter")

 This interpreter has only one input: program and input to the 
 program have to be separated with ! e.g. ",.!a" prints 'a'
 To use it in interactive mode paste your program as input.

 This program can be compiled with NOLNR macro defined.
 NOLNR disables optimization of linear loops (where '<>' balanced), e.g. [->+>++<<].
 Linear loop is then executed in one step.

 Oleg Mazonka 4 Dec 2006  http://mazonka.com/

 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct _op
{
	int shift, off;
	int * d, sz;
	struct _op * go;
	int c;
	int igo, linear;
	int * db, dbsz;
} op;

void printop(op *z)
{
	int j;
	printf("op='");
	if( !strchr("<>+-",z->c) ) printf("%c",(char)z->c);
	for( j=0; j<z->dbsz; j++ )  printf("%c",(char)z->db[j]);
	printf("' shift=%d off=%d go=%d { "
			,z->shift, z->off, z->igo );
	for( j=0; j<z->sz; j++ )
		printf("%d ",z->d[j]);
	printf("}\n");
}

void * zalloc(void *p, int sz, int osz)
{
	p = realloc(p,sz);
	memset((char*)p+osz,0,sz-osz);
	return p;
}
#define zalloci(p,sz,osz) zalloc(p,(sz)*sizeof(int),(osz)*sizeof(int));

int getbf()
{
	int a;
	next:
	a = getchar();
	if( a==-1 ) return -1;
	if( !strchr(",.[]+-<>!",a) ) goto next;		
	return a;
}

int consume(op *o)
{
	int mp=0,i;
	int a = o->c;

	if( strchr("[]",a) ) a=getbf();

	o->sz = 1;
	o->d = zalloci(0,1,0);
	o->off = 0;

	o->dbsz=0;
	o->db=0;

	for(;;a=getbf())
	{
	  if( a==-1 || a=='!' ) break;
	  if( strchr(",.[]",a) ) break;

	  o->db = zalloci(o->db,o->dbsz+1,o->dbsz);
	  o->db[o->dbsz++] = a;

	  if( a=='+' ) o->d[mp]++;
	  if( a=='-' ) o->d[mp]--;
	  if( a=='>' )
	  {
		mp++;
		if( mp>=o->sz ) 
		{
			o->d = zalloci(o->d,o->sz+1,o->sz);
			o->sz++;
		}
	  }
	  if( a=='<' )
	  {
	  	if( mp>0 ) mp--;
		else 
		{ 
			o->off--; 
			o->d = zalloci(o->d,o->sz+1,o->sz);
			for( i=o->sz; i>0; i-- ) o->d[i] = o->d[i-1];
			o->d[0] = 0;
			o->sz++;
		}
	  }
	}
	o->shift = mp + o->off;

	/* cut corners */
	while( o->sz && o->d[o->sz-1] == 0 ) o->sz--;
	while( o->sz && o->d[0] == 0 )
	{
	  o->sz--;
	  for( i=0; i<o->sz; i++ ) o->d[i] = o->d[i+1];
	  o->off++;
	}

	return a;
}

int main()
{
	op * o=0, *z, *zend;
	int sz=0, i, *m, mp, msz;
	int a = getbf();
	for(;;sz++)
	{
		o = zalloc(o,(sz+1)*sizeof(op),sz*sizeof(op));
		if( a==-1 || a=='!' ) break;

		o[sz].c = a;
		if( strchr(",.",a) ){ a=getbf(); continue; }
		if( a==']' ) 
		{
			int l=1, i=sz;
			while(l&&i>=0) if(i--) l+=(o[i].c==']')-(o[i].c=='[');
			if( i<0 ){ printf("unbalanced ']'\n"); exit(1); }
			o[i].igo = sz;
			o[sz].igo = i;
		}
		a = consume(o+sz);
	}

	for( i=0;i<sz;i++ )
	{
	 	o[i].go = &o[o[i].igo];
#ifndef NOLNR
		if( o[i].c == '[' && o[i].igo == i+1 && o[i].shift==0 && o[i].off <= 0 )	
		{
			o[i].linear = -o[i].d[-o[i].off];
			if( o[i].linear < 0 )
			{
			  printf("Warning: infinite loop "); printop(&o[i]);
			  printf("linear=%d\n",o[i].linear);
			  o[i].linear = 0;
			}
		}
		else o[i].linear = 0;
#endif

	}

	msz = 1000; /* any number */
	m = zalloci(0,msz,0);
	mp=0;

	z = o;
	zend = o+sz;
	for( ; z!=zend; ++z )
	{
#ifdef DBG
		printop(z);
#endif

		if( z->c == ']' )
		{
			if( m[mp] ) z=z->go;
		}

		else if( z->c == '[' )
		{
			if( !m[mp] ) z=z->go; 
		}

		else if( z->c == ',' ){ m[mp] = getchar(); continue; }

		else if( z->c == '.' ){ putchar(m[mp]); continue; }

		/* apply */
		if( z->sz )
		{
			int nmsz = mp+z->sz+z->off;
			if( nmsz > msz )
			{
			  m = zalloci(m,nmsz,msz);
			  msz = nmsz;
			}


#ifndef NOLNR
			if( z->linear )
			{
				int del = m[mp]/z->linear;
				for( i=0; i<z->sz; i++ ) m[mp+z->off+i]+=del*z->d[i];
			}else
#endif
				for( i=0; i<z->sz; i++ ) m[mp+z->off+i]+=z->d[i];

		}

		if( z->shift>0 )
		{  
			int nmsz = mp+z->shift+1;
			if( nmsz > msz )
			{
			  m = zalloci(m,nmsz,msz);
			  msz = nmsz;
			}
		}
		mp += z->shift;

#ifdef DBG
		for( i=0; i<msz; i++ )
		{
		  if( i==mp ) printf("'");
		  printf("%d ",m[i]); 
		}
		printf("\n");
#endif
	}
	return 0;
}

