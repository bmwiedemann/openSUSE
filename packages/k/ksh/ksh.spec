#
# spec file for package ksh
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ksh
%global		date		2012-08-01
%global         use_suid_exe	0
%global         use_opt_bins	1
%if !0%{?qemu_user_space_build:1}
%global         do_tests	1
%else
%global         do_tests	0
%endif
%global         use_locale	0
%if 0%{?suse_version} >= 1550
%define libdir %{_libdir}
%define bindir %{_bindir}
%else
%define libdir /%{_lib}
%define bindir /bin
%endif
BuildRequires:  bind-utils
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gdbm-devel
BuildRequires:  glibc-devel
BuildRequires:  groff
BuildRequires:  libbz2-devel
BuildRequires:  ncurses-devel
BuildRequires:  procps
BuildRequires:  psmisc
BuildRequires:  update-alternatives
BuildRequires:  zlib-devel
# /bin/ex and /bin/ed required for build
BuildRequires:  awk
BuildRequires:  ed
BuildRequires:  strace
BuildRequires:  vim
URL:            http://www.research.att.com/~gsf/download/
Requires(post): /bin/ln /bin/rm /etc/bash.bashrc /bin/true
Requires(postun):/bin/ln /bin/rm /etc/bash.bashrc /bin/true
Requires(post): update-alternatives
Requires(preun):update-alternatives
%if %use_suid_exe
PreReq:         permissions
%endif
Version:        93vu
Release:        0
Summary:        Korn Shell
License:        CPL-1.0 AND EPL-1.0
Group:          System/Shells
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         INIT.%{date}.tar.bz2
Source1:        ast-base.%{date}.tar.bz2
Source3:        EPL
Source4:        CPL
Source10:       leak1.sh
Source11:       leak2.sh
Source12:       ifs-crash.sh
Source13:       ulimit.sh
Source14:       leak3.sh
Source20:       Agreement
Source21:       Warning
Source30:       ksh-rpmlintrc
Source31:       vmbalance
Source42:       sigexec.c
Patch:          ksh93.dif
Patch1:         workaround-stupid-build-system.diff
Patch2:         ksh-qemu.patch
Patch3:         ksh93-shift_ijs.dif
Patch4:         ksh93-gmt2utc.dif
Patch5:         ksh93-uname.dif
Patch6:         ksh93-vi.dif
Patch7:         ksh93-profile.dif
Patch8:         ksh93-test.dif
Patch9:         ksh93-compat.dif
Patch10:        ksh93-suid_exec.dif
Patch11:        ksh93-signals.dif
Patch12:        ksh93-limits.dif
Patch13:        ksh93-unset-f.dif
Patch14:        ksh93-ia64.dif
Patch15:        ksh93-s390.dif
Patch16:        ksh93-gcc.dif
Patch17:        ksh93-heredoc.dif
Patch18:        ksh93-jobs.dif
Patch19:        ksh93-reg.dif
Patch20:        ksh93-aso.dif
Patch21:        ksh93-vm.dif
Patch22:        ksh93-limit-name-len.dif
Patch23:        ksh93-foreground-prgrp.dif
Patch24:        ksh93-builtin.dif
# PATCH-FIX-UPSTREAM ksh93-read-dont-ignore-esc.dif [bnc#765171]
# is part of ksh93u+ 2012-06-28
# PATCH-EXTEND-UPSTREAM astksh_builtin_poll20120806_001.diff [bnc#779888]
Patch27:        astksh_builtin_poll20120806_001.diff
# PATCH-FIX-UPSTREAM ksh93-env.dif [bnc#785266, bnc#803613]
Patch28:        ksh93-env.dif
# PATCH-FIX-UPSTREAM ksh93-typedef.dif
Patch29:        ksh93-typedef.dif
# PATCH-EXTEND-UPSTREAM ksh93-pathtemp.dif [bnc#786134]
# the fix is part of ksh93u+ 2012-06-28
# nevertheless the /dev/shm extension is useful
Patch30:        ksh93-pathtemp.dif
# PATCH-FIX-UPSTREAM ksh93-dttree-crash.dif [bnc#795324]
Patch31:        ksh93-dttree-crash.dif
# PATCH-FIX-UPSTREAM ksh93-heredoclex.dif [bnc#804998]
Patch32:        ksh93-heredoclex.dif
# PATCH-FIX-UPSTREAM ksh93-fdstatus.dif [bnc#808449, bnc#814135]
# this is a backport from the alpha version ksh93v-2013-04-22
Patch33:        ksh93-fdstatus.dif
# PATCH-FIX-UPSTREAM ksh93-alias-k.dif [bnc#824187]
Patch34:        ksh93-alias-k.dif
# PATCH-FIX-SUSE Reduce warnings about uninitialized varaibles (most of them are handled correct)
Patch35:        ksh93-uninitialized.dif
# PATCH-FIX-UPSTREAM Ouch ... use memmove instead of memcopy on overlapping areas
Patch36:        ksh93-sfio.dif
# [bnc#899014]
Patch37:        ksh93-path-skip.dif
Patch38:        ksh93-fs3d.dif
# [bnc#852160]
Patch39:        ksh93-subshellpwd.dif
# [bnc#867401]
Patch40:        ksh93-cdpwd.dif
# [bnc#893031]
Patch41:        ksh93-longenv.dif
Patch42:        ksh93-malloc-hook.dif
Patch43:        ksh93-disable-vfork.dif
Patch44:        ksh93-joblock.dif
Patch45:        ksh93-stkfreeze.dif
Patch46:        ksh93-stkset-abort.dif
Patch47:        ksh93-stkalias.dif
Patch48:        ksh93-backtick.dif
Patch49:        ksh93-nvtree-free.dif
Patch50:        ksh93-int16double.dif
Patch51:        ksh93-jpold.dif
Patch52:        ksh93-redirectleak.dif
Patch53:        ksh93-optimizeleak.dif
Patch54:        ksh93-edpredict.dif
Patch55:        ksh93-spawnlock.dif
Patch56:        ksh93-filedefined.dif
Patch57:        ksh93-no-sysctl.dif
Patch62:        ksh-locale.patch
Patch63:        cpp.patch

