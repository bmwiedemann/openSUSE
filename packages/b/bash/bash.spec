#
# spec file for package bash
#
# Copyright (c) 2021 SUSE LLC
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


%define         bextend %{nil}
%define         bversion 5.1
%define         bpatchlvl %(bash %{_sourcedir}/get_version_number.sh %{_sourcedir})
%global         _incdir     %{_includedir}
%global         _ldldir     %{_libdir}/bash
%global         _minsh      0
%bcond_with     import_function
%bcond_with     sjis
Name:           bash
Version:        %{bversion}.%{bpatchlvl}
Release:        0
Summary:        The GNU Bourne-Again Shell
# The package bash-completion is a source of
# bugs which will hit at most this package
#Recommends:	bash-completion
License:        GPL-3.0-or-later
Group:          System/Shells
URL:            https://www.gnu.org/software/bash/bash.html
# Git:          http://git.savannah.gnu.org/cgit/bash.git
Source0:        ftp://ftp.gnu.org/gnu/bash/bash-%{bversion}%{bextend}.tar.gz
Source1:        bash-%{bversion}-patches.tar.bz2
Source2:        get_version_number.sh
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
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  makeinfo
BuildRequires:  patchutils
BuildRequires:  pkgconfig
BuildRequires:  screen
BuildRequires:  sed
BuildRequires:  update-alternatives
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(ncurses)
# This has to be always the same version as included in the bash its self
BuildRequires:  pkgconfig(readline) = 8.1
Requires(post): update-alternatives
Requires(preun):update-alternatives
Suggests:       bash-doc = %{version}
Suggests:       command-not-found
Provides:       /bin/bash
Provides:       /bin/sh

%description
Bash is an sh-compatible command interpreter that executes commands
read from standard input or from a file.  Bash incorporates useful
features from the Korn and C shells (ksh and csh).  Bash is intended to
be a conformant implementation of the IEEE Posix Shell and Tools
specification (IEEE Working Group 1003.2).

%package doc
Summary:        Documentation how to Use the GNU Bourne-Again Shell
Group:          Documentation/HTML
Supplements:    (bash and patterns-base-documentation)
Provides:       bash:%{_infodir}/bash.info.gz
BuildArch:      noarch

%description doc
This package contains the documentation for using the bourne shell
interpreter Bash.

%lang_package

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

%if 0%{?usrmerged}
%package legacybin
Summary:        Legacy usrmove helper files
Group:          System/Shells
Requires:       bash = %{version}-%{release}
Requires:       this-is-only-for-build-envs
Conflicts:      rpmlib(X-CheckUnifiedSystemdir)

%description legacybin
Legacy usrmove helper files for the build system. Do not install.
%endif

%prep
%if %{with sjis}
echo -e '\033[1m\033[31mWarning: Shift JIS support is enabled\033[m'
%else
echo -e '\033[1m\032[31mShift JIS support disabled\033[m'
%endif
%setup -q -n bash-%{bversion}%{bextend} -b1
typeset -i level
set +x
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
set -x
%patch1   -b .manual
%patch3   -b .2.4.4
%patch4   -b .evalexp
%patch5   -b .warnlc
%patch7   -b .decl
%patch9   -b .unistd
%patch10  -b .printf
%patch11  -b .plugins
%patch12  -b .completion
%patch13  -b .nscdunmap
%patch14  -b .sigrestart
%patch16  -b .setlocale
#%patch18 -p0 -b .winch
%patch40  -b .bashrc
%if %{with sjis}
%patch42  -b .sjis
%endif
%patch46  -b .notimestamp
%patch47  -b .perl522
%if %{with import_function}
%patch48 -b .eif
%endif
%patch49  -b .pthtmp
%patch0   -b .0

# This has to be always the same version as included in the bash its self
rl1=($(sed -rn '/RL_READLINE_VERSION/p' lib/readline/readline.h))
rl2=($(sed -rn '/RL_READLINE_VERSION/p' %{_includedir}/readline/readline.h))
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
  HOSTTYPE=%{_target_cpu}
  VENDOR=%{_target_vendor}
  OSTYPE=%{_target_os}
  MACHTYPE=${HOSTTYPE}-${VENDOR}-${OSTYPE}
  export LANG LC_ALL HOSTTYPE VENDOR OSTYPE MACHTYPE
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
  CFLAGS="%{optflags} $LARGEFILE -D_GNU_SOURCE -DRECYCLES_PIDS -Wall -g"
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
%if %{_minsh}
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
%if %{_minsh}
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
  profilecflags=CFLAGS="$CFLAGS %{cflags_profile_generate}"
