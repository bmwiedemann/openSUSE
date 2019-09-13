#ifndef lint
static char rcsid[] = "$Id: hdcode.c,v 1.6 1997/11/19 04:16:52 news Exp news $";
#endif

/*
 * $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 * CLEAN_QP Copyright Notice
 *
 * Most of the following CLEAN_QP codes are stealed from a package called
 * hmailer-beta2 written by Song Woo-Geel   cookie@venus.etri.re.kr.
 *
 * I am not sure if I can distribute it or not.
 * However, The following is the original copyright statement.
 * ***************************************************************
 *	Copyright (C) 1995  Song Woo-Geel
 *	Written by cookie@venus.etri.re.kr on May. 12 '95.
 * ***************************************************************
 *
 * Now, the person who stealed cookie's code and his Copyright is
 * ***************************************************************
 * Copyright (C) 1997  Sang-yong Suh <sysuh@kigam.re.kr>
 *
 * THIS CODE IS PROVIDED AS IS AND WITHOUT ANY WARRANTY.
 * USE IT AT YOUR OWN RISK AND DON'T COMAPLAIN ME OR TO COOKIE.
 *
 * $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 */

/*
 * Revision history
 *
 * 1997/05/16  sysuh  Check charset="iso-2022-kr" (note the quotes)
 * 1997/06/14  sysuh  Replace charset=iso-8859-1 to EUC-KR
 * 1997/11/18  sysuh  Decode embedded QP texts within multipart.
 */

/*
 * hMailDecode : decode Korean "Q" or "B" encoded HANGUL news article
 *	
 * SYNOPSIS
 *  1. standalone usage:   compile with -D_MAIN
 *	hdcode [file]
 *
 *  2. as subroutine:
 *
 *      hMailDecode(char *NULL, char *NULL);	# initialize
 *	while (fgets(ibuf, sizeof(ibuf), stdin))
 *	    hMailDecode(char *ibuf, char *obuf); # pass one line at a time
 *
 * OPTIONS
 *
 * decode file and write to stdout.
 *      [file]	If file arg is missing, read stdin.
 *
 * NOTE: 
 *      Header encoding	: 	RFC-1342 	( "Q" or "B" encoding )
 *	Content encoding :	Quoted-printable or ISO-2022-KR or Base64.
 */

#ifndef	CLEAN_QP
void 
hMailDecode(ibuf, obuf)
char *ibuf;
char *obuf;
{ }
#else	/* CLEAN_QP */
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>

/*	RFC-1342 header encoding start/end sequence	*/
#define PREFIX		"=?" 
#define	POSTFIX	 	"?="
#define SUFFIXQP	"?Q?" 
#define SUFFIXB64	"?B?" 
#define OLDPREFIX	"=?B?EUC-KR?" 
#define HEADER_CTE	"Content-Transfer-Encoding: "
#define HEADER_CT	"Content-Type: "
#define	KOR_CHARSET	"EUC-KR"	/* KSC-5601	*/

/*	ISO-2022 encoding designator escape sequence	*/
#define	INTRO_ISO	"\033$)C"
#define	SHIFTOUT	'\016'		/* ASCII SO	*/
#define	SHIFTIN		'\017'		/* ASCII SI	*/
#define	DEL		'\177'		/* ASCII DEL	*/
#define OFFSET	( unsigned char ) 0200	/* or ISO encoding offset */

#define	LSIZ		4096
#define	TRUE		1
#define	FALSE		0

enum section_t { SEC_HEADER, SEC_BODY };
enum encode_t { ENC_UNKNOWN, ENC_NONE, ENC_QP, ENC_ISO, ENC_B64 };

/* recognize encoding name and convert to encode_t type */
static enum encode_t encodingInfo(arg)
char  *arg ;
{
    if (!arg) return(ENC_UNKNOWN);

    while (isspace(*arg)) arg++;
    if (strncasecmp(arg, "7bit", 4) == 0
		|| strncasecmp(arg, "8bit", 4) == 0
		|| strncasecmp(arg, "none", 4) == 0) 
	return(ENC_NONE);
    else if (strncasecmp(arg, "quoted-printable", 16) == 0)
	return(ENC_QP);
    else if (strncasecmp(arg, "base64", 6) == 0)
	return(ENC_B64);
    else 
	return(ENC_UNKNOWN);
}