%description
The original Korn Shell.  The ksh is an sh-compatible command
interpreter that executes commands read from standard input or from a
file.



Authors:
--------
    David Korn <dgk@research.att.com>
    Glenn Fowler <gsf@research.att.com>
    Phong Vo <kpv@research.att.com>

%package -n ksh-devel
Summary:        Korn Shell development environment
License:        CPL-1.0
Group:          Development/Libraries/C and C++
Requires:       ksh = %{version}-%{release}

%description -n ksh-devel
The package includes C header files and the static libraries together
with the shared libraries for linking with other projects.  Please be
aware that the CPL licensed code can not be used within GPL licensed
project.



Authors:
--------
    David Korn <dgk@research.att.com>
    Glenn Fowler <gsf@research.att.com>
    Phong Vo <kpv@research.att.com>

%prep
chmod +x %{S:31}
%setup -q -n ksh93 -T -c -a 0
tar --use-compress-program=bzcat -xf %{S:1} \
    lib/package/ \
    src/cmd/ksh93/ src/lib/libast/ src/lib/libcmd/ src/lib/libcoshell/ src/lib/libdll/ src/lib/libsum/ \
    src/cmd/builtin/ src/cmd/msgcc/ src/lib/libpp/ src/lib/libuu/
if test -d share ; then
    find share/ \( -name chef -o -name fudd -o -name piglatin -o -name valley \) -a -type d |\
      xargs -r rm -vrf
    find share/ ! \( -name libast -o -name libcmd -o -name libdll -o -name libshell \) -a -type f |\
      xargs -r rm -vf
    find share/ -type d -a -empty | xargs -r rm -vrf
    find share/ -type d -a -empty | xargs -r rm -vrf
fi
%patch
%patch62
%patch1
%ifarch %arm
%patch2
%endif
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11
%patch12
%patch13
%ifarch ia64
%patch14
%endif
%patch15
%patch16
%patch17
%patch18
%patch19
%patch20
%patch21
%patch22
%patch23
%patch24
%patch27
%patch28
%patch29
%patch30
%patch31
%patch32
%patch33
%patch34
%patch35
%patch36
%patch37
%patch38
%patch39
%patch40
%patch41
%patch42
%if 0%{?ksh_no_vfork}
%patch43
%endif
%patch44
%patch45
%patch46
%patch47
%patch48
%patch49
%patch50
%patch51
%patch52
%patch53
%patch54
%patch55
%patch56
%patch57

%patch63 -p 1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

  #
  # Check for a clean signal environment for runtime tests
  #
  typeset -i IGNORED=0x$(ps --no-headers -o ignored $$)
  typeset -i SIGMASK=0x0
  typeset -i usesigexec=0

  let "SIGMASK|=(1<<($(kill -l PIPE)-1))"
  let "SIGMASK|=(1<<($(kill -l URG) -1))"
  let "SIGMASK|=(1<<($(kill -l XFSZ)-1))"

  ((IGNORED & SIGMASK)) && let ++usesigexec || true
  test -t 0 || let ++usesigexec

%if 0%{?qemu_user_space_build:1}
  # agraf: In a qemu user space build, ps can not find the actual sigmask
  #        of processes, so we run into an endless loop. Disable sigexec.
  usesigexec=0
