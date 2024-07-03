#
# spec file for package ncurses
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_with     hasheddb
%if 0%{?suse_version} > 1320
%bcond_without  symversion
%else
%bcond_with     symversion
%endif
%bcond_with     memleakck
%bcond_without  onlytinfo
%bcond_with     ada
%bcond_with     libbsd
%bcond_with     usepcre2
%bcond_with     gpgverify

%if %{with onlytinfo}
%global soname_tinfo tinfo
%else
%global soname_tinfo tinfow
%endif

%global patchlvl %(bash %{_sourcedir}/get_version_number.sh %{_sourcedir})
%global basevers 6.5
%global tackvers 1.10
%global tacklvl  20240501

Name:           ncurses
#!BuildIgnore: terminfo
%if %{with hasheddb}
BuildRequires:  db-devel
%endif
%if %{with gpgverify}
BuildRequires:  /usr/bin/gpg
%endif
BuildRequires:  /usr/bin/zcat
BuildRequires:  expect
%if %{with ada}
# Currently we're missing gprbuild and gprconfig
BuildRequires:  gcc-ada
BuildRequires:  m4
%endif
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
%if %{with libbsd}
BuildRequires:  pkgconfig(libbsd)
%endif
BuildRequires:  screen
%if %{with usepcre2}
BuildRequires:  pkgconfig(libpcre2-8)
%endif
%if 0%{?suse_version} > 1130
BuildRequires:  gpm-devel
%else
BuildRequires:  gpm
%endif
BuildRequires:  makedepend
%define terminfo() %{_datadir}/%{0}/%{1}
%define tabset()   %{_datadir}/%{0}/%{1}
# bug437293
%ifarch ppc64
Obsoletes:      ncurses-64bit
%endif
#
# Note that this spec files does not only build the ABI version 6
# but also build the ABI version 5 as this is part of the source
# tar ball including the latest upstream fixes for ABI 5.
#
Version:        6.5.%{patchlvl}
Release:        0
Summary:        Terminal control library
#Git:           http://ncurses.scripts.mit.edu
License:        MIT
Group:          System/Base
URL:            https://www.invisible-island.net/ncurses/ncurses.html
Source0:        https://www.invisible-island.net/archives/ncurses/ncurses-%{basevers}.tar.gz
Source1:        ncurses-%{basevers}-patches.tar.bz2
Source2:        handle.linux
Source3:        README.devel
Source4:        ncurses-rpmlintrc
# Latest tack can be found at ftp://ftp.invisible-island.net/pub/ncurses/current/
Source5:        https://www.invisible-island.net/archives/ncurses/current/tack-%{tackvers}-%{tacklvl}.tgz
Source6:        edit.sed
Source7:        baselibs.conf
Source8:        cursescheck
Source9:        https://www.invisible-island.net/archives/ncurses/ncurses-%{basevers}.tar.gz.asc
Source10:       https://www.invisible-island.net/archives/ncurses/current/tack-%{tackvers}-%{tacklvl}.tgz.asc
Source11:       ncurses.keyring
Patch0:         ncurses-6.4.dif
Patch1:         ncurses-5.9-ibm327x.dif
Patch2:         ncurses-5.7-tack.dif
Patch3:         FORTIFY_SOURCE_3-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _miscdir    %{_datadir}/misc
%global         _incdir     %{_includedir}
%global         root        %{_tmppath}/%{name}-%{version}-store

%description
As soon as a text application needs to directly control its output to
the screen (if it wants to place the cursor at location (x,y) then
write text), ncurses is used. The panel and the forms libraries are
included in this package. The ncurses libraries support color, special
characters, forms, and panels.

%package -n ncurses-utils
Summary:        Tools using the new curses libraries
License:        MIT
Group:          System/Base
Provides:       ncurses:%{_bindir}/tput

%description -n ncurses-utils
The ncurses based utilities are as follows:

clear -- emits clear-screen for current terminal

tabs -- set tabs on a terminal

toe   -- table of entries utility

tput  -- shell-script access to terminal capabilities.

tset  -- terminal-initialization utility

reset -- terminal initialization utility

%package -n ncurses-examples
Provides:       ncurses-tests = %{version}
Obsoletes:      ncurses-tests <= 6.3.20211127
Summary:        Tools using the new curses libraries
License:        MIT
Group:          System/Base
Requires:       ncurses-utils >= %{version}

%description -n ncurses-examples
The ncurses based test programs, that is a set of tools
showing the features of the new curses libraries.

%package -n terminfo-base
Summary:        A terminal descriptions database
License:        MIT
Group:          System/Base
Requires:       ncurses >= %{version}
Recommends:     terminfo-screen = %{version}
Provides:       ncurses:%{_datadir}/tabset

%description -n terminfo-base
This is the terminfo basic database, maintained in the ncurses package.
This database is the official successor to the 4.4BSD termcap file and
contains information about any known terminal. The ncurses library
makes use of this database to use terminals correctly.

%package -n terminfo-screen
Summary:        A terminal descriptions database for screen
License:        MIT
Group:          System/Base
Requires:       terminfo-base
Provides:       terminfo:%{_datadir}/terminfo/s/screen.konsole

%description -n terminfo-screen
This package includes some useful entries for the screen utility in the
terminfo database, which might introduce trouble if used over network
connections like ssh or slogin onto systems without those terminfo database
entries.

%package -n terminfo-iterm
Summary:        A terminal descriptions database for iterm
License:        MIT
Group:          System/Base
Requires:       terminfo-base
Provides:       terminfo:%{_datadir}/terminfo/i/iTerm.app

%description -n terminfo-iterm
This package includes some useful entries for the iterm utility in the
terminfo database, which might introduce trouble if used over network
connections like ssh or slogin onto systems without those terminfo database
entries.

%package -n libncurses5
Summary:        Terminal control library
License:        MIT
Group:          System/Libraries
Requires:       terminfo-base
Provides:       ncurses = 5.9
Obsoletes:      ncurses < 5.9
# bug437293
%ifarch ppc64
Obsoletes:      ncurses-64bit
%endif
#

%description -n libncurses5
The ncurses library is used by many terminal applications for
controlling output to the screen and input from the user.

This package contains the library built with the version 5 ABI.

%package -n libncurses6
Summary:        Terminal control library
License:        MIT
Group:          System/Libraries
Requires:       terminfo-base
Provides:       ncurses = %{version}
Recommends:     ncurses-utils = %{version}

%description -n libncurses6
The ncurses library is used by many terminal applications for
controlling output to the screen and input from the user.

This package contains the library built with the version 6 ABI.

%package -n terminfo
Summary:        A terminal descriptions database
License:        SUSE-Public-Domain
Group:          System/Base
Requires:       terminfo-base = %{version}