/* convert CR+LF in middle or tail to LF. Overwrite! */
static void uncanonize(iptr)
char   *iptr ;
{
    char   *optr = iptr ;   /*  overwrite input buffer  */
    static char   oldch = '\0' ;
    while ( *iptr ) {
	if (( oldch=='\r' && (*iptr=='\n'||*iptr=='\r' )) || *iptr != '\r' )
	    *optr++ = *iptr ;
	oldch = *iptr++;
    }
    *optr = '\0' ;
}

/* Decode ISO-2022-kr coded line to KSC-5601 */
static void decodeISOLine (iptr, optr)
char *iptr, *optr ;
{
    int    shifted = 0 ;   /* 	Each line begins in unshifted state  	*/
    assert( iptr != NULL && optr != NULL );

    while( *iptr ) {
	if ( *iptr == SHIFTOUT ) 
	    shifted = 1 ;
	else if ( *iptr == SHIFTIN ) 
	    shifted = 0 ;
	else if ( shifted  && *iptr > ' ' && *iptr <  DEL )
	    *optr++ = (char) ( (unsigned char) *iptr + OFFSET);
	else 
	    *optr++ = *iptr ; 
	iptr++ ;
    }
    *optr = '\0';
    assert( !shifted );  /* missing shift-in code ?? */
}

/*
 *	decodeB64Str()
 *	Return value : actual decoded resulting string length.
 *   	limit is max length to decode, actual input may be shorter.
 *	Input size may be not multiple of 3 or 4. returns right size.
 *
 *	Adapted by from bq.c,   Copyright (C) 1992 Ienup Sung.
 *  @(#)bq.c: base64 encode/decode modules by is@ev.trigem.co.kr   1992.7.22
 */

#define LS6B			00077L	/* least significant 6 bits */
#define LS8B			00377L	/* least significant 8 bits */
#define PAD			'='

static char *b64_alphabet = 
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

/* Decode base64 encoded string */
static int decodeB64Str(ibuf, obuf, limit )
char ibuf[], obuf[];
int	limit ;
{
    register unsigned long bitbuf = 0 ;
    char    *iptr = ibuf, *optr = obuf, *offs ;
    int     valid = 0 , mod4 = 0 ;
    assert( ibuf !=NULL && obuf != NULL && limit >= 0 ) ;

    while  ( limit > 0 ) { 
        bitbuf = (bitbuf << 6) & ~ LS6B;
	if( (offs = strchr( b64_alphabet, *iptr )) != NULL ) {
	    bitbuf |= (unsigned long) (offs - b64_alphabet) ;
	    valid++ ; 
	}
	else   /*  if *iptr is PAD or non b64 alphabet, ignore   */ 
	    bitbuf &= ~LS6B;

	iptr++ ;
        if  (  *iptr == '\0' || iptr - ibuf >= limit ) {
	    /* 	 align to 4 * 6 bit shifted postion */
	    while  ( ++mod4 % 4  != 0 ) bitbuf = (bitbuf << 6) & ~ LS6B;
	    limit = 0 ;   /*   exit root   */
	}
	else
	    ++mod4 ;
	if ( mod4 % 4 == 0 ) {
	    if (valid >= 2 ) *optr++ = (char)((bitbuf >> 16 ) & LS8B);
	    if (valid >= 3 ) *optr++ = (char)((bitbuf >> 8 ) & LS8B);
	    if (valid == 4 ) *optr++ = (char)((bitbuf) & LS8B);
	    bitbuf = 0 ; valid = 0 ; 
	} 
    } 
    *optr = '\0';
    return(optr - obuf);
} 

/* RFC1341 BASE64 BODY section decoding */ 
static void decodeB64Line(ibuf, obuf)
char ibuf[], obuf[] ;
{
    assert( ibuf != NULL && obuf != NULL );
    decodeB64Str(ibuf, obuf, strlen(ibuf)-1) ;   /* ignore '\n'  */
}

