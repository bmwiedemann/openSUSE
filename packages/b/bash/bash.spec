#
# spec file for package bash
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_with     import_function
%bcond_with     sjis

Name:           bash
%define         bextend	 %nil
%define         bversion 5.0
%define         bpatchlvl 11
Version:        %{bversion}.%{bpatchlvl}
Release:        0
Summary:        The GNU Bourne-Again Shell
# The package bash-completion is a source of
# bugs which will hit at most this package
#Recommends:	bash-completion
License:        GPL-3.0-or-later
Group:          System/Shells
Suggests:       command-not-found
Suggests:       bash-doc = %version
URL:            http://www.gnu.org/software/bash/bash.html
# Git:          http://git.savannah.gnu.org/cgit/bash.git
Source0:        ftp://ftp.gnu.org/gnu/bash/bash-%{bversion}%{bextend}.tar.gz
Source1:        bash-%{bversion}-patches.tar.bz2
Source4:        run-tests
Source5:        dot.bashrc
Source6:        dot.profile
Source7:        bash-rpmlintrc
Source8:        baselibs.conf
# Remember unsafe method, compare with
# http://lists.gnu.org/archive/html/bug-bash/2011-03/msg00070.html
# http://lists.gnu.org/archive/html/bug-bash/2011-03/msg00071.html
# http://lists.gnu.org/archive/html/bug-bash/2011-03/msg00073.html
Source9:        bash-4.2-history-myown.dif.bz2
Patch0:         bash-%{bversion}.dif
Patch1:         bash-2.03-manual.patch
Patch2:         bash-4.0-security.patch
Patch3:         bash-4.3-2.4.4.patch
Patch4:         bash-3.0-evalexp.patch
Patch5:         bash-3.0-warn-locale.patch
Patch7:         bash-4.3-decl.patch
Patch9:         bash-4.3-include-unistd.dif
Patch10:        bash-3.2-printf.patch
Patch11:        bash-4.3-loadables.dif
Patch12:        bash-4.1-completion.dif
Patch13:        bash-4.2-nscdunmap.dif
Patch14:        bash-4.3-sigrestart.patch
# PATCH-FIX-UPSTREAM bnc#382214 -- disabled due bnc#806628 by -DBNC382214=0
Patch16:        bash-4.0-setlocale.dif
# PATCH-FIX-UPSTREAM
Patch17:        bash50-fix-016-close-new-fifos.patch
# PATCH-EXTEND-SUSE bnc#828877 -- xterm resizing does not pass to all sub clients
Patch18:        bash-4.3-winch.dif
Patch40:        bash-4.1-bash.bashrc.dif
# PATCH-FIX-SUSE For bsc#1065158 add support for broken Japanese locale Shift JIS
Patch42:        bash-4.3-SJIS.patch
Patch46:        man2html-no-timestamp.patch
Patch47:        bash-4.3-perl522.patch
# PATCH-FIX-SUSE
Patch48:        bash-4.3-extra-import-func.patch
# PATCH-EXTEND-SUSE Allow root to clean file system if filled up
Patch49:        bash-4.3-pathtemp.patch
BuildRequires:  audit-devel
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  patchutils
BuildRequires:  pkg-config
# This has to be always the same version as included in the bash its self
BuildRequires:  readline-devel == 8.0
BuildRequires:  screen
BuildRequires:  sed
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives
%global         _sysconfdir /etc
%global         _incdir     %{_includedir}
%global         _ldldir     /%{_lib}/bash
%global         _minsh      0

%description
Bash is an sh-compatible command interpreter that executes commands
read from standard input or from a file.  Bash incorporates useful
features from the Korn and C shells (ksh and csh).  Bash is intended to
be a conformant implementation of the IEEE Posix Shell and Tools
specification (IEEE Working Group 1003.2).

%package doc
Summary:        Documentation how to Use the GNU Bourne-Again Shell
Group:          Documentation/HTML
Provides:       bash:%{_infodir}/bash.info.gz
Supplements:    packageand(bash:patterns-base-documentation)
PreReq:         %install_info_prereq
BuildArch:      noarch

%description doc
This package contains the documentation for using the bourne shell
interpreter Bash.