%description -n terminfo
This is the terminfo reference database, maintained in the ncurses
package. This database is the official successor to the 4.4BSD termcap
file and contains information about any known terminal. The ncurses
library makes use of this database to use terminals correctly. If you
just use the Linux console, xterm, and VT100, you probably will not
need this database -- a minimal /usr/share/terminfo tree for these
terminals is already included in the terminfo-base package.

%package -n ncurses-devel
Summary:        Development files for the ncurses6 terminal control library
License:        MIT
Group:          Development/Libraries/C and C++
Provides:       ncurses6-devel
Provides:       ncurses:%{_incdir}/ncurses.h
Requires:       %{_bindir}/tack
Requires:       libncurses6 = %{version}-%{release}
Requires:       ncurses = %{version}-%{release}
%if %{with usepcre2}
Requires:       pkgconfig(libpcre2-8)
%endif
# bug437293
%ifarch ppc64
Obsoletes:      ncurses-devel-64bit
%endif
#

%description -n ncurses-devel
This package contains the headers needed to build against
the ncurses library in its ABI version 6 form.

%package -n ncurses-devel-static
Summary:        Static libraries for the ncurses6 terminal control library
License:        MIT
Group:          Development/Libraries/C and C++
Provides:       ncurses-devel:%{_libdir}/libform.a
Provides:       ncurses-devel:%{_libdir}/libformw.a
Provides:       ncurses-devel:%{_libdir}/libmenu.a
Provides:       ncurses-devel:%{_libdir}/libmenuw.a
Provides:       ncurses-devel:%{_libdir}/libncurses++.a
Provides:       ncurses-devel:%{_libdir}/libncurses++w.a
Provides:       ncurses-devel:%{_libdir}/libncurses.a
Provides:       ncurses-devel:%{_libdir}/libncurses.a
Provides:       ncurses-devel:%{_libdir}/libncursesw.a
Provides:       ncurses-devel:%{_libdir}/libpanel.a
Provides:       ncurses-devel:%{_libdir}/libpanelw.a
Provides:       ncurses-devel:%{_libdir}/libtic.a
Provides:       ncurses-devel:%{_libdir}/libticw.a
Provides:       ncurses-devel:%{_libdir}/libtinfo.a
Requires:       ncurses-devel = %{version}-%{release}

%description -n ncurses-devel-static
This package contains the static library files for
the ncurses library in its ABI version 6 form.

%package -n ncurses5-devel
Summary:        Development files for the ncurses5 terminal control library
License:        MIT
Group:          Development/Libraries/C and C++
Provides:       ncurses:%{_incdir}/ncurses5/ncurses.h
Requires:       %{_bindir}/tack
Requires:       libncurses5 = %{version}-%{release}
Requires:       ncurses = %{version}-%{release}
Requires:       ncurses-devel = %{version}-%{release}

%description -n ncurses5-devel
This package contains the headers needed to build against
the ncurses library in its ABI version 5 form.

%package -n ncurses5-devel-static
Summary:        Static libraries for the ncurses5 terminal control library
License:        MIT
Group:          Development/Libraries/C and C++
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libform.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libformw.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libmenu.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libmenuw.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libncurses++.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libncurses++w.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libncurses.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libncurses.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libncursesw.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libpanel.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libpanelw.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libtic.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libticw.a
Provides:       ncurses5-devel:%{_libdir}/ncurses5/libtinfo.a
Requires:       ncurses5-devel = %{version}-%{release}

%description -n ncurses5-devel-static
This package contains the static library files for
the ncurses library in its ABI version 5 form.

%package -n tack
Version:        %{tackvers}.%{tacklvl}
Summary:        Terminfo action checker
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Provides:       ncurses-devel:%{_bindir}/tack
Requires:       ncurses = %{basevers}.%{patchlvl}

%description -n tack
This package contains the tack utility to help to build a new terminfo
entry describing an unknown terminal. It can also be used to test the
correctness of an existing entry, and to develop the correct pad
timings needed to ensure that screen updates do not fall behind the
incoming data stream.

