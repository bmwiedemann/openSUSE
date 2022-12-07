#
# complete.tcsh		Define some intelligent command completions
#
# Modified version of complete.tcsh (1993) found in the source code
# the tcsh-6.03.  Complemented with the following versions and extend
# with other features. This was a part of csh.cshrc until 1999/06/25.
#
# Author: 1993-99 Werner Fink <werner@suse.de>
#
# 1999/06/28: <werner@suse.de> resort to the order to fit complete.tcsh
#		found in tcsh-6.08.05, add the mh completes.
#
    set autolist=ambiguous
    set noglob
#
    set hosts
    foreach _f ("$HOME/.hosts" /etc/csh.hosts "$HOME/.rhosts" /etc/hosts.equiv)
	if ( -r $_f ) then
	    set hosts=($hosts `grep -E -shv '^#|\+' $_f |awk '{ print $1 }'`)
	endif
    end
    if ( -r "$HOME/.netrc" ) then
	set _f=`awk '/machine/ { print $2 }' < "$HOME/.netrc"` >& /dev/null
	set hosts=($hosts $_f)
    endif
    set hosts=(`echo $hosts localhost $HOSTNAME|tr ' ' '\n'|sort -u -t '.'`)
    unset _f
    set _maildir = /var/mail
    set _ypdir  =  /var/yp
    set _domain =  "`domainname`"
    if ($?MANPATH) then
	set _manpath="{${MANPATH:as/:/,/}}/man"
    else
	set _manpath="/usr{{/X11/man,/openwin/man,/share/man}/{man,cat},{/man/{man,cat}}}"
    endif
if ( -d /usr/lib/ispell/ ) then
    set _hash=(`\ls -1fUA /usr/lib/ispell/|&\sed -rn \\%.\*\\.hash%{s%\.hash%%p}`)
else
    set _hash=(english deutsch)