/* Convert two hexadecimal digit char to integer  	*/
/*   ex)  h2toi('4', 'E') == 0x4e == 'N' 		*/
/* If any char is not hexadecimal digit, return -1	*/
static int h2toi( ch1, ch2 )
char ch1, ch2 ;
{
    unsigned d1, d2 ;

    if ((ch1) >= '0' && (ch1) <= '9' ) d1 = ( ch1 - '0' );
    else if ((ch1) >= 'A' && (ch1) <= 'F' ) d1 = ( 10 + ch1 - 'A' );
    else if ((ch1) >= 'a' && (ch1) <= 'f' )  d1 = ( 10 + ch1 - 'a' );
    else return(-1);

    if ((ch2) >= '0' && (ch2) <= '9' ) d2 = ( ch2 - '0' );
    else if ((ch2) >= 'A' && (ch2) <= 'F' ) d2 = ( 10 + ch2 - 'A' );
    else if ((ch2) >= 'a' && (ch2) <= 'f' )  d2 = ( 10 + ch2 - 'a' );
    else return(-1);
 
    return ( (int) (((d1<<4) + d2 ) & LS8B)) ;
}

static void decodeQPStr(ibuf, obuf, limit)
char ibuf[], obuf[] ;
int limit ;
{
    char *iptr = ibuf, *optr = obuf ;
    int ctmp ;
    assert( iptr != NULL && obuf != NULL && limit >= 0 );

    while( *iptr && ( iptr - ibuf < limit ) ) {
	if ( *iptr == '=' && ( ctmp = h2toi( iptr[1], iptr[2])) >= 0 ){
	    *optr++ = (char) ctmp ;
	    iptr += 3 ; 
	}
	else if ( *iptr == '_' ) {  /* 	translate    */
	    *optr++ = ' ' ; iptr++ ;
	}
	else  
	    *optr++ = *iptr++ ;
    }
    *optr = '\0' ;
}

/* do RFC1341 QP BODY section decoding */ 
static void decodeQPLine(iptr, obuf)
char *iptr, obuf[] ;
{
    char   *optr = obuf ;
    int ctmp ;   /*    h2toi() returns -1 on non-hexa digit	*/
    assert( iptr != NULL && obuf != NULL );

    while( *iptr ) {
	if ( *iptr == '=' && ( ctmp = h2toi( iptr[1], iptr[2])) >= 0 ){
	    *optr++ = (char) ctmp ;
	    iptr += 3 ;
	}
	else if ( *iptr == '=' && ( iptr[1] == '\n' )) 
	    iptr += 2 ; /*   skip soft line break     */ 
	else 
	    *optr++ = *iptr++;
    }
    *optr = '\0' ;
}

/*   Cut off trailing blanks or CR-LF to LF */ 
static void fixTrailer(ibuf)
char ibuf[] ;
{
    char *end = ibuf + strlen(ibuf)-1 ; /*  line break  */
    assert( ibuf != NULL ) ;

    if ( *end == '\n' && end >= ibuf ) end-- ;
    if ( *end == '\r' && end >= ibuf  ) end-- ;
    while (( *end == ' ' || *end == '\t' ) &&  end >= ibuf ) end-- ;
    if ( *++end != '\n' ) 
	strcpy( end, "\n") ;
}
	
/*    similar to strncpy(), but "to" string is always terminated  */
static void strncpyz(to, from, len)
char *to, *from ;
int len ;
{
    assert( to != NULL && from != NULL && len >= 0 ) ;
    while( len-- > 0 && *from )
	*to++ = *from++;
    *to = '\0';
}

/* Decode header section by RFC1342 MIME "Q" or "B" header encoding rule */
static enum encode_t decodeHeader(iptr, optr, HeadEncoding)
char *iptr, *optr ;
enum encode_t HeadEncoding;
{
    char *preptr, *sufptr, *txtptr, *postptr ;
    assert( iptr != NULL && optr != NULL );
    