%prep
%setup -q -n %{name}-%{basevers} -b1 -a5
set +x
%if %{with gpgverify}
GPGTMP=$(mktemp -d ${PWD}/tmp.XXXXXXXXXX)
gpg --homedir $GPGTMP -q --no-default-keyring --trust-model always --import %{S:11}
gpg --homedir $GPGTMP -q --multifile --verify ../patches/*.patch.gz.asc
unset GPGTMP
rm -rf "$GPGTMP"
%endif
for patch in ../patches/ncurses*.patch.gz
do
    test -e "$patch" || continue
    echo Apply patch: $patch
    zcat $patch | patch -f -T -p1 -s
done
set -x
%if ! %{defined donttouch}
rm -rf ../patches/
%endif
find -name '*.orig' -delete
# replace tack from ncurses tarball with the latest version in
# separate tarball
rm -fr tack
mv tack-* tack
%patch -P1 -p0 -b .327x
%patch -P2 -p0 -b .hs
%patch -P0 -p0 -b .p0
%patch -P3 -p1

%build
#
# Do not run auto(re)conf here as this will fail later on ncurses
# is build with special autoconf based on autoconf-2.13 at upstream
#
%global _lto_cflags_shared %{?_lto_cflags} -ffat-lto-objects
%global _lto_cflags %nil
#
# Note that there is a test if the system call poll(2) really works
# on terminal or files.  To make sure that even in OBS the configure
# script has its own terminal we use screen here (could be also tmux).
#
# Remark: A better solution would be that in OBS a real pty/tty pair
# would be used instead of redirecting stdout/stderr to a log file.
#
CFLAGS_SHARED="%{_lto_cflags_shared}"
export CFLAGS_SHARED
%global configtack	%configure
%global _configure	screen -D -m ./configure
    SCREENDIR=$(mktemp -d ${PWD}/screen.XXXXXX) || exit 1
    SCREENRC=${SCREENDIR}/ncurses
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
    # Used to test out various cflags of the gcc
    #
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
	    if ${CC:-gcc} -Werror $flag -S -o /dev/null -xc /dev/null > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	    if ${CXX:-g++} -Werror $flag -S -o /dev/null -xc++ /dev/null > /dev/null 2>&1 ; then
		eval $var=\${$var:+\$$var\ }$flag
	    fi
	esac
	set +o noclobber
    }

    test ! -f /.buildenv || . /.buildenv
       OPATH=$PATH
%ifarch s390x s390
      FALLBK="unknown,dumb,xterm,xterm-256color,ibm327x,ms-terminal,vt100,vt102,vt220"
%else
      FALLBK="unknown,dumb,xterm,xterm-256color,linux,ms-terminal,vt100,vt102,vt220"
%endif
	  CC=gcc
	 CXX=g++
    CFLAGS="${RPM_OPT_FLAGS} -pipe -D_REENTRANT"
    if [[ "$BUILD_BASENAME" = debug-* ]] ; then
	CFLAGS="${CFLAGS} -g -DTRACE"
    fi
    cflags -Wl,-O2                  LDFLAGS
    cflags -Wl,-Bsymbolic-functions LDFLAGS
    cflags -Wl,--hash-size=8599     LDFLAGS
    cflags -Wl,--as-needed          LDFLAGS
    CXXFLAGS=$CFLAGS
    CPPFLAGS=
    include=
    for header in stddef.h limits.h
    do
	set -- $(echo '#include <'$header'>'|gcc -E -|sed -rn 's@[^/]*"([a-z0-9/\._-]+)/'$header'".*@\1@p'| sort -u)
	for found
	do
	    case "$found" in
	    /usr/include*) continue ;;
	    esac
	    include=${include+"-I$found $include"}
	done
    done
    if test -n "$include"
    then
        CPPFLAGS="$include"
	unset include
    fi
    test -n "$TERM" || TERM=linux
    INSTALL_PROGRAM='${INSTALL}'
    INSTALL_OPT_S=""
    export CC CFLAGS CXX CXXFLAGS CPPFLAGS TERM LDFLAGS INSTALL_PROGRAM INSTALL_OPT_S
    #
    # Detect 64bit architecures and be sure that we use an
    # unsigned long for chtype to be backward compatible with
    # already existing ncurses applications.  Otherwise we
    # might break existing applications on any update!
    #
    if test $(getconf LONG_BIT) -gt 32 ; then
	WITHCHTYPE="--with-chtype=long"
    else
	WITHCHTYPE=""
	CFLAGS="${CFLAGS} $(getconf LFS_CFLAGS)"
    fi
    #
    # Let's care about people which build ncurses on their own
    # system. That is take care that some configure tests might
    # be exploitable below /tmp ... compare with aclocal.m4
    #
    TMPDIR=$(mktemp -d /tmp/ncurses.XXXXXXXX) || exit 1
    trap 'rm -rf ${TMPDIR}' EXIT
    export TMPDIR
    #
    # getttynam(3) as well as /etc/ttys are not used under Linux
    # (obsolate with patch 6.3 20211204)
    #   sed -ri '/^getttynam\s*\\$/d' configure
    #
    # No --enable-term-driver as this had crashed last time
    # in ncurses/tinfo/lib_setup.c due to the fact that
    # _nc_globals.term_driver was a NULL function pointer as
    # this is for the MinGW port!
    #
    # No --enable-tcap-names because we may have to recompile
    # programs or foreign programs won't work
    #
    # No --enable-safe-sprintf because this seems to
    # crash on some architectures
    #
    # No --enable-xmc-glitch because this seems to break yast2
    # on console/konsole (no magic cookie support on those?)
    #
    # No --enable-hard-tabs for users which have disabled
    # the use of tabs
    #
    touch --reference=README config.sub config.guess
    > $SCREENLOG
    tail -q -s 0.5 -f $SCREENLOG & pid=$!
    %configure \
%if %{with ada}
	--with-ada		\
%else
	--without-ada		\
%endif
	--without-debug		\
	--without-profile	\
	--without-manpage-tbl	\
	--without-tests		\
	--with-shared		\
	--with-normal		\
	--with-manpage-renames=${PWD}/man/man_db.renames.in	\
	--with-manpage-aliases	\
	--with-manpage-symlinks	\
	--with-ospeed=speed_t	\
%if 0%{?suse_version} > 1310
	--with-gpm=$(readlink %{_libdir}/libgpm.so) \
%else
	--with-gpm		\
%endif
	--with-dlsym		\
	--with-default-terminfo-dir=%{_datadir}/terminfo \
	--with-terminfo-dirs=%{_sysconfdir}/terminfo:%{_datadir}/terminfo \
	--with-xterm-kbs=DEL	\
%if %{with usepcre2}
	--with-pcre2		\
%endif
	--disable-stripping	\
	--disable-root-access	\
	--disable-root-environ	\
	--disable-setuid-environ\
	--disable-termcap	\
	--disable-overwrite	\
	--disable-rpath		\
	--disable-rpath-hack	\
%if %{with memleakck}
	--disable-leaks		\
%endif
	--disable-xmc-glitch	\
	--enable-symlinks	\
	--enable-big-core	\
	--enable-const		\
	--enable-hashmap	\
	--enable-no-padding	\
	--enable-sigwinch	\
	--enable-colorfgbg	\
	--enable-sp-funcs	\
	--enable-interop	\
	--with-pthread		\
	--enable-reentrant	\
%if 0%{?suse_version} > 1500
	--enable-opaque-curses	\
	--enable-opaque-form	\
	--enable-opaque-menu	\
	--enable-opaque-panel	\
%endif
	--enable-ext-mouse	\
	--enable-widec		\
	--enable-wattr-macros	\
	--with-termlib=%{soname_tinfo}	\
	--with-ticlib=ticw	\
%if %{with symversion}
	--with-versioned-syms=${PWD}/package/ncursestw.map \
%endif
	--enable-ext-colors	\
	--enable-weak-symbols	\
	--disable-wgetch-events	\
	--enable-pthreads-eintr	\
	--enable-string-hacks	\
	--enable-check-size	\
	--prefix=%{_prefix}	\
	--exec-prefix=%{_prefix}\
	--libdir=%{_libdir}	\
	--datadir=%{_datadir}	\
	--mandir=%{_mandir}	\
	--includedir=%{_incdir}	\
	"${WITHCHTYPE}" 	\
	--disable-tic-depends	\
	--with-cxx-shared	\
	--with-pc-suffix	\
	--enable-pc-files	\
%if 0%{?_crossbuild}
	--with-fallbacks="$FALLBK" \
%else
	--with-fallbacks=""	\
%endif
%if %{with hasheddb}
	--with-hashed-db	\
%endif
	--with-pkg-config-libdir=%{_libdir}/pkgconfig
    sleep 1
    kill $pid
    #
    #  The configure line used above.  Note that we override
    #  several options later with other configurations.
    #  It has been verified several times that this works.
    #
    c=$(grep '^ *$ *\./configure' config.log)
    make depend
    make -C c++ etip.h
    make %{?_smp_mflags}
    #
    # Refresh second install path
    #
    rm -rf %{root}
    mkdir  %{root}
%if !0%{?_crossbuild}
    #
    # This is a hack to be able to boot strap libncurses with
    # our preferred fallback.c.  For this we need the appropiate
    # tools list infocmp(1) and tic(1).  The first step was with
    # an empty fallback.c, now we include the latest terminfo
    # of our preferred fallback terminfo list into the final
    # fallback.c.
    #
    mkdir lib/.build
    cp -p progs/tic progs/tic.build
    cp -p progs/infocmp progs/infocmp.build
    cp -p lib/*.so* lib/.build/
    PATH=$PWD/progs:$OPATH
    export PATH
    (cat > ${PWD}/.build_tic)<<-EOF
	export LD_LIBRARY_PATH=$PWD/lib/.build
	export BUILD_TIC=$PWD/progs/tic.build
	export BUILD_INFOCMP=$PWD/progs/infocmp.build
	EOF
    pushd ncurses/
	. ${PWD}/../.build_tic
	$BUILD_TIC -I -r -e $FALLBK ../misc/terminfo.src > terminfo.src
	$BUILD_TIC -o $TERMINFO -s terminfo.src
	bash -e ./tinfo/MKfallback.sh $PWD/tmp_info ../misc/terminfo.src $BUILD_TIC $BUILD_INFOCMP ${FALLBK//,/ } > fallback.c
	rm -rf $TERMINFO
	unset  TERMINFO
	cp -p fallback.c ../fallback.c.build
	unset LD_LIBRARY_PATH
    popd
    PATH=$OPATH
    #
    # Now rebuild libncurses and do the rest of this job
    #
    find -name fallback.o -print -delete
    cp fallback.c.build ncurses/fallback.c
    make depend
    make -C c++ etip.h
    make %{?_smp_mflags}
%else
    (cat > ${PWD}/.build_tic)<<-EOF
	export BUILD_TIC=/usr/bin/tic
	export BUILD_INFOCMP=/usr/bin/infocmp
	EOF
%endif
    # must not use %jobs here (would lead to: ln: ncurses.h already exists)
    find man/ -name '*.[1-8]x.*' -print -delete
    make install DESTDIR=%{root} includedir=%{_incdir} includesubdir=/ncursesw libdir=%{_libdir}
%if %{with onlytinfo}
    # This ensures that we get the libtinfo *with* _nc_read_entry2 symbol as well
    gcc $CFLAGS $LDFLAGS -fPIC -shared -Wl,--auxiliary=libtinfo.so.6,-soname,libtinfow.so.6,-stats,-lc \
	 -Wl,--version-script,ncurses/resulting.map -o %{root}%{_libdir}/libtinfow.so.%{basevers}
    cp -p %{root}%{_libdir}/libtinfo.so.%{basevers}  libtinfo.so.%{basevers}.back
    cp -p %{root}%{_libdir}/libtinfow.so.%{basevers} libtinfow.so.%{basevers}.back
%endif
    ln -sf %{_incdir}/ncurses/{curses,ncurses,term,termcap}.h %{root}%{_incdir}
    mkdir pc
    PKG_CONFIG_PATH=$PWD/pc:$(pkg-config --variable pc_path pkg-config)
    export PKG_CONFIG_PATH
    rm -vf %{root}%{_libdir}/pkgconfig/tic.pc
    rm -vf %{root}%{_libdir}/pkgconfig/tinfo.pc
    mv -vf %{root}%{_libdir}/pkgconfig/*.pc pc/
    sed -ri 's@^(Requires.private:).*@\1@'  pc/*.pc
    echo $PKG_CONFIG_PATH
    what=ncursesw
    cflags="$(pkg-config --cflags $what)"
      libs="$(pkg-config --libs   $what)"
    test -n "$cflags" -a -n "$libs" || exit 1
    bash %{S:6} --cflags "${cflags%%%% }" --libs "${libs%%%% }" %{root}%{_bindir}/${what}6-config

    #
    # Some tests
    #
%if 0%{?_crossbuild}
	echo "Skipping tests due to cross-building"
%else
    #
    # Check for tack program on base of above ncurses
    #
    LD_LIBRARY_PATH=$PWD/lib
    export LD_LIBRARY_PATH PATH
    pushd tack/
	OCFLAGS="$CFLAGS"
	OLDFLAGS="$LDFLAGS"
	OPKG_CONFIG_PATH="$PKG_CONFIG_PATH"
	CFLAGS="$CFLAGS -I%{root}%{_incdir}/ncursesw/ -I%{root}%{_incdir}/ -fPIE" \
	LDFLAGS="$LDFLAGS  -Wl,-rpath-link=%{root}%{_libdir} -L%{root}%{_libdir} -pie" \
	PKG_CONFIG_PATH=${PWD}/../pc/ \
	%configtack --with-ncursesw --disable-rpath-hack
	make %{?_smp_mflags}
	CFLAGS="$OCFLAGS"
	LDFLAGS="$OLDFLAGS"
	PKG_CONFIG_PATH="$OPKG_CONFIG_PATH"
	ldd ./tack
    popd
    unset LD_LIBRARY_PATH
%if 0%{?suse_version} > 1500
    #
    # Make the test suite for ncursesw6
    #
    pushd test
	CFLAGS="$CFLAGS -I%{root}%{_incdir}/ncursesw/ -I%{root}%{_incdir}/" \
	LDFLAGS="$LDFLAGS -Wl,-rpath-link=%{root}%{_libdir} -L%{root}%{_libdir}" \
	LIBS="$LDFLAGS" \
	./configure --with-ncursesw --with-screen=ncursesw --enable-widec --enable-wattr-macros --prefix=%{_prefix} --datadir=%{_datadir}/ncurses

	LD_LIBRARY_PATH=%{root}%{_libdir} \
%if %{with usepcre2}
	make %{?_smp_mflags} TEST_ARGS='-lformw -lmenuw -lpanelw -lncursesw -lticw -l%{soname_tinfo} -Wl,--as-needed' TEST_LIBS='-lutil -lpthread -lpcre2-posix -lpcre2-8'
	make install DESTDIR=${PWD} TEST_ARGS='-lformw -lmenuw -lpanelw -lncursesw -lticw -l%{soname_tinfo} -Wl,--as-needed' TEST_LIBS='-lutil -lpthread -lpcre2-posix -lpcre2-8'
%else
	make %{?_smp_mflags} TEST_ARGS='-lformw -lmenuw -lpanelw -lncursesw -lticw -l%{soname_tinfo} -Wl,--as-needed' TEST_LIBS='-lutil -lpthread'
	make install DESTDIR=${PWD} INSTALL_PROG=install TEST_ARGS='-lformw -lmenuw -lpanelw -lncursesw -lticw -l%{soname_tinfo} -Wl,--as-needed' TEST_LIBS='-lutil -lpthread'
%endif
	mv usr usr.back
	cp Makefile Makefile.back
	make distclean
    popd
%endif
%endif
    pushd tack/
        make install DESTDIR=%{root} INSTALL_PROG=install
    popd
    test ! -L tack || rm -f tack
    make clean
    #
    # Now use --without-pthread to disable pthread support (abi == 5).
    #
    > $SCREENLOG
    tail -q -s 0.5 -f $SCREENLOG & pid=$!

    eval screen -D -m ./${c#*./} --with-abi-version=5		\
				    --without-manpages		\
				    --without-progs		\
				    --without-tack		\
				    --without-pthread		\
				    --disable-reentrant		\
				    --disable-opaque-curses	\
				    --disable-opaque-form	\
				    --disable-opaque-menu	\
				    --disable-opaque-panel	\
				    --disable-ext-mouse		\
				    --disable-widec		\
				    --disable-wattr-macros	\
%if %{with usepcre2}
				    --without-pcre2		\
%endif
				    --with-termlib=tinfo	\
				    --with-ticlib=tic		\
%if %{with symversion}
				    --with-versioned-syms=${PWD}/package/ncurses.map \
%endif
				    --disable-ext-colors	\
				    --disable-overwrite		\
				    --without-progs
    sleep 1
    kill $pid
%if !0%{?_crossbuild}
    find -name fallback.o -print -delete
    cp fallback.c.build ncurses/fallback.c
%endif
    make depend
    make -C c++ etip.h
    make %{?_smp_mflags}
    sed -ri 's@^(LDFLAGS=)$@\1-L\\${libdir}@
	     s@^(libdir=).show_libdir@\1%{_libdir}/ncurses5@
	     s@^(includedir=).show_includedir@\1%{_incdir}/ncurses5@' misc/gen-pkgconfig
    # must not use %jobs here (would lead to: ln: ncurses.h already exists)
    make install.libs install.includes DESTDIR=%{root} includedir=%{_incdir}/ncurses5 includesubdir=/ncurses libdir=%{_libdir}/ncurses5
    ln -sf %{_incdir}/ncurses5/ncurses/{curses,ncurses,term}.h %{root}%{_incdir}/ncurses5/
    pushd man
	bash ../edit_man.sh normal installing %{root}%{_mandir} . ncurses5-config.1
    popd
    for pc in %{root}%{_libdir}/pkgconfig/*.pc
    do
	test -e "$pc" || break
	base=${pc%%.pc}
	base=${base##*/}
	sed -ri '\@includedir=@i\
includedir5=%{_incdir}/ncurses5' "$pc"
	sed -ri 's@^(includedir=).*@\1${includedir5}/ncurses@' "$pc"
	sed -ri 's@^(libdir=).*@\1%{_libdir}/ncurses5@' "$pc"
	sed -ri 's@^(Libs: )(.*)@\1-L${libdir}\2@' "$pc"
	mv -f $pc pc/${base}5.pc
	sed -ri 's@^(Cflags:.*)(-I.*)@\1-I${includedir5} \2@' pc/${base}5.pc
	sed -ri 's@^(Requires.private:).*@\1@'             pc/${base}5.pc
    done
    echo $PKG_CONFIG_PATH
    what=ncurses5
    cflags="$(pkg-config --cflags $what)"
      libs="$(pkg-config --libs   $what)"
    test -n "$cflags" -a -n "$libs" || exit 1
    bash %{S:6} --cflags "${cflags%%%% }" --libs "${libs%%%% }" %{root}%{_bindir}/${what}-config

    #
    # Now use --disable-widec for narrow character support.
    # The libs with 16 bit wide characters are binary incompatible
    # to the normal 8bit wide character libs.
    #
    make clean
    > $SCREENLOG
    tail -q -s 0.5 -f $SCREENLOG & pid=$!
    eval screen -D -m ./${c#*./} --with-pthread			\
				    --without-manpages		\
				    --without-progs		\
				    --without-tack		\
				    --enable-reentrant		\
				    --enable-opaque-curses	\
				    --enable-opaque-form	\
				    --enable-opaque-menu	\
				    --enable-opaque-panel	\
				    --enable-ext-mouse		\
				    --disable-widec		\
				    --disable-wattr-macros	\
				    --with-termlib=tinfo	\
				    --with-ticlib=tic		\
%if %{with symversion}
				    --with-versioned-syms=${PWD}/package/ncursest.map \
%endif
				    --enable-ext-colors		\
				    --disable-overwrite		\
				    --without-progs
    sleep 1
    kill $pid
%if !0%{?_crossbuild}
    find -name fallback.o -print -delete
    cp fallback.c.build ncurses/fallback.c
%endif
    make depend
    make -C c++ etip.h
    make %{?_smp_mflags}
    # must not use %jobs here (would lead to: ln: ncurses.h already exists)
    make install.libs install.includes DESTDIR=%{root} includedir=%{_incdir} includesubdir=/ncurses libdir=%{_libdir}
%if %{with onlytinfo}
    # This ensures that we get the libtinfo *with* _nc_read_entry2 symbol as well
    cp -p libtinfo.so.%{basevers}.back  %{root}%{_libdir}/libtinfo.so.%{basevers}
    cp -p libtinfow.so.%{basevers}.back %{root}%{_libdir}/libtinfow.so.%{basevers}
%endif
    pushd man
	bash ../edit_man.sh normal installing %{root}%{_mandir} . ncurses6-config.1
    popd
    mv -f %{root}%{_libdir}/pkgconfig/*.pc pc/
    sed -ri 's@^(Requires.private:).*@\1@' pc/*.pc
    echo $PKG_CONFIG_PATH
    what=ncurses
    cflags="$(pkg-config --cflags $what)"
      libs="$(pkg-config --libs   $what)"
    test -n "$cflags" -a -n "$libs" || exit 1
    bash %{S:6} --cflags "${cflags%%%% }" --libs "${libs%%%% }" %{root}%{_bindir}/${what}6-config

    #
    # Some tests
    #
%if 0%{?_crossbuild} || 0%{?suse_version} <= 1500
	echo "Skipping tests due to cross-building"
%else
    #
    # Make the test suite for ncurses6
    #
    pushd test
	CFLAGS="$CFLAGS -I%{root}%{_incdir}ncurses/ -I%{root}%{_incdir}/" \
	LDFLAGS="$LDFLAGS -Wl,-rpath-link=%{root}%{_libdir} -L%{root}%{_libdir}" \
	LIBS="$LDFLAGS" \
	./configure --with-ncurses --with-screen=ncurses --disable-widec --disable-wattr-macros --prefix=%{_prefix} --datadir=%{_datadir}/ncurses
	LD_LIBRARY_PATH=%{root}%{_libdir} \
%if %{with usepcre2}
	make %{?_smp_mflags} TEST_ARGS='-lform -lmenu -lpanel -lncurses -ltic -ltinfo -Wl,--as-needed' TEST_LIBS='-lutil -lpthread -lpcre2-posix -lpcre2-8'
	make install DESTDIR=${PWD} TEST_ARGS='-lform -lmenu -lpanel -lncurses -ltic -ltinfo -Wl,--as-needed' TEST_LIBS='-lutil -lpthread -lpcre2-posix -lpcre2-8'
%else
	make %{?_smp_mflags} TEST_ARGS='-lform -lmenu -lpanel -lncurses -ltic -ltinfo -Wl,--as-needed' TEST_LIBS='-lutil -lpthread'
	make install DESTDIR=${PWD} TEST_ARGS='-lform -lmenu -lpanel -lncurses -ltic -ltinfo -Wl,--as-needed' TEST_LIBS='-lutil -lpthread'
%endif
	rm -rf usr/
	make distclean
    popd
%endif
    test ! -L tack || rm -f tack
    make clean
    #
    # ABI == 5
    #
    > $SCREENLOG
    tail -q -s 0.5 -f $SCREENLOG & pid=$!

    #
    # Now use --without-pthread to disable pthread support (abi == 5).
    #
    eval screen -D -m ./${c#*./} --with-abi-version=5		\
				    --without-manpages		\
				    --without-progs		\
				    --without-tack		\
				    --without-pthread		\
				    --disable-reentrant		\
				    --disable-opaque-curses	\
				    --disable-opaque-form	\
				    --disable-opaque-menu	\
				    --disable-opaque-panel	\
				    --disable-ext-mouse		\
				    --enable-widec		\
				    --enable-wattr-macros	\
%if %{with usepcre2}
				    --without-pcre2		\
%endif
				    --with-termlib=%{soname_tinfo}	\
				    --with-ticlib=ticw		\
%if %{with symversion}
				    --with-versioned-syms=${PWD}/package/ncursesw.map \
%endif
				    --disable-ext-colors	\
				    --disable-overwrite		\
				    --without-progs
    sleep 1
    kill $pid
%if !0%{?_crossbuild}
    find -name fallback.o -print -delete
    cp fallback.c.build ncurses/fallback.c
%endif
    make depend
    make -C c++ etip.h
    make %{?_smp_mflags}
    sed -ri 's@^(LDFLAGS=)$@\1-L\\${libdir}@
	     s@^(libdir=).show_libdir@\1%{_libdir}/ncurses5@
	     s@^(includedir=).show_includedir@\1%{_incdir}/ncurses5/ncursesw@' misc/gen-pkgconfig
    # must not use %jobs here (would lead to: ln: ncurses.h already exists)
    make install.libs install.includes DESTDIR=%{root} includedir=%{_incdir}/ncurses5 includesubdir=/ncursesw libdir=%{_libdir}/ncurses5
%if %{with onlytinfo}
    gcc $CFLAGS $LDFLAGS -fPIC -shared -Wl,--auxiliary=libtinfo.so.5,-soname,libtinfow.so.5,-stats,-lc \
	-Wl,--version-script,package/ncursesw.map -o %{root}%{_libdir}/libtinfow.so.5.9
%endif
    pushd man
	bash ../edit_man.sh normal installing %{root}%{_mandir} . ncursesw5-config.1
    popd
    rm -vf %{root}%{_libdir}/pkgconfig/tic.pc
    rm -vf %{root}%{_libdir}/pkgconfig/tinfo.pc
    for pc in %{root}%{_libdir}/pkgconfig/*.pc
    do
	test -e "$pc" || break
	base=${pc%%.pc}
	base=${base##*/}
	sed -ri '\@includedir=@i\
includedir5=%{_incdir}/ncurses5' "$pc"
	sed -ri 's@^(includedir=).*@\1${includedir5}/ncursesw@' "$pc"
	sed -ri 's@^(libdir=).*@\1%{_libdir}/ncurses5@' "$pc"
	sed -ri 's@^(Libs: )(.*)@\1-L${libdir}\2@' "$pc"
	mv -f $pc pc/${base}5.pc
	sed -ri 's@^(Cflags:.*)(-I.*)@\1-I${includedir5} \2@' pc/${base}5.pc
	sed -ri 's@^(Requires.private:).*@\1@'             pc/${base}5.pc
    done
    echo $PKG_CONFIG_PATH
    what=ncursesw5
    cflags="$(pkg-config --cflags $what)"
      libs="$(pkg-config --libs   $what)"
    test -n "$cflags" -a -n "$libs" || exit 1
    bash %{S:6} --cflags "${cflags%%%% }" --libs "${libs%%%% }" %{root}%{_bindir}/${what}-config

