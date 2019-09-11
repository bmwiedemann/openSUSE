#
# spec file for package readline
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           readline
BuildRequires:  autoconf
BuildRequires:  fdupes
%if %suse_version > 1220
BuildRequires:  makeinfo
%endif
BuildRequires:  ncurses-devel
BuildRequires:  patchutils
BuildRequires:  pkg-config
BuildRequires:  sed
%define         rextend %nil
Version:        8.0
Release:        0
Summary:        The readline library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            http://www.gnu.org/software/readline/
# Git:          http://git.savannah.gnu.org/cgit/bash.git
Source0:        ftp://ftp.gnu.org/gnu/readline/readline-%{version}%{rextend}.tar.gz
Source1:        readline-%{version}-patches.tar.bz2
Source2:        baselibs.conf
Patch0:         readline-%{version}.dif
Patch1:         readline-6.3-input.dif
Patch2:         readline-5.2-conf.patch
Patch3:         readline-6.2-metamode.patch
Patch5:         readline-6.2-xmalloc.dif
Patch6:         readline-6.3-destdir.patch
Patch7:         readline-6.3-rltrace.patch
Patch8:         readline-7.0-screen.patch
%{expand:       %%global rl_major %(echo %{version} | sed -r 's/.[0-9]+//g')}

%description
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package -n libreadline8
Summary:        The Readline Library
Group:          System/Libraries
Provides:       bash:/%{_lib}/libreadline.so.%{rl_major}
Recommends:     readline-doc = %{version}
Provides:       readline =  %{version}
Obsoletes:      readline <= 6.3

%description -n libreadline8
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package devel
Summary:        Development files for readline
Group:          Development/Libraries/C and C++
Requires:       libreadline8 = %{version}
Requires:       ncurses-devel
Recommends:     readline-doc = %{version}

%description devel
This package contains the header files for the readline library.

%package devel-static
Summary:        Static library for development with readline
Group:          Development/Libraries/C and C++
Requires:       ncurses-devel
Requires:       readline-devel = %{version}
Recommends:     readline-doc = %{version}

%description devel-static
This package contains the static library for the readline library.

%package doc
Summary:        Documentation how to Use and Program with the Readline Library
Group:          Documentation/Other
Provides:       readline:%{_infodir}/readline.info.gz
PreReq:         %install_info_prereq
BuildArch:      noarch

%description doc
This package contains the documentation for using the readline library
as well as programming with the interface of the readline library.

%prep
%setup -q -n readline-%{version}%{rextend} -b1
for patch in ../readline-%{version}-patches/*; do
    test -e $patch || break
    let level=0 || true
    file=$(lsdiff --files=1 $patch)
    if test ! -e $file ; then
	file=${file#*/}
	let level++ || true
    fi
    sed -ri '/^\*\*\* \.\./{ s@\.\./readline-%{version}[^/]*/@@ }' $patch
    echo Patch $patch
    patch -s -p$level < $patch
done
%patch1 -p2 -b .zerotty
%patch2 -p2 -b .conf
%patch3 -p2 -b .metamode
%patch5 -p0 -b .xm
%patch6 -p0 -b .destdir
%patch7 -p2 -b .tmp
%patch8 -p2 -b .screen
%patch0 -p0 -b .0

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
LANG=POSIX
LC_ALL=$LANG
unset LC_CTYPE
autoconf
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
(cat > dyn.map)<<-'EOF'
	{
	    *;
	    !rl_*stream;
	};
	EOF
(cat > rl.map)<<-'EOF'
	READLINE_6.3 {
	    rl_change_environment;
	    rl_clear_history;
	    rl_executing_key;
	    rl_executing_keyseq;
	    rl_filename_stat_hook;
	    rl_history_substr_search_backward;
	    rl_history_substr_search_forward;
	    rl_input_available_hook;
	    rl_print_last_kbd_macro;
	    rl_signal_event_hook;
	};
	EOF
