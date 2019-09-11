#
# spec file for package clisp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           clisp
Version:        2.49.92
Release:        0
Summary:        A Common Lisp Interpreter
# Included gllib is GPL-3.0-or-later
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Development/Languages/Other
Url:            https://gitlab.com/gnu-clisp/clisp
Source:         %name-%version.tar.bz2
Source3:        clisp-rpmlintrc
Source4:        README.SUSE
# PATCH-EXTEND-OPENSUSE Set the process execution domain
Patch1:         clisp-2.49-personality.patch
# PATCH-FIX-OPENSUSE Fix crash on Ia64
Patch2:         clisp-2.39-ia64-wooh.dif
# PATCH-EXTEND-OPENSUSE Make sure to be able to use MYCLFAGS
Patch4:         clisp-2.49-configure.dif
# PATCH-FIX-OPENSUSE Make sure to use initialized token on garbage collection
Patch5:         clisp-2.49-gctoken.dif
# PATCH-FEATURE-OPENSUSE Make CLX demos usable at runtime
Patch6:         clisp-2.49-clx_demos.dif
# PATCH-EXTEND-OPENSUSE Enable postgresql SSL feature
Patch7:         clisp-2.49-postgresql.dif
# PATCH-FIX-OPENSUSE Do not use rpath but rpath-link
Patch8:         clisp-2.49-rpath.dif
# PATCH-FIX-OPENSUSE Correct path for header for System V IPC system calls
Patch12:        clisp-linux.patch
Patch14:        clisp-link.dif
Patch16:        clisp-db6.diff

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global vimdir  %{_datadir}/vim/site/after/syntax
BuildRequires:  FastCGI-devel
BuildRequires:  db-devel
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  ffcall
#%ifarch s390x
#BuildRequires:  gcc8
#%endif
BuildRequires:  gdbm-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-tools
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  postgresql-devel
BuildRequires:  readline-devel
BuildRequires:  screen
BuildRequires:  vim-data
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw6)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
#
# If set to yes do not forget to add
#   gcc-c++
# to BuildRequires
#
%define debug   no
%global rlver   %(rpm -q --qf '%%{VERSION}' readline-devel | sed 's/\\.//g')
Requires(pre):  vim
Requires(pre):  vim-data
Requires:       ffcall
Provides:       %{name}-devel
Suggests:       %{name}-doc

%description
Common Lisp is a high-level, all-purpose programming language. CLISP is
an implementation of Common Lisp that closely follows the book "Common
Lisp - The Language" by Guy L. Steele Jr. This package includes an
interactive programming environment with an interpreter, a compiler,
and a debugger.  Start this environment with the command 'clisp'.

%package doc
Summary:        Documentation of CLisp
Group:          Development/Languages/Other
Requires:       %{name}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
CLISP documentation is placed in the following directories:

/usr/share/doc/packages/clisp/

/usr/share/doc/packages/clisp/doc/

As well as the conventional CLISP, this package also includes CLX, an
extension of CLISP for the X Window System. The X Window System must be
installed before running the clx command. The description of this CLX
version (new-clx) is placed in

/usr/share/doc/packages/clisp/clx/

with the file README. The subdirectory

/usr/share/doc/packages/clisp/clx/demos/

contains two nice applications.

%prep
%setup -qT -b0
%patch1  -p1 -b .sel
%patch2  -p1 -b .wooh
%patch4  -p1 -b .conf
%patch5  -p1 -b .gc
%patch6  -p1 -b .demos
%patch7  -p1 -b .psql
%patch8  -p1 -b .rpath
%patch12 -p1 -b .p12
%patch14 -p0 -b .p14
%patch16 -p1 -b .p16

%build
#
# Overwrite stack size limit (hopefully a soft limit only)
#
ulimit -Ss unlimited || true
ulimit -Hs unlimited || true
unset LC_CTYPE
LANG=POSIX
LC_ALL=POSIX
export LANG LC_ALL
#
# Current system
#
SYSTEM=${RPM_ARCH}-suse-linux
export PATH="$PATH:."
#
# Set gcc command line but do not use CFLAGS
#
if test %debug = yes ; then
    CC="g++"
else
    CC="gcc"