%install
%if %{with usepcre2}
    pcre2="-lpcre2-posix -lpcre2-8"
%else
    pcre2=""
%endif
    PATH=$PWD/gzip:$PATH
    (cd %{root}/; tar -cpSf - *)|tar -xpsSf - -C %{buildroot}/
    rm -rf %{root}
    for model in libncurses libncursest libncursesw libncursestw libtinfo libtinfow libtic libticw
    do
	for lib in %{buildroot}%{_libdir}/${model}.so.* ; do
	    test   -e "${lib}" || continue
	    mv "${lib}" %{buildroot}%{_libdir}/ || continue
	done
	for lib in %{buildroot}%{_libdir}/${model}.so.6 ; do
	    test -e "${lib}" || continue
	    test -L "${lib}" || continue
	    lib=${lib#%{buildroot}}
	    lnk=%{buildroot}%{_libdir}/${model}.so
	    case "${lib##*/}" in
	    libncursesw*)
		rm -f ${lnk}
		echo '/* GNU ld script */'			>  ${lnk}
		echo "INPUT(${lib} AS_NEEDED(-l%{soname_tinfo} -ldl $pcre2))" >> ${lnk}
		;;
	    libncurses*)
		rm -f ${lnk}
		echo '/* GNU ld script */'			>  ${lnk}
		echo "INPUT(${lib} AS_NEEDED(-ltinfo -ldl $pcre2))" >> ${lnk}
		;;
	    *)	ln -sf ${lib} %{buildroot}%{_libdir}/${model}.so
	    esac
	done
    done
    /sbin/ldconfig -r %{buildroot}/ -n -v %{_libdir}