%endif
  makeopts="Machine=${HOSTTYPE} OS=${OSTYPE} VENDOR=${VENDOR} MACHTYPE=${MACHTYPE}"
  make $makeopts "$profilecflags" \
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
  profilecflags=CFLAGS="$CFLAGS %{cflags_profile_feedback} -fprofile-correction"
  clean=clean
%endif
  make $makeopts "$profilecflags" $clean all
  make $makeopts -C examples/loadables/
  make $makeopts documentation

%install
  %make_install
  make -C examples/loadables/ install-supported DESTDIR=%{buildroot} libdir=%{_libdir}
  mv -vf %{buildroot}%{_ldldir}/*.h   %{buildroot}%{_includedir}/bash/
  mv -vf %{buildroot}%{_ldldir}/*.inc %{buildroot}%{_datadir}/bash
  rm -rf %{buildroot}/%{_lib}/pkgconfig
  sed -ri '/CC = gcc/s@(CC = gcc).*@\1@' %{buildroot}%{_libdir}/pkgconfig/bash.pc
  mkdir -p %{buildroot}%{_sysconfdir}/alternatives
#
# It should be noted that the move of /bin/bash to /usr/bin/bash
# had NOT done by me at 2019/02/08. Now only a symbolic link
# remains here :(
# The same had happen for the system POSIX shell /bin/sh
#
  mkdir -p %{buildroot}/bin
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
  install -m 644 %{SOURCE5}    %{buildroot}%{_sysconfdir}/skel/.bashrc
  install -m 644 %{SOURCE6}    %{buildroot}%{_sysconfdir}/skel/.profile
  touch -t 199605181720.50 %{buildroot}%{_sysconfdir}/skel/.bash_history
  chmod 600                %{buildroot}%{_sysconfdir}/skel/.bash_history
  %find_lang bash
  %fdupes -s %{buildroot}%{_datadir}/bash/helpfiles
  sed -ri '1{ s@/bin/sh@/bin/bash@ }' %{buildroot}%{_bindir}/bashbug

%post -p %{_bindir}/bash
%{_sbindir}/update-alternatives --quiet --force \
	--install %{_bindir}/sh sh %{_bindir}/bash 10100

%preun -p %{_bindir}/bash
if test "$1" = 0; then
        %{_sbindir}/update-alternatives --quiet --remove sh %{_bindir}/bash
fi

%files
%license COPYING
%config %attr(600,root,root) %{_sysconfdir}/skel/.bash_history
%config %attr(644,root,root) %{_sysconfdir}/skel/.bashrc
%config %attr(644,root,root) %{_sysconfdir}/skel/.profile
%ghost %config %{_sysconfdir}/alternatives/sh
%dir %{_sysconfdir}/bash_completion.d
%if !0%{?usrmerged}
/bin/bash
/bin/sh
%endif
%{_bindir}/bash
%{_bindir}/bashbug
%{_bindir}/rbash
%{_bindir}/sh
%dir %{_datadir}/bash
%dir %{_datadir}/bash/helpfiles
%{_datadir}/bash/helpfiles/*
%{_mandir}/man1/bash.1%{?ext_man}
%{_mandir}/man1/bashbuiltins.1%{?ext_man}
%{_mandir}/man1/bashbug.1%{?ext_man}
%{_mandir}/man1/rbash.1%{?ext_man}

%files lang -f bash.lang

%files doc
%{_infodir}/bash.info%{?ext_info}
%doc %{_docdir}/%{name}

%files devel
%dir %{_includedir}/bash/
%dir %{_includedir}/bash/builtins/
%dir %{_includedir}/bash/include/
%{_incdir}/bash/*.h
%{_incdir}/bash/builtins/*.h
%{_incdir}/bash/include/*.h
%{_libdir}/pkgconfig/bash.pc
%{_datadir}/bash/*.inc

%files loadables
%{_ldldir}

%if 0%{?usrmerged}
%files legacybin
/bin/bash
/bin/sh
%endif

%changelog
