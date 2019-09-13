/* EUC-KR < - > ISO-2022-KR code converter for Hangul Mail Exchange
   with non-localized MTA(e.g. sendmail )

   version 1.0pl5 ( Nov. 30, 1997) : Comment and help change
   version 1.0pl4 ( March 11,1997) : modified to make use of
                                     __STDC__ defined by
                                     most ISO/ANSI C compiler
   version 1.0pl3 ( July 11, 1996) : Thanks to D. Lim,
                                     1. change in cmd line argument parsing
                                     2. more portability issues addressed
                                     3. now exits gracefully as required in 
                                        some OS : 'return(0)' at the end,
                                        which solves problem in Solaris
                                        when used as a filter for Pine.
                      

   version 1.0pl2 ( July  9, 1996) : 1.portability issue related
                                     to 'char' type range addressed.
                                     2. another portability issue
                                     resolved : To compile with
                                     pre-ANSI C compiler, give 
                                     '-DKNR' option at the cmd line
                                     for c compiler or uncomment
                                     '#define KNR'.(See below)
                                     
    

   version 1.0pl1 ( June, 8, 1996) : supercedes one included in hmconv.tar.gz
                                     now is a bit more robust
                                     and works better in Emacs.

   version 1.0    ( May, 1996)

   By Jungshik Shin(jshin@pantheon.yale.edu)

   For details on Hangul mail exchange with this filter,
   see documents included in hmconv.tar.gz and
   references there. You may also subscribe to
   han.comp.mail and han.comp.hangul for further
   development in Hangul mail exchange including
   customization for Emacs+Rmail (.emacs setting)
   I plan to post.

*/

/* Uncomment following line if pre-ANSI C compiler is used */
/* 
#define KNR
*/


#include <stdio.h>
#include <string.h>

#if ! defined(KNR) ||  defined(__STDC__)
#include <stdlib.h>
#endif

#define isksc(c)   ( (unsigned char) (c) > (unsigned char) '\240'   && \
       (unsigned char)  (c) < (unsigned char) '\377' ) 
#define is7ksc(c)   ( (unsigned char) (c) > (unsigned char) '\040'   && \
       (unsigned char)  (c) < (unsigned char) '\177' ) 

#define BUF 4096
#define SI '\017'
#define SO '\016'


FILE *in,*out;
int isdecode;
unsigned char line[BUF];
int ishangul;

#if defined(KNR) &&  ! defined(__STDC__)
int openfile();
int convert();
int	getoption();
#else
int openfile(char *,char *,FILE **);
int convert();
int	getoption(int argc, char *argv[], char *optstring);
#endif

/*************************************************************
*** getoption() parses command line options.                    *
*** This was adapted from the code written by Henry Spencer, *
*** University of Toronto.                                   *
*** --- D. Lim ---                                           *
**************************************************************/

char	*optarg;	/* Global argument pointer. */
int	optind = 0;	/* Global argv index. */

#if defined(KNR) &&  ! defined(__STDC__)
int	getoption (argc, argv, optstring)
int	argc;
char	*argv[];
char	*optstring;
#else
int	getoption (int argc, char *argv[], char *optstring)
#endif
{
	register int	c;
	register char	*place;
	static char	*scan = NULL;

	optarg = NULL;

	if (!scan || !*scan) {
		if (optind == 0) optind++;
		if (optind >= argc) return EOF;
		place = argv[optind];
		if (place[0] != '-' || place[1] == '\0') return EOF;
		optind++;
		if (place[1] == '-' && place[2] == '\0') return EOF;
		scan = place+1;
	}

	c = *scan++;
	place = strchr(optstring, c);
	if (place == NULL || c == ':') {
		fprintf(stderr, "%s: unknown option %c\n", argv[0], c);
		return '?';
	}
	if (*++place == ':') {
		if (*scan != '\0') {
			optarg = scan, scan = NULL;
		} else {
			optarg = argv[optind], optind++;
		}
	}
	return c;
}

#if defined(KNR) &&  ! defined(__STDC__)
main (argc,argv)
int argc;
char **argv;
#else
main (int argc, char **argv)
#endif

{
	int	opt;
	char	*p;

	isdecode = 0;
	ishangul = 0;
	in = stdin;
	out = stdout;

	while ((opt = getoption(argc, argv, "hu")) != EOF ) {
		switch (opt) {
		case '?':
		case 'h':
			if ((p = strrchr(argv[0], '/'))) p++; else p = argv[0];
			fprintf(stderr,"Usage: %s [-h] [-u] [input file [output file] ]\n", p);
			fputs("\t -h : prints this help\n",stderr);
			fputs("\t -u : ISO-2022-KR -> EUC-KR\n",stderr);
			fputs("\t      without '-u', EUC-KR -> ISO-2022-KR\n",stderr);
			fputs("\t standard input(output) is assumed when\n",stderr); 
			fputs("\t input(output) file isn't specified.\n",stderr);
			exit(-1);
		case 'u':
			isdecode = 1;
			break;
		}
	}

	if (argc - optind > 0) openfile(argv[optind],"r",&in);
	if (argc - optind > 1) openfile(argv[optind+1],"w",&out);

	while (fgets((char *) line,BUF,in)) convert();

	if (in != stdin) fclose(in);
	if (out != stdout) fclose(out); 

        exit (EXIT_SUCCESS);

/*       return(0); */
}