%if %{defined lang_package}
%lang_package(bash)
%else

%package lang
Summary:        Languages for package bash
Group:          System/Localization
Requires:       bash = %{version}
Supplements:    bash

%description lang
Provides translations to the package bash
%endif

%package devel
Summary:        Include Files mandatory for Development of bash loadable builtins
Group:          Development/Languages/C and C++

%description devel
This package contains the C header files for writing loadable new
builtins for the interpreter Bash. Use the output of the command
`pkg-config bash --cflags' on the compilers command line.

%package loadables
Summary:        Loadable bash builtins
Group:          System/Shells

%description loadables
This package contains the examples for the ready-to-dynamic-load
builtins found in the source tar ball of the bash:

basename      Return non-directory portion of pathname.

cut	      cut(1) replacement.

dirname       Return directory portion of pathname.

finfo	      Print file info.

getconf       POSIX.2 getconf utility.

head	      Copy first part of files.

id	      POSIX.2 user identity.

ln	      Make links.

logname       Print login name of current user.

mkdir	      Make directories.

pathchk       Check pathnames for validity and portability.

print	      Loadable ksh-93 style print builtin.

printenv      Minimal builtin clone of BSD printenv(1).

push	      Anyone remember TOPS-20?

realpath      Canonicalize pathnames, resolving symlinks.

rmdir	      Remove directory.

sleep	      sleep for fractions of a second.

strftime      Loadable builtin interface to strftime(3).

sync	      Sync the disks by forcing pending filesystem writes to
complete.

tee	      Duplicate standard input.

tty	      Return terminal name.

uname	      Print system information.

unlink	      Remove a directory entry.

whoami	      Print out username of current user.


%prep
%if %{with sjis}
echo -e '\033[1m\033[31mWarning: Shift JIS support is enabled\033[m'
%else
echo -e '\033[1m\032[31mShift JIS support disabled\033[m'
%endif
%setup -q -n bash-%{bversion}%{bextend} -b1
typeset -i level
for patch in ../bash-%{bversion}-patches/*; do
    test -e $patch || break
    let level=0 || true
    file=$(lsdiff --files=1 $patch)
    if test ! -e $file ; then
	file=${file#*/}
	let level++ || true
    fi
    test -e $file || exit 1
    sed -ri '/^\*\*\* \.\./{ s@\.\./bash-%{bversion}[^/]*/@@ }' $patch
    echo Patch $patch
    patch -s -p$level < $patch
done
%patch1  -p0 -b .manual
%patch2  -p0 -b .security
%patch3  -p0 -b .2.4.4
%patch4  -p0 -b .evalexp
%patch5  -p0 -b .warnlc
%patch7  -p0 -b .decl
%patch9  -p0 -b .unistd
%patch10 -p0 -b .printf
%patch11 -p0 -b .plugins
%patch12 -p0 -b .completion
%patch13 -p0 -b .nscdunmap
%patch14 -p0 -b .sigrestart
%patch16 -p0 -b .setlocale
%patch17 -p0 -b .fix016
#%patch18 -p0 -b .winch
%patch40 -p0 -b .bashrc
%if %{with sjis}
%patch42 -p0 -b .sjis
%endif
%patch46 -p0 -b .notimestamp
%patch47 -p0 -b .perl522
%if %{with import_function}
%patch48 -b .eif
%endif
%patch49 -p0 -b .pthtmp
%patch0  -p0 -b .0

# This has to be always the same version as included in the bash its self
rl1=($(sed -rn '/RL_READLINE_VERSION/p' lib/readline/readline.h))
rl2=($(sed -rn '/RL_READLINE_VERSION/p' /usr/include/readline/readline.h))
test ${rl1[2]} = ${rl2[2]} || exit 1

%build
  LANG=POSIX
  LC_ALL=$LANG
  unset LC_CTYPE
  SCREENDIR=$(mktemp -d ${PWD}/screen.XXXXXX) || exit 1
  SCREENRC=${SCREENDIR}/bash
  export SCREENRC SCREENDIR
  exec 0< /dev/null
  SCREENLOG=${SCREENDIR}/log
  cat > $SCREENRC<<-EOF
	deflogin off
	deflog on
	logfile $SCREENLOG
	logfile flush 1
	logtstamp off
	log on
	setsid on
	scrollback 0
	silence on
	utf8 on
	EOF
  CPU=$(uname -m 2> /dev/null)
  HOSTTYPE=${CPU}
  MACHTYPE=${CPU}-suse-linux
  export LANG LC_ALL HOSTTYPE MACHTYPE
  cflags ()
  {
      local flag=$1; shift
      local var=$1; shift
      test -n "${flag}" -a -n "${var}" || return
      case "${!var}" in
      *${flag}*) return
      esac
      set -o noclobber
      case "$flag" in
      -Wl,*)
	  if echo 'int main () { return 0; }' | \
	     ${CC:-gcc} -Werror $flag -o /dev/null -xc - > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
	  ;;
      *)
	  if ${CC:-gcc} -Werror ${flag/#-Wno-/-W} -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
	  if ${CXX:-g++} -Werror ${flag/#-Wno-/-W} -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
      esac
      set +o noclobber
  }
  LARGEFILE="$(getconf LFS_CFLAGS)"
  CFLAGS="$RPM_OPT_FLAGS $LARGEFILE -D_GNU_SOURCE -DRECYCLES_PIDS -Wall -g"
  LDFLAGS=""
  #
  # Never ever put -DMUST_UNBLOCK_CHLD herein as this breaks bash
  #
  cflags -Wuninitialized         CFLAGS
  cflags -Wextra                 CFLAGS
  cflags -Wno-unprototyped-calls CFLAGS
  cflags -Wno-switch-enum        CFLAGS
  cflags -Wno-unused-variable    CFLAGS
  cflags -Wno-unused-parameter   CFLAGS
  cflags -Wno-parentheses        CFLAGS
  cflags -ftree-loop-linear      CFLAGS
  cflags -pipe                   CFLAGS
  cflags -DBNC382214=0           CFLAGS
  cflags -DIMPORT_FUNCTIONS_DEF=0 CFLAGS
  cflags -Wl,--as-needed         LDFLAGS
  cflags -Wl,-O2                 LDFLAGS
  cflags -Wl,-rpath,%{_ldldir}		      LDFLAGS
  # /proc is required for correct configuration
  test -d /dev/fd || { echo "/proc is not mounted!" >&2; exit 1; }
  CC=gcc
%if %_minsh
  cflags -Os CFLAGS
# cflags -U_FORTIFY_SOURCE CFLAGS
# cflags -funswitch-loops CFLAGS
# cflags -ftree-loop-im CFLAGS
# cflags -ftree-loop-ivcanon CFLAGS
# cflags -fprefetch-loop-arrays CFLAGS
# cflags -fno-stack-protector CFLAGS
# cflags -fno-unwind-tables CFLAGS
# cflags -fno-asynchronous-unwind-tables CFLAGS
%endif
  CC_FOR_BUILD="$CC"
  CFLAGS_FOR_BUILD="$CFLAGS"
  export CC_FOR_BUILD CFLAGS_FOR_BUILD CFLAGS LDFLAGS CC
  autoconf
  #
  # We have a malloc with our glibc
  #
  SYSMALLOC="
	--without-gnu-malloc
	--without-bash-malloc
	--enable-mem-scramble
  "
  #
  # System readline library (comment out it not to be used)
  #
  READLINE="
	--with-installed-readline
  "
  bash support/mkconffiles -v
%if %_minsh
  ./configure --build=%{_target_cpu}-suse-linux	\
	--prefix=%{_prefix}		\
	--mandir=%{_mandir}		\
	--infodir=%{_infodir}		\
	--libdir=%{_libdir}		\
	--with-curses			\
	--with-afs			\
	--with-gnu-ld			\
	$SYSMALLOC			\
	--enable-minimal-config		\
	--enable-arith-for-command	\
	--enable-array-variables	\
	--enable-brace-expansion	\
	--enable-casemod-attributes	\
	--enable-casemod-expansion	\
	--enable-command-timing		\
	--enable-cond-command		\
	--enable-cond-regexp		\
	--enable-coprocesses		\
	--enable-directory-stack	\
	--enable-dparen-arithmetic	\
	--enable-extended-glob		\
	--enable-job-control		\
	--enable-net-redirections	\
	--enable-process-substitution	\
	--enable-glob-asciiranges-default \
	--disable-strict-posix-default	\
	--enable-separate-helpfiles=%{_datadir}/bash/helpfiles \
	$READLINE
  make Program=sh sh
  make distclean
%endif
  ./configure --build=%{_target_cpu}-suse-linux	\
	--prefix=%{_prefix}		\
	--mandir=%{_mandir}		\
	--infodir=%{_infodir}		\
	--libdir=%{_libdir}		\
	--docdir=%{_docdir}/%{name}	\
	--with-curses			\
	--with-afs			\
	--with-gnu-ld			\
	$SYSMALLOC			\
	--enable-job-control		\
	--enable-net-redirections	\
	--enable-alias			\
	--enable-readline		\
	--enable-history		\
	--enable-bang-history		\
	--enable-directory-stack	\
	--enable-process-substitution	\
	--enable-prompt-string-decoding	\
	--enable-select			\
	--enable-help-builtin		\
	--enable-separate-helpfiles	\
	--enable-array-variables	\
	--enable-brace-expansion	\
	--enable-command-timing		\
	--enable-disabled-builtins	\
	--enable-glob-asciiranges-default \
	--disable-strict-posix-default	\
	--enable-multibyte		\
	--enable-separate-helpfiles=%{_datadir}/bash/helpfiles \
	$READLINE
  sed -rn '/Configuration feature settings controllable by autoconf/,/End of configuration settings controllable by autoconf/p' <  config.h
  profilecflags=CFLAGS="$CFLAGS"
%if 0%{?do_profiling}
  profilecflags=CFLAGS="$CFLAGS %cflags_profile_generate"
%endif
  make "$profilecflags" \
	all printenv recho zecho xcase
  TMPDIR=$(mktemp -d /tmp/bash.XXXXXXXXXX) || exit 1
  > $SCREENLOG
  tail -q -s 0.5 -f $SCREENLOG & pid=$!
  env -i HOME=$PWD TERM=$TERM LD_LIBRARY_PATH=$LD_RUN_PATH TMPDIR=$TMPDIR \
	SCREENRC=$SCREENRC SCREENDIR=$SCREENDIR \
	screen -D -m make TESTSCRIPT=%{SOURCE4} check
  kill -TERM $pid
%if 0%{?do_profiling}
  rm -f jobs.gcda
  profilecflags=CFLAGS="$CFLAGS %cflags_profile_feedback -fprofile-correction"
  clean=clean
%endif
  make "$profilecflags" $clean all
  make -C examples/loadables/
  make documentation

%install
  %make_install
  make -C examples/loadables/ install-supported DESTDIR=%{buildroot} libdir=/%{_lib}
  mv -vf %{buildroot}%{_ldldir}/*.h   %{buildroot}%{_includedir}/bash/
  mv -vf %{buildroot}%{_ldldir}/*.inc %{buildroot}%{_datadir}/bash
  rm -rf %{buildroot}%{_libdir}/bash
  rm -rf %{buildroot}/%{_lib}/pkgconfig
  sed -ri '/CC = gcc/s@(CC = gcc).*@\1@' %{buildroot}%{_libdir}/pkgconfig/bash.pc
  mkdir -p %{buildroot}/bin
  mkdir -p %{buildroot}%{_sysconfdir}/alternatives
#
# It should be noted that the move of /bin/bash to /usr/bin/bash
# had NOT done by me at 2019/02/08. Now only a symbolic link
# remains here :(
# The same had happen for the system POSIX shell /bin/sh
#
  ln -sf %{_bindir}/bash %{buildroot}/bin/bash
  ln -sf %{_bindir}/sh   %{buildroot}/bin/sh
  ln -sf bash            %{buildroot}%{_bindir}/rbash
  ln -sf %{_sysconfdir}/alternatives/sh %{buildroot}%{_bindir}/sh
  install -m 644 COMPAT NEWS    %{buildroot}%{_docdir}/%{name}
  install -m 644 COPYING        %{buildroot}%{_docdir}/%{name}
  install -m 644 doc/FAQ        %{buildroot}%{_docdir}/%{name}
  install -m 644 doc/INTRO      %{buildroot}%{_docdir}/%{name}
  install -m 644 doc/*.html     %{buildroot}%{_docdir}/%{name}
  install -m 644 doc/builtins.1 %{buildroot}%{_mandir}/man1/bashbuiltins.1
  install -m 644 doc/rbash.1    %{buildroot}%{_mandir}/man1/rbash.1
  gzip -9f %{buildroot}%{_infodir}/*.inf*[^z] || true
  mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
  sed 's/^|//' > %{buildroot}%{_docdir}/%{name}/BUGS <<\EOF
Known problems
--------------
|
This version of bash/readline supports multi byte handling
that is e.g. wide character support for UTF-8.  This causes
problems in geting the current cursor position within the
readline runtime library:
|
bash-%{bversion}> LANG=ja_JP
bash-%{bversion}> echo -n "Hello"
bash-%{bversion}>
|
In other words the prompt overwrites the output of the
echo comand.  The boolean variable byte-oriented
set in %{_sysconfdir}/inputrc or $HOME/.inputrc avoids this
but disables multi byte handling.
EOF
  # remove unpackaged files
  mkdir -p %{buildroot}%{_sysconfdir}/skel
  install -m 644 %{S:5}    %{buildroot}%{_sysconfdir}/skel/.bashrc
  install -m 644 %{S:6}    %{buildroot}%{_sysconfdir}/skel/.profile
  touch -t 199605181720.50 %{buildroot}%{_sysconfdir}/skel/.bash_history
  chmod 600                %{buildroot}%{_sysconfdir}/skel/.bash_history
  %find_lang bash
  %fdupes -s %{buildroot}%{_datadir}/bash/helpfiles
  sed -ri '1{ s@/bin/sh@/bin/bash@ }' %{buildroot}%{_bindir}/bashbug

%post -p /bin/bash
%{_sbindir}/update-alternatives --quiet --force \
	--install %{_bindir}/sh sh %{_bindir}/bash 10100

%preun -p /bin/bash
if test "$1" = 0; then
        %{_sbindir}/update-alternatives --quiet --remove sh %{_bindir}/bash
fi

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/bash.info.gz

%preun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/bash.info.gz

%clean
LD_LIBRARY_PATH=%{buildroot}/%{_lib} \
ldd -u -r %{buildroot}/bin/bash || true
%{?buildroot: %__rm -rf %{buildroot}}

%files
%defattr(-,root,root)
%license COPYING
%config %attr(600,root,root) %{_sysconfdir}/skel/.bash_history
%config %attr(644,root,root) %{_sysconfdir}/skel/.bashrc
%config %attr(644,root,root) %{_sysconfdir}/skel/.profile
%ghost %config %{_sysconfdir}/alternatives/sh
%dir %{_sysconfdir}/bash_completion.d
/bin/bash
/bin/sh
%{_bindir}/bash
%{_bindir}/bashbug
%{_bindir}/rbash
%{_bindir}/sh
%dir %{_datadir}/bash
%dir %{_datadir}/bash/helpfiles
%{_datadir}/bash/helpfiles/*
%{_mandir}/man1/bash.1*
%{_mandir}/man1/bashbuiltins.1*
%{_mandir}/man1/bashbug.1*
%{_mandir}/man1/rbash.1*

%files lang -f bash.lang
%defattr(-,root,root)

%files doc
%defattr(-,root,root)
%doc %{_infodir}/bash.info*
%doc %{_docdir}/%{name}

%files devel
%defattr(-,root,root)
%dir %{_includedir}/bash/
%dir %{_includedir}/bash/builtins/
%dir %{_includedir}/bash/include/
%{_incdir}/bash/*.h
%{_incdir}/bash/builtins/*.h
%{_incdir}/bash/include/*.h
%{_libdir}/pkgconfig/bash.pc
%{_datadir}/bash/*.inc

%files loadables
%defattr(-,root,root)
%{_ldldir}

%changelog