fi
%ifarch s390x
##RPM_OPT_FLAGS="$(echo %{optflags}|sed -r 's/-fstack-protector-strong ?//g;s/-f(stack-clash-protection)/-fno-\1/') -fno-stack-limit"
%endif
CC="${CC} -g ${RPM_OPT_FLAGS} -fno-strict-aliasing -fPIC -pipe"
case "$(uname -m)" in
    i[0-9]86)
	    CC="${CC} -ffloat-store"  ;;
    arm*)   CC="${CC}"				;;
    aarch64)CC="${CC}"				;;
    ppc)    CC="${CC}"				;;
    s390)   CC="${CC}"				;;
    x86_64) CC="${CC} -fno-gcse"		;;
    sparc*) CC="${CC} -mcpu=v9 -fno-gcse"	;;
    ppc64)  CC="${CC} -fno-gcse -mpowerpc64"	;;
    ppc64le)CC="${CC} -fno-gcse"		;;
    s390x)  CC="${CC} -fno-gcse -fno-schedule-insns";;
    ia64)   CC="${CC} -fno-gcse"		;;
    axp|alpha)
	    CC="${CC}"				;;
esac
#
# FastCGI-devel seems a bit broken
#
CC="${CC} -I%{_includedir}/fastcgi"

safety='-O'
MYCFLAGS="$(getconf LFS_CFLAGS)"
if grep -q _DEFAULT_SOURCE /usr/include/features.h
then
    MYCFLAGS="${MYCFLAGS} -D_GNU_SOURCE -D_DEFAULT_SOURCE"
else
    MYCFLAGS="${MYCFLAGS} -D_GNU_SOURCE"
fi
MYCFLAGS="${MYCFLAGS} -Wno-unused -Wno-uninitialized -Wno-implicit-fallthrough -Wno-volatile-register-var"
# From src/makemake.in
# <cite>
# Do NOT enable -DSAFETY=3 here, because -DSAFETY=3 not only disables some
# optimizations but also enables some debugging features (STACKCHECKs), which
# is not in the scope of --enable-portability.
# </cite>
port=''
%ifarch s390x
##port='--enable-portability'
%endif
case "$(uname -m)" in
    i[0-9]86)
            MYCFLAGS="${MYCFLAGS}"				;;
    arm*)   MYCFLAGS="${MYCFLAGS} ${safety}"			;;
    aarch64)MYCFLAGS="${MYCFLAGS}"				;;
    ppc)    MYCFLAGS="${MYCFLAGS}"				;;
    s390)   MYCFLAGS="${MYCFLAGS}"				;;
    x86_64) MYCFLAGS="${MYCFLAGS}"				;;
    sparc*) MYCFLAGS="${MYCFLAGS} ${safety}"			;;
    ppc64)  MYCFLAGS="${MYCFLAGS} ${safety}"			;;
    ppc64le)MYCFLAGS="${MYCFLAGS} ${safety}"			;;
    s390x)  MYCFLAGS="${MYCFLAGS} ${safety}"			;;
    ia64)   MYCFLAGS="${MYCFLAGS} ${safety}"			;;
    axp|alpha)
	    MYCFLAGS="${MYCFLAGS}"				;;
esac
export CC
export MYCFLAGS
unset noexec nommap safety

#
# Report final architectures
#
echo $(uname -i -m -p) %_build_arch %_arch
echo | $CC $MYCFLAGS -v -E - 2>&1 | grep /cc1
#
# Environment for the case of missing terminal
#
%global _configure	screen -D -m setarch $(uname -m) -R ./configure
%global _make		screen -D -m setarch $(uname -m) -R make
SCREENDIR=$(mktemp -d ${PWD}/screen.XXXXXX) || exit 1
SCREENRC=${SCREENDIR}/clisp
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
#
# Build the current system
#
if test %debug = yes ; then
    DEBUG=--with-debug
    MYCFLAGS="${MYCFLAGS} -g3 -DDEBUG_GCSAFETY"
else
    DEBUG=""
    MYCFLAGS="${MYCFLAGS}"
fi

find -name configure | xargs -r \
    sed -ri "/ac_precious_vars='build_alias\$/ {N; s/build_alias\\n//; }"
