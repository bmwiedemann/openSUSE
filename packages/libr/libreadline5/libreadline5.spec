#
# spec file for package libreadline5
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


Name:           libreadline5
%define         rl_vers   5.2
Provides:       bash:/%{_lib}/libreadline.so.5
Version:        5.2
Release:        0
Summary:        The Readline Library
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            http://www.gnu.org/software/bash/bash.html
Source0:        readline-%{rl_vers}.tar.bz2
Source1:        readline-%{rl_vers}-patches.tar.bz2
Source2:        baselibs.conf
Patch20:        readline-%{rl_vers}.dif
Patch21:        readline-4.3-input.dif
Patch22:        readline-5.2-wrap.patch
Patch23:        readline-5.2-conf.patch
Patch30:        readline-5.1-destdir.patch
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _sysconfdir /etc
%global         _incdir     %{_includedir}
%if !%{defined ext_man}
%global         ext_man	    .gz
%endif

%description
The readline library is used by the Bourne Again Shell (bash, the
standard command interpreter) for easy editing of command lines.  This
includes history and search functionality.

%package -n readline5-devel
Summary:        Development files for the readline library version 5
Group:          Development/Libraries/C and C++
Provides:       bash:%{_libdir}/libreadline.a
Version:        5.2
Release:        0
Requires:       libreadline5 = %{version}
Requires:       ncurses-devel
Conflicts:      readline-devel

%description -n readline5-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n readline-%{rl_vers}
for p in ../readline-%{rl_vers}-patches/*; do
    test -e $p || break
    echo Patch $p
    patch -s -p0 < $p
done
%patch21 -p0 -b .zerotty
%patch22 -p0 -b .wrap
%patch23 -p0 -b .conf
%patch30 -p0 -b .destdir
%patch20 -p0

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
  autoconf
  cflags ()
  {
      local flag=$1; shift
      case "${RPM_OPT_FLAGS}" in
      *${flag}*) return
      esac
      if test -n "$1" && gcc -Werror $flag -S -o /dev/null -xc   /dev/null > /dev/null 2>&1 ; then
	  local var=$1; shift
	  eval $var=\${$var:+\$$var\ }$flag
      fi
  }
  echo 'int main () { return !(sizeof(void*) >= 8); }' | gcc -x c -o test64 -
  if ./test64 ; then
      LARGEFILE=""
  else
      LARGEFILE="-D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64"
  fi
  rm -f ./test64
  CFLAGS="$RPM_OPT_FLAGS $LARGEFILE -D_GNU_SOURCE -DRECYCLES_PIDS -Wall -g"
  LDFLAGS=""
  cflags -std=gnu89              CFLAGS
  cflags -Wuninitialized         CFLAGS
  cflags -Wextra                 CFLAGS
  cflags -Wno-unprototyped-calls CFLAGS
  cflags -Wno-switch-enum        CFLAGS
  cflags -ftree-loop-linear      CFLAGS
  cflags -pipe                   CFLAGS
  cflags -Wl,--as-needed         LDFLAGS
  cflags -Wl,-O,2                LDFLAGS
  CC=gcc
  CC_FOR_BUILD="$CC"
  CFLAGS_FOR_BUILD="$CFLAGS"
  LDFLAGS_FOR_BUILD="$LDFLAGS"
  export CC_FOR_BUILD CFLAGS_FOR_BUILD LDFLAGS_FOR_BUILD CFLAGS LDFLAGS CC
  ./configure --build=%{_target_cpu}-suse-linux	\
	--prefix=%{_prefix}			\
	--with-curses			\
	--mandir=%{_mandir}		\
	--infodir=%{_infodir}		\
	--libdir=%{_libdir}
  make
  make documentation
  ln -sf shlib/libreadline.so.%{rl_vers} libreadline.so
  ln -sf shlib/libreadline.so.%{rl_vers} libreadline.so.5
  ln -sf shlib/libhistory.so.%{rl_vers} libhistory.so
  ln -sf shlib/libhistory.so.%{rl_vers} libhistory.so.5

%install
  make install htmldir=%{_defaultdocdir}/readline DESTDIR=%{buildroot}
%if 0%{?suse_version} < 1550
  make install-shared libdir=/%{_lib} linkagedir=%{_libdir} DESTDIR=%{buildroot}
  rm -rf %{buildroot}%{_defaultdocdir}/bash
  rm -rf %{buildroot}%{_defaultdocdir}/readline
  chmod 0755 %{buildroot}/%{_lib}/libhistory.so.%{rl_vers}
  chmod 0755 %{buildroot}/%{_lib}/libreadline.so.%{rl_vers}
  rm -f %{buildroot}/%{_lib}/libhistory.so.%{rl_vers}*old
  rm -f %{buildroot}/%{_lib}/libreadline.so.%{rl_vers}*old
  # remove unpackaged files
  rm -fv %{buildroot}%{_libdir}/libhistory.so.*
  rm -fv %{buildroot}%{_libdir}/libreadline.so.*
%else
  make install-shared libdir=%{_libdir} linkagedir=%{_libdir} DESTDIR=%{buildroot}
  rm -rf %{buildroot}%{_defaultdocdir}/bash
  rm -rf %{buildroot}%{_defaultdocdir}/readline
  chmod 0755 %{buildroot}%{_libdir}/libhistory.so.%{rl_vers}
  chmod 0755 %{buildroot}%{_libdir}/libreadline.so.%{rl_vers}
  rm -f %{buildroot}%{_libdir}/libhistory.so.%{rl_vers}*old
  rm -f %{buildroot}%{_libdir}/libreadline.so.%{rl_vers}*old
%endif
  # remove unpackaged files
  rm -fv %{buildroot}%{_mandir}/man3/history.3*
  rm -fv %{buildroot}%{_infodir}/*.info*
  rm -rfv %{buildroot}%{_infodir}/dir

#
# Make sure not to be broken
#
mv %{buildroot}%{_incdir}/readline %{buildroot}%{_incdir}/readline5
mkdir %{buildroot}%{_libdir}/readline5
for lib in %{buildroot}%{_libdir}/lib*.{a,so}
do
  mv $lib %{buildroot}%{_libdir}/readline5/
done
mv %{buildroot}%{_mandir}/man3/readline.3 %{buildroot}%{_mandir}/man3/readline5.3

%post -n libreadline5 -p /sbin/ldconfig

%postun -n libreadline5 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%if %{defined license}
%license COPYING
%else
%doc COPYING
%endif
%if 0%{?suse_version} < 1550
/%{_lib}/libhistory.so.5
/%{_lib}/libhistory.so.%{rl_vers}
/%{_lib}/libreadline.so.5
/%{_lib}/libreadline.so.%{rl_vers}
%else
%{_libdir}/libhistory.so.5
%{_libdir}/libhistory.so.%{rl_vers}
%{_libdir}/libreadline.so.5
%{_libdir}/libreadline.so.%{rl_vers}
%endif

%files -n readline5-devel
%defattr(-,root,root)
%dir %{_incdir}/readline5/
%{_incdir}/readline5/*
%dir %{_libdir}/readline5/
%{_libdir}/readline5/libhistory.a
%{_libdir}/readline5/libhistory.so
%{_libdir}/readline5/libreadline.a
%{_libdir}/readline5/libreadline.so
%doc %{_mandir}/man3/readline5.3%{ext_man}

%changelog
