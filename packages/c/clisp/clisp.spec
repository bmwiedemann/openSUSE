#
# spec file for package clisp
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_with     debug
%global commit  f5acef38
%global vdate   20240704

Name:           clisp
Version:        2.49.93
Release:        0
Summary:        A Common Lisp Interpreter
# Included gllib is GPL-3.0-or-later
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Development/Languages/Other
URL:            https://gitlab.com/gnu-clisp/clisp
Source:         %{name}-%{version}+git%{vdate}.%{commit}.tar.xz
Source2:        clhs.el
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
# PATCH-FIX-OPENSUSE Correct path for header for System V IPC system calls
Patch12:        clisp-linux.patch
Patch13:        clisp-gcc14.patch
Patch14:        clisp-link.dif
Patch16:        clisp-db6.diff

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
BuildRequires:  groff
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  libsvm-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-tools
BuildRequires:  openssl-devel
BuildRequires:  pari-devel
BuildRequires:  pari-gp
BuildRequires:  pcre-devel
BuildRequires:  pcre2-devel
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
%global ldflags %{nil}
%ifarch %arm ppc ppc64 ppc64le s390 s390x %ix86
%global _lto_cflags %{nil}
%else
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%endif
%global rlver   %(rpm -q --qf '%%{VERSION}' readline-devel | sed 's/\\.//g')
%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}
%define add_ldflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global ldflags %{ldflags} %{**}
Requires(pre):  vim
Requires(pre):  vim-data
Requires:       ffcall
# CLISP memory image data are compressed with gzip
Requires:       /usr/bin/gzip
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
%setup -qT -b0 -n %{name}-%{version}+git%{vdate}.%{commit}
%patch -P 1  -p1 -b .sel
%patch -P 2  -p1 -b .wooh
%patch -P 4  -p1 -b .conf
%patch -P 5  -p1 -b .gc
%patch -P 6  -p1 -b .demos
%patch -P 7  -p1 -b .psql
%patch -P 12 -p1 -b .p12
%patch -P 13 -p0 -b .p13
%patch -P 14 -p0 -b .p14
%patch -P 16 -p1 -b .p16