#define KSC 1
#define ASCII 0
int convert()
{

   int mode=ASCII;
   int i=0;
   int c;
   
   if ( !isdecode ) {

      if ( !ishangul )

        /* search for KSC 5601 character(s) in line */

        while (line[i] != '\n' && line[i] != (unsigned char) EOF && 
                 line[i] != '\0'  ) {
                          /* the last case for buffer fill or
                             input from emacs which doesn't 
                             pad the region with EOF or '\n' 
                             when handing it over to a filter 
                             ( 'shell-command-on-region) */
           if ( isksc(line[i]) ) {
              ishangul = 1;               /* found KSC 5601 */
              fprintf(out,"\033$)C\n");   /* put out the designator */
              break;                      
/*            fprintf(out,"\033$)C");  */

/* RFC 1557 does not require '\n' after the designator
   and Hangul sendmail and cvt8.exe work fine without it,
   but 'hcode' expects '\n' and breaks a few characters
   after the designator if it's not followed by '\n'
*/ 
           }
           i++;
        }

      if ( !ishangul) {     /* KSC 5601 doesn't appear, yet */
         fputs((char *) line,out);   /* no conversion */
         return;
      }


      i = 0 ;        /* back to the beginning of the line */

      while (  line[i] != '\n' && line[i] != (unsigned char) EOF &&
               line[i] != '\0'  ) {
                          /* the last case for buffer fill or
                             input from emacs which doesn't 
                             pad the region with EOF or '\n' 
                             when handing it over to a filter 
                             ( 'shell-command-on-region) */

        if ( mode == ASCII && isksc(line[i]))  {
         
          fputc(SO,out);
          fputc(0x7f & line[i],out);
          mode = KSC;
        }
        else if ( mode == ASCII && !isksc(line[i]) )
          fputc(line[i],out);
        else if ( mode == KSC && isksc(line[i]) )
/*       else if ( mode == KSC && ( isksc(line[i] || line[i] == ' ' ) ) */
          fputc(0x7f & line[i],out);
        else {
          fputc(SI,out);
          fputc(line[i],out);
          mode = ASCII;
        }
        i++;
     }
     if ( mode == KSC) 
        fputc(SI,out);


     if ( line[i] == '\n'  || ( line[i] == '\0' && i == BUF ) )      
       fputc('\n',out);       

/* added after testing with emacs.  EOF is added by fclose.    
   no need to add it manually. '\0' is replaced by '\n' only in 
   case of buffer fill */
 
       
   } /* end of if  for EUC-KR -> ISO-2022-KR */

   else {  

/* It is more economical and strictly conforms to ISO-2022-KR,
   but some programs (e.g. Mule) seem to use 'ESC $ ) C'
   as the character-set switcher instead of the designator.
   Hence, these lines were commented out, and routine to work with 
   embeded designator was put in, instead */ 

  
/*      if ( ! strncmp(line,"\033$)C",4) ) {
         ishangul = 1;
         i+=4;
      }

      if ( !ishangul) {
         fputs(line,out);
         return(0);
      }

*/

      
      while (  line[i] != '\n' && line[i] != (unsigned char) EOF && 
               line[i] != '\0'  ) {
                          /* the last case for buffer fill or
                             input from emacs which doesn't 
                             pad the region with EOF or '\n' 
                             when handing it over to a filter 
                             (shell-command-on-region)   */

        if ( ! strncmp((char *) &line[i],"\033$)C",4) ) {
            ishangul = 1;
            i+=4;
            if ( line[i] == '\n' && i == 4 ) 
                                   /* remove '\n' from lines containing */
              return(0);           /* only the designator ESC+$)C       */
            continue;
        }

        if ( ! ishangul )
           fputc(line[i],out);

        else {

           switch( line[i] ) {
   
             case SO:
               mode=KSC;
               break;
             case SI:
               mode=ASCII;
               break;
             default:
               if ( mode==ASCII)
                  fputc(line[i],out);
               else  
                      /* space and tab can be embeded among KSC 5601 */
                  if ( line[i] != '\040' && line[i] != '\011' ) 

/* Or is it more reasonable to weed out characters outside [0x21,0x7e] ? */               
/*                if ( is7ksc(line[i]) )                */
                     fputc(line[i] | 0x80,out);
                  else
                     fputc(line[i],out);
            } /* end of switch */
         }

         i++;

      } /* end of while */

     if ( line[i] == '\n' )      /* added after testing with emacs */
       fputc(line[i],out);       /* EOF is added by fclose.        
                                    no need to add it manually 
                                    The same is true of '\0'      */

    }  /* end of else for ISO-2022-KR -> EUC-KR */

    return(0); 
}    

#if defined(KNR) &&  ! defined(__STDC__)
int openfile(name,mode,fp)
char *name;
char *mode;
FILE **fp;
#else
int openfile(char *name,char *mode,FILE **fp)
#endif

{
   if ( (*fp=fopen(name,mode)) == NULL ) {
      fprintf(stderr,"File %s open error !\n", name);
      exit(-1);
   }
   return (0);
}   
