#
# spec file for package readline6
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


Name:           readline6
BuildRequires:  audit-devel
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  patchutils
BuildRequires:  screen
BuildRequires:  sed
%define         rl_vers   6.3
Version:        %{rl_vers}
Release:        0
Summary:        The Readline Library
License:        GPL-3.0-or-later
Group:          System/Shells
URL:            http://www.gnu.org/software/bash/bash.html
# Git:          http://git.savannah.gnu.org/cgit/bash.git
Source0:        ftp://ftp.gnu.org/gnu/readline/readline-%{rl_vers}.tar.gz
Source1:        readline-%{rl_vers}-patches.tar.bz2
Source2:        baselibs.conf
Patch20:        readline-%{rl_vers}.dif
Patch21:        readline-6.3-input.dif
Patch22:        readline-6.1-wrap.patch
Patch23:        readline-5.2-conf.patch
Patch24:        readline-6.2-metamode.patch
Patch25:        readline-6.2-endpw.dif
Patch27:        readline-6.2-xmalloc.dif
Patch30:        readline-6.3-destdir.patch
Patch31:        readline-6.3-rltrace.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _sysconfdir /etc
%global         _incdir     %{_includedir}
%global         _ldldir     /%{_lib}/bash
%global         _minsh      0
%{expand:       %%global rl_major %(echo %{rl_vers} | sed -r 's/.[0-9]+//g')}

%description
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package -n libreadline6
Summary:        The Readline Library
Group:          System/Libraries
Provides:       bash:/%{_lib}/libreadline.so.%{rl_major}
Provides:       readline =  %{rl_vers}
Obsoletes:      readline <= 6.2

%description -n libreadline6
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package -n readline6-devel
Summary:        Development files for the readline library version 6
Group:          Development/Libraries/C and C++
Provides:       bash:%{_libdir}/libreadline.a
Version:        %{rl_vers}
Release:        0
Requires:       libreadline6 = %{rl_vers}
Requires:       ncurses-devel

%description -n readline6-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n readline-%{rl_vers}
typeset -i level
pushd ../readline-%{rl_vers}
for patch in ../readline-%{rl_vers}-patches/*; do
    test -e $patch || break
    let level=0 || true
    file=$(lsdiff --files=1 $patch)
    if test ! -e $file ; then
	file=${file#*/}
	let level++ || true
    fi
    sed -ri '/^\*\*\* \.\./{ s@\.\./readline-%{rl_vers}[^/]*/@@ }' $patch
    echo Patch $patch
    patch -s -p$level < $patch
done
%patch21 -p2 -b .zerotty
%patch22 -p2 -b .wrap
%patch23 -p2 -b .conf
%patch24 -p2 -b .metamode
#%patch25 -p2 -b .endpw
%patch31 -p2 -b .tmp
%patch27 -p0 -b .xm
%patch30 -p0 -b .destdir
%patch20 -p0 -b .0

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
  cflags -Wl,-rpath,%{_ldldir}/%{bash_vers}   LDFLAGS
  cflags -Wl,--version-script=${PWD}/rl.map   LDFLAGS
  cflags -Wl,--dynamic-list=${PWD}/dyn.map    LDFLAGS
  CC=gcc
  CC_FOR_BUILD="$CC"
  CFLAGS_FOR_BUILD="$CFLAGS"
  LDFLAGS_FOR_BUILD="$LDFLAGS"
  export CC_FOR_BUILD CFLAGS_FOR_BUILD LDFLAGS_FOR_BUILD CFLAGS LDFLAGS CC
  ./configure --build=%{_target_cpu}-suse-linux	\
	--disable-static		\
	--prefix=%{_prefix}		\
	--with-curses			\
	--mandir=%{_mandir}		\
	--infodir=%{_infodir}		\
	--docdir=%{_defaultdocdir}/readline	\
	--libdir=%{_libdir}
  make
  make documentation