#
# The modules i18n, syscalls, regexp
# are part of the base clisp system.
#
> $SCREENLOG
tail -q -s 0.5 -f $SCREENLOG & pid=$!
%_configure build ${DEBUG}	\
    ${port+"$port"}		\
    --prefix=%{_prefix}		\
    --exec-prefix=%{_prefix}	\
    --libdir=%{_libdir}		\
    --vimdir=%{vimdir}		\
    --fsstnd=suse		\
    --with-readline		\
    --with-dynamic-modules      \
    --with-gettext		\
    --with-module=asdf		\
    --with-module=dbus		\
    --with-module=editor	\
    --with-module=fastcgi	\
    --with-module=queens	\
    --with-module=gdbm		\
    --with-module=gtk2		\
    --with-module=pcre		\
    --with-module=rawsock	\
    --with-module=zlib		\
    --with-module=bindings/glibc\
    --with-module=clx/new-clx	\
    --with-module=berkeley-db	\
    --with-module=postgresql

%_make -C build lispbibl.h
grep TYPECODES build/lispbibl.h || :
%_make -C build
%_make -C build check

#
# Stop tail
#
sleep 1
kill $pid

#
# Check for errors
#

check=no
for err in build/tests/*.erg
do
    test -e "$err" || break
    check=yes
    cat $err
done
if test $check != no
then
    type -p uname   > /dev/null 2>&1 && uname -a || :
    type -p netstat > /dev/null 2>&1 && netstat -i || :
    type -p netstat > /dev/null 2>&1 && netstat -x || :
    type -p ip > /dev/null 2>&1 && ip link || :
    type -p ss > /dev/null 2>&1 && ss -x   || :
fi
#
%install
#
# Clean
#
find modules/clx/ -name '*.demos' | xargs --no-run-if-empty rm -vf
#
# Current system
#
SYSTEM=${RPM_ARCH}-suse-linux
LSPDOC=%{_docdir}/clisp
DOCDOC=${LSPDOC}/doc
CLXDOC=${LSPDOC}/clx
LSPLIB=%{_libdir}/clisp-%{version}
CLXLIB=${LSPLIB}/full
#
# Install the current system
#
setarch $(uname -m) -R make -C build install prefix=%{_prefix}   \
        exec_prefix=%{_prefix}      \
        mandir=%{_mandir}       \
        libdir=%{_libdir}       \
    DESTDIR=%{buildroot}        \
    INSTALL_DATA="install -cm 0444"

#
# The CLX interface
#
install -d %{buildroot}${CLXDOC}
install -d %{buildroot}${CLXLIB}
pushd modules/clx/new-clx/
  install -c -m 0444 README %{buildroot}${CLXDOC}/
  install -c -m 0444 %{S:4} %{buildroot}${CLXDOC}/
  tar cf - demos/ | (cd %{buildroot}${CLXDOC}/ ; tar xf - )
popd
pushd modules/clx/
  tar xfz clx-manual.tar.gz -C %{buildroot}${CLXDOC}
popd
find %{buildroot} -name "*.a" | xargs chmod u+w
chmod    u+xrw,a+rx %{buildroot}%{_bindir}/clisp
chmod    u+xrw,a+rx %{buildroot}%{_bindir}/clisp-link
chmod -R g+r,o+r    %{buildroot}${LSPDOC}/
chmod    a-x        %{buildroot}${CLXDOC}/clx-manual/html/doc-index.cgi
find   %{buildroot}${LSPDOC} -type d | xargs chmod 755
rm -f  %{buildroot}${CLXDOC}/*,v
rm -f  %{buildroot}${CLXDOC}/.\#*
rm -f  %{buildroot}${CLXDOC}/demos/*,v
rm -f  %{buildroot}${CLXDOC}/demos/.\#*
rm -f  %{buildroot}${CLXDOC}/demos/*.orig
find   %{buildroot}${LSPLIB}/ -name '*.dvi' | xargs -r rm -f
find   %{buildroot}${LSPLIB}/ -name '*.run' | xargs -r chmod 0755
rm -rf %{buildroot}${LSPLIB}/new-clx/demos/
find   %{buildroot} -type f | xargs -r chmod u+w
chmod a+x %{buildroot}${LSPLIB}/build-aux/{config,depcomp}*
%fdupes %{buildroot}${LSPLIB}/
%find_lang clisp
%find_lang clisplow clisp.lang

%files -f clisp.lang
%defattr(-,root,root,755)
%{_bindir}/clisp
%{_bindir}/clisp-link
%{_libdir}/clisp-%{version}/
%{_datadir}/aclocal/clisp.m4
%{_datadir}/emacs/site-lisp/
%doc %{_datadir}/man/man1/clisp*.1.gz
%{vimdir}/lisp.vim

%files doc
%defattr(-,root,root,755)
%{_docdir}/clisp/

%changelog
