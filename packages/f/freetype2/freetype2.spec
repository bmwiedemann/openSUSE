#
# spec file for package freetype2
#
# Copyright (c) 2023 SUSE LLC
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


%define doc_version 2.12.1
Name:           freetype2
Version:        2.12.1
Release:        0
Summary:        A TrueType Font Library
License:        GPL-2.0-or-later OR SUSE-Freetype
Group:          System/Libraries
URL:            https://www.freetype.org
Source0:        https://downloads.sourceforge.net/project/freetype/freetype2/%{version}/freetype-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/project/freetype/freetype-docs/%{version}/freetype-doc-%{version}.tar.xz
Source2:        %{name}.sh
Source10:       https://downloads.sourceforge.net/project/freetype/freetype2/%{version}/freetype-%{version}.tar.xz.sig
Source11:       https://downloads.sourceforge.net/project/freetype/freetype-docs/%{version}/freetype-doc-%{version}.tar.xz.sig
Source12:       freetype2.keyring
Source20:       https://downloads.sourceforge.net/project/freetype/freetype-demos/%{version}/ft2demos-%{version}.tar.xz
Source21:       https://downloads.sourceforge.net/project/freetype/freetype-demos/%{version}/ft2demos-%{version}.tar.xz.sig
Source1000:     baselibs.conf
Patch0:         bugzilla-308961-cmex-workaround.patch
# PATCH-FIX-OPENSUSE don-t-mark-libpng-as-required-library.patch -- it is private in .pc
Patch1:         don-t-mark-libpng-as-required-library.patch
Patch2:         enable-long-family-names-by-default.patch
Patch3:         enable-subpixel-rendering.patch
Patch4:         enable-infinality-subpixel-hinting.patch
BuildRequires:  gawk
BuildRequires:  libbz2-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(zlib)

%description
This library features TrueType fonts for open source projects. This
version also contains an autohinter for producing improved output.

%package -n libfreetype6
Summary:        A TrueType Font Library
Group:          System/Libraries
Obsoletes:      freetype2 < %{version}
Provides:       freetype2 = %{version}

%description -n libfreetype6
This library features TrueType fonts for open source projects. This
version also contains an autohinter for producing improved output.

%package profile-tti35
Summary:        Set TrueType interpreter to version 35
Group:          System/Shells
Requires:       bash
Requires:       freetype2
BuildArch:      noarch

%description profile-tti35
System environment for set TrueType interpreter to version 35.
In release 2.6.4, a new hinting mode for TrueType fonts was added,
which enabled by default to activate sub-pixel hinting for TrueType.
This broke the work of full hinting. This optional package with a bash profile
that will switch the TrueType Interpreter to the old version 35.

%package devel
Summary:        Development environment for the freetype2 TrueType font library
Group:          Development/Libraries/C and C++
Requires:       libfreetype6 = %{version}
Requires:       pkgconfig(libbrotlidec)
Requires:       pkgconfig(zlib)
# there is no freetype-devel on suse:
Provides:       freetype-devel
# Static library provides:
Provides:       libfreetype6-devel-static

%description devel
This package contains all necessary include files, libraries and
documentation needed to develop applications that require the freetype2
TrueType font library.

It also contains a small tutorial for using that library.

%package -n ftdump
Summary:        Simple font dumper
Group:          Productivity/Publishing/Other
Conflicts:      ft2demos < %{version}-%{release}

%description -n ftdump
Simple font dumper
This tool is part of the FreeType project

%prep

%setup -q -n freetype-%{version} -a 1 -a 20
%autopatch -p1

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE $(getconf LFS_CFLAGS)"
%configure \
	--with-bzip2 \
	--with-png \
	--with-zlib \
    --enable-freetype-config \
	--disable-static
%make_build ANSIFLAGS=

cd ft2demos-%{version}
%make_build TOP_DIR=..  $PWD/bin/ftdump

%install
%make_install
cd ft2demos-%{version}
../builds/unix/libtool --mode=install %{_bindir}/install -c bin/ftdump %{buildroot}%{_bindir}/ftdump
cd ..
install -Dm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

# remove documentation that does not belong in an rpm
rm docs/INSTALL*

rm %{buildroot}%{_libdir}/libfreetype.la

%post -n libfreetype6 -p /sbin/ldconfig
%postun -n libfreetype6 -p /sbin/ldconfig

%files -n libfreetype6
%{_libdir}/libfreetype.so.*
%doc ChangeLog README
%doc docs/{CHANGES,CUSTOMIZE,DEBUG,MAKEPP,PROBLEMS,TODO,*.txt}

%files profile-tti35
%config %{_sysconfdir}/profile.d/%{name}.sh

%files devel
%doc docs/reference/*
%{_bindir}/freetype-config
%{_includedir}/*
%{_libdir}/libfreetype.so
%{_libdir}/pkgconfig/freetype2.pc
%{_mandir}/man1/freetype-config.1%{?ext_man}
%{_datadir}/aclocal

%files -n ftdump
%{_bindir}/ftdump

%changelog