    while(*iptr ) {
	if ( ( preptr = strstr( iptr, PREFIX )) == NULL
	    || ( sufptr = strchr( preptr+strlen(PREFIX), '?' )) == NULL 
	    /*   misssing POSTFIX, do not decode   */
	    || ( postptr = strstr( sufptr+strlen(SUFFIXQP), POSTFIX ))==NULL ) {
	    strcpy(optr, iptr ) ;
	    return HeadEncoding;
	}
	txtptr = sufptr+strlen(SUFFIXQP) ; 
	/* (header)  =?EUC-KR?Q?=89=AB=CD=EF?=       */
	/* (ptr's)   ^pre    ^sf^txt        ^post    */ 

	strncpy( optr, iptr, preptr-iptr ) ;
	optr += preptr - iptr ;    /* watch out order */
	iptr = preptr ;

	if ( strncasecmp( sufptr, SUFFIXQP, strlen(SUFFIXQP) ) == 0 ) {
	    decodeQPStr( txtptr , optr, postptr-txtptr ) ; 
	    HeadEncoding = ENC_QP ;
	}
	else if ( strncasecmp( sufptr, SUFFIXB64, strlen(SUFFIXB64) ) == 0 ) {
	    decodeB64Str( txtptr , optr, postptr-txtptr ) ; 
	    HeadEncoding = ENC_B64 ;
	}
	/* For compatibility with old (before Dec. 94) elm2.3h or hcode2.0  */
	else if ( strncasecmp( preptr, OLDPREFIX, strlen(OLDPREFIX)) == 0 ) {
	    txtptr = preptr+strlen(OLDPREFIX) ; 
	    decodeB64Str( txtptr , optr, postptr-txtptr ) ; 
	    HeadEncoding = ENC_B64 ;
	}
	else {   /* Unknown coding, do not decode */
	    strncpyz( optr, iptr, postptr+ strlen(POSTFIX)-iptr );
	}

	optr += strlen(optr) ;
	iptr = postptr + strlen(POSTFIX) ;
        *optr = '\0';
    }
    return HeadEncoding;
}

static int replace_charset(ibuf)
char *ibuf;
{
    char *p, *q;

    if ((p = strstr(ibuf, "charset="))) {	/* replace with "euc-kr" */
	q = p + 8;
	if (*q == '"')
	    q++;
	if (strncasecmp(q, "iso-2022-kr", 11) == 0 ||
	    strncasecmp(q, "iso-8859-1",  10) == 0)
	    strcpy(p+8, "EUC-KR\n");
	return 1;		/* charset detected */
    }
    return 0;
}

static char *strcasestr(buf, str)
char *buf;
char *str;
{
    int i, n;
    int lenstr = strlen(str);

    n = strlen(buf) - lenstr + 1;
    for (i=0; i<n; i++,buf++)
	if (strncasecmp(buf, str, lenstr) == 0)
	    return buf;
    return NULL;
}

static char *get_mpb_string(ibuf)
char *ibuf;
{
    char *p, *bstr=NULL;
    int len;

    if ((p = strcasestr(ibuf, "boundary=\""))) {	/* mpString */
	p += 10;
	len = strlen(p);
	if (len > 10) {		/* minimum length of the boundary string */
	    bstr = strdup(p);
	    p = bstr + len;
	    while (*--p == '\n' || *p == '"' || *p == ';')
		*p = '\0';
	}
    }
    return bstr;
}

static int isContentTypeText(cstr)
char *cstr;
{
    return (strcasestr(cstr, "text") != NULL);
}

static int isUueHeader(str)
char *str;
{
    int i, n;

    while (isspace(*str))
	str++;
    if (strncasecmp(str, "begin ", 6) != 0)
	return 0;

    /* check three digits and a <blank>. */
    str += 6;
    n = strlen(str);
    if (n < 5)		/* 3 digits, 1 blank, and 1 filename */
	return 0;

    for (i=0; i<3; i++)
	if (!isdigit(*str++))
	    return 0;
    while (isspace(*str))	/* skip blanks */
	str++;
    if (*str)
	return 1;
    return 0;
}