%if 0
    lnk=%{buildroot}%{_libdir}/libtermcap.so
    echo '/* GNU ld script */'		>  ${lnk}
    echo "INPUT(AS_NEEDED(-ltinfo))"	>> ${lnk}
%endif
    chmod 0755 %{buildroot}%{_libdir}/lib*.so.*
    chmod 0755 %{buildroot}%{_libdir}/lib*.so.*
    chmod a-x  %{buildroot}%{_libdir}/lib*.a
    if test -d %{buildroot}%{_libdir}/ncurses5 ; then
	mv %{buildroot}%{_libdir}/ncurses5/*.so.5*   %{buildroot}%{_libdir}/
	for lib in %{buildroot}%{_libdir}/ncurses5/*.so
	do
	    lnk=$lib
	    lib=%{_libdir}/${lib##*/}.5
	    case "${lib##*/}" in
	    libncursesw*)
		rm -f "${lnk}"
		echo '/* GNU ld script */'		>  ${lnk}
		echo "INPUT(${lib} AS_NEEDED(-l%{soname_tinfo}))">> ${lnk}
		;;
	    libncurses*)
		rm -f "${lnk}"
		echo '/* GNU ld script */'		>  ${lnk}
		echo "INPUT(${lib} AS_NEEDED(-ltinfo))"	>> ${lnk}
		;;
	    libtinfo*)
		test -L "${lnk}" || continue
		ln -sf ${lib} ${lnk}
		;;
	    *)
		test -L "${lnk}" || continue
		ln -sf ../${lib##*/} ${lnk}
	    esac
	done
	for model in libncurses libncursest libncursesw libncursestw libtinfo libtinfow libtic libticw
	do
	    for lib in %{buildroot}%{_libdir}/${model}.so.* ; do
		test   -e "${lib}" || continue
		mv "${lib}" %{buildroot}%{_libdir}/ || continue
	    done
	    for lib in %{buildroot}%{_libdir}/${model}.so.5 ; do
		test -e "${lib}" || continue
		test -L "${lib}" || continue
		lib=${lib#%{buildroot}}
		lnk=%{buildroot}%{_libdir}/ncurses5/${model}.so
		case "${lib##*/}" in
		libncursesw*)
		    rm -f ${lnk}
		    echo '/* GNU ld script */'		    >  ${lnk}
		    echo 'SEARCH_DIR(%{_libdir}/ncurses5)'  >> ${lnk}
		    echo "INPUT(${lib} AS_NEEDED(-l%{soname_tinfo}))">> ${lnk}
		    ;;
		libncurses*)
		    rm -f ${lnk}
		    echo '/* GNU ld script */'		    >  ${lnk}
		    echo 'SEARCH_DIR(%{_libdir}/ncurses5)'  >> ${lnk}
		    echo "INPUT(${lib} AS_NEEDED(-ltinfo))" >> ${lnk}
		    ;;
		*)  ln -sf ${lib} %{buildroot}%{_libdir}/ncurses5/${model}.so
	    esac
	    done
	done
	chmod 0755 %{buildroot}%{_libdir}/lib*.so.5*
	chmod 0755 %{buildroot}%{_libdir}/lib*.so.5*
	chmod a-x  %{buildroot}%{_libdir}/ncurses5/lib*.a
    fi
    test -n "%{buildroot}" || ldconfig -N
    mkdir -p %{buildroot}%{_defaultdocdir}/ncurses
    bzip2 -c misc/terminfo.src > misc/terminfo.src.bz2
    install -m 644 misc/terminfo.src.bz2	%{buildroot}%{_defaultdocdir}/ncurses/
    install -m 644 doc/html/*.html		%{buildroot}%{_defaultdocdir}/ncurses/
    bzip2 doc/ncurses-intro.doc -c > doc/ncurses-intro.txt.bz2
    install -m 644 doc/ncurses-intro.txt.bz2	%{buildroot}%{_defaultdocdir}/ncurses/
    bzip2 doc/hackguide.doc -c > doc/hackguide.txt.bz2
    install -m 644 doc/hackguide.txt.bz2	%{buildroot}%{_defaultdocdir}/ncurses/
    install -m 644 %{S:3}			%{buildroot}%{_defaultdocdir}/ncurses/
    install -m 644 README			%{buildroot}%{_defaultdocdir}/ncurses/
    install -m 644 NEWS				%{buildroot}%{_defaultdocdir}/ncurses/
    mkdir -p %{buildroot}%{_sysconfdir}/terminfo
    mkdir -p %{buildroot}%{_miscdir}
    pushd ncurses/
	. ${PWD}/../.build_tic
	{ echo "# See annotated version in %{_defaultdocdir}/ncurses/terminfo.src.bz2"
	$BUILD_TIC -C -r ../misc/terminfo.src | grep -E -v '^#'; } > termcap
	# Gererate new termcap entries for various linux consoles
	TERMCAP=termcap \
	TERMINFO=%{buildroot}%{_datadir}/terminfo \
	    bash %{SOURCE2}
	install -m 0644 termcap.new %{buildroot}%{_miscdir}/termcap
	unset LD_LIBRARY_PATH
    popd
    if test `%{_bindir}/id -u` = '0' ; then
	chown root:root %{buildroot}%{_miscdir}/termcap
	chmod 0644      %{buildroot}%{_miscdir}/termcap
    fi
    ln -sf %{_miscdir}/termcap %{buildroot}%{_sysconfdir}/termcap
    (cat > default.list) <<-EOF
	%{tabset std}
	%{tabset stdcrt}
	%{tabset vt100}
	%{tabset vt300}
	%{terminfo a/ansi}
	%{terminfo a/arpanet}
	%{terminfo d/dumb}
	%{terminfo d/dialup}
	%{terminfo f/foot}
	%{terminfo g/gnome}
	%{terminfo g/gnome-rh72}
	%{terminfo g/gnome-rh80}
	%{terminfo g/gnome-rh90}
	%{terminfo g/gnome-fc5}
	%{terminfo i/ibm327x}
	%{terminfo k/klone+color}
	%{terminfo k/konsole}
	%{terminfo k/konsole-256color}
	%{terminfo k/kvt}
	%{terminfo k/kvt-rh}
	%{terminfo l/linux}
	%{terminfo l/linux-m}
	%{terminfo l/linux-nic}
	%{terminfo m/mlterm}
	%{terminfo n/net}
	%{terminfo n/network}
	%{terminfo n/nxterm}
	%{terminfo p/patch}
	%{terminfo r/rxvt}
	%{terminfo r/rxvt-basic}
	%{terminfo r/rxvt-color}
	%{terminfo r/rxvt-256color}
	%{terminfo r/rxvt-unicode}
	%{terminfo r/rxvt-unicode-256color}
	%{terminfo s/screen+fkeys}
	%{terminfo s/screen}
	%{terminfo s/screen-16color}
	%{terminfo s/screen-256color}
	%{terminfo s/screen-bce}
	%{terminfo s/screen-w}
	%{terminfo s/sun}
	%{terminfo s/switch}
	%{terminfo u/unknown}
	%{terminfo v/vt100}
	%{terminfo v/vt102}
	%{terminfo v/vt220}
	%{terminfo v/vt220-8}
	%{terminfo v/vt220-8bit}
	%{terminfo v/vt320}
	%{terminfo v/vt52}
	%{terminfo v/vte}
	%{terminfo x/xterm}
	%{terminfo x/xterm-color}
	%{terminfo x/xterm-256color}
	%{terminfo x/xterm-basic}
	%{terminfo x/xterm-nic}
	%{terminfo x/xterm-r6}
	EOF
# Better screen support and workaround about missing terminfo entries
# might be help on boo#812067 as well as on boo#935736 but may cause
# boo#940459  (which should be fixed by screen its self!)
    rm -vf  %{buildroot}%{terminfo s/screen.xterm}
    (cat > screen.list) <<-EOF
	%{terminfo s/screen.gnome}
	%{terminfo s/screen.konsole}
	%{terminfo s/screen.linux}
	EOF
    (cat > iterm.list) <<-EOF
	%{terminfo i/iTerm.app}
	%{terminfo i/iTerm2.app}
	%{terminfo i/iterm}
	%{terminfo i/iterm2}
	EOF
    find %{buildroot}%{tabset ""} %{buildroot}%{terminfo ""} \
	\( -type f -or -type l \) | \
	sed "s@^%{buildroot}@@g" | \
	grep -v -F -x -f default.list -f screen.list -f iterm.list \
	> extension.list
#
# Remove backward compatibilty link if any
#
    rm -f %{buildroot}%{_prefix}/lib/terminfo
#
# Store pkg-config files
#
    cp -p pc/*.pc %{buildroot}%{_libdir}/pkgconfig/

#
# Install test binaries and, if exists, the manual pages
#
pushd test
    mv usr.back usr
    mkdir -p ./%{_mandir}/man6
    cp -p $(find -name '*.6') .%{_mandir}/man6/
    (cd usr/; tar -cpSf - .) | tar -xpsSf - -C %{buildroot}%{_prefix}
    install -m 0755 %{S:8} %{buildroot}%{_libexecdir}/ncurses-examples/
popd

%if 0%{?_crossbuild}
# No test here
%else

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export LD_LIBRARY_PATH
nm -D %{buildroot}%{_libdir}/libncursesw.so.%{basevers} | grep -q in_wch
%if %{with onlytinfo}
nm -D %{buildroot}%{_libdir}/libtinfo.so.%{basevers} | grep -q _nc_read_entry2
%endif
%if 0%{?suse_version} > 1500
pushd test
    expect -d <<-'EOF'
	set env(TERM) xterm
	set timeout 20
	spawn -noecho ".%{_libexecdir}/ncurses-examples/newdemo"
	send -- "x"
	sleep 5
	send -- "x"
	sleep 5
	send -- "x"
	sleep 5
	send -- "q"
	wait -nowait
	EOF
popd
%endif
%endif

%post   -n libncurses5 -p /sbin/ldconfig

%postun -n libncurses5 -p /sbin/ldconfig

%post   -n libncurses6 -p /sbin/ldconfig

%postun -n libncurses6 -p /sbin/ldconfig

%files -n terminfo-base -f default.list
%defattr(-,root,root)
%{_sysconfdir}/termcap
%config %{_miscdir}/termcap
%dir %{_sysconfdir}/terminfo
%dir %{_datadir}/tabset/
%dir %{_datadir}/terminfo/
%dir %{_datadir}/terminfo/*/

