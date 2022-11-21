#
# spec file for package mingw64-filesystem
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


# Tumbleweed
%if %suse_version >= 1550
%define _rpmlintdir /opt/testing/share/rpmlint
%else
%define _rpmlintdir /opt/testing/share/rpmlint/mini
%endif

%define debug_package %{nil}
%if %{undefined _distconfdir}
%define _distconfdir %{_sysconfdir}
%endif
%if %{undefined _rpmmacrodir}
%define _rpmmacrodir %{_sysconfdir}/rpm
%endif
Name:           mingw64-filesystem
Version:        20221115
Release:        0
Summary:        MinGW base filesystem and environment
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
URL:            http://hg.et.redhat.com/misc/fedora-mingw--devel/
Source0:        COPYING
Source1:        macros.mingw64
Source2:        mingw64.sh
Source3:        mingw64-find-debuginfo.sh
Source4:        mingw64-find-requires.sh
Source5:        mingw64-find-provides.sh
Source6:        mingw64-scripts.sh
Source7:        mingw64-rpmlintrc
Source8:        mingw64-install-post.sh
Source9:        mingw64-find-lang.sh
Source10:       languages
Source11:       languages.man
Source12:       mingw64-cmake.prov
Source13:       mingw64-cmake.attr
Source14:       macros.mingw64-cmake
Source15:       mingw64-filesystem-rpmlintrc
Source16:       mingw-objdump-srcfiles
# add excluded system libraries to mingw64-find-requires.sh
# TODO: The following provides could be removed after all packages has been rebuild
Provides:       mingw64(bcrypt.dll)
Provides:       mingw64(dbghelp.dll)
Provides:       mingw64(mpr.dll)
Provides:       mingw64(odbccp32.dll)
Provides:       mingw64(userenv.dll)
Provides:       mingw64(uxtheme.dll)
# TODO: The available DLL's can be identified by the
# available import libraries of the mingw64-runtime package.
# needed by mingw64-libqt5-qtbase
Provides:       mingw64(d2d1.dll)
Provides:       mingw64(d3d11.dll)
Provides:       mingw64(d3d12.dll)
Provides:       mingw64(dcomp.dll)
Provides:       mingw64(dwrite.dll)
Provides:       mingw64(dxgi.dll)
Provides:       mingw64(ncrypt.dll)
Provides:       mingw64(wtsapi32.dll)
Requires:       coreutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       mingw64-cross-binutils-utils
Requires:       mingw64-cross-pkgconf-utils
Requires:       python3
Requires:       rpm
Requires:       rpmlint-mini
Requires:       sed
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
sed 's/@VERSION@/%{version}/' < %{SOURCE4} > mingw64-find-requires.sh

%build
# nothing

%install
mkdir -p %{buildroot}

mkdir -p %{buildroot}%{_prefix}/lib

mkdir -p %{buildroot}%{_libexecdir}
install -m 755 %{SOURCE6} %{buildroot}%{_libexecdir}/mingw64-scripts

# this is already provided by _mingw64_create_macro_links
# but including macros.mingw64 results into an unknown failure
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
for i in mingw64-configure mingw64-make mingw64-cmake mingw64-gdb ; do
  ln -s %{_libexecdir}/mingw64-scripts $i
done
popd

mkdir -p %{buildroot}%{_distconfdir}/profile.d
install -m 644 %{SOURCE2} %{buildroot}%{_distconfdir}/profile.d

mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.mingw64
install -m 644 %{SOURCE14} %{buildroot}%{_rpmmacrodir}/$(basename %{SOURCE14})

mkdir -p %{buildroot}%_rpmlintdir
# tumbleweed
%if %suse_version >= 1550
# convert to toml file format, which seems to be required
sed "s,addFilter *(\",     ',g;s#\")#',#g" %{SOURCE7} | gawk 'BEGIN { print "Filters = ["} { print $0 } END { print "]"}' > %{SOURCE7}.toml
install -m 644 %{SOURCE7}.toml %{buildroot}%_rpmlintdir/mingw64.toml
%else
install -m 644 %{SOURCE7} %{buildroot}%_rpmlintdir/mingw64-rpmlint.config
%endif

mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32

# GCC requires these directories, even though they contain links
# to binaries which are also installed in /usr/bin etc.  These
# contain native binaries.
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/bin
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/lib

# The MinGW system root which will contain Windows native binaries
# and Windows-specific header files, pkgconfig, etc.
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/bin
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/include
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/include/sys
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/lib
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/lib/cmake
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/lib/pkgconfig
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/aclocal
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/pkgconfig
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/var
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw%{_localstatedir}/lib
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw%{_localstatedir}/lib/rpm-state
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw%{_localstatedir}/lib/rpm-state/gconf

(cd %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root && ln -s mingw x86_64-w64-mingw32)

# Let programs locate their plugins relative to the executable without using
# upward movement ("..") in those packages, cf. libdbi, libenchant.
#
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/bin/lib
ln -s ../../lib "%buildroot/%_prefix/x86_64-w64-mingw32/sys-root/mingw/bin/lib/x86_64-pc"

mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/doc
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/info
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/man
mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/man/man{1,2,3,4,5,6,7,8,9,n}

# NB. NOT _libdir
mkdir -p %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE4} %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE5} %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE8} %{buildroot}%{_rpmconfigdir}
install -m 0755 %{SOURCE9} %{buildroot}%{_rpmconfigdir}

# cmake support
install -m 0755 %{SOURCE12} %{buildroot}%{_rpmconfigdir}
mkdir -p %{buildroot}%{_fileattrsdir}
install -m 0644 %{SOURCE13} %{buildroot}%{_fileattrsdir}

# Create the locale directories:
while read LANG ; do
  mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/locale/$LANG/LC_MESSAGES
  mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/help/$LANG
done < %{SOURCE10}
# Create the locale directories for man:
while read LANG ; do
  mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/man/$LANG
  for sec in 1 2 3 4 5 6 7 8 9 n; do
    mkdir -p %{buildroot}%{_prefix}/x86_64-w64-mingw32/sys-root/mingw/share/man/$LANG/man$sec
  done
done < %{SOURCE11}

install -m 0755 %{SOURCE16} %{buildroot}%{_bindir}/x86_64-w64-mingw32-objdump-srcfiles

%files
%license COPYING
%{_rpmmacrodir}/macros.mingw64
%{_rpmmacrodir}/macros.mingw64-cmake
%if %{undefined _distconfdir}
%config %{_sysconfdir}/profile.d/mingw64.sh
%else
%{_distconfdir}/profile.d/mingw64.sh
%endif
%if %suse_version >= 1550
%_rpmlintdir/mingw64.toml
%else
%_rpmlintdir/mingw64-rpmlint.config
%endif
%{_rpmconfigdir}/mingw64-cmake.prov
%{_fileattrsdir}/mingw64-cmake.attr
%{_bindir}/mingw64-*
%{_bindir}/x86_64-w64-mingw32-*
%{_libexecdir}/mingw64-scripts
%{_prefix}/x86_64-w64-mingw32/
%{_rpmconfigdir}/mingw64-*
%dir %{_prefix}/x86_64-w64-mingw32/sys-root/mingw/lib/cmake

%changelog