static enum section_t
hMailDecode(ibuf, obuf)
char *ibuf;
char *obuf;
{
    char *p, *q;
    static enum section_t section = SEC_HEADER ;
    static enum encode_t HeadEncoding = ENC_UNKNOWN;
    static enum encode_t Encoding = ENC_UNKNOWN;
    static int  isoMode = 0 ;
    static int  isPendingCT = 0;	/* previous CT header is incomplete */
    static char *mpBoundary = NULL;	/* multipart boundary text holder */

    /* initialize */
    if (!ibuf || !*ibuf) {
	section = SEC_HEADER;
	HeadEncoding = ENC_UNKNOWN;
	Encoding = ENC_UNKNOWN;
	isoMode = 0;
	isPendingCT = 0;
	if (mpBoundary)
	    free(mpBoundary);
	mpBoundary = NULL;
	return section;
    }

    fixTrailer(ibuf);
    if (section == SEC_HEADER && *ibuf == '\n') {
	section = SEC_BODY;
	strcpy(obuf, "\n");
	return section;
    }

    if (section == SEC_HEADER) {

	if (isPendingCT) {
	    if (!isspace(*ibuf))
		isPendingCT = 0;
	    else if (!replace_charset(ibuf) && !mpBoundary
			&& (mpBoundary = get_mpb_string(ibuf))) {
		strcpy(obuf, ibuf);
		uncanonize(obuf);
		return section;
	    }
	}

	/* Content-Type must be checked before Content-Transfer-Encoding */
	if (strncasecmp(ibuf, HEADER_CT, strlen(HEADER_CT)) == 0) {
	    p = ibuf + strlen(HEADER_CT);
	    if ((q = strcasestr(p, "multipart"))) {
		if ((mpBoundary = get_mpb_string(q+9)) == 0)
		    isPendingCT = 1;		/* continued header */
	    } else if (!isContentTypeText(p)) {
		Encoding = ENC_NONE;
	    } else if (!replace_charset(p))
		isPendingCT = 1;
	    strcpy(obuf, ibuf);
	    /* Encoding = ENC_ISO and iso-8859-1 */
	}
	else if (Encoding != ENC_NONE &&
		strncasecmp(ibuf, HEADER_CTE, strlen(HEADER_CTE)) == 0) {
	    Encoding = encodingInfo(ibuf+strlen(HEADER_CTE)) ;
	    if (Encoding == ENC_QP || Encoding == ENC_B64) 
		sprintf(obuf, "%s%s\n", HEADER_CTE, "8bit") ;
	    else
		strcpy(obuf, ibuf);
	}
	else if (strstr(ibuf, PREFIX))
	    HeadEncoding = decodeHeader(ibuf, obuf, HeadEncoding);
	else
	    strcpy(obuf, ibuf);
    }
    else if (section == SEC_BODY) {

	if (mpBoundary && strstr(ibuf, mpBoundary)) {
	    section = SEC_HEADER;
	    HeadEncoding = ENC_UNKNOWN;
	    Encoding = ENC_UNKNOWN;
	    isoMode = 0;
	    strcpy(obuf, ibuf);
	}
	    
	else if (Encoding == ENC_NONE)
	    strcpy(obuf, ibuf);
	else if (isUueHeader(ibuf)) {
	    Encoding = ENC_NONE;
	    strcpy(obuf, ibuf);
	}

	else if (Encoding == ENC_QP)
	    decodeQPLine(ibuf, obuf);
	else if (Encoding == ENC_B64)
	    decodeB64Line(ibuf, obuf) ; 
	else if ((p = strstr(ibuf, INTRO_ISO))) {
	    /* remove ISO intro sequnce from ibuf */
	    strcpy( p, p + strlen(INTRO_ISO)); 
	    decodeISOLine(ibuf, obuf);
	    isoMode = 1 ;
	}
    /*
     * If headers are "B" encoded AND content line has SO char without prioior 
     * ISO introducer, we assume missing introducer. It's feature.
     */
	else if ((isoMode || HeadEncoding == ENC_B64)
				&& strchr(ibuf, SHIFTOUT) != NULL )
	    decodeISOLine(ibuf, obuf );
	else
	    strcpy(obuf, ibuf);
    }
    uncanonize(obuf);
    return section;
}