%endif

  if ((usesigexec > 0)) ; then
      ${CC:-gcc} ${RPM_OPT_FLAGS} -o sigexec %{S:42} -lutil
      for fd in /proc/$$/fd/*; do
 	  test -s $fd -a ! -c $fd && break || true
      done
      set -- $(readlink $fd)
      exec ./sigexec $SHELL ${1+"$@"}
  fi
  IGNORED=0x$(ps --no-headers -o ignored $$)

  AR="ar"
  CC=gcc
  PATH=${PWD}:$PATH
  LANG=POSIX
  TMPDIR=$(mktemp -d /tmp/ksh-build.XXXXXX) || exit 1
  SUSE_ASNEEDED=0
  export AR CC PATH LANG TMPDIR SUSE_ASNEEDED
  #
  # Remove optimizer which cause runtime leaks in ksh
  #
  RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-funwind-tables/}"
  RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-fasynchronous-unwind-tables/}"
  # This package failed when testing with -Wl,-as-needed being default.
  # So we disable it here, if you want to retest, just delete this
  # comment and the line below.
  RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-as-needed/-no-as-needed/}"
  # Use POSIX as environment
  test -n "${!LC_*}" && unset "${!LC_*}"
  # ksh currently does not build with -Werror=return-type
  RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-Werror=return-type/}"
  cflags ()
  {
      set +x
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
	  if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
	      eval $var=\${$var:+\$$var\ }$flag
	  fi
      esac
      set +o noclobber
      set -x
  }
  relink ()
  {
      set +x
      local search=$1; shift
      local target=$1; shift
      test -n "${search}" -a -n "${target}" || exit 1
      local object=$(find ${root:-/tmp}/src/cmd/ -name ${search}.o)
      local cmd=$(
	  grep -e "-o $search" ${log:-/dev/null} | tail -n 1 | \
	  sed -r -e "s@\+ g?cc@${CC:-gcc}@" \
		 -e "s@-o $search@-o ${root:-/tmp}$target@" \
		 -e "s@[[:blank:]]${search}.o[[:blank:]]@ $object @" \
		 -e "s@[[:blank:]](/[^[:blank:]]*)?lib([[:alnum:]]+)\.a@ -l\2@g" \
		 -e "s@'@@g")
      set -x
      $cmd ${1+"$@"}
  }
  #
  # If _you_ are knowing how to fix this in the autogenerated
  # sources of ksh/ast without breaking them, then let me know.
  #
  cflags -Wno-missing-braces		IGNORE
  cflags -Wno-unknown-pragmas		IGNORE
  cflags -Wno-parentheses		IGNORE
  cflags -Wno-char-subscripts		IGNORE
  cflags -Wno-uninitialized		IGNORE
  cflags -Wno-implicit			IGNORE
  cflags -Wno-unused-value		IGNORE
  cflags -Wno-type-limits		IGNORE
  cflags -Wclobbered			RPM_OPT_FLAGS
  #
  # Do not use -DSHOPT_SPAWN=1 and/or -DSHOPT_AMP=1 this would cause
  # errors due race conditions while executing the test suite.
  #
  feature=${PWD}/.feature.h
  set -C
  (cat > $feature)<<-'EOF'
	#define SHOPT_FS_3D	    0
	#define SHOPT_SYSRC	    1
	#define SHOPT_REMOTE	    1
	#define SHOPT_CMDLIB_BLTIN  1
	#define SHOPT_CMDLIB_HDR    <cmdlist.h>
	#define SHOPT_CMDLIB_DIR    "%{libdir}/ast/bin"
	#define SH_CMDLIB_DIR	    "%{libdir}/ast/bin"
	#define THISPROG	    "%{libdir}/ast/bin/suid_exec"
	#define _AST_std_malloc	    0
	#define _map_malloc	    1
	EOF
  set +C
  FEATURE="-include $feature"
  cat $feature
  #
  #
  LARGEFILE="$(getconf LFS_CFLAGS)"
  case "$RPM_ARCH" in
  i[3456]86)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O2}"
	 cflags -m32			RPM_OPT_FLAGS
	 HOSTTYPE=linux.i386
	 ;;
  x86_64)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O2}"
	 cflags -m64			RPM_OPT_FLAGS
	 HOSTTYPE=linux.i386-64
	 ;;
  ia64)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O}"
	 cflags -mlp64			RPM_OPT_FLAGS
 	 cflags -mno-volatile-asm-stop	RPM_OPT_FLAGS
	 HOSTTYPE=linux.ia64
	 ;;
  s390)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O}"
	 cflags -m31			RPM_OPT_FLAGS
	 HOSTTYPE=linux.s390
	 ;;
  s390*)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O}"
	 cflags -m64			RPM_OPT_FLAGS
	 HOSTTYPE=linux.s390-64
	 ;;
  ppc|powerpc)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O}"
	 cflags -mno-powerpc64		RPM_OPT_FLAGS
	 HOSTTYPE=linux.powerpc
	 _PACKAGE_HOSTTYPE_=linux.powerpc
	 export _PACKAGE_HOSTTYPE_
	 ;;
  ppc64le|powerpc64le)
	RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O}"
	# -mpowerpc64 is correct, the compiler defaults to
	# little endian anyway
	cflags -mpowerpc64             RPM_OPT_FLAGS
	HOSTTYPE=linux.powerpc64le
	;;
  ppc64|powerpc64)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O}"
	 cflags -mpowerpc64		RPM_OPT_FLAGS
	 HOSTTYPE=linux.powerpc64
	 ;;
  *)
	 RPM_OPT_FLAGS="${RPM_OPT_FLAGS//-O[s0-9]/-O}"
	 HOSTTYPE=linux.$RPM_ARCH
	 ;;
  esac
  MEMORY=execve
  for mm in mmap mmap2 mmap64 munmap munmap2 munmap64 ; do
      if strace -e $mm /bin/true > /dev/null 2>&1 ; then
	 MEMORY="${MEMORY:+${MEMORY},}$mm"
      fi
  done
  MEMORY="-s 128 ${MEMORY:+-e ${MEMORY}}"
  RPM_OPT_FLAGS=$(echo "${RPM_OPT_FLAGS}"|sed -r 's/([[:blank:]]+)-g[[:digit:]]+/\1-g2/g;s/([[:blank:]]+)-g([[:blank:]]+|$)/\1-g2\2/g')
  UNIVERSE=att
  LDFLAGS="-lm"
  LDSOFLG=""
  cflags -std=gnu99				RPM_OPT_FLAGS
  cflags -fPIC					RPM_OPT_FLAGS
  cflags -fno-strict-aliasing			RPM_OPT_FLAGS
  cflags -fno-zero-initialized-in-bss		RPM_OPT_FLAGS
  cflags -fno-delete-null-pointer-checks	RPM_OPT_FLAGS
  cflags -fno-unsafe-loop-optimizations		RPM_OPT_FLAGS
  cflags -fsigned-bitfields			RPM_OPT_FLAGS
  cflags -fsigned-chars				RPM_OPT_FLAGS
  cflags -fsigned-zeros				RPM_OPT_FLAGS
  case "$(gcc --version | head -n 1)" in
  *4.[012345].*)
     cflags -fno-tree-sink			RPM_OPT_FLAGS ;;
  *) cflags -ftree-loop-linear			RPM_OPT_FLAGS ;;
  esac
  cflags -g2					RPM_OPT_FLAGS
  cflags -pipe					RPM_OPT_FLAGS
  cflags -Wl,-O2				LDFLAGS
  cflags -Wl,--hash-size=16699			LDFLAGS
  cflags -Wl,-O2				LDSOFLG
  cflags -Wl,-warn-common			LDSOFLG
  cflags -Wl,--as-needed			LDSOFLG
  cflags -Wl,--hash-size=8599			LDSOFLG
  cflags -Wl,-Bsymbolic-functions		LDSOFLG
  cflags -Wl,-rpath,%{libdir}/ast		LDSOFLG
  RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE $LARGEFILE"
  RPM_OPT_FLAGS="$RPM_OPT_FLAGS $IGNORE $FEATURE"
  mam_cc_L=use
  mam_cc_OPTIMIZE=-pipe
  export mam_cc_L mam_cc_OPTIMIZE HOSTTYPE LDFLAGS RPM_OPT_FLAGS UNIVERSE
  printenv
  getconf PAGESIZE

  #
  # Build libast first and then determine the library functions used
  # by this library simply to avoid that gcc will overwrites those with
  # its own builtin functions.
  #
  bin/package view
  root=$(echo ${PWD}/arch/linux*)
  bin/package make ast-ast CCFLAGS="$RPM_OPT_FLAGS -fno-builtin -I${root}/include" HOSTTYPE="$HOSTTYPE" AR="$AR" CC="$CC"
  test -d $root || exit 1
  log=${root}/lib/package/gen/make.out
  test -s $log || exit 1
  for lib in libast ; do
      test -s ${root}/lib/${lib}.a || exit 1
      obj=$(ar t ${root}/lib/${lib}.a)
      test $? -eq 0 || exit 1
      case "$lib" in
      libast)
	  base=src/lib/$lib
	  vers=$(grep :LIBRARY: ${base}/Makefile | sed "s@.*\([0-9]\+\.[0-9]\+\).*@\1@")
	  link="-L${root}/lib/ -Wl,-rpath-link,${root}/lib -Wl,-rpath,%{libdir}/ast $LDSOFLG"
	  ;;
      esac
      soname="-Wl,-soname,${lib}.so.${vers%.*},-stats"
      pushd ${root}/${base}
      $CC -shared $soname -o ${root}/lib/${lib}.so.${vers} ${obj} $link
      ln -sf ${lib}.so.${vers} ${root}/lib/${lib}.so.${vers%.*}
      ln -sf ${lib}.so.${vers} ${root}/lib/${lib}.so
      popd
  done
  nobuiltin=${PWD}/.nobuiltin
  nm -D ${root}/lib/libast.so | \
      grep -E 'T[[:blank:]](_ast_)?(str|mem|(get|put|set)env|free|(c|m|re|v|vm)alloc)' | \
      sed -r 's/[[:xdigit:]]+[[:blank:]]+T[[:blank:]]+(_ast_)?([^[:blank:]]*)/-fno-builtin-\2/' | \
      sort -u > $nobuiltin
  rm -rf $root
  case "$(gcc --version | head -n 1)" in
  *4.[01].*)
     set +x
     for opt in $(cat $nobuiltin) ; do
	cflags $opt				RPM_OPT_FLAGS
     done
     set -x
     ;;
  *) cflags @$nobuiltin				RPM_OPT_FLAGS
  esac

  export | grep -vE 'PROFILEREAD|PWD|MAIL|HOME|HOST|HIST|LESS|TMP' > .env
  bin/package make CCFLAGS="$RPM_OPT_FLAGS -I${root}/include" HOSTTYPE="$HOSTTYPE" AR="$AR" CC="$CC"
  root=$(echo ${PWD}/arch/linux*)
  test -d $root || exit 1
  log=${root}/lib/package/gen/make.out
  test -s $log || exit 1
  for lib in libast libcmd libdll libshell ; do
      test -s ${root}/lib/${lib}.a || exit 1
      obj=$(ar t ${root}/lib/${lib}.a)
      test $? -eq 0 || exit 1
      case "$lib" in
      libshell)
	  base=src/cmd/ksh93
	  vers=$(grep ^VERSION  ${base}/Makefile | sed "s@.*\([0-9]\+\.[0-9]\+\).*@\1@")
	  link="-L${root}/lib/ -Wl,-rpath-link,${root}/lib -Wl,-rpath,%{libdir}/ast $LDSOFLG $LDFLAGS -ldll -lcmd -last -lm -ldl"
	  ;;
      libdll)
	  base=src/lib/$lib
	  vers=$(grep :LIBRARY: ${base}/Makefile | sed "s@.*\([0-9]\+\.[0-9]\+\).*@\1@")
	  link="-L${root}/lib/ -Wl,-rpath-link,${root}/lib -Wl,-rpath,%{libdir}/ast $LDSOFLG -ldl -last"
	  ;;
      libcmd)
	  base=src/lib/$lib
	  vers=$(grep :LIBRARY: ${base}/Makefile | sed "s@.*\([0-9]\+\.[0-9]\+\).*@\1@")
	  link="-L${root}/lib/ -Wl,-rpath-link,${root}/lib -Wl,-rpath,%{libdir}/ast $LDSOFLG -last"
	  ;;
      libast)
	  base=src/lib/$lib
	  vers=$(grep :LIBRARY: ${base}/Makefile | sed "s@.*\([0-9]\+\.[0-9]\+\).*@\1@")
	  link="-L${root}/lib/ -Wl,-rpath-link,${root}/lib -Wl,-rpath,%{libdir}/ast $LDSOFLG"
	  ;;
      esac
      soname="-Wl,-soname,${lib}.so.${vers%.*},-stats"
      pushd ${root}/${base}
      $CC -shared $soname -o ${root}/lib/${lib}.so.${vers} ${obj} $link
      ln -sf ${lib}.so.${vers} ${root}/lib/${lib}.so.${vers%.*}
      ln -sf ${lib}.so.${vers} ${root}/lib/${lib}.so
      popd
  done
  base=src/cmd/ksh93
  test=${PWD}/${base}/tests
  OPATH=$PATH
  OSHELL=$SHELL
  PATH=$PATH:${root}/bin
  SHELL=${root}/bin/ksh
  SHCOMP=${root}/bin/shcomp
  export PATH SHCOMP SHELL
%if %do_tests
  pushd ${test}
      typeset -i failed=0
      ln -sf ${root}/lib ${test}/../
      sed -ri '/^L[[:blank:]]/a \t 8000' pty.sh
      sed -ri 's/(SECONDS[[:blank:]]*>[[:blank:]]*)([[:digit:]]+)/\18/' signal.sh
      unset ${!LESS*}
      printf '\033[1m'
      grep -E '^(model name|flags)[[:blank:]]*:' /proc/cpuinfo | sort -ur | fold -s
      printf '\033(B\033[m'
      ${SHELL} shtests
      result=$(${SHELL} -k -c 'd=`/bin/echo x y=z`; echo $d x y=z')
      test "$result" = 'x x' || exit 1
      result=$(${SHELL} -c 'echo | echo "x`/bin/echo y`"')
      test "$result" = xy || exit 1
      result=$(${SHELL} -c 'echo | echo "x$(/bin/echo y)"')
      test "$result" = xy || exit 1
      exec 3> ${TMPDIR:-/tmp}/log
      LANG=POSIX
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:10} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:10} 4000
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:11} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:11} 4000
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:12} 4
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:12} 40
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:13} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:13} 4000
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:14} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:14} 4000
      if test $((IGNORED & SIGPIPE)) -eq 0 ; then
	  ${SHELL} -c 'g="false"; trap "print -u2 PIPED; \$g && exit 0 ; g=true" PIPE ; while true ; do echo hello ; done' | head -n 10
      fi
      LANG=en_US.UTF-8
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:10} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:10} 4000
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:11} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:11} 4000
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:12} 4
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:12} 40
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:13} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:13} 4000
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:14} 400
      strace $MEMORY -o '!%{S:31}' ${SHELL} %{S:14} 4000
      if test $((IGNORED & SIGPIPE)) -eq 0 ; then
	  ${SHELL} -c 'g="false"; trap "print -u2 PIPED; \$g && exit 0 ; g=true" PIPE ; while true ; do echo hello ; done' | head -n 10
      fi
      LANG=POSIX
      exec 3>&-
      printf '\033[1m'
      uniq  -c ${TMPDIR:-/tmp}/log
      printf '\033(B\033[m'
      killall -q -s 9 ${SHELL} || true
  popd
%endif
  pushd ${root}/${base}
      rm -f libshell.a
      rm -f ${root}/bin/ksh
      rm -f ${root}/bin/shcomp
      for bin in ksh shcomp pty what mime asa dlls suid_exec ; do
	  relink $bin /bin/$bin -Wl,-rpath-link,${root}/lib -Wl,-rpath,%{libdir}/ast
      done
  popd
  LD_LIBRARY_PATH=${root}/lib
  export LD_LIBRARY_PATH
  mkdir -p share/locale/C/LC_MESSAGES
  includes="-I$(cpp -print-search-dirs | sed -rn 's@^install:[[:blank:]]@@p')include"
  includes="$includes $(find $root -name FEATURE -printf ' -I%h')"
  includes="$includes -I/usr/include/linux"
  sed -rn "\@mamake -C cmd/ksh93@,\@mamake -C@ {
        s@^\+ g?cc@$SHELL msgcc -M-set=ast $includes@
	s@[[:blank:]]-c[[:blank:]]([^[:blank:]\.]+/([^[:blank:]\.\/]+))\.c@ -c \1\.c -o msgs/\2\.mso@p
  }" ${root}/lib/package/gen/make.out > src/cmd/ksh93/doit
  pushd src/cmd/ksh93
      mkdir msgs
      ${root}/lib/probe/C/pp/probe $(type -p gcc) > pp_default.h
      $SHELL ./doit
      $SHELL msgcc -o libshell.msg msgs/*.mso
      rm -rf msgs/
  popd
  msggen share/locale/C/LC_MESSAGES/libshell src/cmd/ksh93/libshell.msg
  pushd ${root}/bin
      PATH=$PATH:.
      set -- $(shcomp --version 2>&1)
      eval version=\${$#}
      for bin in shcomp pty what mime asa dlls ; do
	  $bin --nroff 2>&1 | sed 's/\(\.TH .*\)/\1 "%{date}" "" "Korn shell utilities"/' > ../man/man1/$bin.1ast
      done
  popd
  test -d /tmp -a /tmp -ef ${TMPDIR} || rm -rf ${TMPDIR}
  SHELL=$OSHELL
  PATH=$OPATH

%install
  root=$(echo ${PWD}/arch/linux*)
  test -d $root || exit 1
  pushd $root   || exit 1
  mkdir -p %{buildroot}%{bindir}
  mkdir -p %{buildroot}%{_bindir}
  mkdir -p %{buildroot}%{libdir}/ast/bin
  mkdir -p %{buildroot}%{_includedir}/ast
  mkdir -p %{buildroot}%{_libdir}/ast
  mkdir -p %{buildroot}%{_mandir}
  mkdir    %{buildroot}%{_mandir}/man1
  mkdir    %{buildroot}%{_mandir}/man3
%if %use_locale
  mkdir -p %{buildroot}%{_datadir}/locale
%endif
  mkdir -p %{buildroot}%{_datadir}/ksh/fun
  mkdir -p %{buildroot}%{_sysconfdir}/permissions.d
  install bin/ksh       %{buildroot}%{bindir}/ksh93
  install bin/shcomp    %{buildroot}%{_bindir}/shcomp
%if %use_opt_bins
  for bin in pty what mime asa dlls ; do
      install bin/$bin  %{buildroot}/%{_bindir}/$bin
  done
%endif
%if %use_suid_exe
  install bin/suid_exec %{buildroot}%{libdir}/ast/bin/
%endif
  # create update-alternatives symlinks
  mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
  touch %{buildroot}/%{_sysconfdir}/alternatives/ksh
%if 0%{?suse_version} < 1550
  touch %{buildroot}/%{_sysconfdir}/alternatives/usr-bin-ksh
  ln -sf %{_sysconfdir}/alternatives/usr-bin-ksh        %{buildroot}%{_bindir}/ksh
%endif
  touch %{buildroot}/%{_sysconfdir}/alternatives/ksh.1.gz
  touch %{buildroot}/%{_sysconfdir}/alternatives/rksh.1.gz
  ln -sf %{_sysconfdir}/alternatives/ksh                %{buildroot}%{bindir}/ksh
  ln -sf %{_sysconfdir}/alternatives/ksh.1.gz   %{buildroot}/%{_mandir}/man1/ksh.1.gz
  ln -sf %{_sysconfdir}/alternatives/rksh.1.gz  %{buildroot}/%{_mandir}/man1/rksh.1.gz
  ln -sf %{bindir}/ksh93	%{buildroot}%{_bindir}/rksh
  ln -sf ../../bin/ksh93	%{buildroot}%{libdir}/ast/ksh
  ln -sf ast			%{buildroot}%{libdir}/ksh
  cp -a lib/*.so*		%{buildroot}%{libdir}/ast/
  cp -a fun/*			%{buildroot}%{_datadir}/ksh/fun/
  if cmp -s %{buildroot}%{_datadir}/ksh/fun/pushd %{buildroot}%{_datadir}/ksh/fun/popd ; then
      ln -sf pushd %{buildroot}%{_datadir}/ksh/fun/popd
  fi
%if 0%{?suse_version} < 1550
  for so in %{buildroot}%{libdir}/ast/*.so.*.* ; do
      so=${so##*/}
      ln -sf %{libdir}/ast/$so %{buildroot}%{_libdir}/ast/${so%%%%.*}.so
  done
  rm -f %{buildroot}%{_libdir}/ast/*.so.*
%endif
  sed -rn '/^\.de Af/,/^\.\./p;/^\.de aF/,/^\.\./p' man/man3/int.3 > af.man
  for man in $(grep -l '\.}S' man/man[138]/*.[138]); do
      sed -ri '1r af.man' $man
  done
  for man in man/man[138]/*.[138] ; do
      sed -ri 's/\\f5/\\fB/g;s/^\.H/\.P\n\.H/g;s/\.}S/\.aF/;s/^\.LI/\.LR/;s/\\\(le/\\\(<=/' $man
  done
  install -m 0644 lib/*.a		%{buildroot}%{_libdir}/ast/
  install -m 0644 man/man1/sh.1		%{buildroot}%{_mandir}/man1/ksh93.1
  install -m 0644 man/man1/shcomp.1ast	%{buildroot}%{_mandir}/man1/shcomp.1ast
%if %use_opt_bins
  for bin in pty what mime asa dlls ; do
      install -m 0644 man/man1/$bin.1ast	%{buildroot}%{_mandir}/man1/$bin.1ast
  done
%endif
  for man in man/man3/*.3 ; do
      man=${man##*/}
      ast=${man}ast
      install -m 0644 man/man3/${man}	%{buildroot}%{_mandir}/man3/${ast}
  done
  install -m 0644 include/ast/*		%{buildroot}%{_includedir}/ast/
  if cmp -s %{buildroot}%{_includedir}/ast/namval.h %{buildroot}%{_includedir}/ast/ast_namval.h ; then
      ln -sf ast_namval.h %{buildroot}%{_includedir}/ast/namval.h
  fi
  popd
%if %use_locale
  for msg in share/locale/* ; do
      test -d $msg || continue
      mkdir -p %{buildroot}%{_datadir}/locale/${msg##*/}/LC_MESSAGES
      cp -vp ${msg}/LC_MESSAGES/*	%{buildroot}%{_datadir}/locale/${msg##*/}/LC_MESSAGES/
  done
  echo %%dir %{_datadir}/locale/C > ksh.lang
  echo %%dir %{_datadir}/locale/C/LC_MESSAGES >> ksh.lang