%build
%add_optflags -g3 -D_GNU_SOURCE -D_DEFAULT_SOURCE -D_XOPEN_SOURCE
%add_optflags -fno-strict-aliasing -fPIC -pipe -Wa,--noexecstack
%add_optflags -Wno-unused -Wno-uninitialized -Wno-implicit-fallthrough -Wno-volatile-register-var -Wno-address
%add_optflags -Wno-clobbered -Wno-dangling-pointer -Wno-unused-result -Wno-missing-declarations -Wno-cast-function-type
%{expand:%%global optflags %(echo "%{optflags}"|sed -r -e s/-fstack-protector-strong// -e s/-fstack-clash-protection//)}
%{expand:%%global optflags %%optflags %(getconf LFS_CFLAGS)}
%add_ldflags -Wl,--as-needed -Wl,-z,relro -Wl,-z,noexecstack
#
# Overwrite stack size limit (hopefully a soft limit only)
#
ulimit -Ss unlimited || true
ulimit -Hs unlimited || true
unset LC_CTYPE
LANG=C.UTF-8
LC_ALL=C.UTF-8
export LANG LC_ALL
#
# Current system
#
SYSTEM=${RPM_ARCH}-suse-linux
export PATH="$PATH:."
#
# Set gcc command line but do not use CFLAGS
%if %{with debug}
    export CC="g++"
    DEBUG=--with-debug
%add_optflags -g3 -DDEBUG_GCSAFETY
%else
    DEBUG=
    export CC="gcc"
%endif
export MYCFLAGS=""
%ifarch s390x ppc64 ppc64le
%{expand:%%global optflags %(echo "%{optflags}"|sed -r -e s/-fstack-protector-strong// -e s/-fstack-clash-protection//)}
%add_optflags -fno-pie -fno-PIE
%add_ldflags -no-pie
MYCFLAGS=-O
%endif
%ifarch %arm
%{expand:%%global optflags %(echo "%{optflags}"|sed -r -e s/-O[0-9]/-O/g)}
MYCFLAGS=-O
%endif
%ifarch aarch64
%endif
%ifarch ppc
%endif
%ifarch s390
%endif
%ifarch alpha
%endif
%ifarch %ix86
%add_optflags -ffloat-store
MYCFLAGS=-O
%endif
%ifarch x86_64 sparc sparc64 ia64 s390x ppc64 ppc64le
%add_optflags -fno-gcse
%endif
%ifarch ia64 s390x ppc64 ppc64le
%{expand:%%global optflags %(echo "%{optflags}"|sed -r -e s/-O[0-9]/-O/g)}
MYCFLAGS=-O
%endif
%ifarch sparc sparc64
%add_optflags -mcpu=v9
%endif
#
# FastCGI-devel seems a bit broken
#
%add_optflags -I%{_includedir}/fastcgi

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

#
# Report final architectures
#
echo $(uname -i -m -p) %_build_arch %_arch
echo | $CC %{optflags} -v -E - 2>&1 | grep /cc1
#
# Environment for the case of missing terminal
#
%global _configure	screen -D -m setarch $(uname -m) -R ./configure
%global _make		screen -D -m setarch $(uname -m) -R make
#
# Shorten socket path as otherwise bind(2) used by screen(1)
# fails with invalid argument due shorten patch of 108 chracters
# of sun_path used in glibc (note that kernel use UNIX_PATH_MAX)
#
TMPDIR=$(mktemp -d /tmp/clisp.XXXXXX) || exit 1
SCREENDIR=$TMPDIR
SCREENRC=${SCREENDIR}/clisp
export SCREENRC SCREENDIR TMPDIR
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

find -name configure | xargs -r \
    sed -ri "/ac_precious_vars='build_alias\$/ {N; s/build_alias\\n//; }"
# Runtime linker choose system libraries
sed -ri 's/(\$\{wl\})-rpath (\$\{wl\})/\1-rpath-link \2/g' src/build-aux/config.rpath
# Link libraries if really needed
sed -ri "s/CC='\\$\{CC\}'/CC='\\$\{CC\} -Wl,--as-needed'/g" src/makemake.in
#Default browser
sed -ri 's/;; (\(setq \*browser\* .*\))/\1/' src/cfgunix.lisp
#The pari lib doesn ot know anymore about diffptrE
sed -ri 's/(\(def-c-var diffptr)/;; \1/p' modules/pari/pari.lisp

#
# The modules i18n, syscalls, regexp
# are part of the base clisp system.
#
> $SCREENLOG
tail -q -s 0.5 -f $SCREENLOG & pid=$!
env -i HOME=$HOME TERM=$TERM PATH=$PATH TMPDIR=$TMPDIR \
       LANG=C.UTF-8 LC_ALL=C.UTF-8 SCREENRC=$SCREENRC SCREENDIR=$SCREENDIR \
%_configure build ${DEBUG}	\
    ${port+"$port"}		\
    --prefix=%{_prefix}		\
    --exec-prefix=%{_prefix}	\
    --libdir=%{_libdir}		\
    --vimdir=%{vimdir}		\
    --fsstnd=suse		\
    --with-readline		\
    --with-dynamic-modules      \
    --with-ffcall		\
    --with-gettext		\
    --with-module=asdf		\
    --with-module=dbus		\
    --with-module=editor	\
    --with-module=fastcgi	\
    --with-module=queens	\
    --with-module=gdbm		\
    --with-module=gtk2		\
    --with-module=pari		\
    --with-module=pcre		\
    --with-module=rawsock	\
    --with-module=zlib		\
    --with-module=libsvm	\
    --with-module=bindings/glibc\
    --with-module=clx/new-clx	\
    --with-module=berkeley-db	\
    --with-module=postgresql	\
    --config			\
    CC="${CC}"			\
    CFLAGS="%{optflags}"	\
    LDFLAGS="%{ldflags}"

env -i HOME=$HOME TERM=$TERM PATH=$PATH TMPDIR=$TMPDIR \
       LANG=C.UTF-8 LC_ALL=C.UTF-8 SCREENRC=$SCREENRC SCREENDIR=$SCREENDIR \
%_make -C build lispbibl.h
grep TYPECODES build/lispbibl.h || :
env -i HOME=$HOME TERM=$TERM PATH=$PATH TMPDIR=$TMPDIR \
       LANG=C.UTF-8 LC_ALL=C.UTF-8 SCREENRC=$SCREENRC SCREENDIR=$SCREENDIR \
%_make -C build
env -i HOME=$HOME TERM=$TERM PATH=$PATH TMPDIR=$TMPDIR \
       LANG=C.UTF-8 LC_ALL=C.UTF-8 SCREENRC=$SCREENRC SCREENDIR=$SCREENDIR \
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
. ./version.sh
SYSTEM=${RPM_ARCH}-suse-linux
LSPDOC=%{_docdir}/clisp
DOCDOC=${LSPDOC}/doc
CLXDOC=${LSPDOC}/clx
LSPLIB=%{_libdir}/clisp-${VERSION_NUMBER}
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
install -c -m 644 %{S:2} %{buildroot}%{_datadir}/emacs/site-lisp/clhs.el
%fdupes %{buildroot}${LSPLIB}/
%find_lang clisp
%find_lang clisplow clisp.lang

%files -f clisp.lang
%defattr(-,root,root,755)
%{_bindir}/clisp
%{_bindir}/clisp-link
%{_libdir}/clisp-%{version}*/
%{_datadir}/aclocal/clisp.m4
%{_datadir}/emacs/site-lisp/
%doc %{_datadir}/man/man1/clisp*.1.gz
%{vimdir}/lisp.vim

%files doc
%defattr(-,root,root,755)
%{_docdir}/clisp/

%changelog