CFLAGS="%{optflags} $LARGEFILE -D_GNU_SOURCE -D_RPM_OPT_FLAGS -g"
LDFLAGS=""
cflags -Wuninitialized         CFLAGS
cflags -Wextra                 CFLAGS
cflags -Wno-unprototyped-calls CFLAGS
cflags -Wno-switch-enum        CFLAGS
cflags -Wno-unused-variable    CFLAGS
cflags -Wno-unused-parameter   CFLAGS
cflags -Wno-parentheses        CFLAGS
cflags -ftree-loop-linear      CFLAGS
cflags -pipe                   CFLAGS
cflags -Wl,--as-needed         LDFLAGS
cflags -Wl,-O2                 LDFLAGS
cflags -Wl,--version-script=${PWD}/rl.map   LDFLAGS
cflags -Wl,--dynamic-list=${PWD}/dyn.map    LDFLAGS
CC=gcc
CC_FOR_BUILD="$CC"
CFLAGS_FOR_BUILD="$CFLAGS"
LDFLAGS_FOR_BUILD="$LDFLAGS"
export CC_FOR_BUILD CFLAGS_FOR_BUILD LDFLAGS_FOR_BUILD CFLAGS LDFLAGS CC
./configure --build=%{_target_cpu}-suse-linux	\
	--enable-static			\
	--enable-shared			\
	--enable-multibyte		\
	--prefix=%{_prefix}		\
	--with-curses			\
	--mandir=%{_mandir}		\
	--infodir=%{_infodir}		\
	--docdir=%{_docdir}/%{name}	\
	--libdir=%{_libdir}
make
make documentation

%install
%make_install htmldir=%{_docdir}/%{name} installdir=%{_docdir}/%{name}/examples \
	      libdir=/%{_lib} linkagedir=%{_libdir}
chmod 0755 %{buildroot}/%{_lib}/libhistory.so.%{version}
chmod 0755 %{buildroot}/%{_lib}/libreadline.so.%{version}
rm -vf %{buildroot}/%{_lib}/libhistory.so.%{version}*old
rm -vf %{buildroot}/%{_lib}/libreadline.so.%{version}*old
rm -vf %{buildroot}/%{_lib}/libhistory.so
rm -vf %{buildroot}/%{_lib}/libreadline.so
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
ln -sf /%{_lib}/libhistory.so.%{version}  %{buildroot}/%{_libdir}/libhistory.so
ln -sf /%{_lib}/libreadline.so.%{version} %{buildroot}/%{_libdir}/libreadline.so
mv -vf %{buildroot}/%{_lib}/libhistory.a  %{buildroot}/%{_libdir}/libhistory.a
mv -vf %{buildroot}/%{_lib}/libreadline.a %{buildroot}/%{_libdir}/libreadline.a 
mv -vf %{buildroot}/%{_lib}/pkgconfig/readline.pc \
					  %{buildroot}/%{_libdir}/pkgconfig/readline.pc
rm -vrf %{buildroot}%{_datadir}/readline/

%post -n libreadline8 -p /sbin/ldconfig

%postun -n libreadline8 -p /sbin/ldconfig

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/history.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/readline.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/rluserman.info.gz

%preun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/history.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/readline.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/rluserman.info.gz

%files -n libreadline8
%license COPYING
/%{_lib}/libhistory.so.%{rl_major}
/%{_lib}/libhistory.so.%{version}
/%{_lib}/libreadline.so.%{rl_major}
/%{_lib}/libreadline.so.%{version}

%files devel
%{_includedir}/readline/
%{_libdir}/libhistory.so
%{_libdir}/libreadline.so
%{_libdir}/pkgconfig/readline.pc

%files devel-static
%{_libdir}/libhistory.a
%{_libdir}/libreadline.a

%files doc
%doc %{_infodir}/history.info*
%doc %{_infodir}/readline.info*
%doc %{_infodir}/rluserman.info*
%doc %{_mandir}/man3/history.3*
%doc %{_mandir}/man3/readline.3*
%doc %{_docdir}/%{name}/

%changelog