%install
%if 0%{?suse_version} < 1550
  make install-shared libdir=/%{_lib} linkagedir=%{_libdir} DESTDIR=%{buildroot}
  chmod 0755 %{buildroot}/%{_lib}/libhistory.so.%{rl_vers}
  chmod 0755 %{buildroot}/%{_lib}/libreadline.so.%{rl_vers}
  rm -vf %{buildroot}/%{_lib}/libhistory.so.%{rl_vers}*old
  rm -vf %{buildroot}/%{_lib}/libreadline.so.%{rl_vers}*old
  rm -vf %{buildroot}/%{_lib}/libhistory.so
  rm -vf %{buildroot}/%{_lib}/libreadline.so
  mkdir -p  %{buildroot}/%{_libdir}/readline6
  ln -sf /%{_lib}/libhistory.so.%{rl_vers}  %{buildroot}/%{_libdir}/readline6/libhistory.so
  ln -sf /%{_lib}/libreadline.so.%{rl_vers} %{buildroot}/%{_libdir}/readline6/libreadline.so
%else
  make install-shared libdir=%{_libdir} linkagedir=%{_libdir} DESTDIR=%{buildroot}
  chmod 0755 %{buildroot}%{_libdir}/libhistory.so.%{rl_vers}
  chmod 0755 %{buildroot}%{_libdir}/libreadline.so.%{rl_vers}
  rm -vf %{buildroot}%{_libdir}/libhistory.so.%{rl_vers}*old
  rm -vf %{buildroot}%{_libdir}/libreadline.so.%{rl_vers}*old
  rm -vf %{buildroot}%{_libdir}/libhistory.so
  rm -vf %{buildroot}%{_libdir}/libreadline.so
  mkdir -p  %{buildroot}%{_libdir}/readline6
  ln -sf %{_libdir}/libhistory.so.%{rl_vers}  %{buildroot}/%{_libdir}/readline6/libhistory.so
  ln -sf %{_libdir}/libreadline.so.%{rl_vers} %{buildroot}/%{_libdir}/readline6/libreadline.so
%endif
  rm -fv %{buildroot}%{_mandir}/man3/history.3*
  rm -fv %{buildroot}%{_defaultdocdir}/readline/INSTALL
  mv %{buildroot}%{_mandir}/man3/readline.3 %{buildroot}%{_mandir}/man3/readline6.3
  mv %{buildroot}%{_incdir}/readline %{buildroot}%{_incdir}/readline6
  rm -rf %{buildroot}%{_infodir}
  rm -rf %{buildroot}%{_defaultdocdir}/readline

%post -n libreadline6 -p /sbin/ldconfig

%postun -n libreadline6 -p /sbin/ldconfig

%clean
LD_LIBRARY_PATH=%{buildroot}/%{_lib} \
ldd -u -r %{buildroot}/bin/bash || true
ldd -u -r %{buildroot}/%{_lib}/libreadline.so.* || true
%{?buildroot: %{__rm} -rf %{buildroot}}

%files -n libreadline6
%defattr(-,root,root)
%if %{defined license}
%license COPYING
%else
%doc COPYING
%endif
%if 0%{?suse_version} < 1550
/%{_lib}/libhistory.so.%{rl_major}
/%{_lib}/libhistory.so.%{rl_vers}
/%{_lib}/libreadline.so.%{rl_major}
/%{_lib}/libreadline.so.%{rl_vers}
%else
%{_libdir}/libhistory.so.%{rl_major}
%{_libdir}/libhistory.so.%{rl_vers}
%{_libdir}/libreadline.so.%{rl_major}
%{_libdir}/libreadline.so.%{rl_vers}
%endif

%files -n readline6-devel
%defattr(-,root,root)
%dir %{_incdir}/readline6/
%{_incdir}/readline6/*
%dir %{_libdir}/readline6/
%{_libdir}/readline6/libhistory.so
%{_libdir}/readline6/libreadline.so
%doc %{_mandir}/man3/readline6.3.gz

%changelog