%endif
  find %{buildroot}/ -type f -o -type l | sed -r '
      s:%{buildroot}::
      s:(%{_datadir}/locale/)([^/_]+)(.*$):%%lang\(\2\) \1\2\3:
      s:^([^%%].*)::
      s:%%lang\(C\) ::
      /^ *$/d' >> ksh.lang
  if test -s lib/package/LICENSES/ast ; then
    cp lib/package/LICENSES/ast LICENSE
  else
    cp %{S:3} EPL-1.0
    cp %{S:4} CPL-1.0
    ln -sf EPL-1.0 LICENSE
  fi
  mv  src/cmd/ksh93/OBSOLETE src/cmd/ksh93/OBSOLETE.mm
  echo '.VERBON 22' > grep.mm
  sed -rn '/function grep/,/^}/p' src/cmd/ksh93/tests/grep.sh >> grep.mm
  echo '.VERBOFF' >> grep.mm
  tdevice=ascii8
  troff -Tascii8 < /dev/null > /dev/null 2>&1 || tdevice=utf8
  cat src/cmd/ksh93/builtins.mm | sed 's/\\f5/\\fB/g;s/^\.H/\.P\n\.H/g' | troff -T$tdevice -t -mm | grotty -bou > Builtins
  cat src/cmd/ksh93/PROMO.mm    | sed 's/\\f5/\\fB/g;s/^\.H/\.P\n\.H/g' | troff -T$tdevice -t -mm | grotty -bou > PROMO
  cat src/cmd/ksh93/OBSOLETE.mm | sed 's/\\f5/\\fB/g;s/^\.H/\.P\n\.H/g' | troff -T$tdevice -t -mm | grotty -bou > OBSOLETE
  cat src/cmd/ksh93/sh.memo     | sed 's/\\f5/\\fB/g;s/^\.H/\.P\n\.H/g' | troff -T$tdevice -t -mm | grotty -bou > MEMORANDUM
  cp %{S:21} .
