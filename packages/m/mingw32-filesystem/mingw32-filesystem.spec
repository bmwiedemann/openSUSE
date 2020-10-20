#
# spec file for package mingw32-filesystem
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define debug_package %{nil}
%define _rpmlibdir    %{_prefix}/lib/rpm
Name:           mingw32-filesystem
Version:        20201017
Release:        0
Summary:        MinGW base filesystem and environment
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
Url:            http://hg.et.redhat.com/misc/fedora-mingw--devel/
Source0:        COPYING
Source1:        macros.mingw32
Source2:        mingw32.sh
Source3:        mingw32-find-debuginfo.sh
Source4:        mingw32-find-requires.sh
Source5:        mingw32-find-provides.sh
Source6:        mingw32-scripts.sh
Source7:        mingw32-rpmlintrc
Source8:        mingw32-install-post.sh
Source9:        mingw32-find-lang.sh
Source10:       languages
Source11:       languages.man
Source12:       mingw32-cmake.prov
Source13:       mingw32-cmake.attr
Source14:       macros.mingw32-cmake
Provides:       mingw32(dbghelp.dll)
Provides:       mingw32(mpr.dll)
Provides:       mingw32(odbccp32.dll)
Provides:       mingw32(userenv.dll)
Provides:       mingw32(uxtheme.dll)
# TODO: The available DLL's can be identified by the
# available import libraries of the mingw32-runtime package.
# needed by mingw32-libqt5-qtbase 
Provides:       mingw32(d2d1.dll)
Provides:       mingw32(d3d11.dll)
Provides:       mingw32(dwrite.dll)
Requires:       mingw32-cross-breakpad-tools
Requires:       python3
Requires:       rpm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#!BuildIgnore: post-build-checks

%description
This package contains the base filesystem layout, RPM macros and
environment for all MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW

%prep
%setup -q -c -T
cp %{SOURCE0} COPYING
sed 's/@VERSION@/%{version}/' < %{SOURCE4} > mingw32-find-requires.sh

%build
# nothing

%install
mkdir -p %{buildroot}

mkdir -p %{buildroot}%{_prefix}/lib

mkdir -p %{buildroot}%{_libexecdir}
install -m 755 %{SOURCE6} %{buildroot}%{_libexecdir}/mingw32-scripts

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
for i in mingw32-configure mingw32-make mingw32-cmake ; do
  ln -s %{_libexecdir}/mingw32-scripts $i
done
popd

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/

mkdir -p %{buildroot}%{_sysconfdir}/rpm
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.mingw32
install -m 644 %{SOURCE14} %{buildroot}%{_sysconfdir}/rpm/$(basename %{SOURCE14})

mkdir -p %{buildroot}%{_sysconfdir}/rpmlint
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/rpmlint/mingw32-rpmlint.config

mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32

# GCC requires these directories, even though they contain links
# to binaries which are also installed in /usr/bin etc.  These
# contain native binaries.
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/bin
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/lib

# The MinGW system root which will contain Windows native binaries
# and Windows-specific header files, pkgconfig, etc.
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/bin
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/include
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/include/sys
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/lib
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/lib/cmake
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/lib/pkgconfig
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/aclocal
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/pkgconfig
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/var
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw%{_localstatedir}/lib
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw%{_localstatedir}/lib/rpm-state
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw%{_localstatedir}/lib/rpm-state/gconf

(cd %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root && ln -s mingw i686-w64-mingw32)

# Let programs locate their plugins relative to the executable without using
# upward movement ("..") in those packages, cf. libdbi, libenchant.
#
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/bin/lib
ln -s ../../lib "%buildroot/%_prefix/i686-w64-mingw32/sys-root/mingw/bin/lib/i386-pc"

mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/doc
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/info
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/man
mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/man/man{1,2,3,4,5,6,7,8,9,n}

# NB. NOT _libdir
mkdir -p %{buildroot}%{_rpmlibdir}
install -m 0755 %{SOURCE3} %{buildroot}%{_rpmlibdir}
install -m 0755 %{SOURCE4} %{buildroot}%{_rpmlibdir}
install -m 0755 %{SOURCE5} %{buildroot}%{_rpmlibdir}
install -m 0755 %{SOURCE8} %{buildroot}%{_rpmlibdir}
install -m 0755 %{SOURCE9} %{buildroot}%{_rpmlibdir}
# cmake support 
install -m 0755 %{SOURCE12} %{buildroot}%{_rpmlibdir}
mkdir -p %{buildroot}%{_rpmlibdir}/fileattrs
install -m 0644 %{SOURCE13} %{buildroot}%{_rpmlibdir}/fileattrs

# Create the locale directories:
while read LANG ; do
  mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/locale/$LANG/LC_MESSAGES
  mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/help/$LANG
done < %{SOURCE10}
# Create the locale directories for man:
while read LANG ; do
  mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/man/$LANG
  for sec in 1 2 3 4 5 6 7 8 9 n; do
    mkdir -p %{buildroot}%{_prefix}/i686-w64-mingw32/sys-root/mingw/share/man/$LANG/man$sec
  done
done < %{SOURCE11}

%files
%defattr(-,root,root,-)
%doc COPYING
%config %{_sysconfdir}/rpm/macros.mingw32
%config %{_sysconfdir}/rpm/macros.mingw32-cmake
%config %{_sysconfdir}/profile.d/mingw32.sh
%config %{_sysconfdir}/rpmlint/mingw32-rpmlint.config
%{_rpmlibdir}/mingw32-cmake.prov
%{_rpmlibdir}/fileattrs/mingw32-cmake.attr
%{_bindir}/mingw32-*
%{_libexecdir}/mingw32-scripts
%{_prefix}/i686-w64-mingw32/
%{_rpmlibdir}/mingw32-*
%dir %{_prefix}/i686-w64-mingw32/sys-root/mingw/lib/cmake

%changelog