endif
    complete ispell	c/-/"(a A b B C d D e ee f L m M p s S T v vv w W)"/ \
			n@-d@"(${_hash})"@ \
			n/-T/"(utf8 tex plaintex nroff latin1 ascii atari)"/ \
			n@-p@'`ls -1 "$HOME"/.ispell_*`'@ \
			n/-W/"(1 2 3 4 5)"/ \
			n/-L/x:'ispell -L <number>'/ \
			n/-f/t/ n/*/f:^*.{dvi,ps,a,o,gz,z,Z}/
    unset _hash
    complete ywho	n/*/\$hosts/	# argument from list in $hosts
    complete {r,s}sh	p/1/\$hosts/ c/-/"(l n)"/   n/-l/u/ N/-l/c/ n/-/c/ p/2/c/ p/*/f/
    complete xrsh	p/1/\$hosts/ c/-/"(l 8 e)"/ n/-l/u/ N/-l/c/ n/-/c/ p/2/c/ p/*/f/
    complete {r,s}login	p/1/\$hosts/ c/-/"(l 8 e)"/ n/-l/u/
    complete xlogin	n/*/\$hosts/
    complete telnet	p/1/\$hosts/ p/2/x:'<port>'/ n/*/n/
    complete xtelnet	n/*/\$hosts/ 
    complete cd		p/1/d/		# Directories only
    complete chdir	p/1/d/
    complete pushd	p/1/d/
    complete popd	p/1/d/
    complete pu		p/1/d/
    complete po		p/1/d/
    complete complete	p/1/X/		# Completions only
    complete uncomplete	n/*/X/
    complete exec	p/1/c/		# Commands only
    complete trace	p/1/c/
    complete strace	p/1/c/
    complete which	n/*/c/
    complete where	n/*/c/
    complete skill	p/1/c/
    complete dde	p/1/c/ 
    complete adb	c/-I/d/ n/-/c/ N/-/"(core)"/ p/1/c/ p/2/"(core)"/
    complete sdb	p/1/c/
    complete dbx	c/-I/d/ n/-/c/ N/-/"(core)"/ p/1/c/ p/2/"(core)"/
    complete xdb	p/1/c/
    complete gdb	n/-d/d/ n/*/c/
    complete ups	p/1/c/
    complete set	'c/*=/f/' 'p/1/s/=' 'n/=/f/'
    complete unset	n/*/s/
    complete alias	p/1/a/		# only aliases are valid
    complete unalias	n/*/a/
    complete xdvi	n/*/f:*.dvi/	# Only files that match *.dvi
    complete laser	n/*/f:*.dvi/
    complete dvips	n/*/f:*.dvi/
    complete tex	n/*/f:*.{tex,TEX}/	# Only files that match *.tex
    complete latex	n/*/f:*.{tex,TEX,texi,latex,ltx}/
    complete pdftex	n/*/f:*.{tex,TEX}/	# Only files that match *.tex
    complete pdflatex	n/*/f:*.{tex,TEX,texi,latex,ltx}/
    complete slitex	n/*/f:*.{tex,TEX,latex,ltx}/
    complete su		c/--/"(login fast preserve-environment command shell \
			help version)"/	c/-/"(f l m p c s -)"/ \
			n/{-c,--command}/c/ \
			n@{-s,--shell}@'`cat /etc/shells`'@ n/*/u/
    complete cc		c/-[IL]/d/ \
			c@-l@'`\ls -1 /usr/lib/lib*.a | sed s%^.\*/lib%%\;s%\\.a\$%%`'@ \
			c/-/"(o l c g L I D U)"/ n/*/f:*.[coasi]/
    complete acc	c/-[IL]/d/ \
			c@-l@'`\ls -1 /usr/lang/SC1.0/lib*.a | sed s%^.\*/lib%%\;s%\\.a\$%%`'@ \
			c/-/"(o l c g L I D U)"/ n/*/f:*.[coasi]/
    complete gcc	c/-[IL]/d/ \
			c/-f/"(caller-saves cse-follow-jumps delayed-branch \
			       elide-constructors expensive-optimizations \
			       float-store force-addr force-mem inline \
			       inline-functions keep-inline-functions \
			       memoize-lookups no-default-inline \
			       no-defer-pop no-function-cse omit-frame-pointer \
			       rerun-cse-after-loop schedule-insns \
			       schedule-insns2 strength-reduce \
			       thread-jumps unroll-all-loops \
			       unroll-loops syntax-only all-virtual \
			       cond-mismatch dollars-in-identifiers \
			       enum-int-equiv no-asm no-builtin \
			       no-strict-prototype signed-bitfields \
			       signed-char this-is-variable unsigned-bitfields \
			       unsigned-char writable-strings call-saved-reg \
			       call-used-reg fixed-reg no-common \
			       no-gnu-binutils nonnull-objects \
			       pcc-struct-return pic PIC shared-data \
			       short-enums short-double volatile)"/ \
			c/-W/"(all aggregate-return cast-align cast-qual \
			       comment conversion enum-clash error format \
			       id-clash-len implicit missing-prototypes \
			       no-parentheses pointer-arith return-type shadow \
			       strict-prototypes switch uninitialized unused \
			       write-strings)"/ \
			c/-m/"(68000 68020 68881 bitfield fpa nobitfield rtd \
			       short c68000 c68020 soft-float g gnu unix fpu \
			       no-epilogue)"/ \
			c/-d/"(D M N)"/ \
			c/-/"(f W vspec v vpath ansi traditional \
			      traditional-cpp trigraphs pedantic x o l c g L \
			      I D U O O2 C E H B b V M MD MM i dynamic \
			      nodtdlib static nostdinc undef)"/ \
			c/-l/f:*.a/ \
			n/*/f:*.{c,C,cc,o,a,s,i}/
    complete g++	n/*/f:*.{C,cc,cpp,o,s,i}/
    complete CC		n/*/f:*.{C,cc,cpp,o,s,i}/
    complete rm		c/--/"(directory force interactive verbose \
			recursive help version)"/ c/-/"(d f i v r R -)"/ \
			n/*/f:^*.{c,cc,C,h,in}/	# Protect precious files
    complete {vi,more}	n/*/f:^*.{o,a,dvi,gz,z,Z}/
    complete less	n/*/f:^*.{o,a,dvi}/
    complete bindkey	N/-a/b/ N/-c/c/ n/-[ascr]/'x:<key-sequence>'/ \
			n/-[svedlr]/n/ c/-[vedl]/n/ c/-/"(a s k c v e d l r)"/ \
			n/-k/"(left right up down)"/ p/2-/b/ \
			p/1/'x:<key-sequence or option>'/

    complete find	n/-fstype/"(nfs 4.2)"/ n/-name/f/ \
			n/-type/"(c b d f p l s)"/ n/-user/u/ n/-group/g/ \
			n/-exec/c/ n/-ok/c/ n/-cpio/f/ n/-ncpio/f/ n/-newer/f/ \
			c/-/"(follow fstype name perm prune type user nouser \
			     group nogroup size inum atime mtime ctime exec \
			     ok print ls cpio ncpio newer xdev depth \
			     daystart follow maxdepth mindepth noleaf version \
			     anewer cnewer amin cmin mmin true false uid gid \
			     ilname iname ipath iregex links lname empty path \
			     regex used xtype fprint fprint0 fprintf \
			     print0 printf not a and o or)"/ \
			n/*/d/

    complete -%*	c/%/j/			# fill in the jobs builtin
    complete -./*	p/0/C/			# expand local executables
    complete {fg,bg,stop}	c/%/j/ p/1/"(%)"//

    complete limit	c/-/"(h)"/ n/*/l/
    complete unlimit	c/-/"(h)"/ n/*/l/

    complete nm		n/*/f:^*.{h,C,c,cc}/

    complete finger	c/*@/\$hosts/ n/*/u/@ 
    complete ping	p/1/\$hosts/
    complete traceroute	p/1/\$hosts/

    complete {talk,ntalk,phone,otalk,ytalk}	p/1/'`users | tr " " "\012" | uniq`'/ \
		n/*/\`who\ \|\ grep\ \$:1\ \|\ awk\ \'\{\ print\ \$2\ \}\'\`/

    complete ftp	c/-/"(d i g n v)"/ n/-/\$hosts/ p/1/\$hosts/ n/*/n/
    complete ncftp	c/-/"(a I N)"/     n/-/\$hosts/ p/1/\$hosts/ n/*/n/

    # this one is simple...
    #complete rcp c/*:/f/ C@[./\$~]*@f@ n/*/\$hosts/:
    # From Michael Schroeder <mlschroe@immd4.informatik.uni-erlangen.de>
    # This one will rsh to the file to fetch the list of files!
    complete rcp 'c%*@*:%`set q=$:-0;set q="$q:s/@/ /";set q="$q:s/:/ /";set q=($q " ");rsh $q[2] -l $q[1] ls -dp $q[3]\*`%' 'c%*:%`set q=$:-0;set q="$q:s/:/ /";set q=($q " ");rsh $q[1] ls -dp $q[2]\*`%' 'c%*@%$hosts%:' 'C@[./$~]*@f@'  'n/*/$hosts/:'
    complete scp 'c%*@*:%`set q=$:-0;set q="$q:s/@/ /";set q="$q:s/:/ /";set q=($q " ");ssh $q[2] -l $q[1] ls -dp $q[3]\*`%' 'c%*:%`set q=$:-0;set q="$q:s/:/ /";set q=($q " ");ssh $q[1] ls -dp $q[2]\*`%' 'c%*@%$hosts%:' 'C@[./$~]*@f@'  'n/*/$hosts/:'

    complete dd	c/--/"(help version)"/ c/[io]f=/f/ \
		c/conv=*,/"(ascii ebcdic ibm block unblock \
			    lcase notrunc ucase swab noerror sync)"/,\
		c/conv=/"(ascii ebcdic ibm block unblock \
			  lcase notrunc ucase swab noerror sync)"/,\
		c/*=/x:'<number>'/ \
		n/*/"(if of conv ibs obs bs cbs files skip file seek count)"/=

    complete nslookup	p/1/x:'<host>'/ p/2/\$hosts/

    complete ar	c/[dmpqrtx]/"(c l o u v a b i)"/ p/1/"(d m p q r t x)"// \
		p/2/f:*.a/ p/*/f:*.o/

    # these should be merged with the MH completion hacks below - jgotts
    complete {sprev,snext} \
		c@+@F:"$HOME/Mail/"@

    # these and interrupt handling from Jaap Vermeulen <jaap@sequent.com>
    complete {rexec,rxexec,rxterm,rmterm} \
			'p/1/$hosts/' 'c/-/(l L E)/' 'n/-l/u/' 'n/-L/f/' \
			'n/-E/e/' 'n/*/c/'
    complete kill	'c/-/S/' 'c/%/j/' 'n/*/`ps xh | cut -d " " -f 1`/'

    # these from Marc Horowitz <marc@cam.ov.com>
    complete attach 'n/-mountpoint/d/' 'n/-m/d/' 'n/-type/(afs nfs rvd ufs)/' \
		    'n/-t/(afs nfs rvd ufs)/' 'n/-user/u/' 'n/-U/u/' \
		    'c/-/(verbose quiet force printpath lookup debug map \
			  nomap remap zephyr nozephyr readonly write \
			  mountpoint noexplicit explicit type mountoptions \
			  nosetuid setuid override skipfsck lock user host)/' \
		    'n/-e/f/' 'n/*/()/'
    complete hesinfo	'p/1/u/' \
			'p/2/(passwd group uid grplist pcap pobox cluster \
			      filsys sloc service)/'

    # these from E. Jay Berkenbilt <ejb@ERA.COM>
    # = isn't always followed by a filename or a path anymore - jgotts
    complete ./configure 'c/--*=/f/' 'c/--{cache-file,prefix,exec-prefix,\
				bindir,sbindir,libexecdir,datadir,\
				sysconfdir,sharedstatedir,localstatedir,\
				libdir,includedir,oldincludedir,infodir,\
				mandir,srcdir}/(=)//' \
			 'c/--/(cache-file verbose prefix exec-prefix bindir \
				sbindir libexecdir datadir sysconfdir \
				sharedstatedir localstatedir libdir \
				includedir oldincludedir infodir mandir \
				srcdir)//'
    complete gs 'c/-sDEVICE=/(x11 cdjmono cdj550 epson eps9high epsonc \
			      dfaxhigh dfaxlow laserjet ljet4 sparc pbm \
			      pbmraw pgm pgmraw ppm ppmraw bit)/' \
		'c/-sOutputFile=/f/' 'c/-s/(DEVICE OutputFile)/=' \
		'c/-d/(NODISPLAY NOPLATFONTS NOPAUSE)/' 'n/*/f/'
    complete perl	'n/-S/c/'
    complete printenv	'n/*/e/'
    complete sccs	p/1/"(admin cdc check clean comb deledit delget \
			delta diffs edit enter fix get help info \
			print prs prt rmdel sccsdiff tell unedit \
			unget val what)"/

    # Complete for MH tools already skipped
    if ( $?SKIP_MH ) goto skip_mh

    # Do not be fooled by asking MH tools
    if ( ! -r "$HOME/.mh_profile" ) goto skip_mh

    # Do not be fooled by broken MH profile
    if ( ! `grep -cE '^Path:' "$HOME/.mh_profile"` ) goto skip_mh

    if ( ! $?FOLDERS ) then
	which folders >& /dev/null
	if ( $status != 0 ) goto skip_mh

	set folders="`/bin/sh -c 'exec folders -fast -recurse < /dev/null 2> /dev/null'`"
	if ( $status != 0 ) then
	    unset folders
	    setenv SKIP_MH
	    goto skip_mh
	endif
	setenv FOLDERS "$folders"
    endif

    if ( ! $?MHA ) then
	which ali >& /dev/null
	if ( $status != 0 ) goto skip_mh

	set mha="`/bin/sh -c 'exec ali < /dev/null 2> /dev/null'`"
	if ( $status != 0 ) then
	    unset mha
	    setenv SKIP_MH
	    goto skip_mh
	endif
	setenv MHA "$mha"
    endif

    # these and method of setting hosts from Kimmo Suominen <kim@tac.nyc.ny.us>
    set folders = ( $FOLDERS )
    set mha = ( $MHA )

    complete ali \
	'c/-/(alias nolist list nonormalize normalize nouser user help)/' \
	'n,-alias,f,'

    complete anno \
	'c/-/(component noinplace inplace nodate date text help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete burst \
	'c/-/(noinplace inplace noquiet quiet noverbose verbose help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete comp \
	'c/-/(draftfolder draftmessage nodraftfolder editor noedit file form nouse use whatnowproc nowhatnowproc help)/' \
	'c,+,$folders,'  \
	'n,-whatnowproc,c,'  \
	'n,-file,f,'\
	'n,-form,f,'\
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete dist \
	'c/-/(noannotate annotate draftfolder draftmessage nodraftfolder editor noedit form noinplace inplace whatnowproc nowhatnowproc help)/' \
	'c,+,$folders,'  \
	'n,-whatnowproc,c,'  \
	'n,-form,f,'\
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete folder \
	'c/-/(all nofast fast noheader header nopack pack noverbose verbose norecurse recurse nototal total noprint print nolist list push pop help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete folders \
	'c/-/(all nofast fast noheader header nopack pack noverbose verbose norecurse recurse nototal total noprint print nolist list push pop help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete forw \
	'c/-/(noannotate annotate draftfolder draftmessage nodraftfolder editor noedit filter form noformat format noinplace inplace digest issue volume whatnowproc nowhatnowproc help)/' \
	'c,+,$folders,'  \
	'n,-whatnowproc,c,'  \
	'n,-filter,f,'\
	'n,-form,f,'\
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete inc \
	'c/-/(audit file noaudit nochangecur changecur file form format nosilent silent notruncate truncate width help)/' \
	'c,+,$folders,'  \
	'n,-audit,f,'\
	'n,-form,f,'

    complete mark \
	'c/-/(add delete list sequence nopublic public nozero zero help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete mhmail \
	'c/-/(body cc from subject help)/' \
	'n,-cc,$mha,'  \
	'n,-from,$mha,'  \
	'n/*/$mha/'

    complete mhpath \
	'c/-/(help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete msgchk \
	'c/-/(nodate date nonotify notify help)/' 

    complete msh \
	'c/-/(prompt noscan scan notopcur topcur help)/' 

    complete next \
	'c/-/(draft form moreproc nomoreproc length width showproc noshowproc header noheader help)/' \
	'c,+,$folders,'  \
	'n,-moreproc,c,'  \
	'n,-showproc,c,'  \
	'n,-form,f,'

    complete packf \
	'c/-/(file help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete pick \
	'c/-/(and or not lbrace rbrace cc date from search subject to othercomponent after before datefield sequence nopublic public nozero zero nolist list help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete prev \
	'c/-/(draft form moreproc nomoreproc length width showproc noshowproc header noheader help)/' \
	'c,+,$folders,'  \
	'n,-moreproc,c,'  \
	'n,-showproc,c,'  \
	'n,-form,f,'

    complete prompter \
	'c/-/(erase kill noprepend prepend norapid rapid nodoteof doteof help)/' 

    complete refile \
	'c/-/(draft nolink link nopreserve preserve src file help)/' \
	'c,+,$folders,'  \
	'n,-file,f,'\
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete rmf \
	'c/-/(nointeractive interactive help)/' \
	'c,+,$folders,'  

    complete rmm \
	'c/-/(help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete scan \
	'c/-/(noclear clear form format noheader header width noreverse reverse file help)/' \
	'c,+,$folders,'  \
	'n,-form,f,'\
	'n,-file,f,'\
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete send \
	'c/-/(alias draft draftfolder draftmessage nodraftfolder filter nofilter noformat format noforward forward nomsgid msgid nopush push noverbose verbose nowatch watch width help)/' \
	'n,-alias,f,'\
	'n,-filter,f,'

    complete show \
	'c/-/(draft form moreproc nomoreproc length width showproc noshowproc header noheader help)/' \
	'c,+,$folders,'  \
	'n,-moreproc,c,'  \
	'n,-showproc,c,'  \
	'n,-form,f,'\
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete sortm \
	'c/-/(datefield textfield notextfield limit nolimit noverbose verbose help)/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete vmh \
	'c/-/(prompt vmhproc novmhproc help)/' \
	'n,-vmhproc,c,'  

    complete whatnow \
	'c/-/(draftfolder draftmessage nodraftfolder editor noedit prompt help)/' 

    complete whom \
	'c/-/(alias nocheck check draft draftfolder draftmessage nodraftfolder help)/' \
	'n,-alias,f,'

    complete plum \
	'c/-/()/' \
	'c,+,$folders,'  \
	'n,*,`(mark | sed "s/:.*//";echo next cur prev first last)|tr " " "\n" | sort -u`,'

    complete mail \
	'c/-/()/' \
	'n/*/$mha/'

skip_mh:

    # from George Cox
    complete acroread	'p/*/f:*.{pdf,fdf,PDF,FDF}/'
    complete xpdf	c/-/"(z g remote raise quit cmap rgb papercolor \
			eucjp t1lib freetype ps paperw paperh level1 \
			upw fullscreen cmd q v h help)"/ \
			n/-z/x:'<zoom (-5 .. +5) or "page" or "width">'/ \
			n/-g/x:'<geometry>'/ n/-remote/x:'<name>'/ \
			n/-rgb/x:'<number>'/ n/-papercolor/x:'<color>'/ \
			n/-{t1lib,freetype}/x:'<font_type>'/ \
			n/-ps/x:'<PS_file>'/ n/-paperw/x:'<width>'/ \
			n/-paperh/x:'<height>'/ n/-upw/x:'<password>'/ \
			n/-/f:*.{pdf,PDF}/ \
			N/-{z,g,remote,rgb,papercolor,t1lib,freetype,ps,paperw,paperh,upw}/f:*.{pdf,PDF}/ \
			N/-/x:'<page>'/ p/1/f:*.{pdf,PDF}/ p/2/x:'<page>'/
    complete kpdf	'p/*/f:*.{pdf,fdf,PDF,FDF}/'
    complete qpdf	'p/*/f:*.{pdf,fdf,PDF,FDF}/'
    complete evince	'p/*/f:*.{pdf,fdf,PDF,FDF}/'
    complete apachectl  'c/*/(start stop restart fullstatus status graceful \
			configtest help)/'
    complete appletviewer	'p/*/f:*.class/'
    complete bison	'c/--/(debug defines file-prefix= fixed-output-files \
			help name-prefix= no-lines no-parser output= \
			token-table verbose version yacc)/' \
			'c/-/(b d h k l n o p t v y V)/' 'n/-b/f/' 'n/-o/f/' \
			'n/-p/f/'
    complete bunzip2	'p/*/f:*.bz2/' 
    complete bzip2	'n/-9/f:^*.bz2/' 'n/-d/f:*.bz2/'
    complete c++	'p/*/f:*.{c++,cxx,c,cc,C,cpp}/'
    complete co		'p@1@`\ls -1a RCS | sed -e "s/\(.*\),v/\1/"`@'
    complete crontab	'n/-u/u/'
    complete camcontrol	'p/1/(cmd debug defects devlist eject inquiry \
			modepage negotiate periphlist rescan reset start \
			stop tags tur)/'
    complete ctlinnd	'p/1/(addhist allow begin cancel changegroup \
			checkfile drop feedinfo flush flushlogs go hangup \
			logmode mode name newgroup param pause readers refile \
			reject reload renumber reserve rmgroup send shutdown \
			kill throttle trace xabort xexec)/'
    complete cvs	'c/--/(help help-commands help-synonyms)/' \
			'p/1/(add admin annotate checkout commit diff \
			edit editors export history import init log login \
			logout rdiff release remove rtag status tag unedit \
			update watch watchers)/' 'n/-a/(edit unedit commit \
			all none)/' 'n/watch/(on off add remove)/'
    complete cxx	'p/*/f:*.{c++,cxx,c,cc,C,cpp}/'
    complete detex	'p/*/f:*.tex/'
    complete edquota    'n/*/u/'
    complete exec	'p/1/c/'
    complete ghostview	'p/*/f:*.{eps,EPS,ps,PS,pdf,PDF,ps.gz}/'
    complete gv		'p/*/f:*.{eps,EPS,ps,PS,pdf,PDF,ps.gz}/'
    complete ifconfig	'p@1@`ifconfig -l`@' 'n/*/(range phase link netmask \
			mtu vlandev vlan metric mediaopt down delete \
			broadcast arp debug)/'
    complete imake	'c/-I/d/'
    complete ipfw 	'p/1/(flush add delete list show zero)/' \
			'n/add/(allow permit accept pass deny drop reject \
			reset count skipto num divert port tee port)/'
    complete javac	'p/*/f:*.java/'
    complete ldif2ldbm	'n/-i/f:*.ldif/'
    complete libtool	'c/--mode=/(compile execute finish install link \
			uninstall)/' 'c/--/(config debug dry-run features \
			finish help quiet silent version mode=)/'
    complete libtoolize	'c/--/(automake copy debug dry-run force help ltdl \
			ltdl-tar version)/'
    complete links	'c/-/(assume-codepage async-dns download-dir \
			format-cache-size ftp-proxy help http-proxy \
			max-connections max-connections-to-host \
			memory-cache-size receive-timeout retries \
			unrestartable-receive-timeout version)/'
    complete natd	c/-/'(alias_address config deny_incoming dynamic \
			inport interface log log_denied log_facility \
			outport outport port pptpalias proxy_only \
			proxy_rule redirect_address redirect_port \
			reverse same_ports unregistered_only use_sockets \
			verbose)'/ 'n@-interface@`ifconfig -l`@'
    complete netstat	'n@-I@`ifconfig -l`@'
    complete objdump	'c/--/(adjust-vma= all-headers architecture= \
			archive-headers debugging demangle disassemble \
			disassemble-all disassemble-zeroes dynamic-reloc \
			dynamic-syms endian= file-headers full-contents \
			headers help info line-numbers no-show-raw-insn \
			prefix-addresses private-headers reloc section-headers \
			section=source stabs start-address= stop-address= \
			syms target= version wide)/' \
			'c/-/(a h i f C d D p r R t T x s S l w)/'
    complete xmodmap	'c/-/(display help grammar verbose quiet n e pm pk \
			pke pp)/'
    complete lynx	'c/-/(accept_all_cookies anonymous assume_charset= \
			assume_local_charset= assume_unrec_charset= auth= base \
			book buried_news cache= case cfg= child cookie_file= \
			cookies core crawl debug_partial display= dump editor= \
			emacskeys enable_scrollback error_file= force_html \
			force_secure forms_options from ftp get_data head help \
			hiddenlinks= historical homepage= image_links index= \
			ismap link= localhost mime_header minimal \
			newschunksize= newsmaxchunk= nobrowse nocc nocolor \
			nofilereferer nolist nolog nopause noprint noredir \
			noreferer nostatus number_links partial partial_thres \
			pauth= popup post_data preparsed print pseudo_inlines \
			raw realm reload restrictions= resubmit_posts rlogin \
			selective show_cursor soft_dquotes source stack_dump \
			startfile_ok tagsoup telnet term= tlog trace traversal \
			underscore useragent= validate verbose version vikeys \
			width=)/' 'c/(http|ftp)/$URLS/'
    complete {gmake,make} \
			'c/{--directory,--include-dir}=/d/' 'c/{-C,-I}/d/' \
			'c/{--assume-new,--assume-old,--makefile,--new-file,--what-if,--file}=/f/' \
			'c/{-W,-o,-f}/f/' 'c/*=/f/' \
			'c/--/(assume-new= assume-old= debug directory= \
			dry-run environment-overrides file= help \
			ignore-errors include-dir= jobs[=N] just-print \
			keep-going load-average[=N] makefile= max-load[=N] \
			new-file= no-builtin-rules no-keep-going \
			no-print-directory old-file= print-data-base \
			print-directory question quiet recon silent stop \
			touch version warn-undefined-variables what-if=)//' \
			'c/-/(- C d e f h i I k n p q r R s S t v w)/' \
			'n@*@`cat -s {GNUm,M,m}akefile |& sed -n -e "/cat:/d" -e "s/^\([A-Za-z0-9-]*\):.*/\1/p"`@' \
			'n/=/f/' 'n/-f/f/'
    complete mixer	p/1/'(vol bass treble synth pcm speaker mic cd mix \
			pcm2 rec igain ogain line1 line2 line3)'/ \
			p@2@'`mixer $:-1 | awk \{\ print\ \$7\ \}`'@

    complete mpg123	'c/--/(2to1 4to1 8bit aggressive au audiodevice \
    			auth buffer cdr check doublespeed equalizer frames \
			gain halfspeed headphones left lineout list mix mono \
			proxy quiet random rate reopen resync right scale \
			shuffle single0 single1 skip speaker stdout stereo \
			test verbose wav)/'
    complete mysqladmin	'n/*/(create drop extended-status flush-hosts \
			flush-logs flush-status flush-tables flush-privileges \
			kill password ping processlist reload refresh \
			shutdown status variables version)/'
    set _muttalias=/dev/null
    foreach _f ("$HOME/.muttrc-alias" "$HOME/.muttalias")
	if ( -r $_f ) then
	    set _muttalias=$_f
	    break
	endif
    end
    unset _f
    complete mutt	c@-f=@F:${HOME}/Mail/@ \
			n/-a/f/ \
			n/-F/f/ n/-H/f/ \
			n/-s/x:'<subject line>'/ \
			n/-e/x:'<command>'/ \
			n@-b@'`awk '"'"'{print $2 }'"'"' $_muttalias`'@ \
			n@-c@'`awk '"'"'{print $2 }'"'"' $_muttalias`'@ \
			n@*@'` awk '"'"'{print $2 }'"'"' $_muttalias`'@
    complete ndc	'n/*/(status dumpdb reload stats trace notrace \
			querylog start stop restart )/'
    complete nm		'c/--/(debug-syms defined-only demangle dynamic \
			extern-only format= help line-numbers no-demangle \
			no-sort numeric-sort portability print-armap \
			print-file-name reverse-sort size-sort undefined-only \
			version)/' 'p/*/f:^*.{h,C,c,cc}/'
    complete nmap	'n@-e@`ifconfig -l`@' 'p/*/$hostnames/'
    complete perldoc 	'n@*@`\ls -1 /usr/lib/perl*/5.*/pod | sed s%\\.pod.\*\$%%`@'
    complete postfix    'n/*/(start stop reload abort flush check)/'
    complete postmap	'n/1/(hash: regexp:)' 'c/hash:/f/' 'c/regexp:/f/'
    complete rcsdiff	'p@1@`\ls -1a RCS | sed -e "s/\(.*\),v/\1/"`@'
    complete X		'c/-/(I a ac allowMouseOpenFail allowNonLocalModInDev \
			allowNonLocalXvidtune ar1 ar2 audit auth bestRefresh \
			bgamma bpp broadcast bs c cc class co core deferglyphs \
			disableModInDev disableVidMode displayID dpi dpms f fc \
			flipPixels fn fp gamma ggamma help indirect kb keeptty \
			ld lf logo ls nolisten string noloadxkb nolock nopn \
			once p pn port probeonly query quiet r rgamma s \
			showconfig sp su t terminate to tst v verbose version \
			weight wm x xkbdb xkbmap)/'
    complete vidcontrol	'p/1/(132x25 132x30 132x43 132x50 132x60 40x25 80x25 \
			80x30 80x43 80x50 80x60 EGA_80x25 EGA_80x43 \
			VESA_132x25 VESA_132x30 VESA_132x43 VESA_132x50 \
			VESA_132x60 VESA_800x600 VGA_320x200 VGA_40x25 \
			VGA_80x25 VGA_80x30 VGA_80x50 VGA_80x60)/'
    complete vim	'n/*/f:^*.[oa]/'
    complete where	'n/*/c/'
    complete which	'n/*/c/'
    complete wmsetbg	'c/-/(display D S a b c d e m p s t u w)/' \
			'c/--/(back-color center colors dither help match \
			maxscale parse scale smooth tile update-domain \
			update-wmaker version workspace)/'
    complete xdb	'p/1/c/'
    complete xdvi	'c/-/(allowshell debug display expert gamma hushchars \
			hushchecksums hushspecials install interpreter keep \
			margins nogrey noinstall nomakepk noscan paper safer \
			shrinkbuttonn thorough topmargin underlink version)/' \
			'n/-paper/(a4 a4r a5 a5r)/' 'p/*/f:*.dvi/'
    complete xlock	'c/-/(allowaccess allowroot debug description \
			echokeys enablesaver grabmouse grabserver hide inroot \
			install inwindow mono mousemotion nolock remote \
			resetsaver sound timeelapsed use3d usefirst verbose \
			wireframe background batchcount bg bitmap both3d \
			count cycles delay delta3d display dpmsoff \
			dpmsstandby dpmssuspend endCmd erasedelay erasemode \
			erasetime fg font foreground geometry help \
			icongeometry info invalid left3d lockdelay logoutCmd \
			mailCmd mailIcon message messagefile messagefont \
			messagesfile mode name ncolors nice nomailIcon none3d \
			parent password planfont program resources right3d \
			saturation size startCmd timeout username validate \
			version visual)/' 'n/-mode/(ant atlantis ball bat \
			blot bouboule bounce braid bubble bubble3d bug cage \
			cartoon clock coral crystal daisy dclock decay deco \
			demon dilemma discrete drift eyes fadeplot flag flame \
			flow forest galaxy gears goop grav helix hop hyper \
			ico ifs image invert julia kaleid kumppa lament laser \
			life life1d life3d lightning lisa lissie loop lyapunov \
			mandelbrot marquee matrix maze moebius morph3d \
			mountain munch nose pacman penrose petal pipes puzzle \
			pyro qix roll rotor rubik shape sierpinski slip sphere \
			spiral spline sproingies stairs star starfish strange \
			superquadrics swarm swirl tetris thornbird triangle \
			tube turtle vines voters wator wire world worm xjack \
			blank bomb random)/' 
    complete xfig	'c/-/(display)/' 'p/*/f:*.fig/'
    complete wget 	c/--/"(accept= append-output= background cache= \
			continue convert-links cut-dirs= debug \
			delete-after directory-prefix= domains= \
			dont-remove-listing dot-style= exclude-directories= \
			exclude-domains= execute= follow-ftp \
			force-directories force-html glob= header= help \
			http-passwd= http-user= ignore-length \
			include-directories= input-file= level= mirror \
			no-clobber no-directories no-host-directories \
			no-host-lookup no-parent non-verbose \
			output-document= output-file= passive-ftp \
			proxy-passwd= proxy-user= proxy= quiet quota= \
			recursive reject= relative retr-symlinks save-headers \
			server-response span-hosts spider timeout= \
			timestamping tries= user-agent= verbose version wait=)"/

    # More completions from waz@quahog.nl.nuwc.navy.mil (Tom Warzeka)
    # this one works but is slow and doesn't descend into subdirectories
    # complete	cd	C@[./\$~]*@d@ \
    #			p@1@'`\ls -1F . $cdpath | grep /\$ | sort -u`'@ n@*@n@

    if ( -r /etc/shells ) then
	complete setenv	p@1@e@ n@DISPLAY@\$hosts@: n@SHELL@'`cat /etc/shells`'@ 'c/*:/f/'
    else
	complete setenv	p@1@e@ n@DISPLAY@\$hosts@: 'c/*:/f/'
    endif
    complete unsetenv	n/*/e/

    if (-r "$HOME/.mailrc") then
	complete mail	c/-/"(e i f n s u v)"/ c/*@/\$hosts/ \
			c@+@F:"$HOME/Mail"@ C@[./\$~]@f@ n/-s/x:'<subject>'/ \
			n@-u@T:$_maildir@ n/-f/f/ \
			n@*@'`sed -n s/alias//p "$HOME/.mailrc" | tr -s " " "\t" | cut -f 2`'@
    else
	complete mail	c/-/"(e i f n s u v)"/ c/*@/\$hosts/ \
			c@+@F:"$HOME/Mail"@ C@[./\$~]@f@ n/-s/x:'<subject>'/ \
			n@-u@T:$_maildir@ n/-f/f/ n/*/u/
    endif

    complete man	'n@[0-9n]@`\ls -1fUA ${_manpath}$:-1/|&\sed \\%.\*:%d\;s%\\.$:-1.\*\$%%|\sort -u`@' \
			c@-@"(- f k M P s S t)"@ n@-f@c@ n@-k@x:'<keyword>'@ n/-l/f/ C@./*@f@ n@-[MP]@d@    \
			'N@-[MP]@`\ls -1 $:-1/man? |&\sed -n s%\\..\\+\$%%p`@' \
			'n@-[sS]@`\ls -1 ${_manpath:h}|&\sed -n \\%/.\*:%d\;s%man%%p|\sort -u`@' \
			'n@*@`\find ${_manpath:h} \( -type f -o -type l \) -printf "%f\n"|&\sed -r "\%find:.*:%d;s%([^.]+).([^ ]*?)%\1%g"|\sort -u`@'
    complete ps		c/-t/x:'<tty>'/ c/-/"(a c C e g k l S t u v w x)"/ \
			n/-k/x:'<kernel>'/ N/-k/x:'<core_file>'/ n/*/x:'<PID>'/
    complete compress	c/-/"(c f v b)"/ n/-b/x:'<max_bits>'/ n/*/f:^*.Z/
    complete uncompress	c/-/"(c f v)"/                        n/*/f:*.Z/
    complete psompress	c/-/"(d c f)"/                        n/*/f:^*.Z/

    complete uuencode	p/1/f/ p/2/x:'<decode_pathname>'/ n/*/n/
    complete uudecode	c/-/"(f)"/ n/-f/f:*.{uu,UU}/ p/1/f:*.{uu,UU}/ n/*/n/

    complete xhost	c/[+-]/\$hosts/ n/*/\$hosts/

    complete tcsh	c/-D*=/'x:<value>'/ c/-D/'x:<name>'/ \
			c/-/"(b c d D e f F i l m n q s t v V x X -version)"/ \
			n/-c/c/ n/{-l,--version}/n/ n/*/'f:*.{,t}csh'/

    complete rpm	c/--/"(query verify nodeps nofiles nomd5 noscripts    \
			    nogpg nopgp install upgrade freshen erase allmatches  \
			    notriggers repackage test rebuild recompile initdb    \
			    rebuilddb addsign resign querytags showrc setperms    \
			    setugids all file group package querybynumber qf      \
			    triggeredby whatprovides whatrequires changelog       \
			    configfiles docfiles dump filesbypkg info last list   \
			    provides queryformat requires scripts state triggers  \
			    triggerscripts allfiles badreloc excludepath checksig \
			    excludedocs force hash ignoresize ignorearch ignoreos \
			    includedocs justdb noorder oldpackage percent prefix  \
			    relocate replace-files replacepkgs buildroot clean    \
			    nobuild rmsource rmspec short-circuit sign target     \
			    help version quiet rcfile pipe dbpath root specfile)"/\
			c/-/"(q V K i U F e ba bb bp bc bi bl bs ta tb tp tc  \
			    ti tl ts a f g p c d l R s h ? v vv -)"/              \
			n/{-f,--file}/f/ n/{-g,--group}/g/ n/--pipe/c/ n/--dbpath/d/  \
			n/--querybynumber/x:'<number>'/ n/--triggeredby/x:'<package>'/\
			n/--what{provides,requires}/x:'<capability>'/ n/--root/d/     \
			n/--{qf,queryformat}/x:'<format>'/ n/--buildroot/d/           \
			n/--excludepath/x:'<oldpath>'/  n/--prefix/x:'<newpath>'/     \
			n/--relocate/x:'<oldpath=newpath>'/ n/--target/x:'<platform>'/\
			n/--rcfile/x:'<filelist>'/ n/--specfile/x:'<specfile>'/       \
			n/{-[iUFep],--{install,upgrade,freshen,erase,package}}/f:*.rpm/
if (-X emacs) then
    complete emacs	c/--/"(batch terminal display no-windows no-init-file \
			    user debug-init unibyte multibyte version help \
			    no-site-file funcall load eval insert kill)"/ \
			c/-/"(t d nw q u f l -)"/ c/+/x:'<line_number>'/ \
			n/{-t,--terminal}/x:'<terminal>'/ n/{-d,--display}/x:'<display>'/ \
			n/{-u,--user}/u/ n/{-f,--funcall}/x:'<lisp_function>'/ \
			n@{-l,--load}@F:/usr/share/emacs/@ \
			n/--eval/x:'<expression>'/ n/--insert/f/ n/*/f:^*{[\#~],.dvi,.o}/
endif
if (-X gpg) then
    set _gpg_hash=(`gpg --version | sed -rn '/^Supported algorithms:/,$ {:join; /,$/{N; s/\n//; b join};/^Hash:/{s/(,|.*: )//g;s/.*/\L&/p}}'`)
    set _gpg_cipher=(`gpg --version | sed -rn '/^Supported algorithms:/,$ {:join; /,$/{N; s/\n//; b join};/^Cipher:/{s/(,|.*: )//g;s/.*/\L&/p}}'`)

    complete gpg	c/--/'(sign clearsign detach-sign encrypt symmetric \
			    store decrypt verify search-keys list-keys list-sigs check-sigs \
			    fingerprint list-secret-keys gen-key delete-key \
			    delete-secret-key sign-key lsign-key edit-key gen-revoke \
			    export send-keys recv-keys import list-packets \
			    export-ownertrust import-ownertrust update-trustdb \
			    check-trustdb fix-trustdb dearmor enarmor print-md armor\
			    recipient default-recipient default-recipient-self \
			    local-user textmode output verbose quiet no-tty \
			    force-v3-sigs force-mdc dry-run batch yes no keyring \
			    secret-keyring default-key keyserver charset options \
			    status-fd load-extension rfc1991 openpgp s2k-mode \
			    s2k-digest-algo s2k-cipher-algo cipher-algo digest-algo \
			    compress-algo throw-keyid notation-data help)'/ \
			c/-/'(s b e c d a r u z o v q n N -)'/\
			n/{-z,--s2k-mode,--compress-algo}/'(0 1 2 3 4 5 6 7 8 9)'/ \
			n/{--digest-algo,--print-md,--s2k-digest-algo}/"($_gpg_hash)"/ \
			n/{-u,--local-user}/u/ \
			n/{--cipher-algo,--s2k-cipher-algo}/"($_gpg_cipher)"/ \
			n/{--keyserver}/'<keyserver>'/
    unset _gpg_cipher
    unset _gpg_hash
endif
    complete {gzcat,zcat} c/--/"(force help license quiet version)"/ \
			c/-/"(f h L q V -)"/ n/*/f:*.{gz,Z,z,zip}/
    complete gzip	c/--/"(stdout to-stdout decompress uncompress \
			force help list license no-name quiet recurse \
			suffix test verbose version fast best)"/ \
			c/-/"(c d f h l L n q r S t v V 1 2 3 4 5 6 7 8 9 -)"/ \
			n/{-S,--suffix}/x:'<file_name_suffix>'/ \
			n/{-d,--{de,un}compress}/f:*.{gz,Z,z,zip,taz,tgz}/ \
			N/{-d,--{de,un}compress}/f:*.{gz,Z,z,zip,taz,tgz}/ \
			n/*/f:^*.{gz,Z,z,zip,taz,tgz}/
    complete {gunzip,ungzip} c/--/"(stdout to-stdout force help list license \
			no-name quiet recurse suffix test verbose version)"/ \
			c/-/"(c f h l L n q r S t v V -)"/ \
			n/{-S,--suffix}/x:'<file_name_suffix>'/ \
			n/*/f:*.{gz,Z,z,zip,taz,tgz,tar.gz}/
    complete zgrep	c/-*A/x:'<#_lines_after>'/ c/-*B/x:'<#_lines_before>'/ \
			c/-/"(A b B c C e f h i l n s v V w x)"/ \
			p/1/x:'<limited_regular_expression>'/ N/-*e/f/ \
			n/-*e/x:'<limited_regular_expression>'/ n/-*f/f/ n/*/f/
    complete zegrep	c/-*A/x:'<#_lines_after>'/ c/-*B/x:'<#_lines_before>'/ \
			c/-/"(A b B c C e f h i l n s v V w x)"/ \
			p/1/x:'<full_regular_expression>'/ N/-*e/f/ \
			n/-*e/x:'<full_regular_expression>'/ n/-*f/f/ n/*/f/
    complete zfgrep	c/-*A/x:'<#_lines_after>'/ c/-*B/x:'<#_lines_before>'/ \
			c/-/"(A b B c C e f h i l n s v V w x)"/ \
			p/1/x:'<fixed_string>'/ N/-*e/f/ \
			n/-*e/x:'<fixed_string>'/ n/-*f/f/ n/*/f/
    complete znew	c/-/"(f t v 9 P K)"/ n/*/f:*.Z/
    complete zmore	n/*/f:*.{gz,Z,z,zip,bz2}/
    complete zfile	n/*/f:*.{gz,Z,z,zip,taz,tgz}/
    complete ztouch	n/*/f:*.{gz,Z,z,zip,taz,tgz}/
    complete zforce	n/*/f:^*.{gz,taz,tgz}/

    complete dcop	'p/1/`$:0`/ /' \
			'p/2/`$:0 $:1 | awk \{print\ \$1\}`/ /' \
			'p/3/`$:0 $:1 $:2 | sed "s%.* \(.*\)(.*%\1%"`/ /'

    complete grep	c/-*A/x:'<#_lines_after>'/ c/-*B/x:'<#_lines_before>'/ \
			c/--/"(extended-regexp fixed-regexp basic-regexp \
			regexp file ignore-case word-regexp line-regexp \
			no-messages revert-match version help byte-offset \
			line-number with-filename no-filename quiet silent \
			text directories recursive files-without-match \
			files-with-matches count before-context after-context \
			context binary unix-byte-offsets)"/ \
			c/-/"(A a B b C c d E e F f G H h i L l n q r s U u V v w x)"/ \
			p/1/x:'<limited_regular_expression>'/ N/-*e/f/ \
			n/-*e/x:'<limited_regular_expression>'/ n/-*f/f/ n/*/f/
    complete egrep	c/-*A/x:'<#_lines_after>'/ c/-*B/x:'<#_lines_before>'/ \
			c/--/"(extended-regexp fixed-regexp basic-regexp \
			regexp file ignore-case word-regexp line-regexp \
			no-messages revert-match version help byte-offset \
			line-number with-filename no-filename quiet silent \
			text directories recursive files-without-match \
			files-with-matches count before-context after-context \
			context binary unix-byte-offsets)"/ \
			c/-/"(A a B b C c d E e F f G H h i L l n q r s U u V v w x)"/ \
			p/1/x:'<full_regular_expression>'/ N/-*e/f/ \
			n/-*e/x:'<full_regular_expression>'/ n/-*f/f/ n/*/f/
    complete fgrep	c/-*A/x:'<#_lines_after>'/ c/-*B/x:'<#_lines_before>'/ \
			c/--/"(extended-regexp fixed-regexp basic-regexp \
			regexp file ignore-case word-regexp line-regexp \
			no-messages revert-match version help byte-offset \
			line-number with-filename no-filename quiet silent \
			text directories recursive files-without-match \
			files-with-matches count before-context after-context \
			context binary unix-byte-offsets)"/ \
			c/-/"(A a B b C c d E e F f G H h i L l n q r s U u V v w x)"/ \
			p/1/x:'<fixed_string>'/ N/-*e/f/ \
			n/-*e/x:'<fixed_string>'/ n/-*f/f/ n/*/f/

    complete sed	c/--/"(quiet silent version help expression file)"/   \
			c/-/"(n V e f -)"/ n/{-e,--expression}/x:'<script>'/  \
			n/{-f,--file}/f:*.sed/ N/-{e,f,-{file,expression}}/f/ \
			n/-/x:'<script>'/ N/-/f/ p/1/x:'<script>'/ p/2/f/

    complete users	c/--/"(help version)"/ p/1/x:'<accounting_file>'/
    complete who	c/--/"(heading mesg idle count help message version \
			writable)"/ c/-/"(H T w i u m q s -)"/ \
			p/1/x:'<accounting_file>'/ n/am/"(i)"/ n/are/"(you)"/

    complete chown	c/--/"(changes dereference no-dereference silent \
			quiet reference recursive verbose help version)"/ \
			c/-/"(c f h R v -)"/ C@[./\$~]@f@ c/*[.:]/g/ \
			n/-/u/: p/1/u/. n/*/f/
    complete chgrp	c/--/"(changes no-dereference silent quiet reference \
			recursive verbose help version)"/ \
			c/-/"(c f h R v -)"/ n/-/g/ p/1/g/ n/*/f/
    complete chmod	c/--/"(changes silent quiet verbose reference \
			recursive help version)"/ c/-/"(c f R v)"/
    complete df		c/--/"(all block-size human-readable si inodes \
			kilobytes local megabytes no-sync portability sync \
			type print-type exclude-type help version)"/ \
			c/-/"(a H h i k l m P T t v x)"/
    complete du		c/--/"(all block-size bytes total dereference-args \
			human-readable si kilobytes count-links dereference \
			megabytes separate-dirs summarize one-file-system \
			exclude-from exclude max-depth help version"/ \
			c/-/"(a b c D H h k L l m S s X x)"/

    complete cat	c/--/"(number-nonblank number squeeze-blank show-all \
			show-nonprinting show-ends show-tabs help version)"/ \
			c/-/"(b e n s t u v A E T -)"/ n/*/f/
    complete mv		c/--/"(backup force interactive update verbose suffix \
			version-control help version)"/ \
			c/-/"(b f i u v S V -)"/ \
			n/{-S,--suffix}/x:'<suffix>'/ \
			n/{-V,--version-control}/"(t numbered nil existing \
			never simple)"/ n/-/f/ N/-/d/ p/3-/d/ n/*/f/
    complete cp		c/--/"(archive backup no-dereference force \
			interactive link preserve parents sparse recursive \
			symbolic-link suffix update verbose version-control \
			one-file-system help version)"/ \
			c/-/"(a b d f i l P p R r S s u V v x -)"/ \
			n/-*r/d/ n/{-S,--suffix}/x:'<suffix>'/ \
			n/{-V,--version-control}/"(t numbered nil existing \
			never simple)"/ n/-/f/ N/-/d/ p/3-/d/ n/*/f/
    complete ln		c/--/"(backup directory force no-dereference \
			interactive symbolic suffix verbose version-control \
			help version)"/ \
			c/-/"(b d F f i n S s V v -)"/ \
			n/{-S,--suffix}/x:'<suffix>'/ \
			n/{-V,--version-control}/"(t numbered nil existing \
			never simple)"/ n/-/f/ N/-/x:'<link_name>'/ \
			p/1/f/ p/2/x:'<link_name>'/
    complete touch	c/--/"(date reference time help version)"/ \
			c/-/"(a c d f m r t -)"/ \
			n/{-d,--date}/x:'<date_string>'/ \
			c/--time/"(access atime mtime modify use)"/ \
			n/{-r,--file}/f/ n/-t/x:'<time_stamp>'/ n/*/f/
    complete mkdir	c/--/"(mode parents verbose help version)"/ \
			c/-/"(p m -)"/ \
			n/{-m,--mode}/x:'<mode>'/ n/*/d/
    complete rmdir	c/--/"(ignore-fail-on-non-empty parents verbose help \
			version)"/ c/-/"(p -)"/ n/*/d/

    complete tar	c/-[Acru]*/"(b B C f F g G h i l L M N o P \
			R S T v V w W X z Z j I)"/ \
			c/-[dtx]*/"( B C f F g G i k K m M O p P \
			R s S T v w x X z Z j I)"/ \
			p/1/"(A c d r t u x -A -c -d -r -t -u -x \
			--catenate --concatenate --create --diff --compare \
			--delete --append --list --update --extract --get \
			--help --version)"/ \
			c/--/"(catenate concatenate create diff compare \
			delete append list update extract get atime-preserve \
			block-size read-full-blocks directory checkpoint file \
			force-local info-script new-volume-script incremental \
			listed-incremental dereference ignore-zeros \
			ignore-failed-read keep-old-files starting-file \
			one-file-system tape-length modification-time \
			multi-volume after-date newer old-archive portability \
			to-stdout same-permissions preserve-permissions \
			absolute-paths preserve record-number remove-files \
			same-order preserve-order same-owner sparse \
			files-from null totals verbose label version \
			interactive confirmation verify exclude exclude-from \
			compress uncompress gzip ungzip use-compress-program \
			block-compress help version)"/ \
			c/-/"(b B C f F g G h i k K l L m M N o O p P R s S \
			T v V w W X z Z 0 1 2 3 4 5 6 7 -)"/ \
			C@[/dev]@f@ \
			n/-c*{zf,fz}/x:'<new_gziped_tar_file, device_file, or "-">'/ \
			n/-c*{jf,fj}/x:'<new_bziped_tar_file, device_file, or "-">'/ \
			n/-c*f/x:'<new_tar_file, device_file, or "-">'/ \
			n/-[Adrtuxv]*{zf,fz}/f:*.{tar.gz,tgz}/ n/-[Adrtuxv]*{jf,fj}/f:*.tar.bz2/ \
			n/{-[Adrtuxv]*f,--file}/f:*.tar/ \
			N/-x*{zf,fz}/'`tar -tzf $:-1`'/ N/-x*{jf,fj}/'`tar -tjf $:-1`'/ \
			N/{-x*f,--file}/'`tar -tf $:-1`'/ \
			n/--use-compress-program/c/ \
			n/{-b,--block-size}/x:'<block_size>'/ \
			n/{-V,--label}/x:'<volume_label>'/ \
			n/{-N,--{after-date,newer}}/x:'<date>'/ \
			n/{-L,--tape-length}/x:'<tape_length_in_kB>'/ \
			n/{-C,--directory}/d/ \
			N/{-C,--directory}/'`\ls $:-1`'/ \
			n/-[0-7]/"(l m h)"/

    complete  mount	c/-/"(a n v t r w)"/ n/-t/"(minix iso9660 msdos vfat ext2 nfs proc)"/ \
   			'C@/de@F@' 'C@/*@F@@' 'n@*@`grep -E -v \(^#\|^\$\) /etc/fstab|awk \{\ print\ \$2\ \}`@'
    complete umount	c/-/"(a n t)"/   n/-t/"(minix iso9660 msdos ext2 nfs proc)"/ \
   			n/*/'`mount | cut -d " " -f 3`'/

    # these deal with NIS (formerly YP); if it's not running you don't need 'em
    complete domainname	p@1@D:$_ypdir@" " n@*@n@
    complete ypcat	c@-@"(d k t x)"@ n@-x@n@ n@-d@D:$_ypdir@" " \
			N@-d@\`\\ls\ -1\ $_ypdir/\$:-1\ \|\&\ sed\ -n\ s%\\\\.by\\[a-z\\]\\\*\\\$%%p\`@ \
			p/1/"(aliases ethers passwd group hosts netid.byname networks protocols \
			rpc.byname services)"/
    complete ypmatch	c@-@"(d k t x)"@ n@-x@n@ n@-d@D:$_ypdir@" " \
			N@-d@\`\\ls\ -1\ $_ypdir/\$:-1\ \|\&\ sed\ -n\ s%\\\\.by\\[a-z\\]\\\*\\\$%%p\`@ \
			n@-@x:'<key ...>'@ p@1@x:'<key ...>'@ \
			p/1/"(aliases ethers passwd group hosts netid.byname networks protocols \
			rpc.byname services)"/
    complete ypwhich	c@-@"(d m t x V1 V2)"@ n@-x@n@ n@-d@D:$_ypdir@" " \
			n@-m@\`\\ls\ -1\ $_ypdir/$_domain\ \|\&\sed\ -n\ s%\\\\.by\\[a-z\\]\\\*\\\$%%p\`@ \
			N@-m@n@ n@*@\$hosts@

    # there's no need to clutter the user's shell with these
    unset _maildir _ypdir _domain

    if ( -X lpstat ) then
	set printers=(`lpstat -p -d |& sed -rn '/^printer/{ s/^printer ([^\s]+) .*/\1/p }'`)

	complete lpr	'c/-P/$printers/'
	complete lpq	'c/-P/$printers/'
	complete lprm	'c/-P/$printers/'
	complete dvips	'c/-P/$printers/' 'n/-o/f:*.{ps,PS}/' 'n/*/f:*.dvi/'
	complete dvilj	'p/*/f:*.dvi/'
    else if ( -r /etc/printcap ) then
	set printers=(`sed -n -e '/^[^ 	#][^:]*:/{s/|.*:.*//p;}' /etc/printcap | sort -u`)

	complete lpr	'c/-P/$printers/'
	complete lpq	'c/-P/$printers/'
	complete lprm	'c/-P/$printers/'
	complete lpquota	'p/1/(-Qprlogger)/' 'c/-P/$printers/'
	complete dvips	'c/-P/$printers/' 'n/-o/f:*.{ps,PS}/' 'n/*/f:*.dvi/'
	complete dvilj	'p/*/f:*.dvi/'
    endif

    unset noglob
#
# complete.tcsh ends here
#