%if %use_suid_exe
  set -C
  (cat > %{buildroot}%{_sysconfdir}/permissions.d/ksh) <<-EOF
	%{libdir}/ast/bin/suid_exec		root:root	4755
	EOF
  (cat > %{buildroot}%{_sysconfdir}/permissions.d/ksh.paranoid) <<-EOF
	%{libdir}/ast/bin/suid_exec		root:root	0755
	EOF
  set +C
%endif

%if %use_suid_exe
%if %{defined verify_permissions}
%verifyscript
%verify_permissions -e %{libdir}/ast/bin/suid_exec
%endif
%endif

%post
test -e etc/bash.bashrc && ln -sf bash.bashrc etc/ksh.kshrc || true
%if %use_suid_exe
%if %{defined set_permissions}
%set_permissions %{libdir}/ast/bin/suid_exec
%endif
%endif
if test -x %{libdir}/ast/bin/ksh ; then
    %{_sbindir}/update-alternatives \
	--quiet \
	--force \
	--remove ksh %{libdir}/ast/bin/ksh
    rm -f %{libdir}/ast/bin/ksh
    rm -f %{libdir}/ast/bin/shcomp
fi
%{_sbindir}/update-alternatives \
    --install %{bindir}/ksh ksh %{bindir}/ksh93 20 \