%files -n terminfo-screen -f screen.list
%defattr(-,root,root)
%dir %{_datadir}/terminfo/

%files -n terminfo-iterm -f iterm.list
%defattr(-,root,root)
%dir %{_datadir}/terminfo/

%files -n ncurses-utils
%defattr(-,root,root)
%{_bindir}/clear
%{_bindir}/infocmp
%{_bindir}/reset
%{_bindir}/tabs
%{_bindir}/toe
%{_bindir}/tput
%{_bindir}/tset
%doc %{_mandir}/man1/clear.1%{ext_man}
%doc %{_mandir}/man1/infocmp.1%{ext_man}
%doc %{_mandir}/man1/reset.1%{ext_man}
%doc %{_mandir}/man1/tabs.1%{ext_man}
%doc %{_mandir}/man1/toe.1%{ext_man}
%doc %{_mandir}/man1/tput.1%{ext_man}
%doc %{_mandir}/man1/tset.1%{ext_man}
%doc %{_mandir}/man5/*%{ext_man}
%doc AUTHORS

%files -n ncurses-examples
%defattr(-,root,root)
%{_bindir}/ncurses-examples
%dir %{_libexecdir}/ncurses-examples/
%{_libexecdir}/ncurses-examples/*
%dir %{_datadir}/ncurses/
%{_datadir}/ncurses/*
%doc %{_mandir}/man6/*%{ext_man}

%files -n libncurses5
%defattr(-,root,root)
%{_libdir}/lib*.so.5*

%files -n libncurses6
%defattr(-,root,root)
%{_libdir}/lib*.so.6*

%files -n ncurses-devel
%defattr(-,root,root)
%dir %{_defaultdocdir}/ncurses/
%doc %{_defaultdocdir}/ncurses/*
%{_bindir}/ncurses*6-config
%{_bindir}/captoinfo
%{_bindir}/infotocap
%{_bindir}/tic
%dir %{_incdir}/ncurses/
%dir %{_incdir}/ncursesw/
%{_incdir}/*.h
%{_incdir}/ncurses/*.h
%{_incdir}/ncursesw/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*[clmosuw\+].pc
%doc %{_mandir}/man1/ncurses*6-config.1%{ext_man}
%doc %{_mandir}/man1/captoinfo.1%{ext_man}
%doc %{_mandir}/man1/infotocap.1%{ext_man}
%doc %{_mandir}/man1/tic.1%{ext_man}
%doc %{_mandir}/man3/*%{ext_man}
%doc %{_mandir}/man7/*%{ext_man}

%files -n ncurses-devel-static
%{_libdir}/lib*.a

%files -n ncurses5-devel
%defattr(-,root,root)
%{_bindir}/ncurses*5-config
%dir %{_incdir}/ncurses5/
%dir %{_incdir}/ncurses5/ncurses/
%dir %{_incdir}/ncurses5/ncursesw/
%{_incdir}/ncurses5/*.h
%{_incdir}/ncurses5/ncurses/*.h
%{_incdir}/ncurses5/ncursesw/*.h
%dir %{_libdir}/ncurses5/
%{_libdir}/ncurses5/lib*.so
%{_libdir}/pkgconfig/*5.pc
%doc %{_mandir}/man1/ncurses*5-config.1%{ext_man}

%files -n ncurses5-devel-static
%{_libdir}/ncurses5/lib*.a

%files -n tack
%defattr(-,root,root)
%{_bindir}/tack
%doc %{_mandir}/man1/tack.1%{ext_man}

%files -f extension.list -n terminfo
%defattr(-,root,root)

%changelog