/*
** Is it posted on a Han newsgroups?
*/
int
IsHanNewsgroups(char *line)
{
    char *p;

    for (p=line; p; p++) {
	while (isspace(*p))
	    p++;
	if (strncmp(p, "han.", 4) == 0 &&
			strncmp(p, "han.test", 8) != 0)
	    return TRUE;
	p = strchr(p, ',');
	if (p == NULL)
	    break;
    }
    return FALSE;
}
    

/*
** Retrun CleanQP filtered article.  NULL indicates ERROR.
*/
char *
hNewsCleanQP(char *article, int checkNewsgroups)
{
    char	*newart;
    size_t	newlen;
    int		used;
    char	*p, *q, *next;
    char	hold;
    char	*orig = NULL;
    enum	section_t section;

    newlen = strlen(article) + LSIZ;
    newart = malloc(newlen);
    if (newart == NULL) {
	fprintf(stderr, "hNewsDecode: can't malloc %d bytes\n", newlen);
	return NULL;
    }

    section = hMailDecode((char *)NULL, (char *)NULL);
    next = article;
    used = 0;
    for (p=next; next; p=next, *p=hold) {

	/*
	** Make the input line.  Remember the char of start of next line.
	*/
	next = strchr(p, '\n');
	if (next) {
	    hold = *++next;
	    *next = '\0';
	}

	/*
	** Check Newsgroups line.
	*/
	if (checkNewsgroups && strncasecmp(p, "newsgroups:", 11) == 0) {
	    checkNewsgroups = FALSE;
	    if (!IsHanNewsgroups(p+11)) {
		free(newart);
		if (next)
		    *next = hold;
		return NULL;
	    }
	}

	/*
	** Allocate output space
	*/
	if (newlen - used < LSIZ + LSIZ) {
	    newlen += LSIZ + LSIZ;
	    newart = realloc(newart, newlen);
	    if (newart == NULL) {
		fprintf(stderr, "hNewsDecode: can't realloc %d bytes\n",
			newlen);
		if (next)
		    *next = hold;		/* recover old char */
		return NULL;
	    }
	}

	/*
	** Apply filter, and set up next output pointer.
	*/
	q = newart + used;
	strcpy(q, p);
	section = hMailDecode(q, q);
	if (section == SEC_HEADER) {
	    if (orig == NULL && !isspace(*p) && strcmp(p, q))
		orig = p;
	    if (orig && (!isspace(hold) || hold == '\n')) {
		used += strlen(q);
		sprintf(newart+used, "X-Orig-%s", orig);
		orig = NULL;
	    }
	}
	used += strlen(newart+used);
	
	if (next == NULL)
	    break;
    }
    return newart;
}

#ifdef _MAIN

int main(argc, argv)
int argc;
char **argv;
{
    char	*article, *newart;
    char	line[LSIZ];
    int		len;
    int		used = 0;
    size_t	artlen = 0;
    int		checkNewsgroups = FALSE;
    int		i;
    char	*infile = NULL;

    for (i=1; i<argc; i++)
	if (strcmp(argv[i], "-n") == 0)
	    checkNewsgroups = TRUE;
	else if (*argv[i] != '-' && infile == NULL)
	    infile = argv[i];
	else {
	    fprintf(stderr, "usage: %s [-n] [file]\n", argv[0]);
	    exit(1);
	}

    if (infile && !freopen(infile, "r", stdin)) {
	fprintf(stderr, "can't open input %s\n", infile);
	exit(1);
    }

    artlen = 100 * LSIZ;
    article = malloc(artlen);
    if (article == NULL) {
	fprintf(stderr, "can't malloc %d bytes\n", artlen);
	exit(1);
    }
    while (fgets(line, sizeof(line), stdin)) {
	len = strlen(line);
	if (artlen <= used + len) {
	    artlen += LSIZ * 10;
	    article = realloc(article, artlen);
	    if (article == NULL) {
		fprintf(stderr, "can't realloc %d bytes\n", artlen);
		exit(1);
	    }
	}
	strncpy(article+used, line, len);
	used += len;
    }
    *(article + used) = '\0';
    newart = hNewsCleanQP(article, checkNewsgroups);
    if (newart) {
	free(article);
	article = newart;
    }
    while (*article) {
	putchar(*article++);
    }
    return 0;
}
#endif	/* _MAIN */
#endif	/* CLEAN_QP */