%if 0%{?suse_version} < 1550
    --slave %{_bindir}/ksh usr-bin-ksh /bin/ksh93 \
%endif
    --slave %{_mandir}/man1/ksh.1.gz ksh.1.gz %{_mandir}/man1/ksh93.1.gz \
    --slave %{_mandir}/man1/rksh.1.gz rksh.1.gz %{_mandir}/man1/ksh93.1.gz

%postun
if test $1 -eq 0 -a ! -x bin/ksh ; then
    if test ! -x bin/pdksh ; then
	rm -f etc/ksh.kshrc
    fi
fi
if [ ! -f %{bindir}/ksh93 ] ; then
    %{_sbindir}/update-alternatives --quiet --remove ksh %{bindir}/ksh93
fi

%posttrans
if test -x bin/ksh -o -x bin/pdksh ; then
    test -e etc/bash.bashrc && ln -sf bash.bashrc etc/ksh.kshrc || true
fi

%files -f ksh.lang
%defattr(-,root,root)
%if %use_suid_exe
%config %attr(0644,root,root) %{_sysconfdir}/permissions.d/ksh
%config %attr(0644,root,root) %{_sysconfdir}/permissions.d/ksh.paranoid
%endif
%doc LICENSE EPL-1.0 CPL-1.0 src/cmd/ksh93/COMPATIBILITY src/cmd/ksh93/RELEASE*
%doc Builtins PROMO OBSOLETE MEMORANDUM
%{_bindir}/ksh
%doc %{_mandir}/man1/ksh.1.gz
%doc %{_mandir}/man1/rksh.1.gz
%doc %{_mandir}/man1/ksh93.1.gz
%ghost %{_sysconfdir}/alternatives/ksh
%if 0%{?suse_version} < 1550
/bin/ksh93
/bin/ksh
%ghost %{_sysconfdir}/alternatives/usr-bin-ksh
%endif
%ghost %{_sysconfdir}/alternatives/ksh.1.gz
%ghost %{_sysconfdir}/alternatives/rksh.1.gz
%doc %{_mandir}/man1/shcomp.1ast.gz
%if %use_opt_bins
%doc %{_mandir}/man1/pty.1ast.gz
%doc %{_mandir}/man1/what.1ast.gz
%doc %{_mandir}/man1/mime.1ast.gz
%doc %{_mandir}/man1/asa.1ast.gz
%doc %{_mandir}/man1/dlls.1ast.gz
%endif
%{_bindir}/*
%dir %{libdir}/ast
%dir %{libdir}/ast/bin
%if %use_suid_exe
%attr(4755,root,root) %{libdir}/ast/bin/suid_exec
%endif
%{libdir}/ast/*.so*
%{libdir}/ast/ksh
%{libdir}/ksh
%dir %{_datadir}/ksh
%dir %{_datadir}/ksh/fun
%{_datadir}/ksh/fun/*

%files -n ksh-devel
%defattr(-,root,root)
%doc LICENSE Warning
%dir %{_libdir}/ast/
%{_libdir}/ast/*.so
%{_libdir}/ast/*.a
%doc %{_mandir}/man3/*
%{_includedir}/ast/

%changelog
